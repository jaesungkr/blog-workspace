# blog-workspace 프로젝트 규칙

dop3n(박재성)의 티스토리 블로그 **dev.log** (https://dop3n.tistory.com) 글을
리서치 → 초안 → 윤문 → 발행용 HTML 까지 처리하는 작업 공간이다.

## 이 레포가 하는 일 / 하지 않는 일

- **한다**: 소재 조사, 초안 작성, 문체 교정, 티스토리 붙여넣기용 HTML 생성
- **하지 않는다**: 자동 발행. 티스토리 Open API는 2024년 2월 완전 종료됨.
  마지막 단계는 반드시 사람이 티스토리 에디터에 붙여넣는다.

## 디렉토리 규칙

| 경로 | 용도 |
|---|---|
| `research/` | 리서치 노트 (출처·인용 원본). 발행물 아님 |
| `drafts/` | 작성 중인 초안 `.md` |
| `published/` | 발행 완료한 글. 발행 후 `drafts/`에서 이동 |
| `dist/` | 변환된 티스토리용 `.html`. git 미추적 |
| `references/` | 문체·카테고리·SEO 규칙 (단일 진실 원천) |
| `.claude/skills/` | 워크플로우 스킬 |

파일명은 `YYYY-MM-DD-slug.md` 형식. slug는 영문 소문자 + 하이픈.

## 워크플로우

```
/research <주제>   → research/YYYY-MM-DD-slug.md   (출처 정리)
/write-post <주제> → drafts/YYYY-MM-DD-slug.md     (초안)
/polish <파일>     → 같은 파일 갱신                (AI 티 제거)
/to-tistory <파일> → dist/slug.html                (붙여넣기용)
```

각 단계는 독립 실행 가능하다. 이미 써둔 글만 변환해도 된다.

## 글 작성 시 반드시 지킬 것

1. **문체는 `references/voice.md`가 단일 진실 원천이다.** 글을 쓰기 전에 읽는다.
2. **카테고리 판별은 `references/categories.md`를 따른다.** 카테고리에 따라
   구조와 어투가 달라진다 (특히 Reflections는 다른 글과 어투가 다름).
3. **사실은 지어내지 않는다.** 수치·날짜·인용·제품명·성경 구절은
   `research/` 노트나 검색 결과에 근거가 있어야 한다. 근거가 없으면
   본문에 쓰지 말고 사용자에게 "확인 필요"로 보고한다.
4. **Health 카테고리 글에는 면책 문구를 넣는다.** (`references/categories.md` 참고)
5. **초안은 항상 파일로 저장한다.** 채팅 본문에 전체 글을 쏟아내지 않는다.
   사용자에게는 파일 경로 + 요약 + 확인이 필요한 항목만 보고한다.

## 프론트매터

모든 초안은 YAML 프론트매터로 시작한다.

```yaml
---
title: 글 제목
category: Log            # Log | Trends | Health | Reflections
subcategory: AI 개념·실전
tags: [태그1, 태그2, 태그3]
date: 2026-07-25
status: draft            # draft | polished | published
sources:                 # 근거 URL. 없으면 빈 배열
    - https://example.com
---
```

`to-tistory`는 프론트매터를 HTML로 변환하지 않고 메타 정보로만 쓴다.

## 코딩 컨벤션

- 들여쓰기 4 spaces
- 코드 주석 한국어
- 스크립트는 Python 표준 라이브러리만 사용 (외부 의존성 추가 금지)
