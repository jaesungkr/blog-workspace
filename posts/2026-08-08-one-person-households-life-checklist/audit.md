# 최종 감사: 1인 가구 800만 시대, 혼자 사는 삶이 바꾼 한국의 일상

현재 lifecycle은 `ready`입니다. 원고·대표 이미지·Tistory CDN 원격 미디어 2회 검증과 creator·independent 최종 페이지 검증을 모두 통과해 오케스트레이터가 독립 검증 뒤 lifecycle을 전환했습니다.

## 구조와 독자

- [x] 제목 앞부분이 검색 의도 `1인 가구`에서 시작합니다.
- [x] 표준 인사 뒤 청년 자취방에 머문 1인 가구의 고정관념과 실제 세대 구성이 4문장 안에 나옵니다.
- [x] 첫 5문장 안에 824만 4천 가구·36.6%와 `가장 흔한 가구 형태`라는 결론이 나옵니다.
- [x] 제목과 6개 소제목만 읽어도 `규모 -> 이유 -> 비용 -> 사회의 기본값 -> 실제 지원 -> 의미` 흐름이 보입니다.
- [x] 비개발자가 코드 없이 1인 가구 증가의 사회·문화적 의미를 이해할 수 있습니다.
- [x] 통계와 필요한 변화의 연결표는 공식 정책 분류가 아닌 편집적 재구성이라고 범위를 밝혔습니다.

## 근거와 독창성

- [x] 2025년 인구주택총조사 824만 4천 가구·36.6%와 연령 구성비를 최신 공식 자료로 교체했습니다.
- [x] 2024년 소비지출 168만 9천 원·주거비 비중 18.4%를 `2025 통계로 보는 1인가구`에서 확인했습니다.
- [x] 2023년 가족실태조사의 이유·생활 어려움·정책 수요는 기준연도를 붙여 이전 자료와 구분했습니다.
- [x] Codex 재계산 입력·산식·결과·한계를 `artifacts/one-person-household-recalculation.txt`에 보존했습니다.
- [x] 39세 이하 34.4%, 60세 이상 38.5%는 공표 구성비를 더한 값이며 개인의 행복·소득·고립을 뜻하지 않는다고 제한했습니다.
- [x] 생성 이미지는 통계 C01을 증명하지 않고 개념 역할 C08만 지원하도록 `media.json`을 수정했습니다.
- [x] 사용자 경험이나 직접 이용 경험을 꾸며 쓰지 않았습니다.

## 독립 원고 검증에서 발견한 최신성 문제

| 회차 | 문제 | 수정 | 재검증 상태 |
|---|---|---|---|
| source 1 | 2024년 804만 5천 가구를 `최신 공식 통계`라고 표현 | 2026-07-28 공표된 2025년 824만 4천 가구·36.6%로 교체 | 재계산·공식 PDF·독립 source-level 재검증 `pass` |
| source 1 | 소비지출이 2023년 163만 원·18.2% | 2024년 168만 9천 원·18.4%로 교체 | `2025 통계로 보는 1인가구` PDF 대조 및 독립 source-level 재검증 `pass` |
| source 1 | C04 조사 방식의 한계가 불명확 | 5점 척도 중 `대체로 그렇다 + 매우 그렇다` 합계로 명시 | evidence.md 반영 완료 |
| source 1 | 생성 이미지가 통계 C01에 연결 | C01을 제거하고 개념 C08만 유지 | media.json 반영 완료 |

## 사용자 피드백 반영과 문장 폴리싱

