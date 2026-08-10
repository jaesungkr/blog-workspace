import binascii
import hashlib
import json
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "dev-log-rich-post-workspace-v2"
SCRIPTS = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS))

from render_rich_post_v2 import render_outputs
from rich_post_v2_common import validate_bundle, validate_source_pass


def png_bytes(width=760, height=480):
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


class RichPostV2Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.post = Path(self.temp.name) / "2026-08-10-v2-test"
        asset_dir = self.post / "assets" / "screenshots"
        asset_dir.mkdir(parents=True)
        self.asset = asset_dir / "lead.png"
        self.asset.write_bytes(png_bytes())

        (self.post / "brief.md").write_text(
            "# 브리프\n\n독자와 시작 경로를 기록합니다.\n",
            encoding="utf-8",
        )
        (self.post / "evidence.md").write_text(
            "# 근거 지도\n\n"
            "| ID | 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |\n"
            "|---|---|---|---|---|---|\n"
            "| C01 | 공개 화면 | 공식 | 확인 | 공식 페이지 | 시점 제한 |\n",
            encoding="utf-8",
        )
        (self.post / "article.md").write_text(
            """---
title: "v2 검증 글"
slug: v2-test
date: 2026-08-10
category: Log
subcategory: "개발 · 디지털"
status: reviewing
format: rich-post-v2
hero_image: assets/screenshots/lead.png
summary: "v2 게이트를 검증합니다."
---
안녕하세요. dev.log입니다.

처음 보는 독자도 시작 위치를 알 수 있도록 설명합니다.

{{media:lead}}

### 어디서 시작할까요?

공식 페이지에서 시작합니다.
""",
            encoding="utf-8",
        )
        self.workflow = {
            "version": 2,
            "profile": "standard-rich",
            "scope": "complete",
            "primary_reader": "처음 접하는 검색 독자",
            "direct_capture": False,
            "gif": False,
            "generated_lead": False,
            "infographic": False,
            "complex_layout": False,
            "high_risk_remote_media": False,
            "include_390": False,
            "include_768": False,
            "second_remote_fetch": False,
            "decision_note": "정적 공식 이미지",
        }
        self.write_workflow()
        media = {
            "version": 2,
            "lead_id": "lead",
            "items": [
                {
                    "id": "lead",
                    "kind": "image",
                    "origin": "official",
                    "role": "lead",
                    "claim_ids": ["C01"],
                    "source_url": "https://example.com/official",
                    "publish_path": "assets/screenshots/lead.png",
                    "tistory_url": "",
                    "width": 760,
                    "height": 480,
                    "display_width": 760,
                    "placement": "after:opening",
                    "rights": "official publication asset",
                    "alt": "공식 공개 화면",
                    "caption": "공식 페이지에서 확인한 공개 화면입니다.",
                    "processing": [],
                    "redactions": [],
                    "sha256": hashlib.sha256(self.asset.read_bytes()).hexdigest(),
                    "status": "validated",
                }
            ],
        }
        (self.post / "media.json").write_text(
            json.dumps(media, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def write_workflow(self):
        (self.post / "workflow-v2.json").write_text(
            json.dumps(self.workflow, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def test_standard_static_bundle_skips_capture_plan_and_renders(self):
        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        preview, fragment = render_outputs(result, self.post / "dist")
        self.assertIn("<h1>v2 검증 글</h1>", preview)
        self.assertNotIn("<h1", fragment)
        self.assertIn("source-frozen article surface", preview)

    def test_screenshot_can_opt_into_mobile_horizontal_scroll(self):
        media_path = self.post / "media.json"
        media = json.loads(media_path.read_text(encoding="utf-8"))
        item = media["items"][0]
        item["kind"] = "screenshot"
        item["mobile_scroll_width"] = 640
        media_path.write_text(
            json.dumps(media, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        preview, fragment = render_outputs(result, self.post / "dist")
        for output in (preview, fragment):
            self.assertIn("devlog-rich__figure--scroll-mobile", output)
            self.assertIn("--rich-mobile-scroll-width:640px", output)
            self.assertIn("스크린샷 가로 스크롤", output)

    def test_mobile_scroll_width_rejects_non_screenshot_media(self):
        media_path = self.post / "media.json"
        media = json.loads(media_path.read_text(encoding="utf-8"))
        media["items"][0]["mobile_scroll_width"] = 640
        media_path.write_text(
            json.dumps(media, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        result = validate_bundle(self.post)
        self.assertTrue(
            any("only supported for screenshots" in error for error in result["errors"])
        )

    def test_source_pass_is_bound_and_article_edit_invalidates_it(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "record_source_pass_v2.py"),
                str(self.post),
                "--by",
                "independent source reviewer",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)

        errors = []
        validate_source_pass(self.post, self.post / "article.md", errors)
        self.assertEqual([], errors)

        with (self.post / "article.md").open("a", encoding="utf-8") as handle:
            handle.write("\n검증 뒤 의미 있는 본문 변경입니다.\n")
        errors = []
        validate_source_pass(self.post, self.post / "article.md", errors)
        self.assertTrue(any("article_content_sha256" in error for error in errors))

    def test_routed_risks_open_only_their_required_gates(self):
        self.workflow["direct_capture"] = True
        self.write_workflow()
        result = validate_bundle(self.post)
        self.assertTrue(any("capture-plan.md" in error for error in result["errors"]))

        (self.post / "capture-plan.md").write_text("# 캡처 계획\n", encoding="utf-8")
        self.workflow["direct_capture"] = False
        self.workflow["high_risk_remote_media"] = True
        self.write_workflow()
        result = validate_bundle(self.post)
        self.assertTrue(any("second fetch" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
