#!/usr/bin/env python3
"""Record and independently verify final Tistory CDN media."""

from __future__ import annotations

import argparse
import hashlib
import http.client
import ipaddress
import json
import signal
import socket
import ssl
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from rich_post_v2_common import (
    REMOTE_FINGERPRINT_FIELDS,
    REMOTE_MAX_BYTES,
    atomic_write_json,
    detected_kind,
    gif_animation_info,
    image_container_error,
    image_dimensions,
    is_tistory_media_url,
    remote_toolchain_files,
    remote_toolchain_sha256,
    sha256_file,
    validate_bundle,
    validate_remote_media_records,
    validate_source_pass,
)


TIMEOUT_SECONDS = 20
MAX_REDIRECTS = 5
USER_AGENT = "dev.log-rich-post-v2-media-check/2.0"
ACCEPT = "image/webp,image/png,image/jpeg,image/gif"


class InconclusiveNetworkError(RuntimeError):
    pass


class FetchDeadline:
    """Enforce one wall-clock deadline around DNS, redirects, headers, and body."""

    def __init__(self, seconds: float) -> None:
        self.seconds = seconds
        self.previous_handler: Any = None
        self.enabled = False

    def _expired(self, signum, frame) -> None:
        raise InconclusiveNetworkError(
            f"remote fetch exceeded {self.seconds:g} seconds"
        )

    def __enter__(self) -> "FetchDeadline":
        if not all(
            hasattr(signal, attribute)
            for attribute in ("SIGALRM", "ITIMER_REAL", "setitimer", "getitimer")
        ):
            raise InconclusiveNetworkError(
                "hard remote-fetch deadlines require a POSIX signal runtime"
            )
        existing_delay, _ = signal.getitimer(signal.ITIMER_REAL)
        if existing_delay > 0:
            raise InconclusiveNetworkError(
                "cannot start remote fetch while another process alarm is active"
            )
        self.previous_handler = signal.getsignal(signal.SIGALRM)
        signal.signal(signal.SIGALRM, self._expired)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)
        self.enabled = True
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        if self.enabled:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, self.previous_handler)
            self.enabled = False


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def validate_network_target(url: str) -> None:
    if not is_tistory_media_url(url):
        raise ValueError("URL is not an allowed HTTPS Tistory media URL")
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    try:
        addresses = socket.getaddrinfo(
            hostname,
            443,
            type=socket.SOCK_STREAM,
        )
    except OSError as exc:
        raise InconclusiveNetworkError(
            f"cannot resolve CDN host: {exc}"
        ) from exc
    if not addresses:
        raise ValueError("CDN host resolved to no addresses")
    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])
        if not ip.is_global:
            raise ValueError(f"CDN host resolved to non-public address {ip}")


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.chain: list[str] = []

    def redirect_request(
        self,
        req,
        fp,
        code,
        msg,
        headers,
        newurl,
    ):
        if len(self.chain) >= MAX_REDIRECTS:
            raise urllib.error.HTTPError(
                req.full_url,
                code,
                "too many redirects",
                headers,
                fp,
            )
        validate_network_target(newurl)
        self.chain.append(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def inspect_bytes(body: bytes) -> tuple[str, int, int, int, float]:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False) as handle:
            handle.write(body)
            temporary_path = Path(handle.name)
        media_format = detected_kind(temporary_path)
        dimensions = image_dimensions(temporary_path)
        if media_format is None or dimensions is None:
            raise ValueError("response is not a supported, structured image")
        container_error = image_container_error(temporary_path, media_format)
        if container_error:
            raise ValueError(container_error)
        if dimensions[0] <= 0 or dimensions[1] <= 0:
            raise ValueError("image dimensions must be positive")
        if media_format == "gif":
            animation = gif_animation_info(temporary_path)
            if animation is None:
                raise ValueError("cannot parse remote GIF animation")
            frame_count, duration = animation
        else:
            frame_count, duration = 1, 0.0
        return (
            media_format,
            dimensions[0],
            dimensions[1],
            frame_count,
            duration,
        )
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except OSError:
                pass