- 비교 표본: `parallel-import-counterfeit`(ready), `hiccup-causes`(ready), `breastfeeding-cold-medicine`(ready), `smoking-cessation-day-5`(ready), `care-for-and-rule-creation`(ready)
- 대체 기준: 같은 `사회 · 문화` 완성 글은 1편뿐이어서 수치와 독자 행동을 연결한 최근 완성 글로 보충했습니다.
- 도입 문제 -> `저녁 메뉴도, 쉬는 시간도 내 마음대로`와 `자유와 책임이 세트`가 낡고 작위적으로 들림 -> 청년 자취방이라는 흔한 인상과 실제 세대 다양성을 바로 대비 -> 친근하지만 감상적이지 않은 도입으로 다시 읽었습니다.
- 본문 문제 -> `혼자 사는 생활을 지탱하는 네 가지 장치`가 개인에게 뻔한 자기관리 요령만 요구 -> 해당 섹션과 15분 체크리스트 전부 삭제 -> 같은 통계를 주거·돌봄·지역서비스가 바꿔야 할 기준으로 연결했습니다.
- 제목·소제목: 네 가지 생활 팁을 약속하던 제목을 `1인 가구 800만 시대, 혼자 사는 삶이 바꾼 한국의 일상`으로 바꿔 사회·문화 분석이라는 실제 본문과 맞췄습니다.
- 문단 연결: `월평균 소비지출 -> 주거비 비중 -> 주택 안정 정책 수요`를 나눠 총액과 부담을 혼동하지 않게 했습니다.
- 제거한 표현: `합산한 결과입니다`, 근거 없이 놀라움을 유도하는 `의외로`를 걷어냈습니다.
- 보호한 사실: 모든 기준연도·수치·공식 링크·Codex 계산 주체·효과 미검증 한계를 유지했습니다.

## 대표 이미지

- 현재 결과: v2 독립 검증 `pass`
- 현재 후보: `assets/screenshots/one-person-household-hero-v2.png`
- 원본: `artifacts/captures/generated/one-person-household-hero-v2-source.png`
- 크기·해시: 1672×941px, SHA-256 `019734e8f63054a935b764b1759db4424f495b1f57472fa6a299a8e71895bdcc`
- 썸네일: `artifacts/qa/hero-thumbnail-v2-360.png`, 360×202px, SHA-256 `be020d9deba23318f64232730ad7472b12e675a6b8e0addc15c5ae4da3060684`
- 생성 방식: OpenAI 내장 이미지 생성의 정밀 오브젝트 편집
- 권장 위치: 도입부 바로 아래
- alt: `햇살이 드는 작은 원룸에 1인용 식탁과 신발 한 켤레가 놓인 모습`
- 캡션: `한 자리의 식탁과 한 켤레의 신발로 혼자 사는 집의 온도를 담았습니다.`
- 편집 프롬프트: `기존 원룸의 가로 구도·원근·가구·아침 창빛·절제된 색을 유지하고 인물을 완전히 제거합니다. 가려졌던 주방과 바닥, 의자, 식탁 가장자리를 자연스럽게 복원합니다. 사람·실루엣·신체·얼굴·인물 사진은 모두 제외하고 한 자리의 식탁, 한 개의 머그, 휴대전화, 정돈된 침대, 신발 한 켤레만으로 1인 가구를 암시합니다. 특정 작가나 스튜디오는 모사하지 않으며 글자·로고·워터마크·의사문자를 넣지 않습니다.`

### v2 독립 대표 이미지 검증

