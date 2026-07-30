import base64
import binascii
import io
import hashlib
import json
import re
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "dev-log-rich-post-workspace"
SCRIPTS = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS))

from rich_post_common import (
    REMOTE_FINGERPRINT_FIELDS,
    REMOTE_MAX_BYTES,
    remote_toolchain_files,
    remote_toolchain_sha256,
    sha256_file,
    validate_bundle,
)
from remote_media import inspect_bytes
import remote_media


def png_bytes(width, height=2):
    def chunk(kind, data):
        payload = kind + data
        return (
            struct.pack(">I", len(data))
            + payload
            + struct.pack(">I", binascii.crc32(payload) & 0xFFFFFFFF)
        )

    rows = b"".join(b"\x00" + (b"\xff\xff\xff" * width) for _ in range(height))
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(rows))
        + chunk(b"IEND", b"")
    )


PNG_BYTES = png_bytes(760, 480)
GIF_POSTER_BYTES = png_bytes(480, 300)


def animated_gif_bytes(delay_cs=210):
    header = (
        b"GIF89a"
        + (480).to_bytes(2, "little")
        + (300).to_bytes(2, "little")
        + b"\x80\x00\x00"
        + b"\x00\x00\x00\xff\xff\xff"
    )
    frame = (
        b"\x21\xf9\x04\x00"
        + delay_cs.to_bytes(2, "little")
        + b"\x00\x00"
        + b"\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00"
        + b"\x02\x02\x44\x01\x00"
    )
    return header + frame + frame + b"\x3b"


GIF_BYTES = animated_gif_bytes()
VP8L_ALPHA_BYTES = base64.b64decode(
    "UklGRkIAAABXRUJQVlA4TDYAAAAvp8IXEQcQEREwkLbN/Nvf/kT0P8N//vOf//"
    "znP//5z3/+85///Oc///nPf/7zn//85z//Ww8="
)


def fake_jpeg_without_scan(width=2, height=2):
    frame = (
        b"\xff\xc0"
        + (11).to_bytes(2, "big")
        + b"\x08"
        + height.to_bytes(2, "big")
        + width.to_bytes(2, "big")
        + b"\x01\x01\x11\x00"
    )
    return b"\xff\xd8" + frame + b"\xff\xd9"


def fake_webp_without_bitstream(width=2, height=2):
    extended_header = (
        b"\x00\x00\x00\x00"
        + (width - 1).to_bytes(3, "little")
        + (height - 1).to_bytes(3, "little")
    )
    chunk = b"VP8X" + len(extended_header).to_bytes(4, "little") + extended_header
    return b"RIFF" + (len(chunk) + 4).to_bytes(4, "little") + b"WEBP" + chunk


class RichPostTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.post = Path(self.temp.name) / "2026-07-30-rich-test"
        (self.post / "assets" / "screenshots").mkdir(parents=True)
        (self.post / "artifacts" / "captures" / "raw").mkdir(parents=True)
        (self.post / "assets" / "screenshots" / "lead.png").write_bytes(PNG_BYTES)
        (self.post / "artifacts" / "captures" / "raw" / "lead.png").write_bytes(
            PNG_BYTES
        )
        (self.post / "capture-plan.md").write_text(
            "# 캡처 계획\n\n| 주장 ID | 자산 ID |\n|---|---|\n| C01 | lead-screen |\n",
            encoding="utf-8",
        )
        (self.post / "evidence.md").write_text(
            "# 근거 지도\n\n"
            "| ID | 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |\n"
            "|---|---|---|---|---|---|\n"
            "| C01 | 연결 화면 | Codex 실행 | 확인 | raw capture | 테스트 환경 |\n"
            "| C02 | 상태 변화 | 공식 | 확인 | official demo | 짧은 동작 |\n",
            encoding="utf-8",
        )
        (self.post / "article.md").write_text(
            """---
title: "도구 설정을 실제 화면으로 확인하는 방법"
slug: rich-test
date: 2026-07-30
category: Log
subcategory: "개발 · 디지털"
status: reviewing
format: rich-post
hero_image: assets/screenshots/lead.png
summary: "설정부터 확인까지 실제 화면으로 짚습니다."
---
안녕하세요. dev.log입니다.

설정 결과를 먼저 확인하고, 실패 범위까지 짧게 정리합니다.

{{media:lead-screen}}

### 설치 직후 확인할 화면

첫 화면에서 연결 상태를 확인합니다.

### 결과가 달라지는 지점

| 상태 | 판단 |
|---|---|
| 연결됨 | 다음 단계 진행 |
| 끊김 | 설정 재확인 |
""",
            encoding="utf-8",
        )
        self.manifest = {
            "version": 1,
            "lead_id": "lead-screen",
            "items": [
                {
                    "id": "lead-screen",
                    "kind": "screenshot",
                    "origin": "first_party",
                    "role": "lead",
                    "claim_ids": ["C01"],
                    "actor": "Codex 브라우저 실행",
                    "captured_at": "2026-07-30",
                    "environment": "macOS 26.5, test app 1.0",
                    "source_url": "",
                    "raw_path": "artifacts/captures/raw/lead.png",
                    "publish_path": "assets/screenshots/lead.png",
                    "tistory_url": "",
                    "width": 760,
                    "height": 480,
                    "display_width": 760,
                    "placement": "after:opening",
                    "rights": "dev.log original capture",
                    "alt": "연결 상태가 표시된 설정 결과 화면",
                    "caption": "첫 화면에서 연결 완료 상태를 확인합니다.",
                    "processing": [],
                    "redactions": [],
                    "sha256": hashlib.sha256(PNG_BYTES).hexdigest(),
                    "status": "validated",
                }
            ],
        }
        self.write_manifest()

    def tearDown(self):
        self.temp.cleanup()

    def write_manifest(self):
        (self.post / "media.json").write_text(
            json.dumps(self.manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def write_remote_baseline(self):
        qa_dir = self.post / "artifacts" / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        observed = []
        for item in self.manifest["items"]:
            publish_path = self.post / item["publish_path"]
            media_format = "gif" if item["kind"] == "gif" else "png"
            observed.append(
                {
                    "id": item["id"],
                    "requested_url": item["tistory_url"],
                    "final_url": item["tistory_url"],
                    "redirect_chain": [],
                    "observed_at": "2026-07-30T03:00:00Z",
                    "http_status": 200,
                    "content_type": f"image/{media_format}",
                    "content_encoding": "",
                    "header_content_length": publish_path.stat().st_size,
                    "byte_length": publish_path.stat().st_size,
                    "sha256": sha256_file(publish_path),
                    "format": media_format,
                    "width": item["width"],
                    "height": item["height"],
                    "frame_count": 2 if media_format == "gif" else 1,
                    "duration_seconds": (
                        item.get("duration_seconds", 0)
                        if media_format == "gif"
                        else 0
                    ),
                    "etag": None,
                    "last_modified": None,
                }
            )
        fetcher_files = remote_toolchain_files()
        baseline = {
            "version": 1,
            "status": "pass",
            "record_id": "test-remote-record",
            "recorded_at": "2026-07-30T03:00:00Z",
            "recorded_by": "creator remote recorder",
            "media_sha256": sha256_file(self.post / "media.json"),
            "fetcher_sha256": remote_toolchain_sha256(fetcher_files),
            "fetcher_files": fetcher_files,
            "policy": {
                "max_bytes": REMOTE_MAX_BYTES,
                "timeout_seconds": 20,
                "deadline_scope": "dns_redirect_headers_body",
                "max_redirects": 5,
                "accept_encoding": "identity",
            },
            "items": observed,
        }
        (qa_dir / "remote-media.json").write_text(
            json.dumps(baseline, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def write_remote_verification(self):
        qa_dir = self.post / "artifacts" / "qa"
        baseline_path = qa_dir / "remote-media.json"
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        fetcher_files = remote_toolchain_files()
        verification = {
            "version": 1,
            "status": "pass",
            "verified_at": "2026-07-30T03:05:00Z",
            "verified_by": "independent test reviewer",
            "remote_media_sha256": sha256_file(baseline_path),
            "media_sha256": sha256_file(self.post / "media.json"),
            "fetcher_sha256": remote_toolchain_sha256(fetcher_files),
            "fetcher_files": fetcher_files,
            "items": [
                {
                    field: item.get(field)
                    for field in REMOTE_FINGERPRINT_FIELDS
                }
                for item in baseline["items"]
            ],
        }
        (qa_dir / "remote-media-verification.json").write_text(
            json.dumps(verification, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def write_browser_receipt(
        self,
        mode,
        preview_path,
        human_viewports,
        reviewer,
        session,
    ):
        if mode == "creator":
            screenshot_root = "artifacts/qa"
            receipt_relative = "artifacts/qa/browser-capture.json"
        else:
            screenshot_root = "artifacts/qa/independent"
            receipt_relative = "artifacts/qa/independent/browser-capture.json"
        preview_markup = preview_path.read_text(encoding="utf-8")
        sources = re.findall(
            r'<img\b[^>]*\bsrc="([^"]+)"',
            preview_markup,
            re.IGNORECASE,
        )
        captured = []
        for viewport in human_viewports:
            screenshot_path = self.post / viewport["screenshot"]
            width = viewport["width"]
            height = viewport["height"]
            captured.append(
                {
                    "ready_state": "complete",
                    "location": preview_path.resolve().as_uri(),
                    "width": width,
                    "height": height,
                    "inner_width": width,
                    "inner_height": height,
                    "client_width": width,
                    "client_height": height,
                    "scroll_width": width,
                    "scroll_height": height * 3,
                    "h1_count": 1,
                    "toc_anchor_count": 2,
                    "toc_targets_unique": True,
                    "image_count": len(sources),
                    "images_loaded": True,
                    "images": [
                        {
                            "src": source,
                            "complete": True,
                            "natural_width": 760,
                            "natural_height": 480,
                        }
                        for source in sources
                    ],
                    "screenshot": viewport["screenshot"],
                    "screenshot_sha256": sha256_file(screenshot_path),
                    "screenshot_pixel_width": width,
                    "screenshot_pixel_height": height,
                    "status": "pass",
                }
            )
        receipt = {
            "version": 1,
            "status": "pass",
            "mode": mode,
            "checked_at": "2026-07-30T03:10:00Z",
            "checked_by": reviewer,
            "tool_sha256": sha256_file(SCRIPTS / "capture_rich_qa.py"),
            "preview_path": preview_path.relative_to(self.post).as_posix(),
            "preview_sha256": sha256_file(preview_path),
            "screenshot_root": screenshot_root,
            "receipt_path": receipt_relative,
            "browser_version": "test browser",
            "protocol_version": "1.3",
            "session": session,
            "viewports": captured,
        }
        receipt_path = self.post / receipt_relative
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def write_qa(self):
        qa_dir = self.post / "artifacts" / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        self.write_remote_baseline()
        reviewed_dir = qa_dir / "rendered"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(reviewed_dir),
                "--preview-media-source",
                "remote",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        preview_path = reviewed_dir / "rich-test-rich-preview.html"
        fragment_path = reviewed_dir / "rich-test-tistory-fragment.html"
        viewports = []
        for width, height, name in (
            (1280, 900, "desktop-1280.png"),
            (390, 844, "mobile-390.png"),
            (360, 800, "mobile-360.png"),
        ):
            (qa_dir / name).write_bytes(png_bytes(width, height))
            viewports.append(
                {
                    "width": width,
                    "height": height,
                    "client_width": width,
                    "scroll_width": width,
                    "h1_count": 1,
                    "toc_targets_unique": True,
                    "images_loaded": True,
                    "readable_media": True,
                    "screenshot": f"artifacts/qa/{name}",
                    "status": "pass",
                }
            )
        measurements = {
            "checked_at": "2026-07-30",
            "checked_by": "creator test reviewer",
            "browser": "test browser",
            "session": "creator-test-session",
            "viewports": viewports,
            "fragment": {
                "h1_count": 0,
                "unresolved_placeholders": 0,
                "local_paths": 0,
                "status": "pass",
            },
        }
        self.write_browser_receipt(
            "creator",
            preview_path,
            viewports,
            "creator test reviewer",
            "creator-test-session",
        )
        measurements_path = qa_dir / "measurements.json"
        measurements_path.write_text(
            json.dumps(measurements, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_rich_qa.py"),
                str(self.post),
                "--preview",
                str(preview_path),
                "--fragment",
                str(fragment_path),
                "--measurements",
                str(measurements_path),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)

    def write_independent_review(self):
        qa_dir = self.post / "artifacts" / "qa"
        self.write_remote_verification()
        reviewed_dir = qa_dir / "independent-rendered"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(reviewed_dir),
                "--require-publish-urls",
                "--preview-media-source",
                "remote",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)

        independent_dir = qa_dir / "independent"
        independent_dir.mkdir(parents=True, exist_ok=True)
        viewports = []
        for width, height, name in (
            (1280, 900, "desktop-1280.png"),
            (390, 844, "mobile-390.png"),
            (360, 800, "mobile-360.png"),
        ):
            (independent_dir / name).write_bytes(png_bytes(width, height))
            viewports.append(
                {
                    "width": width,
                    "height": height,
                    "client_width": width,
                    "scroll_width": width,
                    "h1_count": 1,
                    "toc_targets_unique": True,
                    "images_loaded": True,
                    "readable_media": True,
                    "screenshot": f"artifacts/qa/independent/{name}",
                    "status": "pass",
                }
            )
        measurements = {
            "result": "pass",
            "checked_at": "2026-07-30",
            "checked_by": "independent test reviewer",
            "browser": "test browser",
            "session": "independent-test-session",
            "viewports": viewports,
            "fragment": {
                "h1_count": 0,
                "unresolved_placeholders": 0,
                "local_paths": 0,
                "status": "pass",
            },
            "checks": {
                "captions_attached": True,
                "table_code_scroll": True,
                "content_order_preserved": True,
                "reduced_motion_fallback": "not_applicable",
                "gif_poster_matches_frame": "not_applicable",
            },
        }
        self.write_browser_receipt(
            "independent",
            reviewed_dir / "rich-test-rich-preview.html",
            viewports,
            "independent test reviewer",
            "independent-test-session",
        )
        measurements_path = qa_dir / "independent-measurements.json"
        measurements_path.write_text(
            json.dumps(measurements, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_rich_final_validation.py"),
                str(self.post),
                "--preview",
                str(reviewed_dir / "rich-test-rich-preview.html"),
                "--fragment",
                str(reviewed_dir / "rich-test-tistory-fragment.html"),
                "--measurements",
                str(measurements_path),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)

    def test_valid_reviewing_bundle_passes_without_publish_url(self):
        result = validate_bundle(self.post)

        self.assertEqual([], result["errors"])
        self.assertEqual([], result["warnings"])
        self.assertEqual(["lead-screen"], result["directives"])

    def test_remote_media_inspection_checks_container_and_animation(self):
        self.assertEqual(
            ("png", 760, 480, 1, 0.0),
            inspect_bytes(PNG_BYTES),
        )
        self.assertEqual(
            ("gif", 480, 300, 2, 4.2),
            inspect_bytes(GIF_BYTES),
        )
        self.assertEqual(
            ("webp", 680, 1120, 1, 0.0),
            inspect_bytes(VP8L_ALPHA_BYTES),
        )
        with self.assertRaisesRegex(ValueError, "IEND"):
            inspect_bytes(PNG_BYTES[:-1])
        invalid_gif = bytearray(GIF_BYTES)
        descriptor = invalid_gif.find(b"\x2c", 13)
        invalid_gif[descriptor + 10] = 9
        with self.assertRaisesRegex(ValueError, "GIF animation"):
            inspect_bytes(bytes(invalid_gif))

    def test_remote_media_rejects_structurally_fake_images(self):
        def chunk(kind, data):
            payload = kind + data
            return (
                struct.pack(">I", len(data))
                + payload
                + struct.pack(">I", binascii.crc32(payload) & 0xFFFFFFFF)
            )

        fake_png = (
            b"\x89PNG\r\n\x1a\n"
            + chunk(
                b"IHDR",
                struct.pack(">IIBBBBB", 2, 2, 8, 2, 0, 0, 0),
            )
            + chunk(b"JUNK", b"not pixels")
            + chunk(b"IEND", b"")
        )
        with self.assertRaisesRegex(ValueError, "critical chunk|IDAT"):
            inspect_bytes(fake_png)
        with self.assertRaisesRegex(ValueError, "frame or encoded scan"):
            inspect_bytes(fake_jpeg_without_scan())
        with self.assertRaisesRegex(ValueError, "bitstream"):
            inspect_bytes(fake_webp_without_bitstream())
        with self.assertRaisesRegex(ValueError, "dimensions"):
            inspect_bytes(png_bytes(760, 0))

    def test_invalid_utf8_bundle_reports_errors_without_traceback(self):
        article_path = self.post / "article.md"
        original_article = article_path.read_bytes()
        article_path.write_bytes(b"\xff")
        result = validate_bundle(self.post)
        self.assertTrue(
            any("cannot read article.md" in error for error in result["errors"])
        )

        article_path.write_bytes(original_article)
        (self.post / "media.json").write_bytes(b"\xff")
        result = validate_bundle(self.post)
        self.assertTrue(
            any("cannot read media.json" in error for error in result["errors"])
        )

    def test_paste_ready_gate_requires_final_https_urls(self):
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("missing tistory_url" in error for error in result["errors"])
        )

        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("missing artifacts/qa/remote-media.json" in error for error in result["errors"])
        )
        self.write_qa()
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertEqual([], result["errors"])
        qa = json.loads(
            (self.post / "artifacts" / "qa" / "rich-post.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(1, qa["version"])
        self.assertEqual(64, len(qa["article_content_sha256"]))
        self.assertEqual(64, len(qa["renderer_sha256"]))
        self.assertEqual("remote", qa["preview_media_source"])
        self.assertTrue((self.post / qa["preview_path"]).is_file())
        self.assertTrue((self.post / qa["fragment_path"]).is_file())
        reviewed_preview = (self.post / qa["preview_path"]).read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "https://blog.kakaocdn.net/example/lead.png",
            reviewed_preview,
        )

    def test_record_qa_binds_canonical_reviewed_files(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        qa_dir = self.post / "artifacts" / "qa"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_rich_qa.py"),
                str(self.post),
                "--preview",
                str(qa_dir / "rendered" / "rich-test-rich-preview.html"),
                "--fragment",
                str(qa_dir / "rendered" / "rich-test-tistory-fragment.html"),
                "--measurements",
                str(qa_dir / "measurements.json"),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        qa_path = qa_dir / "rich-post.json"
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        desktop = next(
            viewport
            for viewport in qa["viewports"]
            if viewport["width"] == 1280
        )
        self.assertEqual(900, desktop["screenshot_pixel_height"])
        self.assertEqual(64, len(desktop["screenshot_sha256"]))

        preserved_record = qa_path.read_bytes()
        (qa_dir / "desktop-1280.png").write_bytes(png_bytes(1280, 2))
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_rich_qa.py"),
                str(self.post),
                "--preview",
                str(qa_dir / "rendered" / "rich-test-rich-preview.html"),
                "--fragment",
                str(qa_dir / "rendered" / "rich-test-tistory-fragment.html"),
                "--measurements",
                str(qa_dir / "measurements.json"),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, completed.returncode)
        self.assertIn("screenshot pixels must equal", completed.stderr)
        self.assertEqual(preserved_record, qa_path.read_bytes())
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("screenshot_sha256" in error for error in result["errors"])
        )

    def test_record_qa_rejects_noncanonical_preview_location(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        output_dir = Path(self.temp.name) / "dist"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        measurements = self.post / "measurements.json"
        measurements.write_text("{}\n", encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_rich_qa.py"),
                str(self.post),
                "--preview",
                str(output_dir / "rich-test-rich-preview.html"),
                "--fragment",
                str(output_dir / "rich-test-tistory-fragment.html"),
                "--measurements",
                str(measurements),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, completed.returncode)
        self.assertIn("canonical path", completed.stderr)
        self.assertFalse(
            (self.post / "artifacts" / "qa" / "rich-post.json").exists()
        )

    def test_record_qa_rejects_viewport_evidence_bypasses(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        qa_dir = self.post / "artifacts" / "qa"
        measurements_path = qa_dir / "measurements.json"
        original_measurements = json.loads(
            measurements_path.read_text(encoding="utf-8")
        )
        receipt_path = qa_dir / "browser-capture.json"
        original_receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        preserved_record = (qa_dir / "rich-post.json").read_bytes()

        def run_record(receipt):
            receipt_path.write_text(
                json.dumps(receipt, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            measurements_path.write_text(
                json.dumps(
                    original_measurements,
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "record_rich_qa.py"),
                    str(self.post),
                    "--preview",
                    str(qa_dir / "rendered" / "rich-test-rich-preview.html"),
                    "--fragment",
                    str(
                        qa_dir
                        / "rendered"
                        / "rich-test-tistory-fragment.html"
                    ),
                    "--measurements",
                    str(measurements_path),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

        traversal = json.loads(json.dumps(original_receipt))
        outside_qa = self.post / "artifacts" / "outside-qa.png"
        outside_qa.write_bytes(png_bytes(1280, 900))
        traversal["viewports"][0]["screenshot"] = (
            "artifacts/qa/../outside-qa.png"
        )
        completed = run_record(traversal)
        self.assertEqual(1, completed.returncode)
        self.assertIn("screenshot path is not canonical", completed.stderr)

        duplicate = json.loads(json.dumps(original_receipt))
        for viewport in duplicate["viewports"]:
            viewport["screenshot"] = "artifacts/qa/desktop-1280.png"
        completed = run_record(duplicate)
        self.assertEqual(1, completed.returncode)
        self.assertIn("screenshot path is not canonical", completed.stderr)

        tiny = json.loads(json.dumps(original_receipt))
        for viewport in tiny["viewports"]:
            viewport["height"] = 2
        completed = run_record(tiny)
        self.assertEqual(1, completed.returncode)
        self.assertIn("not a required exact profile", completed.stderr)
        receipt_path.write_text(
            json.dumps(original_receipt, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        self.assertEqual(preserved_record, (qa_dir / "rich-post.json").read_bytes())

    def test_browser_capture_and_remote_toolchain_are_hash_bound(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        qa_dir = self.post / "artifacts" / "qa"

        receipt_path = qa_dir / "browser-capture.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["viewports"][0]["images_loaded"] = False
        receipt_path.write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("images_loaded" in error for error in result["errors"])
        )
        self.assertTrue(
            any("capture_receipt_sha256" in error for error in result["errors"])
        )

        self.write_qa()
        remote_path = qa_dir / "remote-media.json"
        remote = json.loads(remote_path.read_text(encoding="utf-8"))
        remote["fetcher_files"]["rich_post_common.py"] = "0" * 64
        remote_path.write_text(
            json.dumps(remote, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("fetcher_files" in error for error in result["errors"])
        )

    def test_tistory_media_map_plans_and_binds_url(self):
        command = [
            sys.executable,
            str(SCRIPTS / "tistory_media_map.py"),
            "plan",
            str(self.post),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("lead-screen", completed.stdout)
        self.assertIn("assets/screenshots/lead.png", completed.stdout)

        url = "https://blog.kakaocdn.net/example/lead.png"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "tistory_media_map.py"),
                "set-url",
                str(self.post),
                "lead-screen",
                url,
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        manifest = json.loads((self.post / "media.json").read_text(encoding="utf-8"))
        self.assertEqual(url, manifest["items"][0]["tistory_url"])

    def test_failed_remote_rerecord_invalidates_prior_pass(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_remote_baseline()
        self.write_remote_verification()

        with redirect_stdout(io.StringIO()), mock.patch.object(
            remote_media,
            "fetch_all",
            return_value=([], [], ["simulated fetch failure"]),
        ), mock.patch.object(
            sys,
            "argv",
            [
                "remote_media.py",
                "record",
                str(self.post),
                "--by",
                "creator remote recorder",
            ],
        ):
            return_code = remote_media.main()
        self.assertEqual(1, return_code)
        baseline = json.loads(
            (
                self.post / "artifacts" / "qa" / "remote-media.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual("in_progress", baseline["status"])
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("status" in error for error in result["errors"])
        )

    def test_renderer_writes_preview_and_fragment_with_distinct_media_sources(self):
        output_dir = Path(self.temp.name) / "dist"
        command = [
            sys.executable,
            str(SCRIPTS / "render_rich_post.py"),
            str(self.post),
            "--output-dir",
            str(output_dir),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)

        preview = (output_dir / "rich-test-rich-preview.html").read_text(
            encoding="utf-8"
        )
        fragment = (output_dir / "rich-test-tistory-fragment.html").read_text(
            encoding="utf-8"
        )
        self.assertEqual(1, preview.count("<h1>"))
        self.assertNotIn("<h1>", fragment)
        self.assertIn('<figure class="devlog-rich__figure"', preview)
        self.assertIn("<figcaption", preview)
        self.assertIn('href="#설치-직후-확인할-화면"', preview)
        self.assertIn('<h2 id="설치-직후-확인할-화면">', preview)
        self.assertIn(
            'aria-labelledby="설치-직후-확인할-화면"',
            preview,
        )
        self.assertIn("../2026-07-30-rich-test/assets/screenshots/lead.png", preview)
        self.assertIn("Codex 브라우저 실행 캡처 · 2026-07-30", preview)
        self.assertIn("__TISTORY_MEDIA_LEAD_SCREEN__", fragment)
        self.assertNotIn("{{media:", preview)
        self.assertNotIn(str(self.post.resolve()), preview)

    def test_renderer_uses_final_tistory_url_in_strict_mode(self):
        final_url = "https://blog.kakaocdn.net/example/lead.png"
        self.manifest["items"][0]["tistory_url"] = final_url
        self.write_manifest()
        self.write_qa()
        output_dir = Path(self.temp.name) / "dist"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
                "--require-publish-urls",
                "--preview-media-source",
                "remote",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        fragment = (output_dir / "rich-test-tistory-fragment.html").read_text(
            encoding="utf-8"
        )
        self.assertIn(final_url, fragment)
        self.assertNotIn("__TISTORY_MEDIA_", fragment)

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
                "--require-publish-urls",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, completed.returncode)
        self.assertIn("--preview-media-source remote", completed.stderr)

    def test_renderer_identifies_simulated_capture_in_public_credit(self):
        self.manifest["items"][0]["origin"] = "simulated"
        self.manifest["items"][0]["actor"] = "iOS 시뮬레이터"
        self.write_manifest()
        output_dir = Path(self.temp.name) / "dist"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        preview = (output_dir / "rich-test-rich-preview.html").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "iOS 시뮬레이터 시뮬레이션 캡처 · 2026-07-30",
            preview,
        )

    def test_rejects_empty_claim_mapping_and_unknown_directive(self):
        self.manifest["items"][0]["claim_ids"] = []
        self.write_manifest()
        article = (self.post / "article.md").read_text(encoding="utf-8")
        (self.post / "article.md").write_text(
            article.replace(
                "{{media:lead-screen}}",
                "{{media:lead-screen}}\n\n{{media:not-registered}}",
            ),
            encoding="utf-8",
        )

        result = validate_bundle(self.post)
        self.assertTrue(
            any("claim_ids" in error for error in result["errors"])
        )
        self.assertTrue(
            any("not registered" in error for error in result["errors"])
        )

    def test_rejects_non_object_manifest_unsafe_slug_and_source_url(self):
        (self.post / "media.json").write_text("[]\n", encoding="utf-8")
        result = validate_bundle(self.post)
        self.assertTrue(
            any("root must be an object" in error for error in result["errors"])
        )

        self.write_manifest()
        article = (self.post / "article.md").read_text(encoding="utf-8")
        (self.post / "article.md").write_text(
            article.replace("slug: rich-test", "slug: ../../escape"),
            encoding="utf-8",
        )
        self.manifest["items"][0]["source_url"] = "javascript:alert(1)"
        self.manifest["items"][0]["tistory_url"] = "https://example.com/lead.png"
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(any("kebab-case `slug`" in error for error in result["errors"]))
        self.assertTrue(
            any("source_url must be an HTTPS URL" in error for error in result["errors"])
        )
        self.assertTrue(
            any(
                "tistory_url must be an allowed Tistory CDN URL" in error
                for error in result["errors"]
            )
        )

        self.manifest["items"][0]["source_url"] = ""
        self.manifest["items"][0]["tistory_url"] = ""
        self.manifest["items"][0]["publish_path"] = (
            "assets/../screenshots-outside-assets.png"
        )
        self.manifest["items"][0]["raw_path"] = (
            "artifacts/captures/../../assets/screenshots/lead.png"
        )
        (self.post / "screenshots-outside-assets.png").write_bytes(PNG_BYTES)
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "publish_path must resolve under assets/" in error
                for error in result["errors"]
            )
        )
        self.assertTrue(
            any(
                "raw_path must resolve under artifacts/" in error
                for error in result["errors"]
            )
        )

    def test_code_fence_content_is_not_a_section_or_media_directive(self):
        article = (self.post / "article.md").read_text(encoding="utf-8")
        fenced = """```bash
### 셸 주석은 섹션이 아님
{{media:not-registered}}
```

"""
        (self.post / "article.md").write_text(
            article.replace(
                "### 설치 직후 확인할 화면",
                fenced + "### 설치 직후 확인할 화면",
            ),
            encoding="utf-8",
        )
        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        self.assertEqual(["lead-screen"], result["directives"])

        output_dir = Path(self.temp.name) / "dist"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        preview = (output_dir / "rich-test-rich-preview.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('id="셸-주석은-섹션이-아님"', preview)
        self.assertNotIn('data-media-id="not-registered"', preview)
        self.assertIn("{{media:not-registered}}", preview)

    def test_strict_gate_rejects_stale_qa_and_generated_product_screenshot(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        article = (self.post / "article.md").read_text(encoding="utf-8")
        (self.post / "article.md").write_text(
            article + "\n검수 뒤 추가된 문장입니다.\n",
            encoding="utf-8",
        )
        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("article_content_sha256" in error for error in result["errors"])
        )

        (self.post / "article.md").write_text(article, encoding="utf-8")
        self.manifest["items"][0]["origin"] = "generated"
        self.manifest["items"][0]["kind"] = "screenshot"
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "generated media must use kind `image`" in error
                for error in result["errors"]
            )
        )

    def test_ready_transition_keeps_content_bound_qa_valid(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        self.write_independent_review()
        article = (self.post / "article.md").read_text(encoding="utf-8")
        (self.post / "article.md").write_text(
            article.replace("status: reviewing", "status: ready"),
            encoding="utf-8",
        )

        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])

    def test_ready_transition_requires_persisted_independent_pass(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        article_path = self.post / "article.md"
        article = article_path.read_text(encoding="utf-8")
        article_path.write_text(
            article.replace("status: reviewing", "status: ready"),
            encoding="utf-8",
        )

        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "missing artifacts/qa/independent-final-page.json" in error
                for error in result["errors"]
            )
        )

    def test_ready_gate_binds_independent_reviewer_and_remote_verification(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        self.write_manifest()
        self.write_qa()
        self.write_independent_review()
        article_path = self.post / "article.md"
        article = article_path.read_text(encoding="utf-8")
        article_path.write_text(
            article.replace("status: reviewing", "status: ready"),
            encoding="utf-8",
        )
        review_path = (
            self.post
            / "artifacts"
            / "qa"
            / "independent-final-page.json"
        )
        original_review = review_path.read_bytes()
        review = json.loads(original_review)
        review["checked_by"] = "creator test reviewer"
        review_path.write_text(
            json.dumps(review, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "reviewer must differ" in error for error in result["errors"]
            )
        )

        review_path.write_bytes(original_review)
        verification_path = (
            self.post
            / "artifacts"
            / "qa"
            / "remote-media-verification.json"
        )
        verification_path.write_bytes(verification_path.read_bytes() + b"\n")
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "remote_verification_sha256" in error
                for error in result["errors"]
            )
        )

    def test_body_status_line_still_invalidates_content_qa(self):
        self.manifest["items"][0]["tistory_url"] = (
            "https://blog.kakaocdn.net/example/lead.png"
        )
        article_path = self.post / "article.md"
        article = article_path.read_text(encoding="utf-8")
        article_path.write_text(
            article + "\n```text\nstatus: failed\n```\n",
            encoding="utf-8",
        )
        self.write_manifest()
        self.write_qa()
        article_path.write_text(
            article + "\n```text\nstatus: passed\n```\n",
            encoding="utf-8",
        )

        result = validate_bundle(self.post, require_publish_urls=True)
        self.assertTrue(
            any("article_content_sha256" in error for error in result["errors"])
        )

    def test_gif_requires_a_short_clip_and_renders_a_static_fallback(self):
        (self.post / "assets" / "demos").mkdir(parents=True)
        (self.post / "assets" / "demos" / "step.gif").write_bytes(GIF_BYTES)
        (self.post / "assets" / "screenshots" / "step-poster.png").write_bytes(
            GIF_POSTER_BYTES
        )
        article = (self.post / "article.md").read_text(encoding="utf-8")
        (self.post / "article.md").write_text(
            article.replace(
                "### 결과가 달라지는 지점",
                "{{media:step-motion}}\n\n### 결과가 달라지는 지점",
            ),
            encoding="utf-8",
        )
        self.manifest["items"].extend(
            [
                {
                    "id": "step-motion",
                    "kind": "gif",
                    "origin": "official",
                    "role": "change",
                    "claim_ids": ["C02"],
                    "source_url": "https://example.com/official-demo",
                    "publish_path": "assets/demos/step.gif",
                    "tistory_url": "",
                    "width": 480,
                    "height": 300,
                    "display_width": 480,
                    "placement": "before:result-section",
                    "rights": "official documentation asset with attribution",
                    "alt": "설정 상태가 완료로 바뀌는 짧은 동작",
                    "caption": "상태가 바뀌는 순간만 짧게 보여줍니다.",
                    "processing": [],
                    "redactions": [],
                    "sha256": hashlib.sha256(GIF_BYTES).hexdigest(),
                    "status": "validated",
                    "poster_id": "step-poster",
                    "duration_seconds": 4.2,
                },
                {
                    "id": "step-poster",
                    "kind": "image",
                    "origin": "official",
                    "role": "poster",
                    "claim_ids": ["C02"],
                    "source_url": "https://example.com/official-demo",
                    "publish_path": "assets/screenshots/step-poster.png",
                    "tistory_url": "",
                    "width": 480,
                    "height": 300,
                    "display_width": 480,
                    "placement": "gif-fallback:step-motion",
                    "rights": "official documentation asset with attribution",
                    "alt": "설정 완료 상태를 보여주는 정지 화면",
                    "caption": "움직임을 줄인 환경에서는 완료 화면을 표시합니다.",
                    "processing": ["frame_extract"],
                    "redactions": [],
                    "sha256": hashlib.sha256(GIF_POSTER_BYTES).hexdigest(),
                    "status": "validated",
                    "derived_from": "step-motion",
                },
            ]
        )
        self.write_manifest()

        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        output_dir = Path(self.temp.name) / "dist"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "render_rich_post.py"),
                str(self.post),
                "--output-dir",
                str(output_dir),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        preview = (output_dir / "rich-test-rich-preview.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("devlog-rich__motion", preview)
        self.assertIn("devlog-rich__poster", preview)
        self.assertIn("@media (prefers-reduced-motion: reduce)", preview)

        self.manifest["items"][1]["duration_seconds"] = 4.0
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any("differs from file duration" in error for error in result["errors"])
        )

        self.manifest["items"][1]["duration_seconds"] = 4.2
        self.manifest["items"][2]["processing"] = None
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "GIF poster processing must record" in error
                for error in result["errors"]
            )
        )

        self.manifest["items"][2]["processing"] = ["frame_extract"]
        self.manifest["items"][2]["width"] = 479
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any(
                "poster and GIF must use identical dimensions" in error
                for error in result["errors"]
            )
        )

        self.manifest["items"][2]["width"] = 480
        self.manifest["items"][1]["duration_seconds"] = 5.1
        self.write_manifest()
        result = validate_bundle(self.post)
        self.assertTrue(
            any("exceeds five seconds" in error for error in result["errors"])
        )


if __name__ == "__main__":
    unittest.main()
