import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import md2tistory  # noqa: E402


class MarkdownConverterTests(unittest.TestCase):
    def test_frontmatter_lists_are_parsed(self):
        raw = """---
title: 테스트
tags: [하나, 둘]
sources:
    - https://example.com/a
    - https://example.com/b
---

본문
"""
        meta, body = md2tistory.split_frontmatter(raw)

        self.assertEqual(meta["title"], "테스트")
        self.assertEqual(meta["tags"], ["하나", "둘"])
        self.assertEqual(
            meta["sources"],
            ["https://example.com/a", "https://example.com/b"],
        )
        self.assertEqual(body, "본문\n")

    def test_h3_table_code_and_link_render(self):
        body = """### 비교 기준

| 항목 | 값 |
|---|---:|
| 속도 | 3 |

```python
print("ok")
```

[공식 문서](https://example.com)
"""
        markup = md2tistory.convert(body)

        self.assertIn("<h3", markup)
        self.assertIn("<table", markup)
        self.assertIn("<pre", markup)
        self.assertIn('href="https://example.com"', markup)

    def test_sample_comments_can_be_removed_before_render(self):
        sample = ROOT / "tests" / "fixtures" / "markdown-sample.md"
        _, body = md2tistory.split_frontmatter(sample.read_text(encoding="utf-8"))
        body_without_comments = md2tistory.re.sub(
            r"<!--.*?-->",
            "",
            body,
            flags=md2tistory.re.DOTALL,
        )
        markup = md2tistory.convert(body_without_comments)

        self.assertNotIn("주석", markup)
        self.assertIn("인라인 문법", markup)


if __name__ == "__main__":
    unittest.main()
