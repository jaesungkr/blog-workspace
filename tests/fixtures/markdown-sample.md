---
title: "마크다운 변환 회귀 테스트"
slug: markdown-render-test
date: 2026-07-25
category: "Log"
subcategory: "개발 · 디지털"
status: drafting
tags: [마크다운, 티스토리]
summary: "변환기가 주요 마크다운 문법을 보존하는지 확인하는 테스트입니다."
hero_image: assets/hero.png
published_url: ""
sources: [https://dop3n.tistory.com]
---

안녕하세요. dev.log입니다.

이 파일은 변환기의 주요 문법을 한 번에 확인하는 회귀 테스트입니다.

### 인라인 문법

**굵게**와 *기울임*, `인라인 코드`, ~~취소선~~, 그리고
[링크](https://dop3n.tistory.com)가 한 문단에 섞여 있습니다.

### 표와 정렬

| 항목 | 값 | 비고 |
|:---|---:|:---:|
| 왼쪽 정렬 | 1,200 | 가운데 |
| 두 번째 행 | 980 | `코드 셀` |

### 목록과 코드

- 첫 번째 항목
- 두 번째 항목
    - 안쪽 항목

```python
def hello(name):
    print(f"안녕하세요, {name}님")
```

### 인용

> 모델의 이름보다 작업의 모양이 먼저입니다.
> 두 번째 줄도 같은 인용 블록에 들어갑니다.

<!-- 이 주석은 변환 결과에서 제거되어야 합니다. -->
