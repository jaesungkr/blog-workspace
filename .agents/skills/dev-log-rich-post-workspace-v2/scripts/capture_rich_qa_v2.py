#!/usr/bin/env python3
"""Capture the single independent rich-post v2 final-page review."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import secrets
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import uuid
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import ProxyHandler, Request, build_opener

from rich_post_v2_common import (
    SLUG_RE,
    image_dimensions,
    is_tistory_media_url,
    sha256_file,
    split_frontmatter,
)


BASE_VIEWPORTS = (
    (1280, 900, "desktop-1280.png"),
    (360, 800, "mobile-360.png"),
)
OPTIONAL_VIEWPORTS = ((390, 844, "mobile-390.png"),)
OPTIONAL_TABLET_VIEWPORTS = ((768, 900, "tablet-768.png"),)
MODE_PATHS = {
    "final-light": {
        "preview_root": "artifacts/qa-v2/final-rendered",
        "screenshot_root": "artifacts/qa-v2/final/light",
        "receipt": "artifacts/qa-v2/final/light/browser-capture.json",
    },
    "final-dark": {
        "preview_root": "artifacts/qa-v2/final-dark-rendered",
        "screenshot_root": "artifacts/qa-v2/final/dark",
        "receipt": "artifacts/qa-v2/final/dark/browser-capture.json",
    },
}
CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
)
MAX_WEBSOCKET_MESSAGE = 64 * 1024 * 1024


class CaptureError(RuntimeError):
    """A concise, user-actionable capture failure."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def find_chrome(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if path.is_file() and os.access(path, os.X_OK):
            return path
        raise CaptureError(f"Chrome binary is not executable: {explicit}")

    candidates: list[str] = []
    environment_binary = os.environ.get("DEVLOG_CHROME_BINARY")
    if environment_binary:
        path = Path(environment_binary).expanduser().resolve()
        if path.is_file() and os.access(path, os.X_OK):
            return path
        raise CaptureError(
            "DEVLOG_CHROME_BINARY is not an executable file: "
            f"{environment_binary}"
        )
    candidates.extend(CHROME_CANDIDATES)
    for command in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
    ):
        located = shutil.which(command)
        if located:
            candidates.append(located)

    seen: set[Path] = set()
    for candidate in candidates:
        path = Path(candidate).expanduser().resolve()
        if path in seen:
            continue
        seen.add(path)
        if path.is_file() and os.access(path, os.X_OK):
            return path

    raise CaptureError(
        "Chrome or Chromium was not found. Install it, pass --chrome-binary, "
        "or set DEVLOG_CHROME_BINARY."
    )


def require_canonical_bundle_path(
    path: Path,
    post_dir: Path,
    label: str,
) -> None:
    try:
        relative = path.relative_to(post_dir)
    except ValueError as exc:
        raise CaptureError(f"{label} escapes the post bundle") from exc
    current = post_dir
    for component in relative.parts:
        current /= component
        if current.is_symlink():
            raise CaptureError(
                f"{label} must not contain symbolic links: {current}"
            )


