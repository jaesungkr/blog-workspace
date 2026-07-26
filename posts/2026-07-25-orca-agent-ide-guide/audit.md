# 최종 감사: Orca 사용법 - 여러 CLI 에이전트를 워크트리로 병렬 실행하는 방법

검토일: 2026-07-25
최종 재검토일: 2026-07-26

## 사용자 요청 반영

- [x] 제목을 `Orca 사용법`으로 시작했습니다.
- [x] 대상 제품을 여러 CLI 코딩 에이전트를 한 프로젝트에서 병렬 운영하는
  `stablyai/orca`로 한정했습니다.
- [x] 제품 정의, 장점, 설치, 첫 병렬 세션, custom CLI와 자동화 사용법을
  포함했습니다.
- [x] 권한 기본값, 외부 상태 충돌, 병합 충돌, 검토 비용을 함께 다뤘습니다.

## 구조와 독자

- [x] 제목 앞부분이 실제 검색어 `Orca 사용법`으로 시작합니다.
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤에 같은 브랜치에서 여러 agent를 실행할 때 생기는 익숙한
  문제와 글의 필요성이 나옵니다.
- [x] 첫 5문장 안에 `agent 수보다 worktree와 diff 검토가 핵심`이라는
  기억할 결론이 있습니다.
- [x] CLI agent, ADE, Git worktree를 결과표보다 먼저 설명합니다.
- [x] `저장소·기준 ref -> worktree·branch -> agent -> test·diff ->
  commit·push -> 정리`의 전체 판단 사슬이 보입니다.
- [x] 직접 실험 결과와 앱 공식 기능 설명의 범위를 구분했습니다.
- [x] 기본 선택을 `agent 2개, 같은 성공 조건, Manual 권한`으로 직접
  제시하고 순차 작업·비Git 작업의 예외를 적었습니다.
- [x] 비개발자도 코드 블록 없이 Orca의 역할과 한계를 이해할 수 있습니다.

## 근거와 독창성

- [x] 제품 정의, 설치, worktree, Codex, custom CLI, 권한, commit·push,
  CLI, 텔레메트리 주장을 공식 문서에 인라인으로 연결했습니다.
- [x] 제품 기능은 공식 설명, worktree 결과는 Codex 실행, 외부 상태 격리는
  기술 판단으로 구분했습니다.
- [x] 테스트 입력·환경·판정 규칙·전체 스크립트·원시 출력·실패 사례를
  `evidence.md`와 `artifacts/`에 보존했습니다.
- [x] Codex가 실행한 실험을 사용자의 개인 경험이나 Orca 앱 직접 사용으로
  표현하지 않았습니다.
- [x] 미확인 사실과 해결되지 않은 TODO가 본문에 없습니다.
- [x] worktree 격리 뒤에도 같은 줄의 병합 충돌이 발생한 반례가 보입니다.
- [x] 격리 성공과 merge 실패를 함께 재현한 실험이 source summary를 넘는
  first-party contribution입니다.
- [x] dev.log의 `추측 대신 검증` 기준에 맞게 공식 장점보다 검증 범위와
  도입 판단을 중심에 뒀습니다.

## 문장과 형식

- [x] 인사부터 마지막 문장까지 존대어가 일관됩니다.
- [x] 번역투, 이중 피동, 불필요한 명사화, 상투적인 요약 표현을 점검했습니다.
- [x] 병렬 실행이 무조건 빠르거나 안전하다는 과장 표현이 없습니다.
- [x] 비교 가능한 항목은 표로 묶고 문단은 주제별로 나눴습니다.
- [x] 굵은 강조는 각 절의 핵심 판단에만 제한했습니다.
- [x] em dash, 분리된 참고문헌 부록, 관성적인 면책 문구가 없습니다.
- [x] Log 실전 글의 마무리 기준에 맞춰 작은 실패 테스트와 agent 2개로
  시작하는 다음 행동을 제시했습니다.

## 이미지

- [x] 새 이미지를 생성한 뒤 1672x941 원본과 360px 썸네일로 각각 열어
  확인했습니다.
- [x] 한 장의 종이가 두 개의 독립된 경로로 나뉘고 밝은 검사대에서 겹쳐
  비교되는 구도가 글의 `worktree 분리 -> diff 검토` 메시지와 맞습니다.
- [x] 어두운 기술 배경, 네온, 좌우 대칭 유리 박스, 가짜 코드 UI, 플라스틱
  3D 아이콘을 버리고 밝은 실물 편집 스틸라이프로 방향을 바꿨습니다.
