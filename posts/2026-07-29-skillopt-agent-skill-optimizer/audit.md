# 최종 감사: SkillOpt 사용법: 에이전트의 반복 실수를 스킬로 고치는 방법

검토한 사실만 체크합니다. 아직 해당하지 않는 항목은 비워 두고 이유를 적습니다.

## 구조와 독자

- [x] 제목 앞부분이 실제 검색 의도에서 시작합니다.
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤 2-4문장 안에 익숙한 문제와 글의 필요성이 나옵니다.
- [x] 첫 5-6문장 안에 기억할 결론 또는 질문이 있습니다.
- [x] 낯선 용어와 방법을 결과표보다 먼저 설명합니다.
- [x] 중앙 방법의 `입력 -> 처리/표현 -> 비교/판단 -> 출력` 사슬이 보입니다.
- [x] 시나리오 결과, 전체 벤치마크, 실용 추천의 범위를 구분했습니다.
- [x] 선택이 목적인 독자에게 기본 선택과 예외를 직접 제시합니다.
- [x] 비개발자가 코드 없이도 핵심 결론을 이해할 수 있습니다.

## 근거와 독창성

- [x] 모든 수치와 강한 주장에 출처·측정 기준·한계가 붙습니다.
- [x] 벤더 주장, 독립 검증, 추정, 구조 예시를 구분했습니다.
- [x] 테스트 입력·환경·판정 규칙·원시 결과·실패 사례를 보존했습니다.
- [x] Codex가 실행한 작업을 사용자의 개인 경험으로 쓰지 않았습니다.
- [x] 미확인 사실과 해결되지 않은 TODO가 본문에 없습니다.
- [x] 반론과 일반화할 수 없는 범위가 보입니다.
- [x] 출처 요약을 넘어선 first-party contribution이 있습니다.
- [x] 다른 블로그 이름으로 바꾸면 약해지는 dev.log만의 이유가 있습니다.

## 문장과 형식

- [x] 인사부터 마무리까지 존대어가 일관됩니다.
- [x] 번역투, 이중 피동, 명사화, 상투적인 요약 표현을 걷어냈습니다.
- [x] 과장, 감정 부사, 기계적인 병렬, 불필요한 1인칭이 없습니다.
- [x] 문단은 주제에 따라 자연스럽게 나뉘고 문장 리듬이 기계적이지 않습니다.
- [x] 굵은 강조가 할당량처럼 반복되거나 매 절의 격언형 결론을 만들지 않습니다.
- [x] em dash(`—`), 분리된 참고문헌 부록, 관성적인 면책 문구가 없습니다.
- [x] 카테고리별 마무리 기준을 따릅니다.

## 제목·문체 폴리싱

- [x] 제목과 소제목만 읽어도 이 글의 사건·판단·설명 흐름이 보입니다.
- [x] 검색 유입이 최우선이면 현재 검색 의도와 제목 후보를 비교하고, 정성
  판단인지 실제 검색량 자료인지 구분해 기록했습니다.
- [x] 다른 주제로 바꿔도 그대로 성립하는 범용 소제목을 구체화하거나, 탐색상
  필요한 관습적 제목을 유지한 이유를 적었습니다.
- [x] 각 소제목은 본문 없이도 대상과 설명·비교·측정·변화 중 무엇을 다루는지
  알 수 있으며, 수치와 폐기한 실험의 의미를 제목 안에서 풀어 썼습니다.
- [x] 문단 사이를 접속사로만 잇지 않고 원인·결과·대조·시간·예시·질문 또는
  의도한 단절 중 실제 관계가 이어집니다.
- [x] 수치·날짜·링크·코드·표·테스트 주체·한계를 폴리싱 전 자료와 대조했습니다.
- [x] 자연스러움을 위해 일화·감정·대화·실패·개인 경험을 새로 만들지 않았습니다.

- 비교 표본(슬러그·상태): `prompt-injection-document-test`(ready),
  `orca-agent-ide-guide`(ready), `ccshare-manycode-guide`(ready),
  `wsl-containers-without-docker-desktop`(ready), `duckdb-guide`(ready)
