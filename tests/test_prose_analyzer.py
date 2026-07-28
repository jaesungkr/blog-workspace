import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / ".agents"
    / "skills"
    / "dev-log-prose-polish"
    / "scripts"
    / "analyze_prose.py"
)
SPEC = importlib.util.spec_from_file_location("analyze_prose", SCRIPT)
ANALYZER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(ANALYZER)


class ProseAnalyzerTests(unittest.TestCase):
    def test_reports_heading_and_template_signals(self):
        article = """---
title: "테스트 글 - 한눈에 보는 결과"
---

안녕하세요. dev.log입니다.

### 기술의 정체

이번 글에서는 구조와 결과를 살펴보겠습니다. 하지만 결론적으로 중요한 점은
다른 곳에 있습니다.

### 저장소 작업 지침이 섞여 폐기한 첫 실험

처음 실행은 실패했습니다. 이 실패 때문에 환경을 바꿨습니다.
"""

        report = ANALYZER.analyze(article)

        self.assertEqual("테스트 글 - 한눈에 보는 결과", report["title"])
        self.assertEqual(2, report["summary"]["heading_count"])
        self.assertEqual(1, report["summary"]["headings_with_generic_signal"])
        self.assertEqual(1, report["stock_phrases"]["이번 글에서는"])
        self.assertGreater(report["corrective_frames"]["하지만"], 0)
        stock_match = next(
            match
            for match in report["matched_lines"]
            if match["signal"] == "이번 글에서는"
        )
        self.assertEqual(9, stock_match["line"])
        self.assertIn("구조와 결과", stock_match["excerpt"])

    def test_ignores_code_fences_and_table_rows_in_prose_counts(self):
        article = """---
title: "검사"
---

### 실제 관찰

본문 문장입니다.

```text
이번 글에서는 결과를 살펴보겠습니다.
```

| 결과 | 값 |
|---|---|
| 구조 | 1 |
"""

        report = ANALYZER.analyze(article)

        self.assertNotIn("이번 글에서는", report["stock_phrases"])
        self.assertEqual(1, report["summary"]["sentence_count"])
        self.assertEqual([], report["matched_lines"])

    def test_ignores_heading_syntax_inside_fenced_code(self):
        article = """---
title: "검사"
---

### 실제 관찰

```markdown
### 기술의 결과
이번 글에서는 정리해 보겠습니다.
```

본문만 분석합니다.
"""

        report = ANALYZER.analyze(article)

        self.assertEqual(1, report["summary"]["heading_count"])
        self.assertEqual("실제 관찰", report["headings"][0]["text"])
        self.assertNotIn("이번 글에서는", report["stock_phrases"])
        self.assertEqual([], report["matched_lines"])

    def test_fence_marker_type_and_length_do_not_close_each_other(self):
        article = """---
title: "검사"
---

### 바깥 제목

````markdown
```markdown
### 안쪽 제목
```
~~~
### 여전히 안쪽 제목
~~~
````

### 다시 바깥 제목
"""

        report = ANALYZER.analyze(article)

        self.assertEqual(
            ["바깥 제목", "다시 바깥 제목"],
            [heading["text"] for heading in report["headings"]],
        )

    def test_reports_long_sentence_and_ending_context(self):
        article = """---
title: "검사"
---

### 실제 관찰

이 문장은 분석기가 실제 파일 행과 함께 아주 긴 문장의 문맥을 보여 주는지 확인하기 위해 일부러 충분히 길게 작성했습니다.
"""

        report = ANALYZER.analyze(article)

        self.assertEqual(1, len(report["long_sentences"]))
        self.assertEqual(7, report["long_sentences"][0]["line"])
        self.assertIn("실제 파일 행", report["long_sentences"][0]["excerpt"])
        self.assertEqual(
            7, report["sentence_ending_samples"]["했습니다"][0]["line"]
        )


if __name__ == "__main__":
    unittest.main()