- 전체 크기 관찰: 사람·신체·얼굴·인간형 실루엣이 없고 액자와 냉장고 메모에도 식별 가능한 인물 사진이 없습니다. 편집으로 복원한 주방 하부장, 바닥, 식탁 가장자리와 의자는 경계가 끊기거나 번진 흔적 없이 이어집니다. 싱크대·타일·수납장·책장·침대·현관·창의 원근과 물체 크기가 일관되며 부유 물체나 비정상 접촉도 보이지 않습니다.
- 주제 인식: 한 자리 식탁, 한 사람분의 식사와 머그, 신발 한 켤레, 싱글 침대가 한 화면에서 서로 보강되어 인물 없이도 `혼자 사는 집`으로 읽힙니다. 통계나 정책 효과를 증명하는 듯한 상징은 없으며, 글의 `한 사람 기준의 생활 공간`이라는 역할에 맞습니다.
- subject-swap: 식탁을 여러 자리로 바꾸거나 신발·침대를 다인 가구의 수량과 크기로 교체하면 현재의 단일 생활 구조가 약해집니다. 일반적인 원룸 인테리어에도 쓸 수 있는 장면이라는 한계는 있지만, 1인분 식사·한 자리·한 켤레·싱글 침대가 함께 남아 있어 주제 교체가 무의미하지 않습니다.
- 구성·광원·재질: 전경의 한 끼에서 중앙의 싱글 침대와 현관으로 시선이 이어지고, 우측 창의 자연광이 식탁과 바닥의 그림자를 같은 방향으로 만듭니다. 목재·도자기·직물·금속·식물의 표면이 손그림 기반의 사실적 스타일 안에서 자연스럽고, 크림·목재·세이지·청회색 팔레트도 절제되어 있습니다. 일본 애니메이션풍의 색과 선은 느껴지지만 특정 작가·스튜디오·캐릭터를 복제한 식별 요소는 없습니다.
- 결함 검사: 사람 제거 영역의 잔상, 반복 무늬, 휘어진 직선, 비정상 반사·그림자, 과도한 halo·bloom, AI 특유의 녹아내린 형태를 발견하지 못했습니다. 로고·워터마크·가짜 UI·판독 가능한 글자는 없고, 책등과 벽 장치의 작은 표식은 글처럼 읽히지 않는 재질 묘사 수준입니다.
- 360px 썸네일 관찰: 빈 원룸, 한 자리 식탁, 한 사람분의 식사, 한 켤레의 신발, 싱글 침대가 축소 뒤에도 구분됩니다. 인물이나 인간형 그림자가 새로 떠오르지 않고, 전경의 식사와 중앙 생활 공간이 1초 안에 읽히며 주요 단서가 잘리지 않습니다.
- 레퍼런스 비교: 별도 사용자·공식 시각 레퍼런스는 없습니다. 사용자 요구인 `인물 완전 제외`, `사진에서 혼자 사는 집의 느낌`, `살짝 일본 애니메이션풍`과 편집 프롬프트를 기준으로 대조했습니다.
- 문제 -> 수정 -> 재검증: v1의 인물이 사용자 요구와 충돌 -> 인물과 모든 인간형 단서를 제거하고 가려진 공간을 복원한 v2 제작 -> 1672×941 원본과 360×202 썸네일을 각각 직접 열어 인물 부재, 1인 가구 단서, 편집 완결성과 축소 판독성을 다시 확인해 `pass`했습니다.
- 선택 버전: `assets/screenshots/one-person-household-hero-v2.png`, 1672×941px, SHA-256 `019734e8f63054a935b764b1759db4424f495b1f57472fa6a299a8e71895bdcc`
- 선택 위치·alt: 도입부 바로 아래, `햇살이 드는 작은 원룸에 1인용 식탁과 신발 한 켤레가 놓인 모습`

이전 v1의 독립 검증 `pass`는 사용자 요청 전의 역사적 기록입니다. 사용자 피드백에서 인물을 제외하도록 요청해 v1 선택을 무효화하고, 현재 선택은 독립 검증을 통과한 v2입니다.

## 보조 인포그래픽

- 판단: `not_applicable`
- 이유: 생활의 어려움과 필요한 사회적 변화는 세 열짜리 표로 충분합니다. 별도 이미지로 만들면 같은 정보를 반복하고 모바일 읽기 부담만 늘어납니다.

## 로컬 리치 포스트 QA

최신성 수정 전 후보에서 수행한 브라우저 검사는 역사적 참고입니다. 2026-08-09 사용자 피드백을 반영한 원고와 v2 이미지로 밝은·다크 로컬 미리보기를 새로 렌더하고 브라우저에서 다시 확인했습니다. 현재 검사는 creator 로컬 QA이며, CDN 매핑 뒤에는 독립 검토자가 최종 화면을 다시 검사해야 합니다.