- 같은 하위 카테고리 표본이 부족할 때의 대체 기준: 같은 `AI 개념 · 실전`
  ready 글이 2개뿐이라, 직접 테스트를 포함한 도구 설명·설치 글 3개를
  `개발 · 디지털`에서 보충했습니다.
- 대표 제목·소제목 변경: 반복되던 `검색어 - 설명형 훅`을 피하고
  `SkillOpt 사용법: 자동 테스트 557개 통과와 동점 거절 게이트`를 선택했습니다.
  `모델은 그대로...구조`는 `모델 가중치 대신 Markdown을 학습하는 SkillOpt`로,
  `동점도 거절...결과`는 `0.50 동점까지 거절한 SkillOpt 검증 게이트`로,
  성능 절은 최대 학습 토큰을 제목에 드러내도록 바꿨습니다.
- 대표 문단 연결 수정: 추상적인 글 순서 예고를 삭제하고 "문서 설명만으로
  보수성이 보이지 않음 -> Codex가 게이트와 전체 테스트 실행"으로 연결했습니다.
  macOS 테스트 실패는 긴 한 문장에서 실패 항목과 경로 오판을 나눠 읽기 쉽게
  고쳤습니다.
- 삭제한 빈 문구 또는 반복: `이번 글에서는 ... 살펴보겠습니다` 로드맵과
  `따라서 이번 결과는` 같은 관성적 연결을 삭제했습니다.
- 보존 확인한 핵심 사실: 커밋 `8304e6c`, macOS 26.5.2, Python 3.12.13,
  555 pass·6 skip·2 fail, 조건 변경 후 557 pass·6 skip, 게이트 22 pass,
  0.49·0.50·0.51 판단, 논문 52개 셀과 세 평균 향상, 스킬·학습 토큰 범위,
  버전·설정 차이, Codex 테스트 주체, 코드·URL을 모두 대조했습니다.
- 남은 문체·근거 위험: 현재 없음. 논문 성능은 저자 보고이며 전체 벤치마크를
  독립 재현하지 않았다는 한계를 최종 글 검증에서 다시 확인합니다.
- 제목 판단 근거: 검색량 자료를 사용한 제목 최적화 요청은 아니었습니다.
  `SkillOpt 사용법`을 앞에 두고 직접 확인한 557 pass와 동점 거절을 훅으로
  삼은 정성적 검색 의도 판단입니다.
- 2026-07-29 가독성 재수정: 사용자 피드백에 따라 공개 제목을
  `SkillOpt 사용법: 에이전트의 반복 실수를 스킬로 고치는 방법`으로 바꾸고,
  테스트를 빼먹는 코딩 에이전트의 가상 사례를 기술 구조보다 먼저 배치했습니다.
  `가상 예시 -> 작업 설명서 -> 여섯 단계 -> 실제 게이트 검증` 순서로 바꿔
  사용 목적과 실제 측정값의 경계를 먼저 읽을 수 있게 했습니다.
- 재수정에서 보존한 사실: 커밋·환경·테스트 수치·0.49/0.50/0.51 게이트
  결과·논문 성능과 토큰·버전·명령·URL·Codex 실행 주체·한계를 바꾸지
  않았습니다. 새 6/10·8/10 값은 `evidence.md` C16에 실제 측정이 아닌
  구조 예시로 따로 기록했습니다.
- 2026-07-29 책임 경계 폴리싱: 새 절 제목을
  `초기 스킬부터 best_skill.md까지, 사용자와 SkillOpt의 역할`로 구체화했습니다.
  연구 엔진이 맡는 범위를 `준비된 문제 안의 반복 실행·편집·검증`으로 한정하고,
  Sleep은 별도 실행 뒤 staging과 `adopt`가 필요한 흐름으로 표현했습니다.
