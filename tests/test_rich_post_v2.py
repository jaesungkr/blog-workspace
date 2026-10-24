import binascii
import hashlib
import json
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "dev-log-rich-post-workspace-v2"
SCRIPTS = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS))

from render_rich_post_v2 import render_outputs
from rich_post_v2_common import (
    CAPTURE_VIEWPORTS,
    merge_browser_capture_viewports,
    validate_bundle,
    validate_source_pass,
    native_attachment_error,
    native_tistory_reference,
)
from tistory_media_map_v2 import run_set_url


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

    def bind_native_fixture(self):
        self.workflow["publication_mode"] = "codex-browser"
        self.write_workflow()
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        item = manifest["items"][0]
        item["tistory_embed"] = (
            '[##_Image|kage@asset/post/long-key/img.png|alignCenter|'
            'width="100%" alt="공식 공개 화면"|_##]'
        )
        item["tistory_url"] = (
            "https://blog.kakaocdn.net/dna/asset/post/signed-preview-key/img.png"
            "?expires=1793458799&signature=example"
        )
        path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        return item

    def test_native_publication_keeps_attachment_reference_out_of_preview_urls(self):
        item = self.bind_native_fixture()
        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        for theme in ("light", "dark"):
            preview, fragment = render_outputs(
                result, self.post / "dist", preview_media_source="remote",
                preview_theme=theme,
            )
            self.assertIn(item["tistory_embed"], fragment)
            self.assertNotIn('expires=1793458799', fragment)
            self.assertNotIn('[##_Image|', preview)
            self.assertIn('expires=1793458799', preview)
            self.assertIn('<div class="devlog-rich__figure"', fragment)
            self.assertNotIn('<figure class="devlog-rich__figure"', fragment)
            self.assertIn('transform: none !important;', fragment)

    def test_browser_release_cannot_use_only_a_signed_display_url(self):
        self.bind_native_fixture()
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        del manifest["items"][0]["tistory_embed"]
        path.write_text(json.dumps(manifest), encoding="utf-8")
        errors = validate_bundle(self.post, require_publish_urls=True)["errors"]
        self.assertTrue(any('browser publication requires tistory_embed' in e for e in errors))

    def test_native_binder_rejects_another_asset_without_mutating_manifest(self):
        item = self.bind_native_fixture()
        path = self.post / "media.json"
        before = path.read_bytes()
        result = validate_bundle(self.post)
        with redirect_stderr(StringIO()), redirect_stdout(StringIO()):
            status = run_set_url(
                result, self.post, "lead",
                "https://blog.kakaocdn.net/dna/another/post/key/img.png",
                item["tistory_embed"],
            )
        self.assertEqual(1, status)
        self.assertEqual(before, path.read_bytes())

    def test_captured_native_block_can_be_bound_and_rendered_through_cli(self):
        item = self.bind_native_fixture()
        native = item["tistory_embed"]
        url = item["tistory_url"]
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        del manifest["items"][0]["tistory_embed"]
        manifest["items"][0]["tistory_url"] = ""
        path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        captured = self.post / "artifacts" / "qa-v2" / "attachments" / "lead.txt"
        captured.parent.mkdir(parents=True)
        captured.write_text(native, encoding="utf-8")
        commands = [
            ["record_source_pass_v2.py", str(self.post), "--by", "source reviewer"],
            ["tistory_media_map_v2.py", "set-embed", str(self.post), "lead",
             "--embed-file", str(captured), "--url", url],
            ["render_rich_post_v2.py", str(self.post), "--output-dir",
             str(self.post / "dist"), "--preview-media-source", "remote"],
        ]
        for command in commands:
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / command[0]), *command[1:]],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
        fragment = (self.post / "dist" / "v2-test-tistory-fragment.html").read_text()
        self.assertIn(native, fragment)
        self.assertNotIn("expires=1793458799", fragment)

    def test_native_block_validation_preserves_real_formats_and_rejects_extra_html(self):
        item = self.bind_native_fixture()
        reference = 'kage@asset/post/long-key/img.png'
        self.assertEqual(reference, native_tistory_reference(item["tistory_embed"]))
        cdm = '[##_Image|' + reference + '|CDM|1.3|{"originWidth":760,"style":"alignCenter"}_##]'
        self.assertEqual(reference, native_tistory_reference(cdm))
        signed = item["tistory_embed"].replace('img.png|', 'img.png?expires=123&amp;signature=test|')
        self.assertIsNotNone(native_tistory_reference(signed))
        for invalid in (
            '<img src="https://blog.kakaocdn.net/image.png">',
            item["tistory_embed"] + item["tistory_embed"],
            item["tistory_embed"].replace('width="100%"', 'onerror="alert(1)"'),
        ):
            self.assertIsNone(native_tistory_reference(invalid))
        from urllib.parse import quote
        thumbnail = dict(item, tistory_url=(
            'https://img1.daumcdn.net/thumb/R1280x0/?fname=' + quote(item['tistory_url'], safe='')
        ))
        self.assertIsNone(native_attachment_error(thumbnail))

    def test_native_alt_matches_manifest_in_cdm_and_attribute_formats(self):
        item = self.bind_native_fixture()
        reference = 'kage@asset/post/long-key/img.png?expires=123&amp;signature=test'
        expected = 'A & B 사양 화면'
        blocks = [
            '[##_Image|' + reference + '|CDM|1.3|'
            + json.dumps({"originWidth": 760, "alt": expected}, ensure_ascii=False)
            + '_##]',
            '[##_Image|' + reference + '|alignCenter|'
            'width="100%" alt="A &amp; B 사양 화면"|_##]',
            '[##_Image|' + reference + "|alignLeft|alt='A &amp; B 사양 화면'|_##]",
        ]
        for block in blocks:
            with self.subTest(block=block):
                candidate = dict(item, alt=expected, tistory_embed=block)
                self.assertIsNone(native_attachment_error(candidate))

    def test_native_alt_rejects_missing_blank_wrong_and_ambiguous_values(self):
        item = self.bind_native_fixture()
        reference = 'kage@asset/post/long-key/img.png'
        metadata = [{}, {"alt": None}, {"alt": 123}, {"alt": ""},
                    {"alt": " \n "}, {"alt": "다른 이미지 설명"}]
        blocks = [
            '[##_Image|' + reference + '|CDM|1.3|'
            + json.dumps(value, ensure_ascii=False) + '_##]'
            for value in metadata
        ]
        blocks.extend(
            '[##_Image|' + reference + '|alignCenter|' + attrs + '|_##]'
            for attrs in (
                'width="100%"',
                'alt=""',
                'alt="  "',
                'alt="다른 이미지 설명"',
                'data-alt="공식 공개 화면"',
                'alt="공식 공개 화면" alt="다른 이미지 설명"',
            )
        )
        for block in blocks:
            with self.subTest(block=block):
                error = native_attachment_error(dict(item, tistory_embed=block))
                self.assertIsNotNone(error)
                self.assertIn('alt', error)

    def test_invalid_native_alt_blocks_binding_without_mutating_manifest(self):
        item = self.bind_native_fixture()
        path = self.post / "media.json"
        before = path.read_bytes()
        result = validate_bundle(self.post)
        for alt in (None, '다른 이미지 설명'):
            metadata = {} if alt is None else {"alt": alt}
            block = ('[##_Image|kage@asset/post/long-key/img.png|CDM|1.3|'
                     + json.dumps(metadata, ensure_ascii=False) + '_##]')
            with self.subTest(alt=alt), redirect_stderr(StringIO()), redirect_stdout(StringIO()):
                status = run_set_url(result, self.post, "lead", item["tistory_url"], block)
                self.assertEqual(1, status)
                self.assertEqual(before, path.read_bytes())

    def test_bundle_rejects_native_alt_that_only_exists_in_manifest(self):
        self.bind_native_fixture()
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["items"][0]["tistory_embed"] = (
            '[##_Image|kage@asset/post/long-key/img.png|CDM|1.3|'
            '{"originWidth":760,"style":"alignCenter"}_##]'
        )
        path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        errors = validate_bundle(self.post, require_publish_urls=True)["errors"]
        self.assertTrue(any('native attachment must include nonempty alt' in e for e in errors))

    def test_cli_can_repair_selected_native_alt_but_keeps_other_errors(self):
        item = self.bind_native_fixture()
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["items"][0]["tistory_embed"] = (
            '[##_Image|kage@asset/post/long-key/img.png|CDM|1.3|{}_##]'
        )
        broken_manifest = json.dumps(manifest, ensure_ascii=False)
        captured = self.post / "repaired.txt"
        captured.write_text(item["tistory_embed"], encoding="utf-8")
        source = subprocess.run(
            [sys.executable, str(SCRIPTS / "record_source_pass_v2.py"),
             str(self.post), "--by", "source reviewer"],
            capture_output=True, text=True,
        )
        self.assertEqual(0, source.returncode, source.stderr)
        path.write_text(broken_manifest, encoding="utf-8")
        command = [sys.executable, str(SCRIPTS / "tistory_media_map_v2.py"),
                   "set-embed", str(self.post), "lead", "--embed-file", str(captured),
                   "--url", item["tistory_url"]]
        repaired = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, repaired.returncode, repaired.stderr)
        self.assertEqual([], validate_bundle(self.post)["errors"])

        # The selected-alt repair exception must not permit an unreviewed source.
        path.write_text(broken_manifest, encoding="utf-8")
        article = self.post / "article.md"
        article.write_text(article.read_text(encoding="utf-8") + "\n추가한 주장입니다.\n",
                           encoding="utf-8")
        rejected = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, rejected.returncode)
        self.assertEqual(broken_manifest, path.read_text(encoding="utf-8"))

    def test_alt_repair_cli_reports_malformed_manifest_without_traceback(self):
        item = self.bind_native_fixture()
        path = self.post / "media.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["items"] = None
        path.write_text(json.dumps(manifest), encoding="utf-8")
        captured = self.post / "captured.txt"
        captured.write_text(item["tistory_embed"], encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "tistory_media_map_v2.py"),
             "set-embed", str(self.post), "lead", "--embed-file", str(captured),
             "--url", item["tistory_url"]],
            capture_output=True, text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("ERROR:", result.stderr)

    def test_public_caption_omits_internal_media_origin_label(self):
        result = validate_bundle(self.post)
        self.assertEqual([], result["errors"])
        preview, fragment = render_outputs(result, self.post / "dist")
        for output in (preview, fragment):
            self.assertIn("공식 페이지에서 확인한 공개 화면입니다.", output)
            self.assertNotIn('class="devlog-rich__credit"', output)
            self.assertNotIn("공식 자료", output)

    def test_post_css_reaches_both_themes_and_fragment_without_global_changes(self):
        result = validate_bundle(self.post)
        original = render_outputs(result, self.post / "dist")
        path = self.post / "assets" / "post.css"
        override = ".devlog-rich table { min-width: 0; table-layout: fixed; }"
        path.write_text(override, encoding="utf-8")
        for theme in ("light", "dark"):
            preview, fragment = render_outputs(
                result, self.post / "dist", preview_theme=theme
            )
            for output in (preview, fragment):
                self.assertIn(override, output)
                self.assertGreater(output.index(override), output.index("min-width: 620px"))
        path.unlink()
        self.assertEqual(original, render_outputs(result, self.post / "dist"))

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

    def test_optional_capture_profiles_merge_with_human_review(self):
        self.assertEqual(
            {1280: 900, 360: 800, 390: 844, 768: 900},
            CAPTURE_VIEWPORTS,
        )
        receipt = {
            "viewports": [
                {"width": width, "height": height}
                for width, height in CAPTURE_VIEWPORTS.items()
            ]
        }
        human_viewports = [
            {"width": width, "readable_media": True, "status": "pass"}
            for width in CAPTURE_VIEWPORTS
        ]
        errors = []

        merged = merge_browser_capture_viewports(
            receipt,
            human_viewports,
            errors,
        )

        self.assertEqual([], errors)
        self.assertEqual(set(CAPTURE_VIEWPORTS), {item["width"] for item in merged})

    def test_human_review_must_cover_every_captured_optional_profile(self):
        receipt = {
            "viewports": [
                {"width": 1280, "height": 900},
                {"width": 360, "height": 800},
                {"width": 390, "height": 844},
            ]
        }
        errors = []

        merge_browser_capture_viewports(
            receipt,
            [
                {"width": 1280, "readable_media": True, "status": "pass"},
                {"width": 360, "readable_media": True, "status": "pass"},
            ],
            errors,
        )

        self.assertIn(
            "browser measurements must cover exactly the captured widths",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