- 밝은 화면: 1280×900, 390×844, 360×800에서 문서 `scrollWidth = clientWidth`, H1 1개, TOC 링크 6개·대상 유일성을 확인했습니다. 삭제 대상 도입 문구와 소제목은 보이지 않았고 새 소제목 `1인 가구가 바꾼 사회의 기본값`이 렌더됐습니다.
- 대표 이미지: 390px에서 350px, 360px에서 320px로 비율을 유지했고 v2 원본 1672px가 정상 로드됐습니다. 모바일 첫 화면에서도 인물 없이 한 자리 식탁과 작은 원룸이 보였습니다.
- 표: 360px wrapper 320px/scroll 620px, `overflow-x:auto`였습니다. 새 세 열 표를 좌우 끝까지 실제로 스크롤해 마지막 열의 네 행을 읽었습니다.
- 다크 모드: `.dark` 조상 아래 배경 `rgb(30,31,33)`, 본문 `rgb(245,245,247)`, 링크 `rgb(102,179,255)`, 표 머리 `rgb(42,43,46)`를 확인했습니다. 이미지 픽셀에는 변환이 적용되지 않았습니다.
- 문제 -> 수정 -> 재검증: 브라우저의 긴 전체 페이지 캡처가 모바일 화면을 잘못 이어 붙임 -> 일반 뷰포트 캡처와 요소 실제 너비를 다시 확인 -> 360px에서 본문·제목·이미지가 정상 폭으로 표시되고 문서 가로 넘침이 없었습니다.

## Tistory CDN과 creator 최종 페이지 QA

- 사용자 제공 주소는 Daum `R1280x0` 썸네일 래퍼로 1280×720px였습니다. 내부 `blog.kakaocdn.net` 원본은 1672×941px, SHA-256 `019734e8f63054a935b764b1759db4424f495b1f57472fa6a299a8e71895bdcc`로 로컬 v2와 바이트까지 일치해 원본 URL을 `one-person-household-hero`에 연결했습니다.
- `remote_media.py record --by "Codex creator review"`: 실제 HTTPS GET, PNG 1672×941px, 원격 미디어 baseline `pass`.
- canonical remote preview: `artifacts/qa/rendered/one-person-households-life-checklist-rich-preview.html`, SHA-256 `3659f65a1f776e91f98fec893c4f47f00185fac6f9fe9a88e6989c99b898c2e5`.
- creator browser receipt: Chrome/151.0.7922.108, session `cee8578d-fa14-43b3-98ff-8005476651c9`. 1280×900, 390×844, 360×800에서 문서 `scrollWidth = clientWidth`, H1 1개, TOC 6개·대상 유일, 원격 이미지 `complete=true`·natural 1672×941을 확인했습니다.
- 표 집중 검사: 390px에서는 wrapper 350/620px·최대 scrollLeft 270, 360px에서는 320/620px·최대 scrollLeft 300, `overflow-x:auto`, 15px/24px였습니다. 두 폭 모두 표 왼쪽의 통계 항목·비율과 오른쪽의 변화안 네 행을 실제로 읽었고 문서 자체의 가로 넘침은 없었습니다. 증거는 `artifacts/qa/component-details/`에 보존했습니다.
- 다크 모드: 원격 이미지를 사용한 별도 preview에서 1280·390·360px 모두 문서 넘침 없이 로드됐습니다. 배경 `rgb(30,31,33)`, 본문 `rgb(245,245,247)`, 링크 `rgb(102,179,255)`, 표 머리 `rgb(42,43,46)`였으며 이미지 픽셀에는 변환이 적용되지 않았습니다.
- creator 최종 판단: `pass`. `record_rich_qa.py`가 `artifacts/qa/rich-post.json`을 생성했습니다. 현재는 별도 검토자의 두 번째 CDN fetch와 독립 페이지 QA를 기다립니다.

## 검사와 남은 경계