- 책임 경계 수정에서 보존한 사실: 공식 입력 계약, 결과 디렉터리 파일,
  `best_skill.md`, Sleep 명령 흐름을 소스와 다시 대조했습니다. 훈련 20건·선택
  10건·시험 10건은 실제 측정값이 아닌 구조 예시로 `evidence.md` C16에
  기록했고, 기존 테스트·논문 수치·코드·URL·실행 주체는 바꾸지 않았습니다.

## 대표 이미지

- [x] 최종 이미지를 생성한 뒤 실제 결과를 열어 확인했습니다.
- [x] 이미지가 글의 핵심 메시지와 맞고 근거 이상의 내용을 암시하지 않습니다.
- [x] 로고·워터마크·불필요한 내장 텍스트가 없습니다.
- [x] 대표 이미지의 반응형 크롭을 고려한 안전 여백이 있습니다.

- 최종 파일: `assets/skillopt-hero.png`
- 후보 크기: `1672x941` PNG, SHA-256
  `eec2d3b7edce74a0d2488fb8fcb4b509a66e200220abf9d5d528e92cf10ee77a`
- 권장 위치: `대표 이미지 - 제목 바로 아래`
- 한국어 alt: 정밀 검증 장치 안에서 작은 종이 조각으로 수정한 스킬 문서가
  통과하고, 거절된 편집 조각은 옆 트레이에 남은 모습
- 생성 방법: OpenAI 내장 이미지 생성 워크플로, 신규 생성, 참조 이미지 없음
- 주제 인식 단서: 하나의 종이 문서가 몇 개의 국소 패치로 조립되어 정밀
  허용치 게이트를 통과하고, 채택되지 않은 패치가 별도 트레이에 남습니다.
  모델 하드웨어가 아니라 자연어 스킬 문서를 작은 편집과 검증으로 학습하는
  SkillOpt의 핵심 동작을 물리적 은유로 보여 줍니다.
- 레퍼런스 역할과 제약: 사용자·공식 이미지 레퍼런스는 제공되지 않았습니다.
  문서의 핵심 동작만 인식 단서로 사용했고 Microsoft 로고·논문 도판·제품 UI는
  복제하지 않았습니다.
- 후보 단계에서 보이는 위험: 정밀 장치가 제본기나 펀칭 기계로 먼저 보일 수
  있어, 독립 검증에서 축소 인식과 주제 교체 테스트를 엄격히 확인해야 합니다.
  오른쪽 거절 트레이가 16:9 반응형 크롭에서도 남는지도 확인이 필요합니다.
- 전체 크기 관찰: 하나의 종이 문서가 여러 국소 패치로 맞물리고, 정밀 장치의
  중앙 허용치 면을 통과하며, 채택되지 않은 세 조각은 오른쪽 트레이에 남습니다.
  종이 섬유·겹 두께·브러시드 알루미늄·새틴 황동의 표면 반응과 접촉 그림자가
  일관되고, 나사·축·프레임의 원근과 접합도 자연스럽습니다. 읽을 수 있는
  문구·가짜 코드·제품 UI·로고·워터마크는 없습니다.
- 320x180 썸네일 관찰: 왼쪽의 정밀 장치와 패치 문서가 먼저 읽히고, 오른쪽
  거절 트레이도 별도 요소로 유지됩니다. 초록색 통과 가장자리와 흰색 폐기
  조각이 작지만 구분되며, 상단과 오른쪽의 여백이 반응형 크롭을 견딥니다.
- 주제 인식·교체 테스트: 일반 문서 편집이나 인쇄로 바꾸면 `여러 국소 패치가
  한 문서에 결합 -> 좁은 검증 장치 통과 -> 거절 패치는 별도 보존`이라는
  세 단서가 모두 필요하지 않습니다. SkillOpt의 bounded edit와 validation
  gate, rejected-edit buffer에 직접 묶여 있어 subject-swap 테스트를
  통과했습니다.
- 레퍼런스 비교: 사용자·공식 시각 레퍼런스가 없어 해당 없습니다. 공식
  로고나 논문 도판을 대신 쓰지 않고, 확인한 작동 원리만 인식 근거로 삼았습니다.
