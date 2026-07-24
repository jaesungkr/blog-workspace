---
name: write-post
description: dev.log(dop3n.tistory.com) 블로그 글 초안을 dop3n 문체와 카테고리 구조에 맞춰 작성한다. 주제를 받아 카테고리를 판별하고 Log/Trends/Health/Reflections별 템플릿으로 drafts/에 md 초안을 만든다. "블로그 글 써줘", "이 주제로 초안", "포스팅 작성", "묵상글 정리" 같은 요청에 사용.
---

# 블로그 초안 작성

## 시작 전에 반드시 읽는다

1. `references/voice.md` — 문체 SSOT
2. `references/categories.md` — 카테고리 판별과 필수 요소
3. 해당 카테고리의 구조 파일 (아래 4단계)

읽지 않고 쓰면 문체가 어긋난다.

## 절차

### 1. 재료 확인

`research/`에 관련 노트가 있는지 먼저 찾는다.

- 있으면: 그 노트의 사실만 근거로 쓴다
- 없는데 사실 확인이 필요한 주제(수치·날짜·제품 스펙·성경 구절)면:
  **초안을 쓰기 전에 사용자에게 알린다.** "research 스킬을 먼저 돌릴까요?"
- 사용자가 그냥 쓰라고 하면, 확인 못 한 부분을 본문에
  `<!-- TODO: 출처 확인 필요 -->` 주석으로 남긴다

### 2. 카테고리 판별

`references/categories.md`의 기준으로 판단하고, **사용자에게 한 줄로 알린다.**
애매하면 후보 2개를 제시하고 고르게 한다.

### 3. 제목 3개 제안

`references/voice.md` §9 패턴으로 제목 후보 3개를 만들어 사용자에게 보여준다.
사용자가 고르거나 수정한 뒤 본문을 쓴다.

### 4. 카테고리별 구조 파일을 읽는다

| category | 읽을 파일 |
|---|---|
| Log | `references/log.md` |
| Trends | `references/trends.md` |
| Health | `references/health.md` |
| Reflections | `references/reflections.md` |

(스킬 디렉토리 기준 상대 경로: `.claude/skills/write-post/references/`)

### 5. 초안 작성

`drafts/YYYY-MM-DD-slug.md`에 저장한다. slug는 영문 소문자 + 하이픈.

프론트매터는 `CLAUDE.md`의 형식을 따른다.
`sources`에는 실제로 근거로 쓴 URL만 넣는다. 장식으로 채우지 않는다.

### 6. 보고

채팅에는 **본문 전체를 출력하지 않는다.** 아래만 보고한다:

- 저장 경로
- 카테고리 / 예상 글자 수
- 소제목 목록 (개요만)
- **확인이 필요한 항목** — TODO 주석을 남긴 곳, 근거가 약한 주장
- 다음 단계 안내 (`polish` → `to-tistory`)

## 지킬 것

- **사실을 지어내지 않는다.** 특히 수치, 날짜, 가격, 벤치마크 점수,
  성경 구절 원문, 약 용량. 모르면 TODO를 남기고 사용자에게 보고한다
- 분량을 채우려고 같은 내용을 반복하지 않는다
- Health 글은 면책 문구를 반드시 넣는다
- 초안 단계에서 완벽한 문체를 목표로 하지 않는다. 구조와 사실이 먼저다.
  문체는 `polish`가 다듬는다
- 이미지는 넣지 않는다. 자리만 `<!-- 이미지: 설명 -->`로 표시한다