- [x] 썸네일에서도 분리된 두 경로와 하나의 검토면이 한눈에 읽힙니다.
- [x] 원본에서 종이 섬유, 가공 흔적, 금속 결, 종이 두께, 접촉 그림자와
  투과광이 물리적으로 자연스러운지 확인했습니다.
- [x] 로고, 워터마크, 제품명, 글자, 코드, 실제 UI 모조 화면, 보안 상징,
  자동 성공을 암시하는 표현이 없습니다.
- [x] 비대칭 대각선 구도와 넓은 중성 배경에 반응형 크롭용 여백이 있습니다.

- 최종 파일: `assets/orca-worktree-hero-v2.png`
- 해상도: `1672x941`
- SHA-256:
  `80713c612adf77f7fbc15e698bc00ab979b662b6253f16f140fc0d51c49be96e`
- 권장 위치: `대표 이미지 - 제목 바로 아래`
- 한국어 alt: `한 장의 종이가 두 개의 독립된 경로로 나뉜 뒤 밝은 검사대에서
  겹쳐 비교되는 편집 스틸라이프`
- 생성 방식: built-in image generation
- 아트 디렉션: 실제 제작한 종이·금속 미니어처 세트를 촬영한 현대적 편집
  스틸라이프. 따뜻한 밝은 중성색, 절제한 울트라마린 포인트, 비대칭 대각선
  흐름, 자연광 기반의 형태 잡힌 그림자와 재료 미세 질감을 사용했습니다.
- 최종 생성 프롬프트:

  `Use case: stylized-concept
  Asset type: Korean Tistory technology article hero image, wide 16:9 landscape
  Primary request: communicate that one software repository is divided into two
  independent Git worktree paths for parallel CLI-agent work, and that the two
  results are deliberately compared at one review surface before anything is
  merged
  Creative intent: parallel work feels calm, precise, accountable, and
  human-governed rather than chaotic, magical, or futuristic
  Visual idea: a commissioned practical tabletop set photographed in a real
  studio; one continuous strip of warm-white archival paper enters from the
  upper-left, passes through a small precision-machined brushed-aluminum
  divider, and becomes two clearly separated raised folded-paper lanes at
  different depths; each lane develops a different restrained embossed and
  die-cut pattern without any writing; the two lanes arrive at a softly
  illuminated translucent inspection table in the lower-right where their
  layers overlap for comparison, and only one clean paper strip continues
  beyond the review surface
  Art direction: contemporary international magazine still-life photography,
  museum-catalog craft and high-end enterprise campaign finish; clearly a
  physical set, not CGI; refined, tactile, current, intelligent, spacious
  Scene/backdrop: seamless luminous warm-gray studio sweep with faint
  uncoated-paper texture and no horizon clutter
  Subject: the single paper source, two independently crafted physical lanes,
  and the overlapping inspection surface as the immediate focal point
  Style/medium: photorealistic practical miniature set photographed on a
  medium-format camera; realistic lens behavior, subtle film grain, material
  microtexture, slight hand-made imperfection
  Composition/framing: wide landscape with a controlled asymmetric diagonal flow
  from upper-left to lower-right; strong foreground-to-background depth; the
  overlap on the inspection table is the sharpest focal point; meaningful quiet
  negative space; generous crop-safe margins; no mirrored left-right layout
  Lighting/mood: large diffused north-window key light from camera-left, soft
  neutral fill, one narrow warm raking edge light that reveals paper fibers and
  brushed-metal grain; shaped soft shadows and believable contact; bright,
  calm, optimistic, meticulous
  Color palette: ivory, bone, warm gray, graphite, brushed silver, and one
  restrained muted ultramarine accent used sparingly along the inspection edge
  Materials/textures: visible archival paper fibers, crisp but slightly human
  cut edges, believable paper thickness and folds, brushed aluminum machining
  marks, softly frosted acrylic with plausible light transmission, natural
  contact shadows
  Constraints: one clear editorial metaphor; immediately readable at thumbnail
  size; publication-ready; visually connected to isolated parallel work and
  deliberate review; no embedded title, letters, words, code, labels, logos,
  brands, product UI, watermark, people, animals, winner trophy, security
  symbols, or claims of automatic success
  Avoid: dark navy or black technology background, neon cyan or orange,
  glassmorphism boxes, glowing tubes, floating dashboards, fake terminal
  screens, circuit graphics, network-node wallpaper, symmetrical pods, plastic
  3D icons, robot or brain imagery, excessive bloom, volumetric fog, lens flare,
  glossy CG sheen, clutter, cheap stock-photo styling, dated corporate
  illustration, obvious AI artifacts`