- 통과한 검사: `python3 scripts/blog.py check posts/2026-08-08-one-person-households-life-checklist`, `check_rich_post.py`, 라이트·다크 로컬 `render_rich_post.py`.
- 독립 source-level 결과: `pass`. 새 표의 편집적 정책 제안에 효과·우선순위 미검증 경계를 보강한 뒤 원고·렌더를 다시 확인했습니다.
- 독립 final-page 결과: `pass`. CDN 원격 바이트 2회 검증, creator QA, 별도 Chrome 세션의 independent QA, 390·360px 두 번째 표 양끝 확인과 최종 strict gate를 재현했습니다.
- 현재 상태: source-level·final-page `pass`, lifecycle `ready`. 독립 검토자는 `reviewing`을 유지했고, 이후 오케스트레이터가 모든 gate를 확인한 뒤 `ready`로 전환했습니다.
- 남은 외부 단계: orchestrator의 lifecycle 결정과 최종 배포 산출물 생성, 사용자의 Tistory HTML 모드 미리보기·발행.
- Tistory 발행: 사용자가 최종 HTML을 붙여 넣고 미리보기를 확인한 뒤 직접 발행합니다.

## 독립 source-level 재검증 - 사용자 피드백 후보 (2026-08-09)

- 검토자: Codex 독립 원고 검증
- 판정: `pass`
- 범위: 변경된 제목·도입·6개 소제목·두 표·마무리, `brief.md`, `evidence.md`, `media.json`, `capture-plan.md`, 재계산 원자료, v2 대표 이미지와 썸네일, 라이트·다크 로컬 렌더

### 통과한 항목

- 사용자 피드백: 작위적이던 기존 도입, `혼자 사는 생활을 지탱하는 네 가지 장치`, 15분 체크리스트가 모두 제거됐습니다. 새 도입은 청년 자취방이라는 익숙한 인상에서 세대 다양성으로 자연스럽게 넘어갑니다.
- 제목·구조·문장: 제목과 소제목만으로 `규모 -> 이유 -> 비용 -> 사회의 기본값 -> 지원 -> 의미`가 읽히며 존대어, 문단 연결, Trends 사회·문화의 한국 독자 마무리가 자연스럽습니다.
- 수치·연도·출처: 824만 4천 가구·36.6%, 2015년 대비 58.4%·9.4%p, 39세 이하 34.4%, 60세 이상 38.5%, 2024년 소비지출 168만 9천 원·주거·수도·광열 18.4%, 2023년 사유·어려움·정책 수요를 공식 PDF와 다시 대조했습니다.
- 원문 보존: 국가데이터처 PDF 두 건은 원격 파일과 저장 파일의 SHA-256이 각각 `7f8b1e6ddde1ab2ac9663622d72120d3e1dd5a5f8088c9c4ca8dace372e2ca42`, `0f74d8fff2d094d16a6f9034a595fcd0b0ebea711dc809a76ac45316f5d101f3`로 일치했습니다.
- 대표 이미지: v2는 1672×941px, SHA-256 `019734e8f63054a935b764b1759db4424f495b1f57472fa6a299a8e71895bdcc`로 manifest와 일치합니다. 사람·실루엣 없이 한 자리 식탁·한 사람분 식사·한 켤레의 신발·싱글 침대가 1인 가구를 암시하며 통계 증거로 오인될 요소는 없습니다.

### 문제 -> 수정 -> 재검증

- 문제 -> 새 표 앞 문장은 마지막 열이 공식 정책 분류가 아니라는 점만 밝혔고, C08의 `구체적 정책의 효과나 우선순위를 시험하지 않음`이라는 한계가 공개 원고에는 없었습니다. 세 번째 열을 통계가 검증한 정책 권고로 읽을 여지가 있어 최초 판정을 `revision_required`로 반환했습니다.
- 수정 -> 작성 단계에서 표 앞에 `구체적인 정책의 효과나 우선순위를 검증한 결과는 아닙니다.`를 추가했습니다. 독립 검증자는 `article.md`를 직접 수정하지 않았습니다.
- 재검증 -> 공개 원고의 한정 문구가 `evidence.md` C08과 일치하고, 마지막 열이 공식 통계와 편집적 해석을 구분한다는 점을 다시 확인했습니다. 아래 네 명령을 재실행해 모두 통과했으며 최종 source-level 판정은 `pass`입니다.

### 실제 실행 명령과 결과

