# dev.log blog workspace

`dev.log`의 글을 기획하고, 근거를 모으고, 직접 검증하고, 원고와 이미지를 만든 뒤
티스토리에 옮기기 직전까지 관리하는 Codex 작업공간입니다.

핵심 기준은 하나입니다.

> 추측 대신 검증(Tested, not guessed)

자료를 매끈하게 요약하는 데서 끝내지 않습니다. 독자가 이 블로그에서만 얻을 수 있는
실험, 로그, 스크린샷, 데이터, 관찰 또는 판단 기준을 글마다 남깁니다.

## 빠른 시작

저장소 루트에서 Codex를 열고 자연어로 요청하면 `AGENTS.md`와 저장소 전용 스킬이
자동으로 적용됩니다.

```text
Claude Code 비용을 줄이는 실험 글을 새로 준비해줘.
이 글의 근거 표를 검토하고 빠진 1차 출처를 찾아줘.
posts/2026-07-25-example 원고를 발행 전 감사해줘.
```

명시적으로 전체 워크플로를 부르고 싶다면 `$dev-log-workspace`를 사용할 수
있습니다. 이 스킬은 글 작성, 대표 이미지, 보조 인포그래픽과 세 검증 스킬을
순서대로 호출하는 오케스트레이터입니다.

새 글의 빈 작업 묶음은 명령으로도 만들 수 있습니다.

```bash
python3 scripts/blog.py new claude-code-cost \
  --title "Claude Code 비용 줄이기, 재시도부터 측정한 결과" \
  --category Log \
  --subcategory "개발 · 디지털"
```

### Codex에서 작업을 시작하는 방법

가장 확실한 방법은 이 저장소 루트를 Codex 프로젝트로 연 뒤 자연어로 요청하는
것입니다. `AGENTS.md`가 저장소 전용 스킬과 검사·Git 워크플로를 자동으로
적용합니다.

```text
Opus 5와 Fable 5 비교 글을 dev.log 워크플로로 작성해줘.
근거, 원고, 대표 이미지, 감사를 글 묶음에 보존하고 검사 후 master에 올려줘.
```

스킬을 명시하고 싶다면 다음처럼 요청합니다.

```text
$dev-log-workspace를 사용해서 [주제] 글을 작성해줘.
완성된 글 묶음을 검사하고 origin/master에 푸시해줘.
```

특정 단계만 실행할 때는 하위 스킬을 직접 부를 수 있습니다.

```text
$dev-log-writing으로 원고와 근거만 작성해줘.
$dev-log-hero-image로 대표 이미지 후보를 만들고
$dev-log-hero-validation으로 캠페인급 품질을 검증해줘.
$dev-log-infographic로 보조 인포그래픽을 만들고
$dev-log-infographic-validation으로 360px 글자 겹침을 검증해줘.
$dev-log-article-validation으로 본문과 티스토리 렌더만 검사해줘.
```

프로젝트 없는 새 대화에서 시작했다면 저장소까지 함께 지정합니다.

```text
GitHub jaesungkr/blog-workspace의 dev-log-workspace 워크플로로
[주제] 글을 작성하고 검사·커밋·푸시해줘.
```

GitHub 푸시는 작업 아카이브이며 Tistory 자동 발행은 아닙니다. 실제 발행 URL을
받기 전까지 글 상태는 `ready`로 유지합니다.

### Git 관리본을 전역 Codex 스킬로 연결하기

다른 작업 폴더에서도 이 저장소의 최신 스킬을 직접 사용하려면 아래 명령을 한 번
실행합니다.

```bash
sh scripts/link_codex_skill.sh
```

이 명령은 `.agents/skills/`의 모든 `dev-log-*` 스킬을
`~/.codex/skills/`에 복사하지 않고 각각 심볼릭 링크로 연결합니다. 이후
오케스트레이터와 하위 스킬은 이 저장소에서만 수정하고 커밋·푸시합니다.

## 글 한 편의 구조