### 추가 후보 - Orca 연관성 강화

- [x] 1672x941 원본과 360px 썸네일을 각각 열어 확인했습니다.
- [x] 흑백 오르카 조형물과 정확한 `ORCA` 표기가 썸네일에서도 즉시
  식별됩니다.
- [x] 오르카 아래의 분리된 작업 레일과 하나의 투명 검토 렌즈가 병렬
  worktree와 diff review를 보조하므로 단순한 해양 이미지로 보이지 않습니다.
- [x] 오르카의 등지느러미, 가슴지느러미, 꼬리, 흰색 무늬와 몸통 연결이
  조형물이라는 표현 범위 안에서 자연스럽습니다.
- [x] 원본에서 목재 결, 무광 도장, 종이 섬유, 금속 결, 아크릴 투과광,
  접촉 그림자를 확인했습니다.
- [x] 공식 제품 스크린샷은 worktree 목록, 병렬 pane, diff review라는 구조만
  참고했으며 실제 UI·문구·로고를 복제하지 않았습니다.
- [x] 제3자 agent 로고, 가짜 terminal 화면, 보안 상징, 워터마크,
  과장된 성능 표현이 없습니다.

- 후보 파일: `assets/orca-worktree-hero-v3.png`
- 해상도: `1672x941`
- SHA-256:
  `eaf3e7db2d3a3afe5a2fa14a9511ecff8acaaefefdb7516e622c5d7d9d7e3a8b`
- 추천 용도: `Orca 제품 연관성을 우선할 때 사용할 대표 이미지 후보`
- 한국어 alt: `ORCA 표기 옆의 흑백 오르카 조형물 아래에서 여러 작업 레일이
  하나의 투명 검토 렌즈로 이어지는 편집 스틸라이프`
- 생성 방식: built-in image generation
- 참고 이미지 역할:
  - `https://www.onorca.dev/whats-new/posters/orca-split-screen.jpg`:
    worktree 목록과 병렬 pane의 구조 참고
  - `https://www.onorca.dev/whats-new/posters/annotate-ai-diff.jpg`:
    결과를 한곳에서 비교하는 diff review 구조 참고
- 아트 디렉션: 무광 흑백 오르카 조형물을 중심에 둔 밝은 건축 모형형
  편집 스틸라이프. 따뜻한 흰색과 옅은 북극색 바탕, 비대칭 대각선 구도,
  실물 목재·도자·종이·금속 질감을 사용했습니다.