```bash
python3 scripts/blog.py check posts/2026-08-08-one-person-households-life-checklist
python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py posts/2026-08-08-one-person-households-life-checklist
python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py posts/2026-08-08-one-person-households-life-checklist --output-dir posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-source-rendered
python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py posts/2026-08-08-one-person-households-life-checklist --preview-theme dark --output-dir posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-source-rendered-dark
```

- `blog.py check`: 오류 0개, 경고 0개
- `check_rich_post.py`: `rich-post: pass`, media 1개·directive 1개
- 라이트 preview SHA-256: `c9340da3081162428a5ae7b7c085c7be1b68f58e0dd2cb70f72367861c83e937`
- 다크 preview SHA-256: `266e624178aa5eebaf6206e883653a6625e4c62f21940cdfff81d9bf8e241fc6`
- fragment SHA-256: `b91a3893d58191f7b7215642abb57482e4137d4feb317ada426a5ca01ac293fc`
- 두 preview는 H1 1개, fragment는 H1 0개이며 TOC 6개가 모두 고유한 실제 heading ID에 연결됩니다. v2 이미지 경로·alt·1672×941 속성과 새 분석 섹션·두 표가 반영됐고 삭제한 섹션과 체크리스트는 남지 않았습니다.
- source-level 검증 당시에는 `tistory_url`이 비어 있어 fragment에 업로드 자리표시자 1개가 있었습니다. 이후 CDN URL 매핑과 원격·브라우저 검증을 완료한 최종 fragment에는 자리표시자와 로컬 경로가 없습니다.

## 독립 final-page 검증 (2026-08-09)

- 검토자: `Codex independent reviewer`
- 최종 판정: `pass`
- 검증 시 lifecycle: `reviewing` 유지