def load_post_context(
    post_dir: Path,
    mode: str,
) -> tuple[str, Path, Path, Path]:
    article_path = post_dir / "article.md"
    if not article_path.is_file():
        raise CaptureError(f"missing article.md: {article_path}")
    try:
        metadata, _ = split_frontmatter(article_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        raise CaptureError(f"cannot read article.md: {exc}") from exc

    slug = metadata.get("slug")
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        raise CaptureError("article.md must contain a valid kebab-case slug")
    if metadata.get("status") != "reviewing":
        raise CaptureError("browser QA must be captured while status is `reviewing`")
    if metadata.get("format") != "rich-post-v2":
        raise CaptureError("article.md must contain `format: rich-post-v2`")

    paths = MODE_PATHS[mode]
    preview_root = post_dir / paths["preview_root"]
    expected_preview = preview_root / f"{slug}-rich-preview.html"
    screenshot_root = post_dir / paths["screenshot_root"]
    receipt_path = post_dir / paths["receipt"]
    for path, label in (
        (preview_root, "preview root"),
        (expected_preview, "canonical preview"),
        (screenshot_root, "screenshot root"),
        (receipt_path.parent, "receipt root"),
    ):
        require_canonical_bundle_path(path, post_dir, label)
    if not expected_preview.is_file():
        raise CaptureError(
            f"missing canonical {mode} preview: {expected_preview}"
        )
    return slug, expected_preview, screenshot_root, receipt_path


def http_json(url: str, timeout: float) -> Any:
    opener = build_opener(ProxyHandler({}))
    try:
        with opener.open(Request(url, method="GET"), timeout=timeout) as response:
            if response.getcode() != 200:
                raise CaptureError(
                    f"DevTools endpoint returned HTTP {response.getcode()}: {url}"
                )
            payload = response.read()
    except (HTTPError, URLError, OSError) as exc:
        raise CaptureError(f"cannot query DevTools endpoint {url}: {exc}") from exc
    try:
        return json.loads(payload.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise CaptureError(f"DevTools endpoint returned invalid JSON: {url}") from exc


class ChromeProcess:
    def __init__(
        self,
        binary: Path,
        startup_timeout: float,
    ) -> None:
        self.binary = binary
        self.startup_timeout = startup_timeout
        self.profile: tempfile.TemporaryDirectory[str] | None = None
        self.log: Any = None
        self.process: subprocess.Popen[bytes] | None = None
        self.port = 0
        self.version: dict[str, Any] = {}
        self.page_websocket_url = ""

    def __enter__(self) -> "ChromeProcess":
        self.profile = tempfile.TemporaryDirectory(prefix="devlog-rich-chrome-")
        profile_path = Path(self.profile.name)
        self.log = tempfile.TemporaryFile(mode="w+b")
        command = [
            str(self.binary),
            "--headless=new",
            "--disable-background-networking",
            "--disable-component-update",
            "--disable-default-apps",
            "--disable-features=Translate",
            "--disable-gpu",
            "--disable-sync",
            "--metrics-recording-only",
            "--mute-audio",
            "--no-default-browser-check",
            "--no-first-run",
            "--remote-allow-origins=*",
            "--remote-debugging-address=127.0.0.1",
            "--remote-debugging-port=0",
            f"--user-data-dir={profile_path}",
            "about:blank",
        ]
        try:
            self.process = subprocess.Popen(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=self.log,
            )
            self._wait_until_ready(profile_path)
        except BaseException:
            self.close()
            raise
        return self

    def _wait_until_ready(self, profile_path: Path) -> None:
        active_port_path = profile_path / "DevToolsActivePort"
        deadline = time.monotonic() + self.startup_timeout
        while time.monotonic() < deadline:
            if self.process is not None and self.process.poll() is not None:
                raise CaptureError(
                    "Chrome exited before DevTools became ready"
                    + self._log_suffix()
                )
            if active_port_path.is_file():
                try:
                    lines = active_port_path.read_text(encoding="utf-8").splitlines()
                    port = int(lines[0])
                except (OSError, UnicodeError, ValueError, IndexError):
                    time.sleep(0.05)
                    continue
                self.port = port
                break
            time.sleep(0.05)
        if not self.port:
            raise CaptureError(
                f"Chrome DevTools did not start within {self.startup_timeout:g}s"
                + self._log_suffix()
            )

        base_url = f"http://127.0.0.1:{self.port}"
        self.version = http_json(
            f"{base_url}/json/version",
            min(self.startup_timeout, 10),
        )
        deadline = time.monotonic() + self.startup_timeout
        while time.monotonic() < deadline:
            targets = http_json(f"{base_url}/json/list", 5)
            if isinstance(targets, list):
                page = next(
                    (
                        item
                        for item in targets
                        if isinstance(item, dict)
                        and item.get("type") == "page"
                        and isinstance(item.get("webSocketDebuggerUrl"), str)
                    ),
                    None,
                )
                if page is not None:
                    self.page_websocket_url = page["webSocketDebuggerUrl"]
                    return
            time.sleep(0.05)
        raise CaptureError("Chrome did not expose a page DevTools target")

    def _log_suffix(self) -> str:
        if self.log is None:
            return ""
        try:
            self.log.flush()
            self.log.seek(0)
            data = self.log.read().decode("utf-8", errors="replace").strip()
        except OSError:
            return ""
        if not data:
            return ""
        tail = "\n".join(data.splitlines()[-8:])
        return f"\nChrome log:\n{tail}"

    def close(self) -> None:
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    pass
        if self.log is not None:
            self.log.close()
            self.log = None
        if self.profile is not None:
            try:
                self.profile.cleanup()
            except OSError:
                pass
            self.profile = None

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        self.close()


class WebSocket:
    def __init__(self, url: str, timeout: float) -> None:
        parsed = urlparse(url)
        if parsed.scheme not in {"ws", "wss"} or not parsed.hostname:
            raise CaptureError(f"invalid DevTools WebSocket URL: {url}")
        port = parsed.port or (443 if parsed.scheme == "wss" else 80)
        try:
            connection = socket.create_connection(
                (parsed.hostname, port),
                timeout=timeout,
            )
        except OSError as exc:
            raise CaptureError(f"cannot connect to DevTools WebSocket: {exc}") from exc
        if parsed.scheme == "wss":
            connection.close()
            raise CaptureError("unexpected secure local DevTools WebSocket")
        self.socket = connection
        self.timeout = timeout
        self.buffer = bytearray()
        self.closed = False
        path = parsed.path or "/"
        if parsed.query:
            path += f"?{parsed.query}"
        key = base64.b64encode(secrets.token_bytes(16)).decode("ascii")
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {parsed.hostname}:{port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            f"Origin: http://{parsed.hostname}:{port}\r\n"
            "\r\n"
        ).encode("ascii")
        self.socket.sendall(request)
        response = self._read_headers(timeout)
        status_line = response.split(b"\r\n", 1)[0].decode(
            "ascii",
            errors="replace",
        )
        if " 101 " not in f" {status_line} ":
            self.close()
            raise CaptureError(
                f"DevTools WebSocket handshake failed: {status_line}"
            )
        expected_accept = base64.b64encode(
            hashlib.sha1(
                (key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")
            ).digest()
        ).decode("ascii")
        header_lines = response.decode("iso-8859-1").split("\r\n")[1:]
        headers = {}
        for line in header_lines:
            if ":" in line:
                name, value = line.split(":", 1)
                headers[name.strip().lower()] = value.strip()
        if headers.get("sec-websocket-accept") != expected_accept:
            self.close()
            raise CaptureError("DevTools WebSocket handshake signature is invalid")

    def _read_headers(self, timeout: float) -> bytes:
        deadline = time.monotonic() + timeout
        while b"\r\n\r\n" not in self.buffer:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise CaptureError("timed out during DevTools WebSocket handshake")
            self.socket.settimeout(remaining)
            try:
                chunk = self.socket.recv(4096)
            except (OSError, socket.timeout) as exc:
                raise CaptureError(
                    f"failed to read DevTools WebSocket handshake: {exc}"
                ) from exc
            if not chunk:
                raise CaptureError("DevTools WebSocket closed during handshake")
            self.buffer.extend(chunk)
            if len(self.buffer) > 64 * 1024:
                raise CaptureError("DevTools WebSocket handshake is too large")
        boundary = self.buffer.index(b"\r\n\r\n") + 4
        headers = bytes(self.buffer[:boundary])
        del self.buffer[:boundary]
        return headers

    def _receive_exact(self, size: int, deadline: float) -> bytes:
        while len(self.buffer) < size:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise CaptureError("timed out waiting for a DevTools message")
            self.socket.settimeout(remaining)
            try:
                chunk = self.socket.recv(min(65536, size - len(self.buffer)))
            except socket.timeout as exc:
                raise CaptureError("timed out waiting for a DevTools message") from exc
            except OSError as exc:
                raise CaptureError(f"DevTools WebSocket read failed: {exc}") from exc
            if not chunk:
                raise CaptureError("DevTools WebSocket closed unexpectedly")
            self.buffer.extend(chunk)
        value = bytes(self.buffer[:size])
        del self.buffer[:size]
        return value

    def _send_frame(self, opcode: int, payload: bytes) -> None:
        if self.closed:
            raise CaptureError("DevTools WebSocket is closed")
        first = 0x80 | opcode
        length = len(payload)
        if length < 126:
            header = bytes((first, 0x80 | length))
        elif length <= 0xFFFF:
            header = bytes((first, 0x80 | 126)) + struct.pack("!H", length)
        else:
            header = bytes((first, 0x80 | 127)) + struct.pack("!Q", length)
        mask = secrets.token_bytes(4)
        masked = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
        try:
            self.socket.sendall(header + mask + masked)
        except OSError as exc:
            raise CaptureError(f"DevTools WebSocket write failed: {exc}") from exc

    def send_json(self, value: dict[str, Any]) -> None:
        self._send_frame(
            0x1,
            json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode(
                "utf-8"
            ),
        )

    def receive_json(self, timeout: float) -> dict[str, Any]:
        deadline = time.monotonic() + timeout
        fragments = bytearray()
        message_opcode: int | None = None
        while True:
            first, second = self._receive_exact(2, deadline)
            final = bool(first & 0x80)
            opcode = first & 0x0F
            masked = bool(second & 0x80)
            length = second & 0x7F
            if length == 126:
                length = struct.unpack("!H", self._receive_exact(2, deadline))[0]
            elif length == 127:
                length = struct.unpack("!Q", self._receive_exact(8, deadline))[0]
            if length > MAX_WEBSOCKET_MESSAGE:
                raise CaptureError("DevTools WebSocket message exceeds 64 MiB")
            mask = self._receive_exact(4, deadline) if masked else b""
            payload = self._receive_exact(length, deadline)
            if masked:
                payload = bytes(
                    value ^ mask[index % 4]
                    for index, value in enumerate(payload)
                )

            if opcode == 0x8:
                self.closed = True
                raise CaptureError("DevTools WebSocket sent a close frame")
            if opcode == 0x9:
                self._send_frame(0xA, payload)
                continue
            if opcode == 0xA:
                continue
            if opcode in {0x1, 0x2}:
                if message_opcode is not None:
                    raise CaptureError("invalid fragmented DevTools WebSocket message")
                message_opcode = opcode
                fragments.extend(payload)
            elif opcode == 0x0:
                if message_opcode is None:
                    raise CaptureError("unexpected DevTools continuation frame")
                fragments.extend(payload)
            else:
                raise CaptureError(
                    f"unsupported DevTools WebSocket opcode: {opcode}"
                )
            if len(fragments) > MAX_WEBSOCKET_MESSAGE:
                raise CaptureError("DevTools WebSocket message exceeds 64 MiB")
            if not final:
                continue
            if message_opcode != 0x1:
                raise CaptureError("DevTools returned a binary WebSocket message")
            try:
                value = json.loads(fragments.decode("utf-8"))
            except (UnicodeError, json.JSONDecodeError) as exc:
                raise CaptureError("DevTools returned invalid JSON") from exc
            if not isinstance(value, dict):
                raise CaptureError("DevTools returned a non-object message")
            return value

    def close(self) -> None:
        if self.closed:
            return
        try:
            self._send_frame(0x8, b"")
        except (CaptureError, OSError):
            pass
        self.closed = True
        try:
            self.socket.close()
        except OSError:
            pass

    def __enter__(self) -> "WebSocket":
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        self.close()


class CDPClient:
    def __init__(self, websocket: WebSocket, timeout: float) -> None:
        self.websocket = websocket
        self.timeout = timeout
        self.next_id = 1
        self.events: deque[dict[str, Any]] = deque()

    def call(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        request_id = self.next_id
        self.next_id += 1
        self.websocket.send_json(
            {
                "id": request_id,
                "method": method,
                "params": params or {},
            }
        )
        deadline = time.monotonic() + (timeout or self.timeout)
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise CaptureError(f"CDP command timed out: {method}")
            message = self.websocket.receive_json(remaining)
            if message.get("id") == request_id:
                if "error" in message:
                    error = message["error"]
                    if isinstance(error, dict):
                        detail = error.get("message") or str(error)
                    else:
                        detail = str(error)
                    raise CaptureError(f"CDP {method} failed: {detail}")
                result = message.get("result", {})
                if not isinstance(result, dict):
                    raise CaptureError(f"CDP {method} returned an invalid result")
                return result
            if isinstance(message.get("method"), str):
                self.events.append(message)

    def discard_events(self, method: str) -> None:
        self.events = deque(
            event for event in self.events if event.get("method") != method
        )

    def wait_event(self, method: str, timeout: float | None = None) -> dict[str, Any]:
        for index, event in enumerate(self.events):
            if event.get("method") == method:
                del self.events[index]
                return event
        deadline = time.monotonic() + (timeout or self.timeout)
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise CaptureError(f"CDP event timed out: {method}")
            message = self.websocket.receive_json(remaining)
            if message.get("method") == method:
                return message
            if isinstance(message.get("method"), str):
                self.events.append(message)


def evaluation_expression(image_timeout_ms: int) -> str:
    return f"""
(async () => {{
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const frame = () => new Promise((resolve) => requestAnimationFrame(resolve));
  if (document.fonts && document.fonts.ready) {{
    await Promise.race([document.fonts.ready, sleep({image_timeout_ms})]);
  }}

  let previousHeight = -1;
  let y = 0;
  for (let step = 0; step < 240; step += 1) {{
    const height = document.documentElement.scrollHeight;
    if (y >= height && height === previousHeight) break;
    previousHeight = height;
    window.scrollTo(0, y);
    await sleep(60);
    y += Math.max(240, Math.floor(window.innerHeight * 0.75));
  }}

  const deadline = performance.now() + {image_timeout_ms};
  while (
    performance.now() < deadline &&
    Array.from(document.images).some(
      (image) => !image.complete || image.naturalWidth <= 0 || image.naturalHeight <= 0
    )
  ) {{
    await sleep(100);
  }}
  window.scrollTo(0, 0);
  await frame();
  await frame();

  const images = Array.from(document.images).map((image) => ({{
    src: image.currentSrc || image.src || "",
    complete: image.complete,
    natural_width: image.naturalWidth,
    natural_height: image.naturalHeight
  }}));
  const toc = Array.from(
    document.querySelectorAll('.devlog-rich__toc a[href^="#"]')
  );
  const tocTargetIds = toc.map((anchor) => {{
    const raw = anchor.getAttribute("href") || "";
    let id = raw.slice(1);
    try {{ id = decodeURIComponent(id); }} catch (_error) {{}}
    return id;
  }});
  const tocTargetsUnique =
    tocTargetIds.length > 0 &&
    new Set(tocTargetIds).size === tocTargetIds.length &&
    tocTargetIds.every((id) =>
      Boolean(id) &&
      Array.from(document.querySelectorAll("[id]"))
        .filter((element) => element.id === id).length === 1
    );
  const root = document.documentElement;
  return {{
    ready_state: document.readyState,
    location: window.location.href,
    inner_width: window.innerWidth,
    inner_height: window.innerHeight,
    client_width: root.clientWidth,
    client_height: root.clientHeight,
    scroll_width: root.scrollWidth,
    scroll_height: root.scrollHeight,
    h1_count: document.querySelectorAll("h1").length,
    toc_anchor_count: toc.length,
    toc_targets_unique: tocTargetsUnique,
    image_count: images.length,
    images_loaded: images.length > 0 && images.every(
      (image) => image.complete && image.natural_width > 0 && image.natural_height > 0
    ),
    images
  }};
}})()
"""


def evaluate_page(
    client: CDPClient,
    image_timeout: float,
) -> dict[str, Any]:
    result = client.call(
        "Runtime.evaluate",
        {
            "expression": evaluation_expression(int(image_timeout * 1000)),
            "awaitPromise": True,
            "returnByValue": True,
            "userGesture": False,
        },
        timeout=image_timeout + 10,
    )
    if result.get("exceptionDetails"):
        raise CaptureError(
            f"page evaluation failed: {result['exceptionDetails']}"
        )
    remote_object = result.get("result")
    if not isinstance(remote_object, dict):
        raise CaptureError("page evaluation returned no result")
    value = remote_object.get("value")
    if not isinstance(value, dict):
        raise CaptureError("page evaluation returned an invalid value")
    return value


def validate_page_measurements(
    measurements: dict[str, Any],
    preview_uri: str,
    width: int,
    height: int,
) -> None:
    failures: list[str] = []
    if measurements.get("ready_state") != "complete":
        failures.append("document.readyState is not complete")
    if measurements.get("location") != preview_uri:
        failures.append("browser did not remain on the canonical preview")
    if measurements.get("inner_width") != width:
        failures.append(f"window.innerWidth is not {width}")
    if measurements.get("inner_height") != height:
        failures.append(f"window.innerHeight is not {height}")
    if measurements.get("client_width") != width:
        failures.append(f"document clientWidth is not {width}")
    if measurements.get("scroll_width") != measurements.get("client_width"):
        failures.append("page has horizontal overflow")
    if measurements.get("h1_count") != 1:
        failures.append("preview does not contain exactly one H1")
    if measurements.get("toc_targets_unique") is not True:
        failures.append("TOC targets are not unique")
    if measurements.get("images_loaded") is not True:
        failures.append("one or more remote images did not load")

    images = measurements.get("images")
    if not isinstance(images, list) or not images:
        failures.append("preview contains no images")
    else:
        for index, image in enumerate(images):
            if not isinstance(image, dict):
                failures.append(f"image {index} metadata is invalid")
                continue
            source = image.get("src")
            if not isinstance(source, str) or not is_tistory_media_url(source):
                failures.append(f"image {index} does not use an allowed Tistory URL")
            if (
                type(image.get("natural_width")) is not int
                or image["natural_width"] <= 0
                or type(image.get("natural_height")) is not int
                or image["natural_height"] <= 0
            ):
                failures.append(f"image {index} has invalid natural dimensions")
    if failures:
        raise CaptureError(
            f"{width}x{height} browser checks failed: " + "; ".join(failures)
        )


def capture_viewport(
    client: CDPClient,
    preview_uri: str,
    width: int,
    height: int,
    staged_path: Path,
    page_timeout: float,
    image_timeout: float,
) -> dict[str, Any]:
    client.call(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": width < 735,
            "screenWidth": width,
            "screenHeight": height,
            "positionX": 0,
            "positionY": 0,
            "dontSetVisibleSize": False,
        },
    )
    client.discard_events("Page.loadEventFired")
    navigation = client.call("Page.navigate", {"url": preview_uri})
    if navigation.get("errorText"):
        raise CaptureError(
            f"{width}x{height} navigation failed: {navigation['errorText']}"
        )
    client.wait_event("Page.loadEventFired", timeout=page_timeout)
    measurements = evaluate_page(client, image_timeout)
    validate_page_measurements(measurements, preview_uri, width, height)

    screenshot = client.call(
        "Page.captureScreenshot",
        {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": False,
        },
        timeout=page_timeout,
    )
    encoded = screenshot.get("data")
    if not isinstance(encoded, str) or not encoded:
        raise CaptureError(f"{width}x{height} screenshot contains no data")
    try:
        screenshot_bytes = base64.b64decode(encoded, validate=True)
    except ValueError as exc:
        raise CaptureError(f"{width}x{height} screenshot is not valid base64") from exc
    staged_path.write_bytes(screenshot_bytes)
    dimensions = image_dimensions(staged_path)
    if dimensions != (width, height):
        raise CaptureError(
            f"{width}x{height} screenshot raster is "
            f"{dimensions[0]}x{dimensions[1]}"
            if dimensions is not None
            else f"{width}x{height} screenshot is not a supported PNG"
        )

    measurements["screenshot_sha256"] = sha256_file(staged_path)
    measurements["screenshot_pixel_width"] = width
    measurements["screenshot_pixel_height"] = height
    measurements["width"] = width
    measurements["height"] = height
    measurements["status"] = "pass"
    return measurements


def build_receipt(
    post_dir: Path,
    preview_path: Path,
    screenshot_root: Path,
    receipt_path: Path,
    mode: str,
    reviewer: str,
    chrome: ChromeProcess,
    session: str,
    viewport_records: list[dict[str, Any]],
    tool_hash: str,
    preview_hash: str,
) -> dict[str, Any]:
    browser_version = chrome.version.get("Browser")
    if not isinstance(browser_version, str) or not browser_version.strip():
        raise CaptureError("DevTools did not report a browser version")
    protocol_version = chrome.version.get("Protocol-Version")
    if not isinstance(protocol_version, str) or not protocol_version.strip():
        raise CaptureError("DevTools did not report a protocol version")
    return {
        "version": 2,
        "status": "pass",
        "mode": mode,
        "checked_at": utc_now(),
        "checked_by": reviewer,
        "tool_sha256": tool_hash,
        "preview_path": preview_path.relative_to(post_dir).as_posix(),
        "preview_sha256": preview_hash,
        "screenshot_root": screenshot_root.relative_to(post_dir).as_posix(),
        "receipt_path": receipt_path.relative_to(post_dir).as_posix(),
        "browser_version": browser_version,
        "protocol_version": protocol_version,
        "session": session,
        "viewports": viewport_records,
    }


def run_capture(args: argparse.Namespace) -> Path:
    if sys.platform != "darwin":
        raise CaptureError("capture_rich_qa_v2.py currently supports macOS only")
    post_dir = Path(args.post_dir).expanduser().resolve()
    if not post_dir.is_dir():
        raise CaptureError(f"post directory does not exist: {post_dir}")
    expected_receipt = post_dir / MODE_PATHS[args.mode]["receipt"]
    try:
        require_canonical_bundle_path(
            expected_receipt.parent,
            post_dir,
            "receipt root",
        )
        if expected_receipt.is_symlink():
            expected_receipt.unlink()
            raise CaptureError(
                "canonical receipt was a symbolic link and has been removed"
            )
        expected_receipt.unlink(missing_ok=True)
    except OSError as exc:
        raise CaptureError(f"cannot invalidate the prior pass receipt: {exc}") from exc

    for field in ("startup_timeout", "page_timeout", "image_timeout"):
        option = field.replace("_", "-")
        raw_value = getattr(args, field)
        try:
            value = float(raw_value)
        except (TypeError, ValueError) as exc:
            raise CaptureError(
                f"--{option} must be a positive finite number"
            ) from exc
        if not math.isfinite(value) or value <= 0:
            raise CaptureError(f"--{option} must be a positive finite number")
        setattr(args, field, value)
    reviewer = args.reviewer.strip()
    if not reviewer:
        raise CaptureError("--by must name the actual browser reviewer")
    _, preview_path, screenshot_root, receipt_path = load_post_context(
        post_dir,
        args.mode,
    )
    try:
        screenshot_root.mkdir(parents=True, exist_ok=True)
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise CaptureError(f"cannot prepare capture output paths: {exc}") from exc

    tool_path = Path(__file__).resolve()
    tool_hash = sha256_file(tool_path)
    preview_hash = sha256_file(preview_path)
    preview_uri = preview_path.as_uri()
    browser_binary = find_chrome(args.chrome_binary)
    session = str(uuid.uuid4())
    viewport_records: list[dict[str, Any]] = []
    viewports = (
        BASE_VIEWPORTS
        + (OPTIONAL_VIEWPORTS if args.include_390 else ())
        + (OPTIONAL_TABLET_VIEWPORTS if args.include_768 else ())
    )
    receipt: dict[str, Any] | None = None

    with tempfile.TemporaryDirectory(
        prefix=".capture-rich-qa-",
        dir=screenshot_root,
    ) as staging_name:
        staging_root = Path(staging_name)
        with ChromeProcess(browser_binary, args.startup_timeout) as chrome:
            with WebSocket(
                chrome.page_websocket_url,
                timeout=args.page_timeout,
            ) as websocket:
                client = CDPClient(websocket, timeout=args.page_timeout)
                client.call("Page.enable")
                client.call("Runtime.enable")
                client.call("Network.enable")
                client.call("Network.setCacheDisabled", {"cacheDisabled": True})
                client.call(
                    "Network.setBypassServiceWorker",
                    {"bypass": True},
                )
                client.call(
                    "Emulation.setDefaultBackgroundColorOverride",
                    {"color": {"r": 255, "g": 255, "b": 255, "a": 1}},
                )
                for width, height, filename in viewports:
                    staged_path = staging_root / filename
                    measurements = capture_viewport(
                        client,
                        preview_uri,
                        width,
                        height,
                        staged_path,
                        args.page_timeout,
                        args.image_timeout,
                    )
                    final_path = screenshot_root / filename
                    measurements["screenshot"] = final_path.relative_to(
                        post_dir
                    ).as_posix()
                    viewport_records.append(measurements)

            if sha256_file(tool_path) != tool_hash:
                raise CaptureError("capture tool changed during the browser run")
            if sha256_file(preview_path) != preview_hash:
                raise CaptureError("canonical preview changed during the browser run")

            for _, _, filename in viewports:
                source = staging_root / filename
                target = screenshot_root / filename
                os.replace(source, target)
            for record in viewport_records:
                screenshot_path = post_dir / record["screenshot"]
                if (
                    not screenshot_path.is_file()
                    or sha256_file(screenshot_path)
                    != record["screenshot_sha256"]
                    or image_dimensions(screenshot_path)
                    != (
                        record["screenshot_pixel_width"],
                        record["screenshot_pixel_height"],
                    )
                ):
                    raise CaptureError(
                        "committed screenshot differs from the captured raster"
                    )

            receipt = build_receipt(
                post_dir,
                preview_path,
                screenshot_root,
                receipt_path,
                args.mode,
                reviewer,
                chrome,
                session,
                viewport_records,
                tool_hash,
                preview_hash,
            )
    if receipt is None:
        raise CaptureError("browser capture produced no receipt")
    atomic_write_json(receipt_path, receipt)
    return receipt_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Load one canonical rich-post v2 remote preview in macOS "
            "Chrome/Chromium headless session, capture required viewports, "
            "and write an atomic JSON receipt."
        ),
        epilog=(
            "final-light and final-dark share the same independent reviewer but "
            "write separate hash-bound receipts under artifacts/qa-v2/final/."
        ),
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--mode",
        required=True,
        choices=tuple(MODE_PATHS),
        help="Select the final light or dark canonical preview.",
    )
    parser.add_argument(
        "--include-390",
        action="store_true",
        help="Add the conditional 390x844 profile when layout risk justifies it.",
    )
    parser.add_argument(
        "--include-768",
        action="store_true",
        help="Add the conditional 768x900 profile for complex layout transitions.",
    )
    parser.add_argument(
        "--by",
        required=True,
        dest="reviewer",
        help="Actual reviewer identity recorded in the receipt.",
    )
    parser.add_argument(
        "--chrome-binary",
        help=(
            "Chrome/Chromium executable. Otherwise use DEVLOG_CHROME_BINARY, "
            "standard macOS app paths, or PATH."
        ),
    )
    parser.add_argument(
        "--startup-timeout",
        default="20",
        help="Seconds to wait for Chrome DevTools startup (default: 20).",
    )
    parser.add_argument(
        "--page-timeout",
        default="30",
        help="Seconds for navigation and CDP commands (default: 30).",
    )
    parser.add_argument(
        "--image-timeout",
        default="20",
        help="Seconds to wait for remote images per viewport (default: 20).",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        receipt_path = run_capture(args)
    except KeyboardInterrupt:
        print("ERROR: browser capture interrupted; no pass receipt was written", file=sys.stderr)
        return 130
    except (CaptureError, OSError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"browser receipt: {receipt_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