- 독립 대표 이미지 검증: `pass`
- 최종 생성 프롬프트:

  `Use case: stylized-concept. Asset type: Korean Tistory blog hero image,
  wide 16:9 landscape. Create an iconic editorial image for Microsoft SkillOpt,
  a system that improves one natural-language agent skill document through
  small bounded edits and keeps only a candidate that passes strict validation,
  without changing model weights. Creative intent: careful improvement through
  evidence, not uncontrolled rewriting. Visual idea: a single compact ivory
  paper folio made from a few precisely interlocking paper strips is held
  inside a watchmaker-grade mechanical testing jig; three small replacement
  strips sit nearby in a shallow rejected-parts tray, while the coherent folio
  alone has advanced through a narrow calibrated metal tolerance gate. This is
  one physical metaphor, not a diagram or object inventory. Subject-recognition
  cue: the modular paper folio visibly consists of a small number of localized
  add/delete/replace patches, and the narrow precision gate visibly tests that
  same document before it advances; this must read as training a reusable text
  skill, not training model hardware. Art direction: practical miniature set
  photographed as a major enterprise technology campaign, museum-catalog
  object study. Luminous warm-gray tabletop and pale studio backdrop; one
  tactile off-white document folio, localized inset paper patches, precision
  brushed-aluminum and satin-brass validation jig, small rejected-parts tray.
  Wide controlled asymmetry, primary folio and gate slightly left of center,
  shallow diagonal depth, crop-safe quiet area on the right. Broad diffused
  daylight from upper left, neutral fill, narrow warm rim on brass, gentle
  contact shadows. Ivory, warm gray, brushed silver, muted brass, one restrained
  moss-green accepted edge. Visible paper fibers, machined aluminum, satin
  brass, matte stone. No people, logos, title, labels, readable text, letters,
  numbers, watermark, arrows, explanatory panels, fake UI, charts, trophies,
  generic AI imagery, brains, robots, chips, circuits, neural networks, laptops,
  floating dashboards, holograms, glassmorphism, neon, cyberpunk, glowing tubes,
  plastic icons, pseudo-code, pseudo-writing, clutter, rigid symmetry,
  excessive bloom, malformed edges, or impossible mechanics.`

## 보조 인포그래픽

- 판단: `1장`
- 판단 이유: 롤아웃·편집 제안·편집 예산·selection 게이트가 순차 관계이면서,
  거절 편집은 앞 단계로 되돌아갑니다. 글과 선형 목록만으로는 데이터 분리와
  피드백 방향을 동시에 읽기 어려워 과정형 인포그래픽 한 장이 필요합니다.
- Reflections 예외 근거(해당하는 경우): 해당 없음.
- [x] 각 인포그래픽이 장식이나 단순 반복이 아니라 하나의 중요한 관계를 더 빨리 이해하게 합니다.
- [x] 핵심 설명 바로 뒤에 둘 위치를 정했습니다.
- [x] 한국어 문구·수치·화살표·라벨을 결정적으로 조판하고 본문 근거와 대조했습니다.
- [x] 전체 크기와 360px 모바일 너비에서 실제 결과를 확인했습니다.
- [x] 두 장 이상이면 각 이미지가 서로 다른 독자 질문에 답합니다. 한 장만 제작했습니다.

| 최종 파일 | 유형 | 해결하는 독자 질문 | 권장 위치 | 한국어 alt | 문구·수치 근거 |
|---|---|---|---|---|---|
| `assets/skillopt-learning-loop-v5.png` | 과정 | 한 번의 스킬 편집은 어떤 근거로 만들어지고, 왜 train과 selection을 분리하는가? | `예시를 실제 학습으로 바꾸는 여섯 단계`의 판단 사슬 바로 뒤 | 훈련 실행 궤적에서 편집 후보를 만들고, 최대 네 개만 후보 스킬에 적용한 뒤 분리한 선택 작업의 점수가 올라야 채택하는 SkillOpt 학습 루프 | 실행 궤적·add/delete/replace·selection gate·rejected-edit buffer는 논문 §3.1~§3.6과 저장소 코드, `기본 최대 4개`는 현재 `configs/_base_/default.yaml`, TEST 분리는 논문 §3.2와 `evidence.md`의 C1·C2·C3 |