- 최종 생성 프롬프트:

  `Use case: stylized-concept
  Asset type: Korean Tistory technology article hero image, wide 16:9 landscape
  Input images: Image 1 and Image 2 are official Orca product screenshots used
  only as structural references for the ideas of a worktree sidebar, multiple
  side-by-side agent panes, and a deliberate diff-review pane; do not reproduce
  their text, exact UI, exact layout, or logos
  Primary request: create a new publication hero that is unmistakably about
  Orca, the Agent Development Environment that runs multiple CLI coding agents
  in isolated Git worktrees and brings their results back to human diff review
  Creative intent: Orca feels like a calm, powerful conductor of parallel
  technical work; immediately recognizable as the Orca product topic, but
  refined enough for a large enterprise technology campaign
  Visual idea: a bold black-and-white orca sculpture arcs dynamically above a
  luminous architectural tabletop; beneath its tail, one source channel divides
  into two clearly isolated raised worktree lanes with different embossed line
  rhythms; the two lanes run side by side and meet only beneath one circular
  translucent inspection lens near the orca's head, expressing deliberate diff
  review before merge
  Art direction: commissioned contemporary editorial mixed-media campaign,
  photographed practical set rather than glossy CGI; museum-catalog object study
  combined with precise architectural model making; distinctive, confident,
  tactile, current
  Scene/backdrop: bright seamless warm-white studio with a very pale arctic-blue
  floor plane and generous open space
  Subject: one elegant, anatomically coherent stylized orca sculpture as the
  dominant focal point; one source, two isolated physical lanes, one review lens
  as supporting structure
  Style/medium: photorealistic handcrafted sculpture and paper-relief set,
  medium-format studio photography, subtle film grain and physical
  imperfections; the orca is made from matte black painted wood and warm white
  ceramic with believable seams and weight
  Composition/framing: wide landscape, energetic asymmetric diagonal from
  lower-left to upper-right, orca occupying roughly the central third with
  generous crop-safe margins, one-second thumbnail hierarchy, layered
  foreground depth; avoid mirrored symmetry
  Lighting/mood: broad diffused daylight key from upper-left, quiet cool fill,
  narrow warm raking light across paper and ceramic, shaped soft contact shadows;
  bright, calm, precise, optimistic
  Color palette: warm white, charcoal black, bone, brushed silver, pale arctic
  blue, one small muted aqua status accent; no neon
  Materials/textures: matte ceramic, painted wood grain, uncoated paper fibers,
  brushed aluminum, softly frosted acrylic with plausible transmission and
  refraction
  Text (verbatim): "ORCA" exactly once, small but clearly legible in a restrained
  black geometric sans-serif on a simple warm-white title card integrated into
  the upper-left negative space; no other letters, words, labels, numbers,
  pseudo-code, or pseudo-writing
  Constraints: preserve the product concept from the official references
  without copying their UI; make the orca animal and the
  split-worktree-review mechanism both visible at thumbnail size;
  publication-ready; no third-party agent logos; no fake terminal screens; no
  product claims; no security symbols; no watermark
  Avoid: wildlife documentary ocean scene, cute mascot treatment, cartoon whale,
  aquarium imagery, dark navy or black background, neon cyan or orange,
  glassmorphism boxes, floating dashboards, literal laptop, fake code, circuit
  graphics, network wallpaper, symmetrical pods, plastic 3D icons, robot
  imagery, excessive bloom, volumetric fog, lens flare, glossy CG sheen,
  clutter, cheap stock styling, dated corporate illustration, malformed animal
  anatomy, obvious AI artifacts`

## 보조 인포그래픽

- [x] 과정형 인포그래픽 1장으로 `기준 저장소 -> 두 worktree -> 동일 조건
  검증 -> diff 비교 -> 선택적 반영` 관계를 표현했습니다.
- [x] 글자를 숨겨도 한 개의 기준 노드가 파란색·주황색 두 경로로 분기한 뒤
  검토 렌즈에서 합류하고 하나의 반영 경로로 내려가는 구조가 남습니다.
- [x] 한글 문구, 숫자, 단계명, 화살표는 이미지 모델에 맡기지 않고
  HTML/SVG에서 결정론적으로 배치했습니다.
- [x] 완성 PNG와 편집 가능한 HTML, 재현 가능한 Playwright 렌더 스크립트를
  함께 보존했습니다.
- [x] 1080x1350 원본과 360px 모바일 축소본을 실제로 열어 문구, 화살표,
  분기와 합류 관계를 확인했습니다.
- [x] `worktree가 병합 충돌과 외부 상태까지 격리하지 않는다`는 한계를
  하단 주의 영역에 포함했습니다.

- 최종 파일: `assets/orca-worktree-flow-infographic-v3.png`
- 해상도: `1080x1350` (`4:5`)
- SHA-256:
  `f4145cb30f6f480f15e825a8bfb4993810360743d245e30489307dd569e9277e`
- 이전 파일: `assets/orca-worktree-flow-infographic.png`과
  `assets/orca-worktree-flow-infographic-v2.png`은 이전 검토본으로
  보존하고, 본문에는 v3를 사용합니다.
- 유형: `과정`
- 답하는 질문: `Orca에서 하나의 저장소가 어떻게 두 작업으로 나뉘고,
  무엇을 거쳐 하나의 변경으로 채택되는가?`
- 권장 위치: `1. Orca의 정확한 역할` 마지막 설명 뒤, 2절 앞
- 한국어 alt: `기준 저장소에서 두 개의 독립 worktree로 나뉜 작업이 같은
  조건으로 검증된 뒤 diff 검토를 거쳐 하나의 변경으로 반영되는 Orca 흐름
  인포그래픽`
- 본문 근거: 1~4절과 8~9절, `evidence.md`의 C02, C03, C08,
  C11~C14
- 편집 원본:
  `artifacts/orca-worktree-flow-infographic.html`
- 렌더 스크립트:
  `artifacts/render-orca-worktree-infographic.cjs`