def validate_observation(
    item: dict[str, Any],
    observed: dict[str, Any],
) -> list[str]:
    item_id = str(item.get("id", "unknown"))
    errors: list[str] = []
    media_format = observed["format"]
    remote_width = observed.get("width")
    remote_height = observed.get("height")
    if (
        type(remote_width) is not int
        or remote_width <= 0
        or type(remote_height) is not int
        or remote_height <= 0
    ):
        return [f"{item_id}: remote dimensions must be positive integers"]
    if item.get("kind") == "gif":
        if media_format != "gif":
            errors.append(f"{item_id}: remote GIF was transformed to {media_format}")
        if observed["frame_count"] < 2:
            errors.append(f"{item_id}: remote GIF has fewer than two frames")
        if not 0 < observed["duration_seconds"] <= 5:
            errors.append(f"{item_id}: remote GIF duration is outside 0-5 seconds")
    elif media_format not in {"png", "jpeg", "webp"}:
        errors.append(f"{item_id}: remote static format is unsupported")

    local_width = item.get("width")
    local_height = item.get("height")
    if (
        type(local_width) is int
        and local_width > 0
        and type(local_height) is int
        and local_height > 0
    ):
        local_ratio = local_width / local_height
        remote_ratio = remote_width / remote_height
        if abs(remote_ratio - local_ratio) / local_ratio > 0.005:
            errors.append(f"{item_id}: remote aspect ratio differs by over 0.5%")
    display_width = item.get(
        "display_width",
        min(local_width, 916)
        if type(local_width) is int and local_width > 0
        else 916,
    )
    if type(display_width) is int and remote_width < display_width:
        errors.append(f"{item_id}: remote width is below display_width")
    return errors