- 제작 방식: 한국어 문구와 화살표를 결정적으로 조판한 1080x1700 HTML/SVG를
  Chrome으로 래스터화했습니다. 원본은
  `artifacts/skillopt-learning-loop-infographic.html`, 재현 스크립트는
  `artifacts/render-skillopt-learning-loop.cjs`입니다.
- 최종 후보 크기·해시: 1080x1700 PNG, SHA-256
  `96b28849519045a27c082404b66096c64ceece8a7252fefb4105c1d72d84e528`
- 360px 표시 환산 크기: headline 20.7px, primary 15.3px, support 12.7px,
  caveat 11.3px. 헤더는 캔버스 높이의 12.8%입니다. 자동 크기 검사는 전부
  권장 범위를 통과했습니다.
- 버전 이력: v1은 1350px 캔버스에서 단계 제목·도형이 겹쳐 탈락했습니다.
  v2는 세로 간격을 늘렸고, v3에서 게이트 문구와 마름모 여백을 바로잡았습니다.
  v4는 거절 피드백 선을 selection 라벨 밖으로 우회했습니다. 독립 확대
  검수에서 v4의 `거절 편집 버퍼`와 `best_skill.md`가 상자 테두리에
  지나치게 붙어 `revision_required`로 판정했습니다. v5에서 두 결과 상자를
  넓히고 화살표 끝과 상자 사이의 여백도 다시 잡았습니다.
- 전체 래스터 관찰: 제목 아래에 실행 궤적 수집, 성공·실패 반영, 편집 예산,
  selection 게이트가 위에서 아래로 이어집니다. 채택은 초록색 오른쪽 화살표,
  동점·하락은 적갈색 왼쪽 화살표, 거절 피드백은 점선으로 구분됩니다.
  모든 한국어·숫자·영문 혼합 라벨이 정확하고 잘리거나 겹친 곳이 없습니다.
- 360px 브라우저 관찰: 원본 1080x1700 래스터를 다시 인코딩하지 않고
  CSS 너비 360px, 높이 566.65625px로 표시했습니다. 제목과 네 단계가 줌 없이
  읽히며, `기본 최대 4개`, `분리한 SELECTION 작업`, 하단 TEST 주석도
  유지됩니다. 한눈에 작은 편집이 별도 게이트에서 채택·거절되는 과정이 먼저
  보여 1초 관계 인식 테스트를 통과했습니다. 외곽 카드가 없어 포스터나
  슬라이드 속 작은 도표처럼 보이지 않습니다.
- 확대 영역 관찰: 헤더는 초록 장식 원과 글자 사이가 비어 있고, 1단계의
  입력 문서·대상 모델 화살표, 2단계의 성공·실패 곡선과 추가·삭제·교체,
  3단계의 점선 피드백과 후보 깔때기, 4단계의 마름모·두 결과 상자·하단
  주석을 각각 확인했습니다. 모든 선과 `markerUnits="userSpaceOnUse"` 화살표가
  글자 영역을 비켜가며 그림자·질감도 대비를 해치지 않습니다.
- 문구만 읽는 순서와 도형만 보는 순서를 따로 확인했습니다. 문구는
  수집 -> 반영 -> 제한 -> selection 판단 -> 채택·거절 순서이고, 도형만
  보아도 입력 두 개가 대상 모델로 합쳐지고 편집 후보가 좁아진 뒤 양쪽으로
  갈라지는 구조가 남습니다.
- 독립 보조 인포그래픽 검증: `pass`

## 최종 검토와 수정 이력