- 제작 방식: Apple SD Gothic Neo를 사용하는 결정론적 HTML/SVG 도식과
  Playwright 래스터 렌더. 이미지 생성 계층은 사용하지 않았습니다.

## 최종 검토와 수정 이력

| 검토 대상 | 발견한 문제 | 수정 | 재검증 |
|---|---|---|---|
| 360px 상단 배지 | `FLOW` 일부가 캡슐 밖으로 벗어남 | 배지 폭을 330px에서 430px로 확대 | 전체 문구가 캡슐 안에서 보임 |
| 360px 최종 반영 영역 | 채택 문구가 우측 정리 박스와 겹침 | 주 반영 캡슐을 610px로 넓히고 글자 크기와 보조 연결선을 조정 | `commit · push · PR`과 `archive · 삭제`가 분리되어 보임 |
| 전체·360px 흐름 | 분기·합류와 주의 문구의 판독성 | 파란색·주황색 경로, 중앙 검토 렌즈, 하단 주의 띠를 순서대로 확인 | 라벨을 숨겨도 `한 기준 -> 두 작업 -> 한 검토 -> 선택` 관계가 유지됨 |
| 사용자 검토 - worktree 설명 | 색상 경로가 설명 문구 뒤를 지나 축소 시 글자 획과 겹침 | 경로를 양쪽 아이콘 열로 옮기고 오른쪽 설명을 경로 안쪽으로 재배치했으며 라벨 크기를 28px에서 30px로 확대 | 전체 크기와 360px에서 `별도 폴더`, `에이전트`, `같은 성공 조건` 문구 뒤에 선이 남지 않음 |
| 사용자 검토 - 분리 단계 | `2 · 분리`가 분기선과 가까워 작은 화면에서 대비가 약함 | 단계명 뒤에 배경색과 같은 불투명 캡슐을 추가 | 360px에서 단계명과 두 분기선이 서로 분리되어 보임 |
| 사용자 재검토 - 검토 기준 | 중앙 화살촉이 `테스트 결과 · 변경 범위 · 유지보수성` 중 `변경 범위`를 가림 | SVG marker를 `userSpaceOnUse` 22px로 고정하고 화살표 시작점을 아래로 이동 | 검토 영역 확대 크롭과 360px에서 세 문구와 화살촉 사이에 빈 공간이 보임 |
| 확대 크롭 추가 검토 - 양쪽 검증 | 파란색·주황색 화살촉도 `테스트 · lint`에 닿음 | 두 marker를 `userSpaceOnUse` 24px로 고정 | worktree 영역 확대 크롭과 360px에서 두 `테스트 · lint` 문구가 모두 완전히 보임 |
| 최종 겹침 감사 | 전체 미리보기만으로 세부 충돌을 놓칠 수 있음 | 상단, worktree, 검토, 반영 영역의 100% 확대 크롭과 360px 래스터를 별도로 확인 | 모든 텍스트에서 선·화살촉·아이콘·그림자·경계 침범이 없음을 확인 |

## 검사와 남은 위험

- 검사 명령:
  `python3 scripts/blog.py check posts/2026-07-25-orca-agent-ide-guide`
- 검사 결과: ready 상태에서 오류 0개, 경고 0개
- 렌더 검사:
  `dist/orca-agent-ide-guide.html`을 생성하고 760px 폭의 헤드리스 Chrome에서
  전체 문서를 열어 표, 목록, 코드 블록과 문단 순서를 확인했습니다.
- 아직 남은 위험:
  - Orca 앱의 실제 UI 안정성·성능·병렬 agent의 비용과 속도는 직접
    측정하지 않았습니다.
  - 기능과 기본 권한 인자는 업데이트가 잦아 발행 뒤 바뀔 수 있습니다.
  - worktree 실험은 단일 파일·동일 줄·2개 branch의 1회 재현입니다.
  - 공식 텔레메트리 설명은 벤더 자료이며, 각 CLI agent의 데이터 정책은
    별도입니다.
- 사람이 티스토리에서 확인할 항목:
  - 대표 이미지 업로드와 alt 입력
  - 1절 뒤에 보조 인포그래픽 업로드와 alt 입력
  - 카테고리 `Log > AI 개념 · 실전`
  - 영문 주소 `orca-agent-ide-guide`
  - 표와 긴 코드 블록의 모바일 줄바꿈
  - 공식 문서의 권한 메뉴와 기본값이 발행 시점에도 같은지
  - 발행 후 `published_url`과 상태 기록