def fetch_item(item: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    item_id = str(item.get("id", "unknown"))
    deadline = time.monotonic() + TIMEOUT_SECONDS
    requested_url = item.get("tistory_url")
    if not isinstance(requested_url, str):
        raise ValueError(f"{item_id}: missing tistory_url")
    validate_network_target(requested_url)

    redirect_handler = SafeRedirectHandler()
    opener = urllib.request.build_opener(
        redirect_handler,
        urllib.request.HTTPSHandler(context=ssl.create_default_context()),
    )
    request = urllib.request.Request(
        requested_url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": ACCEPT,
            "Accept-Encoding": "identity",
            "Cache-Control": "no-cache",
        },
        method="GET",
    )
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise InconclusiveNetworkError(
            f"{item_id}: remote fetch exceeded {TIMEOUT_SECONDS} seconds"
        )
    with opener.open(request, timeout=remaining) as response:
        status = response.getcode()
        if status != 200:
            raise ValueError(f"{item_id}: remote HTTP status is {status}")
        final_url = response.geturl()
        validate_network_target(final_url)
        content_encoding = (response.headers.get("Content-Encoding") or "").lower()
        if content_encoding not in {"", "identity"}:
            raise ValueError(
                f"{item_id}: unsupported content encoding {content_encoding}"
            )
        header_length_value = response.headers.get("Content-Length")
        header_length: int | None = None
        if header_length_value:
            try:
                header_length = int(header_length_value)
            except ValueError as exc:
                raise ValueError(
                    f"{item_id}: invalid Content-Length header"
                ) from exc
            if header_length > REMOTE_MAX_BYTES:
                raise ValueError(f"{item_id}: remote file exceeds 32 MiB")

        chunks: list[bytes] = []
        total = 0
        digest = hashlib.sha256()
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise InconclusiveNetworkError(
                    f"{item_id}: remote fetch exceeded {TIMEOUT_SECONDS} seconds"
                )
            response_socket = getattr(
                getattr(getattr(response, "fp", None), "raw", None),
                "_sock",
                None,
            )
            if response_socket is not None:
                response_socket.settimeout(remaining)
            chunk = response.read(min(1024 * 1024, REMOTE_MAX_BYTES + 1 - total))
            if time.monotonic() > deadline:
                raise InconclusiveNetworkError(
                    f"{item_id}: remote fetch exceeded {TIMEOUT_SECONDS} seconds"
                )
            if not chunk:
                break
            total += len(chunk)
            if total > REMOTE_MAX_BYTES:
                raise ValueError(f"{item_id}: remote file exceeds 32 MiB")
            digest.update(chunk)
            chunks.append(chunk)
        if total == 0:
            raise ValueError(f"{item_id}: remote response is empty")
        if header_length is not None and header_length != total:
            raise ValueError(
                f"{item_id}: Content-Length differs from received bytes"
            )
        body = b"".join(chunks)
        media_format, width, height, frame_count, duration = inspect_bytes(body)
        content_type = (
            response.headers.get("Content-Type") or ""
        ).split(";", 1)[0].strip().lower()
        if content_type.startswith("text/") or content_type == "application/json":
            raise ValueError(f"{item_id}: remote response is not an image")
        allowed_content_types = {
            "image/png",
            "image/jpeg",
            "image/jpg",
            "image/webp",
            "image/gif",
            "application/octet-stream",
        }
        if content_type not in allowed_content_types:
            raise ValueError(f"{item_id}: unsupported Content-Type {content_type}")
        content_type_formats = {
            "image/png": "png",
            "image/jpeg": "jpeg",
            "image/jpg": "jpeg",
            "image/webp": "webp",
            "image/gif": "gif",
        }
        declared_format = content_type_formats.get(content_type)
        if declared_format is not None and declared_format != media_format:
            raise ValueError(
                f"{item_id}: Content-Type and image signature disagree"
            )
        warnings: list[str] = []
        if content_type == "application/octet-stream":
            warnings.append(
                f"{item_id}: CDN returned application/octet-stream; signature passed"
            )
        observed = {
            "id": item_id,
            "requested_url": requested_url,
            "final_url": final_url,
            "redirect_chain": redirect_handler.chain,
            "observed_at": utc_now(),
            "http_status": status,
            "content_type": content_type,
            "content_encoding": content_encoding,
            "header_content_length": header_length,
            "byte_length": total,
            "sha256": digest.hexdigest(),
            "format": media_format,
            "width": width,
            "height": height,
            "frame_count": frame_count,
            "duration_seconds": duration,
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }
    return observed, warnings