### 실제 실행 명령

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py verify posts/2026-08-08-one-person-households-life-checklist --by 'Codex independent reviewer'
python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py posts/2026-08-08-one-person-households-life-checklist --require-publish-urls --require-remote-verification
python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py posts/2026-08-08-one-person-households-life-checklist --require-publish-urls --preview-media-source remote --output-dir posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-rendered
python3 .agents/skills/dev-log-rich-post-workspace/scripts/capture_rich_qa.py posts/2026-08-08-one-person-households-life-checklist --mode independent --by 'Codex independent reviewer'
python3 /Users/ja2sng/Documents/Codex/2026-08-08/d-2/work/capture_one_person_table.py
cp .agents/skills/dev-log-rich-post-workspace/assets/independent-qa-template.json posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-measurements.json
python3 .agents/skills/dev-log-rich-post-workspace/scripts/record_rich_final_validation.py posts/2026-08-08-one-person-households-life-checklist --preview posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-rendered/one-person-households-life-checklist-rich-preview.html --fragment posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-rendered/one-person-households-life-checklist-tistory-fragment.html --measurements posts/2026-08-08-one-person-households-life-checklist/artifacts/qa/independent-measurements.json
python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py posts/2026-08-08-one-person-households-life-checklist --require-publish-urls --require-remote-verification --require-independent-pass
```

### 원격 미디어와 독립 렌더

- 두 번째 CDN fetch: HTTP 200, `image/png`, 2,260,778 bytes, 1672×941px, SHA-256 `019734e8f63054a935b764b1759db4424f495b1f57472fa6a299a8e71895bdcc`. creator baseline과 URL·바이트·형식·치수·지문이 일치했습니다.
- `remote_media.py verify`: `pass`
- publish URL·remote verification 필수 strict check: `pass`
- 독립 remote preview: `artifacts/qa/independent-rendered/one-person-households-life-checklist-rich-preview.html`, SHA-256 `3659f65a1f776e91f98fec893c4f47f00185fac6f9fe9a88e6989c99b898c2e5`
- 독립 fragment: `artifacts/qa/independent-rendered/one-person-households-life-checklist-tistory-fragment.html`, SHA-256 `511833784ee65cffc5ee09006e6167378e0f2bdfa29f2bb9aa559a3a2f599d1d`. H1 0개, 자리표시자 0개, 로컬 경로 0개, 원격 CDN 이미지 1개입니다.

### 독립 브라우저 관찰

- canonical independent session: Chrome/151.0.7922.108, `48c7f136-8532-4fbf-a74c-c85d6d690108`. creator session `cee8578d-fa14-43b3-98ff-8005476651c9`와 다릅니다.
- 1280×900: document client/scroll width 1280/1280, H1 1개, TOC 6개·대상 유일, 원격 이미지 `complete=true`, natural 1672×941. 제목·도입·이미지의 폭과 계층이 자연스럽고 잘림이 없습니다.
- 390×844: document client/scroll width 390/390, H1 1개, TOC 대상 유일, 원격 이미지 정상. 제목·본문·이미지가 350px 콘텐츠 폭에 맞고 글자 겹침이나 페이지 가로 이동이 없습니다.
- 360×800: document client/scroll width 360/360, H1 1개, TOC 대상 유일, 원격 이미지 정상. 긴 제목과 본문이 자연스럽게 줄바꿈되고 잘림이 없습니다.
- 대표 이미지·캡션: 390px에서 원격 이미지가 정상 로드되고 `한 자리의 식탁과 한 켤레의 신발로 혼자 사는 집의 온도를 담았습니다. · 생성 이미지`가 14px/21.7px로 이미지 바로 아래에 붙어 읽힙니다. 증거: `artifacts/qa/independent/component-details/hero-caption-390.png`.
- 콘텐츠 순서와 독자 흐름: 제목·도입·대표 이미지·목차·6개 섹션의 순서가 source와 같고, 표 뒤 문단도 표와 분리돼 읽힙니다. 목록과 GIF는 없어 marker·reduced-motion 검사는 `not_applicable`입니다.

### 두 번째 표의 별도 세션 양끝 검사

- supplemental session: Chrome/151.0.7922.108, `7efb87b2-5dd7-423d-b11f-75df66809567`. canonical independent session과 별도의 새 Chrome 프로세스입니다.
- 390px: document 390/390px, wrapper client/scroll 350/620px, `overflow-x:auto`, 15px/24px, scrollLeft 0→270. 왼쪽에서 `통계에 잡힌 빈틈`·`응답 또는 비중`의 네 행을, 오른쪽에서 `한 사람 기준에서 필요한 변화`의 네 행을 모두 읽었습니다.
- 360px: document 360/360px, wrapper client/scroll 320/620px, `overflow-x:auto`, 15px/24px, scrollLeft 0→300. 문서 자체는 움직이지 않고 표만 스크롤되며, 세 열과 네 행을 양끝에서 충돌 없이 읽었습니다.
- 증거: `artifacts/qa/independent/component-details/second-table.json`, `table-2-390-left.png`, `table-2-390-right.png`, `table-2-360-left.png`, `table-2-360-right.png`.

### 최종 기록과 gate

- `independent-measurements.json`: 1280·390·360 readable media와 viewport 상태 `pass`, fragment `pass`, caption 부착·table scroll·content order `true`, GIF 항목 `not_applicable`.
- `record_rich_final_validation.py`: `artifacts/qa/independent-final-page.json` 생성, SHA-256 `615597370d7530b3e700ebdd300c70e1b46c5b1e4d47c758c5cde7d7eec9e0fc`, result `pass`.
- 최종 `check_rich_post.py --require-publish-urls --require-remote-verification --require-independent-pass`: `rich-post: pass`, media 1개·directive 1개.
- 알려진 material defect는 남지 않았습니다. 독립 검증 범위에서는 `reviewing`을 유지했고, 이후 오케스트레이터가 `ready`로 전환했습니다.

## ready 전환 (2026-08-09)

- 조건: source-level `pass`, 대표 이미지 v2 독립 `pass`, 인포그래픽 `not_applicable`, CDN 원격 fetch 2회 일치, creator·independent 최종 페이지 `pass`, fragment H1·자리표시자·로컬 경로 0개.
- 결정: 오케스트레이터가 `article.md`를 `status: ready`로 전환했습니다.