- [x] 완성 원고를 처음부터 끝까지 외부 독자 관점으로 다시 읽었습니다.
- [x] 렌더된 티스토리 HTML에서 제목·문단·표·코드·링크·이미지 위치를 확인했습니다.
- [x] 대표이미지는 전체·썸네일, 보조 인포그래픽은 전체·360px 결과를 실제로 확인했습니다.
- [x] 사용자 제공 시각 레퍼런스가 있다면 같은 표시 크기로 나란히 비교했습니다. 제공된 레퍼런스는 없습니다.
- [x] 아래 문제를 수정한 뒤 관련 검사·렌더·시각 검토를 다시 실행했습니다.

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | 제목·소제목 | 최근 글과 같은 `검색어 - 설명` 제목, 범용적인 `구조`·`결과` 표현 | 557개 테스트, 0.50 동점, 최대 학습 토큰처럼 실제 관찰을 제목과 소제목에 반영 | 제목·소제목만 읽어도 원리 -> 게이트 실행 -> 비용 -> 도입 판단 순서가 보임 |
| 2 | 도입부와 문단 이음 | 초고가 글의 항목을 미리 나열해 기계적인 로드맵처럼 읽힘 | 소스 설명만으로 부족해 Codex가 직접 실행했다는 원인과 행동으로 교체 | 테스트 절의 실제 실행 주체와 자연스럽게 이어지고 새 사실은 추가하지 않음 |
| 3 | 테스트 실패 문단 | 112자 문장 하나에 테스트명·두 경로·오판 결과가 겹침 | 실패 위치와 `/var`·`/private/var` 경로 판정을 두 문장으로 분리 | 원자료와 수치·경로·해석을 다시 대조해 의미 변화 없음 |
| 4 | 1차 글 검증 | 제목의 `557개 테스트`가 557 pass·6 skip을 합친 전체 수처럼 읽힐 수 있음 | `자동 테스트 557개 통과`로 정확한 관찰값을 명시 | 본문·test log의 557 pass·6 skip과 일치 |
| 5 | 배포 설명 | 초고가 slow update의 보호 영역까지 배포되지 않는 것처럼 읽힐 여지가 있음 | slow update 지침은 `best_skill.md`에 남을 수 있고, 거절 버퍼·meta skill·학습 루프가 빠진다고 구분 | `ckpt/README.md`와 논문 §3.6·§3.7에 다시 대조 |
| 6 | 1차 독립 글 검증 | 이미지 검증 전 `reviewing` 상태라 Tistory 렌더가 수명주기 규칙에 따라 중단됨 | source·metadata·evidence 검증만 통과시키고 ready 전환과 렌더를 최종 검증으로 넘김 | `blog.py check` 오류·경고 0, article source `pass`, 렌더 보류 사유 확인 |
| 7 | 대표 이미지 전체·썸네일 | 후보 단계에서 정밀 장치가 제본기로 읽히거나 거절 트레이가 축소에서 사라질 위험 | 1672x941 원본과 320x180 축소본에서 패치 문서·검증 프레임·거절 조각을 각각 검사 | 세 단서가 모두 남고 재질·조명·원근·크롭·텍스트 무결성 결함 없음, hero `pass` |
| 8 | 인포그래픽 v1~v4 | v1의 단계 제목·도형이 겹쳤고, v4에서는 하단 결과 라벨이 상자 테두리에 지나치게 붙음 | 1700px 세로 캔버스로 단계 간격을 열고, 게이트 문구·점선 경로를 조정한 뒤 v5에서 두 결과 상자를 확대 | v5 전체·360px·5개 확대 영역을 다시 검사해 글자·선·화살표·상자 충돌 없음, infographic `pass` |
| 9 | 1차 ready HTML | 줄을 가로지른 굵은 강조가 변환되지 않아 `**대상 모델의`과 `가중치는 고정**`이 본문에 그대로 노출됨 | 강조 문구를 한 소스 줄에 두고 상태를 `reviewing`으로 되돌린 뒤 검사·렌더를 반복 | 2차 HTML에서 `<strong>대상 모델의 가중치는 고정</strong>`으로 정상 변환 |
| 10 | 2차 ready HTML 모바일 | 360px에서 첫 비교표가 397px, 연구 엔진·Sleep 표가 496px로 본문을 넘어감 | 첫 표는 채택 기준과 결과를 합친 3열로 줄이고, 두 워크플로 비교는 짧은 항목 두 개로 변환 | 3차 렌더에서 본문·두 표의 `scrollWidth`가 모두 360px, 코드 블록만 `overflow-x:auto`로 동작 |
| 11 | 사용자 가독성 피드백 | 원리와 테스트가 먼저 나와 SkillOpt가 무엇에 필요한지 알기 어렵고 구체적인 예시가 없음 | 제목과 도입을 반복 실수 해결로 바꾸고, 테스트를 빼먹는 코딩 에이전트의 6→8 가상 예시를 첫 절에 추가. 기술 용어는 예시 뒤로 이동 | 원고 검사 오류·경고 0. 360px HTML에서 새 예시 표를 포함한 세 표가 본문 폭에 맞고, 가상 수치와 실제 테스트 범위가 분리됨 |
| 12 | 사용자 책임 경계 피드백 | `SKILL.md`만 주면 일상 업무를 자동으로 관찰·개선·배포하는 것처럼 읽힐 수 있음 | 연구 엔진의 사용자 입력 네 가지, SkillOpt 산출물 두 종류, 최종 검토·배포 책임을 새 절과 버그 수정 예시에 추가. Sleep은 별도 실행·staging·adopt 흐름으로 구분 | 공식 첫 실험·새 벤치마크·Sleep 문서와 소스를 대조함. 원고 검사 오류·경고 0, 360px에서 새 책임 표를 포함한 네 표가 본문 폭 360px에 맞고 링크·강조가 정상 변환됨 |