def fetch_all(
    manifest: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    observations: list[dict[str, Any]] = []
    warnings: list[str] = []
    errors: list[str] = []
    seen_urls: set[str] = set()
    for item in manifest.get("items", []):
        if not isinstance(item, dict):
            continue
        url = item.get("tistory_url")
        if isinstance(url, str) and url in seen_urls:
            errors.append(f"{item.get('id')}: duplicate tistory_url")
            continue
        if isinstance(url, str):
            seen_urls.add(url)
        try:
            with FetchDeadline(TIMEOUT_SECONDS):
                observed, item_warnings = fetch_item(item)
        except urllib.error.HTTPError as exc:
            errors.append(
                f"{item.get('id', 'unknown')}: HTTP error {exc.code}"
            )
            continue
        except ValueError as exc:
            errors.append(f"{item.get('id', 'unknown')}: {exc}")
            continue
        except (
            InconclusiveNetworkError,
            OSError,
            ssl.SSLError,
            http.client.HTTPException,
            urllib.error.URLError,
        ) as exc:
            errors.append(
                f"INCONCLUSIVE: {item.get('id', 'unknown')}: {exc}"
            )
            continue
        observations.append(observed)
        warnings.extend(item_warnings)
        errors.extend(validate_observation(item, observed))
    return observations, warnings, errors


def fingerprint(item: dict[str, Any]) -> dict[str, Any]:
    return {field: item.get(field) for field in REMOTE_FINGERPRINT_FIELDS}


def print_result(
    status: str,
    warnings: list[str],
    errors: list[str],
    payload: dict[str, Any] | None,
    as_json: bool,
) -> None:
    if as_json:
        print(
            json.dumps(
                {
                    "status": status,
                    "warnings": warnings,
                    "errors": errors,
                    "record": payload,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    print(f"remote media: {status}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Record or verify final Tistory CDN media."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("record", "verify"):
        child = subparsers.add_parser(command)
        child.add_argument("post_dir")
        child.add_argument("--by", required=True, dest="reviewer")
        child.add_argument("--json", action="store_true")
    live = subparsers.add_parser("check-live")
    live.add_argument("post_dir")
    live.add_argument("--json", action="store_true")
    args = parser.parse_args()

    post_dir = Path(args.post_dir).resolve()
    if args.command != "check-live":
        reviewer = args.reviewer.strip()
        if not reviewer:
            print_result(
                "revision_required",
                [],
                ["--by must name the actual reviewer"],
                None,
                args.json,
            )
            return 1
        args.reviewer = reviewer
    result = validate_bundle(post_dir)
    errors = list(result["errors"])
    warnings = list(result["warnings"])
    if result["meta"].get("status") != "reviewing" and args.command != "check-live":
        errors.append("remote readiness evidence must be recorded while reviewing")
    if args.command != "check-live" and result["article_path"].is_file():
        validate_source_pass(
            post_dir,
            result["article_path"],
            errors,
        )
    items = result["manifest"].get("items", [])
    if not isinstance(items, list) or not items:
        errors.append("media.json must contain items")
    for item in items if isinstance(items, list) else []:
        if isinstance(item, dict) and not is_tistory_media_url(
            str(item.get("tistory_url", ""))
        ):
            errors.append(
                f"{item.get('id', 'unknown')}: missing allowed Tistory CDN URL"
            )
    if errors:
        print_result("revision_required", warnings, errors, None, args.json)
        return 1

    manifest_path = result["manifest_path"]
    starting_media_hash = sha256_file(manifest_path)
    starting_fetcher_files = remote_toolchain_files()
    starting_fetcher_hash = remote_toolchain_sha256(starting_fetcher_files)
    qa_dir = post_dir / "artifacts" / "qa-v2"
    try:
        qa_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print_result(
            "revision_required",
            warnings,
            [f"cannot create QA directory: {exc}"],
            None,
            args.json,
        )
        return 1

    baseline_path = qa_dir / "remote-media.json"
    baseline: dict[str, Any] = {}
    pending_record_id = str(uuid.uuid4())
    if args.command == "record":
        pending_baseline = {
            "version": 2,
            "status": "in_progress",
            "record_id": pending_record_id,
            "recorded_at": utc_now(),
            "recorded_by": args.reviewer,
            "media_sha256": starting_media_hash,
            "fetcher_sha256": starting_fetcher_hash,
            "fetcher_files": starting_fetcher_files,
            "policy": {
                "max_bytes": REMOTE_MAX_BYTES,
                "timeout_seconds": TIMEOUT_SECONDS,
                "deadline_scope": "dns_redirect_headers_body",
                "max_redirects": MAX_REDIRECTS,
                "accept_encoding": "identity",
            },
            "items": [],
        }
        try:
            atomic_write_json(baseline_path, pending_baseline)
        except OSError as exc:
            print_result(
                "revision_required",
                warnings,
                [f"cannot invalidate prior remote baseline: {exc}"],
                None,
                args.json,
            )
            return 1
    if args.command in {"verify", "check-live"}:
        validation_errors: list[str] = []
        _, baseline, _, _ = validate_remote_media_records(
            post_dir,
            manifest_path,
            result["manifest"],
            validation_errors,
        )
        errors.extend(validation_errors)
        if errors:
            print_result("revision_required", warnings, errors, None, args.json)
            return 1
        if (
            args.command == "verify"
            and args.reviewer.strip()
            == str(baseline.get("recorded_by", "")).strip()
        ):
            errors.append("independent verifier must differ from remote recorder")
            print_result("revision_required", warnings, errors, None, args.json)
            return 1
        if args.command == "verify":
            verification_path = qa_dir / "remote-media-verification.json"
            pending_verification = {
                "version": 2,
                "status": "in_progress",
                "verified_at": utc_now(),
                "verified_by": args.reviewer,
                "remote_media_sha256": sha256_file(baseline_path),
                "media_sha256": starting_media_hash,
                "fetcher_sha256": starting_fetcher_hash,
                "fetcher_files": starting_fetcher_files,
                "items": [],
            }
            try:
                atomic_write_json(verification_path, pending_verification)
            except OSError as exc:
                print_result(
                    "revision_required",
                    warnings,
                    [f"cannot invalidate prior remote verification: {exc}"],
                    None,
                    args.json,
                )
                return 1

    observations, fetch_warnings, fetch_errors = fetch_all(result["manifest"])
    warnings.extend(fetch_warnings)
    errors.extend(fetch_errors)
    if sha256_file(manifest_path) != starting_media_hash:
        errors.append("media.json changed during remote fetch")
    ending_fetcher_files = remote_toolchain_files()
    ending_fetcher_hash = remote_toolchain_sha256(ending_fetcher_files)
    if (
        ending_fetcher_hash != starting_fetcher_hash
        or ending_fetcher_files != starting_fetcher_files
    ):
        errors.append("remote validation toolchain changed during fetch")
    if len(observations) != len(items):
        errors.append("not every media item produced a remote observation")
    if errors:
        status = (
            "inconclusive"
            if any(error.startswith("INCONCLUSIVE:") for error in errors)
            else "revision_required"
        )
        print_result(status, warnings, errors, None, args.json)
        return 1

    fetcher_hash = starting_fetcher_hash
    fetcher_files = starting_fetcher_files
    if args.command == "record":
        payload = {
            "version": 2,
            "status": "pass",
            "record_id": pending_record_id,
            "recorded_at": utc_now(),
            "recorded_by": args.reviewer,
            "media_sha256": starting_media_hash,
            "fetcher_sha256": fetcher_hash,
            "fetcher_files": fetcher_files,
            "policy": {
                "max_bytes": REMOTE_MAX_BYTES,
                "timeout_seconds": TIMEOUT_SECONDS,
                "deadline_scope": "dns_redirect_headers_body",
                "max_redirects": MAX_REDIRECTS,
                "accept_encoding": "identity",
            },
            "items": observations,
        }
        output_path = baseline_path
    else:
        baseline_by_id = {
            item["id"]: item
            for item in baseline["items"]
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        for observed in observations:
            original = baseline_by_id.get(observed["id"])
            if original is None:
                errors.append(f"{observed['id']}: missing from remote baseline")
                continue
            for field in REMOTE_FINGERPRINT_FIELDS:
                if observed.get(field) != original.get(field):
                    errors.append(
                        f"{observed['id']}: live `{field}` differs from baseline"
                    )
        if errors:
            print_result("revision_required", warnings, errors, None, args.json)
            return 1
        if args.command == "check-live":
            print_result("pass", warnings, [], None, args.json)
            return 0
        payload = {
            "version": 2,
            "status": "pass",
            "verified_at": utc_now(),
            "verified_by": args.reviewer,
            "remote_media_sha256": sha256_file(baseline_path),
            "media_sha256": starting_media_hash,
            "fetcher_sha256": fetcher_hash,
            "fetcher_files": fetcher_files,
            "items": [fingerprint(item) for item in observations],
        }
        output_path = qa_dir / "remote-media-verification.json"

    try:
        atomic_write_json(output_path, payload)
    except OSError as exc:
        print_result(
            "revision_required",
            warnings,
            [f"cannot save remote evidence: {exc}"],
            None,
            args.json,
        )
        return 1
    print_result("pass", warnings, [], payload, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
