import argparse
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import blog  # noqa: E402


VALID_ARTICLE = """---
title: "테스트 글의 선택 기준"
slug: test-post
date: 2026-07-25
category: "Log"
subcategory: "개발 · 디지털"
status: drafting
tags: [테스트]
summary: ""
hero_image: assets/hero.png
published_url: ""
sources: []
---

안녕하세요. dev.log입니다.

익숙한 문제에서 출발하는 테스트 본문입니다.

### 핵심 선택 기준

근거를 확인한 뒤 본문을 완성합니다.
"""


def make_bundle(base: Path, article: str = VALID_ARTICLE) -> Path:
    post = base / "2026-07-25-test-post"
    (post / "assets").mkdir(parents=True)
    (post / "artifacts").mkdir()
    (post / "brief.md").write_text("# 기획\n", encoding="utf-8")
    (post / "evidence.md").write_text("# 근거\n", encoding="utf-8")
    (post / "audit.md").write_text("# 감사\n", encoding="utf-8")
    (post / "article.md").write_text(article, encoding="utf-8")
    return post


class BlogCheckerTests(unittest.TestCase):
    def test_drafting_bundle_has_no_errors(self):
        with tempfile.TemporaryDirectory() as temp:
            post = make_bundle(Path(temp))
            diagnostics = blog.check_post(post)

        self.assertFalse([item for item in diagnostics if item.level == "ERROR"])

    def test_title_and_h2_are_rejected(self):
        article = VALID_ARTICLE.replace(
            'title: "테스트 글의 선택 기준"',
            'title: "테스트 글입니다"',
        ).replace("### 핵심 선택 기준", "## 핵심 기준입니다")
        with tempfile.TemporaryDirectory() as temp:
            post = make_bundle(Path(temp), article)
            messages = [item.message for item in blog.check_post(post)]

        self.assertTrue(any("제목이 `~다`" in message for message in messages))
        self.assertTrue(any("`###`" in message for message in messages))
        self.assertTrue(any("소제목이 `~다`" in message for message in messages))

    def test_ready_bundle_requires_summary_sources_image_and_audit(self):
        article = VALID_ARTICLE.replace("status: drafting", "status: ready")
        with tempfile.TemporaryDirectory() as temp:
            post = make_bundle(Path(temp), article)
            messages = [item.message for item in blog.check_post(post)]

        self.assertTrue(any("summary" in message for message in messages))
        self.assertTrue(any("sources" in message for message in messages))
        self.assertTrue(any("대표 이미지" in message for message in messages))

    def test_ready_bundle_can_pass_automated_gate(self):
        article = (
            VALID_ARTICLE.replace("status: drafting", "status: ready")
            .replace('summary: ""', 'summary: "검증된 테스트 글입니다."')
            .replace("sources: []", "sources: [https://example.com/source]")
        )
        with tempfile.TemporaryDirectory() as temp:
            post = make_bundle(Path(temp), article)
            (post / "assets" / "hero.png").write_bytes(b"\x89PNG\r\n\x1a\n")
            (post / "evidence.md").write_text(
                "# 근거\n\n상태 설명에는 `미확인`이라는 단어도 사용할 수 있습니다.\n",
                encoding="utf-8",
            )
            (post / "audit.md").write_text(
                "# 감사\n\n- [x] 실제 원고를 확인했습니다.\n",
                encoding="utf-8",
            )
            diagnostics = blog.check_post(post)

        self.assertFalse([item for item in diagnostics if item.level == "ERROR"])

    def test_new_command_copies_complete_template_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            posts_dir = Path(temp) / "posts"
            args = argparse.Namespace(
                slug="new-post",
                title="새 글의 검증 기준",
                category="Log",
                subcategory="개발 · 디지털",
                date="2026-07-25",
            )
            with mock.patch.object(blog, "POSTS_DIR", posts_dir):
                result = blog.cmd_new(args)

            post = posts_dir / "2026-07-25-new-post"
            self.assertEqual(result, 0)
            self.assertTrue((post / "brief.md").is_file())
            self.assertTrue((post / "evidence.md").is_file())
            self.assertTrue((post / "article.md").is_file())
            self.assertTrue((post / "audit.md").is_file())
            self.assertTrue((post / "assets").is_dir())
            self.assertTrue((post / "artifacts").is_dir())


if __name__ == "__main__":
    unittest.main()
