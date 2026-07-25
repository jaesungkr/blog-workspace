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

- [x] 최종 이미지를 생성한 뒤 1672x941 원본으로 열어 확인했습니다.
- [x] 두 worktree가 분리되어 작업하고 중앙 diff 검토 지점으로 모이는
  구도가 글의 핵심 메시지와 맞습니다.
- [x] 초기 이미지의 자물쇠·방패가 보안 샌드박스를 암시할 수 있어 중립적인
  branch 검토 checkpoint로 한 차례 수정했습니다.
- [x] 로고, 워터마크, 제품명, 장식 텍스트, 실제 UI 모조 화면이 없습니다.
- [x] 양쪽 worktree와 중앙 검토 지점에 반응형 크롭용 여백이 있습니다.

- 최종 파일: `assets/orca-worktree-hero.png`
- 해상도: `1672x941`
- SHA-256:
  `d7b7272c9a7a156a110a0bf46f1d2f9a87630fc05add31f73aca98dad616d3ef`
- 권장 위치: `대표 이미지 - 제목 바로 아래`
- 한국어 alt: `하나의 Git 저장소에서 청록색과 주황색 worktree 두 개로
  작업을 나눈 뒤 중앙의 코드 diff를 검토하는 일러스트`
- 생성 방식: built-in image generation
- 최초 생성 프롬프트:

  `Use case: stylized-concept. Asset type: Korean Tistory blog hero image.
  Visualize one software repository branching into two isolated Git worktree
  environments where separate CLI coding agents work in parallel, then both
  paths converge at a deliberate human diff-review checkpoint before merge.
  Sophisticated dark developer workspace, polished premium editorial 3D
  illustration, wide 16:9 landscape, deep navy with teal and warm amber,
  generous crop-safe margins. Factually neutral, no humans, logos, branded
  mascots, recognizable product UI, watermark, embedded text, labels, title,
  numbers, stock laptop scene, dense infographic, winner symbolism, combat
  imagery, or unsupported speed claims.`

- 최종 수정 프롬프트:

  `Preserve the full 16:9 composition, both isolated glass worktree pods, teal
  and amber branch paths, terminal panels, central magnifying-glass diff review,
  lighting, materials, camera, and all other details. Replace only the small
  lock-and-shield security icon at the central junction with a neutral
  code-review checkpoint symbol: a simple unbranded split-branch junction
  passing through a small circular check marker. It must communicate human
  review before merge, not cybersecurity, sandboxing, guaranteed safety, or
  automatic success. Remove every lock, shield, or security emblem. Keep no
  embedded words, letters, labels, logos, watermark, or recognizable product
  UI.`

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
