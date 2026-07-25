# 최종 감사: Orca 사용법 - 여러 CLI 에이전트를 워크트리로 병렬 실행하는 방법

검토일: 2026-07-25

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

## 검사와 남은 위험

- 검사 명령:
  `python3 scripts/blog.py check posts/2026-07-25-orca-agent-ide-guide`
- 검사 결과: ready 상태에서 오류 0개, 경고 0개
- 아직 남은 위험:
  - Orca 앱의 실제 UI 안정성·성능·병렬 agent의 비용과 속도는 직접
    측정하지 않았습니다.
  - 기능과 기본 권한 인자는 업데이트가 잦아 발행 뒤 바뀔 수 있습니다.
  - worktree 실험은 단일 파일·동일 줄·2개 branch의 1회 재현입니다.
  - 공식 텔레메트리 설명은 벤더 자료이며, 각 CLI agent의 데이터 정책은
    별도입니다.
- 사람이 티스토리에서 확인할 항목:
  - 대표 이미지 업로드와 alt 입력
  - 카테고리 `Log > AI 개념 · 실전`
  - 영문 주소 `orca-agent-ide-guide`
  - 표와 긴 코드 블록의 모바일 줄바꿈
  - 공식 문서의 권한 메뉴와 기본값이 발행 시점에도 같은지
  - 발행 후 `published_url`과 상태 기록