- 중대한 문제가 없으면 `발견한 문제`에 `없음`이라고 쓰고 확인 근거를
  `재검증 결과`에 적습니다.
- 최종 종료 판단: 사용자 입력·출력과 자동화 경계를 보강한 후보도 글
  source·HTML 검증을 통과했습니다. 대표 이미지와 보조 인포그래픽의 뜻과
  배치는 바뀌지 않았고 기존 독립 검증 `pass`를 유지합니다. 현재 후보는
  `ready`입니다.
- 다시 열어 확인한 파일: `article.md`, `brief.md`, `evidence.md`,
  `audit.md`, `artifacts/source-notes.md`, `artifacts/test-log.md`,
  `dist/skillopt-agent-skill-optimizer.html`, `assets/skillopt-hero.png`,
  `assets/skillopt-learning-loop-v5.png`

## 검사와 남은 위험

- 검사 명령:
  - `python3 scripts/blog.py check posts/2026-07-29-skillopt-agent-skill-optimizer`
  - `python3 scripts/blog.py render posts/2026-07-29-skillopt-agent-skill-optimizer`
  - `node artifacts/qa-rendered-article.cjs`
- 최종 검사 결과: 오류 0개·경고 0개. HTML 7,620자이며
  `dist/skillopt-agent-skill-optimizer.html`을 생성했습니다. 760px 자연 폭에서
  본문·표·코드 가로 넘침이 없고, 360px에서는 본문과 새 책임 표를 포함한
  네 표가 정확히 360px에 맞았습니다. 두 코드 블록은 각각 529px·442px
  콘텐츠를 358px 상자 안에서 `overflow-x:auto`로 스크롤합니다. 굵은 강조는
  모두 `<strong>`으로 변환됐고, 공식 링크 6개는 HTTPS 새 창 대상이
  유지됩니다.
- 남은 근거 한계: 논문 성능 52개 셀은 저자 보고이며 독립 재현하지 않았습니다.
  기본 macOS temp 경로의 두 통합 테스트 실패는 현재 소스의 호환 위험으로
  남습니다. 이 범위는 본문에 직접 밝혔습니다.
- 사람이 티스토리에서 확인할 항목: 대표 이미지는 제목 바로 아래, 인포그래픽은
  `예시를 실제 학습으로 바꾸는 여섯 단계` 판단 사슬 뒤에 수동 업로드하고 기록한
  한국어 alt를 입력합니다. 붙여넣은 뒤 실제 스킨에서 외부 링크와 코드
  가로 스크롤을 한 번 확인합니다.