```text
posts/2026-07-25-claude-code-cost/
├── brief.md       # 독자, 검색 의도, 핵심 메시지, 독창성, 설명 순서
├── evidence.md    # 주장-출처-상태-한계, 실험 설계와 결과
├── article.md     # 티스토리에 게시할 Markdown 원고와 발행 메타데이터
├── audit.md       # 구조·근거·문체·이미지 최종 감사
├── assets/        # 생성 후 직접 확인한 대표·본문 이미지
└── artifacts/     # 코드, 입력, 원시 출력, 로그, 스크린샷
```

초안과 발행본을 다른 폴더로 옮기지 않습니다. 한 폴더를 유지하고 `article.md`의
`status`만 다음 순서로 바꿉니다.

```text
planning -> researching -> drafting -> reviewing -> ready -> published
```

이 방식은 어떤 근거와 실험에서 문장이 나왔는지 Git 이력과 함께 보존합니다.

## 기본 워크플로

1. `dev-log-writing`이 `brief.md`, `evidence.md`, `article.md`를 작성합니다.
2. `dev-log-article-validation`이 구조·근거·한국어 문장과 렌더를 검증합니다.
3. `dev-log-hero-image`가 주제에 맞는 아이코닉한 대표 이미지 후보를 만듭니다.
4. `dev-log-hero-validation`이 대기업 캠페인급 완성도와 주제 인식성을
   독립적으로 검증합니다.
5. `dev-log-infographic`이 설명상 필요한 경우에만 보조 인포그래픽을 만듭니다.
6. `dev-log-infographic-validation`이 원본·360px·확대 크롭에서 글자와
   화살표 겹침을 검증합니다.
7. 오케스트레이터가 최종 검사·렌더·커밋·푸시를 마무리하고, 사람은 생성된
   HTML과 이미지를 티스토리에 직접 올립니다.

## 명령

```bash
# 새 작업 묶음 만들기
python3 scripts/blog.py new my-post --title "제목" --category Log --subcategory "개발 · 디지털"

# 한 글 검사
python3 scripts/blog.py check posts/2026-07-25-my-post

# 전체 현재 글 검사
python3 scripts/blog.py check --all

# 티스토리 HTML 만들기
python3 scripts/blog.py render posts/2026-07-25-my-post

# 스크립트 회귀 테스트
python3 -m unittest discover -s tests -v
```

검사기는 자동으로 판단할 수 있는 형식 오류만 막습니다. 출처가 실제 주장을
뒷받침하는지, 설명 순서가 비개발자에게 자연스러운지, 문장이 사람의 책임과 판단을
담고 있는지는 `audit.md`를 읽고 직접 확인해야 합니다.

## 기준 문서

- `standards/editorial-standard.md`: 모든 글의 문체·구조·근거·최종 감사
- `standards/category-guides.md`: 현재 카테고리와 유형별 구성
- `standards/blog-memory.md`: 포트폴리오 현황과 주제 선정 우선순위
- `standards/image-guide.md`: 이미지 생성·검수·보관 기준
- `standards/reflections-guide.md`: 설교 묵상 글 전용 기준

`standards/`만 편집 기준의 단일 진실 원천으로 사용합니다. 템플릿은 구조를 돕는
빈 양식일 뿐, 모든 글에 같은 소제목이나 표를 강제하지 않습니다.

## 티스토리 발행

`python3 scripts/blog.py render ...`는 `dist/<slug>.html`을 만듭니다.

1. 티스토리 글쓰기에서 기본모드를 HTML로 바꿉니다.
2. 생성된 HTML을 붙여넣고 기본모드로 돌아옵니다.
3. `assets/`의 이미지를 직접 업로드하고 alt 텍스트를 넣습니다.
4. 카테고리·태그·영문 slug·요약을 확인한 뒤 발행합니다.
5. 발행 후 `status: published`와 `published_url`을 기록합니다.

자동 발행은 이 저장소의 범위가 아닙니다.

## 과거 Claude 구조

초기 Claude 기반 원고와 리서치는 `archive/legacy-claude/`에 원문 그대로
보존했습니다. 현행 근거 기준을 통과한 자료가 아니므로 새 글의 템플릿이나 검증된
출처로 사용하지 않습니다.
