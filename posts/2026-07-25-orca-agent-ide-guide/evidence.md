# 근거 지도: Orca 사용법 - 여러 CLI 에이전트를 워크트리로 병렬 실행하는 방법

## 조사 기준

- 조사일: 2026-07-25
- 조사 주체: Codex
- 제품 대상: `stablyai/orca`
- 공식 자료: Orca 공식 문서와 공개 GitHub 저장소
- 직접 검증: Git worktree 두 개의 파일 격리와 병합 충돌 재현
- 직접 실행하지 않은 범위: Orca 데스크톱 앱 설치, GUI 안정성, 실제 AI
  에이전트 여러 개의 동시 토큰·시간·품질 비교

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Orca는 여러 AI 코딩 에이전트를 나란히 실행하는 데스크톱 IDE이며 자체 AI 모델이 아님 | 공식 | 확인 | https://www.onorca.dev/docs | 제품 공식 정의 |
| C02 | 각 작업은 별도 Git worktree, 브랜치, 파일, 에이전트 터미널을 가짐 | 공식 | 확인 | https://www.onorca.dev/docs/model/worktrees | 앱 구현의 공식 설명 |
| C03 | 첫 세션은 repo 추가 -> worktree 생성 -> agent 선택 -> 병렬 실행 -> diff 비교 -> commit·push 흐름임 | 공식 | 확인 | https://www.onorca.dev/docs/first-session | 메뉴·화면은 업데이트될 수 있음 |
| C04 | macOS·Windows·Linux 빌드가 있고 macOS는 Homebrew cask로 설치 가능함 | 공식 | 확인 | https://www.onorca.dev/docs/install | 배포 채널은 변경 가능 |
| C05 | Codex는 먼저 설치·로그인해야 하고 Orca가 `~/.codex`와 worktree 경로를 사용함 | 공식 | 확인 | https://www.onorca.dev/docs/agents/codex | 계정 처리 방식은 버전별 확인 필요 |
| C06 | Custom CLI는 이름, binary·command, 기본 인자, startup hook을 설정해 추가할 수 있음 | 공식 | 확인 | https://www.onorca.dev/docs/agents/custom-cli | OSC title이 없으면 상태 점은 제한됨 |
| C07 | 기본 지원 agent는 권한 우회·full autonomy 실행 인자를 사용하며 Manual로 바꿀 수 있음 | 공식 | 확인 | https://www.onorca.dev/docs/agents/supported | 매우 중요한 보안·운영 설정 |
| C08 | diff에서 hunk·file stage, commit, push를 지원하고 일반 push에서 자동 force-push하지 않음 | 공식 | 확인 | https://www.onorca.dev/docs/review/commit-push | 실제 git hook·remote 권한에 종속 |
| C09 | 공식 설명상 코드·프롬프트·terminal 출력은 텔레메트리로 전송하지 않으며 익명 사용 이벤트는 보낼 수 있음 | 공식 | 확인 | https://www.onorca.dev/docs/telemetry | 타사 agent의 데이터 정책은 별도 |
| C10 | 공개 저장소는 MIT License임 | 공식 | 확인 | https://github.com/stablyai/orca | 상표·타사 서비스 조건은 별도 |
| C11 | 두 worktree가 같은 기준 커밋에서 같은 파일을 서로 다른 값으로 수정해도 기준 checkout은 깨끗하게 유지됨 | Codex 실행 | 확인 | `artifacts/worktree-isolation-output.txt` | 작은 로컬 저장소 1회 실험 |
| C12 | 두 브랜치가 같은 줄을 다르게 수정하면 두 번째 병합에서 content conflict가 발생함 | Codex 실행 | 확인 | merge exit 1, conflict marker 3개 | 의도적으로 만든 단일 파일 반례 |
| C13 | worktree는 작업 중 파일 덮어쓰기를 줄이지만 최종 병합 충돌을 없애지는 않음 | Codex 실행·판단 | 확인 | C11과 C12를 함께 해석 | 모든 충돌 유형을 시험한 것은 아님 |
| C14 | worktree는 운영체제 권한·외부 서비스까지 격리하는 보안 샌드박스가 아님 | 기술 판단 | 확인 | Git worktree의 범위와 C07의 권한 기본값 | 컨테이너·VM을 함께 쓰는 구성은 별도 |

## 직접 검증 설계

- 질문:
  1. 같은 기준 커밋에서 만든 두 worktree가 같은 경로의 파일을 서로 다른
     내용으로 수정해도 작업 중에는 서로 덮어쓰지 않는가?
  2. 격리된 두 변경이 같은 줄을 건드리면 최종 병합에서도 충돌이 사라지는가?
- 실행 주체: Codex
- 환경과 확인 시점:
  - 2026-07-25
  - macOS Darwin 25.5.0 arm64
  - Git 2.53.0
- 입력:
  - 임시 Git 저장소 한 개
  - 기준 파일 `config.txt`: `mode=base`
  - 브랜치·worktree `agent-a`: `mode=agent-a`
  - 브랜치·worktree `agent-b`: `mode=agent-b`
- 전처리 또는 표현:
  - 기준 commit에서 `git worktree add -b`로 두 worktree 생성
  - 각 worktree의 같은 경로 파일을 서로 다른 값으로 수정
  - 각 변경을 별도 commit한 뒤 기준 checkout에서 `agent-a`, `agent-b`
    순서로 merge
- 비교·판정 규칙:
  - 격리 성공: 기준 checkout은 `mode=base`와 clean status를 유지하고,
    두 worktree는 서로 다른 파일 내용과 각자의 modified status를 보임
  - 병합 충돌: 두 번째 merge가 0이 아닌 exit code로 끝나고 Git이
    `CONFLICT (content)`를 보고함
- 성공 기준: 격리 결과와 병합 반례가 모두 원시 로그에 남음
- 반복 횟수와 표본 크기: 단일 파일·동일 줄·worktree 2개, 1회
- 보존한 원자료:
  - `artifacts/run-worktree-isolation.sh`
  - `artifacts/worktree-isolation-output.txt`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 기준 checkout | `mode=base`, Git status clean | `artifacts/worktree-isolation-output.txt` | 작업 중 기준 checkout 보존 |
| E02 | `agent-a` worktree | `mode=agent-a`, `M config.txt` | 같은 파일 | A의 작업 디렉터리 |
| E03 | `agent-b` worktree | `mode=agent-b`, `M config.txt` | 같은 파일 | B의 작업 디렉터리 |
| E04 | A를 먼저 merge한 뒤 B merge | exit 1, `CONFLICT (content)`, conflict marker 3개 | 같은 파일 | 같은 줄 수정의 병합 반례 |
| E05 | 이 작은 fixture의 `du -sk` | main 180KB, 각 추가 worktree 8KB | 같은 파일 | 일반 프로젝트의 저장공간 비용으로 일반화 금지 |

## 실패와 반례

- 예상과 달랐던 결과: worktree 두 개가 작업 중에는 완전히 분리됐지만,
  같은 줄을 수정한 두 번째 브랜치는 자동 병합되지 않았습니다.
- 실패한 입력: `agent-a`와 `agent-b` 모두 `config.txt` 첫 줄의 같은 값을
  서로 다르게 변경했습니다.
- 해석: Orca의 worktree 격리는 에이전트 실행 중 파일 상태의 간섭을
  줄입니다. 어느 결과를 채택할지 결정하는 diff 검토와 병합 책임은 남습니다.
- 일반화하면 안 되는 범위:
  - 이번 실험은 Orca 앱의 UI·성능 테스트가 아님
  - worktree의 작은 디스크 사용량을 실제 대형 저장소의 비용으로 일반화하지 않음
  - 한 파일 실험을 모든 Git 충돌 유형의 빈도로 해석하지 않음
  - 여러 에이전트가 같은 외부 DB·포트·클라우드 계정을 공유하는 문제는
    worktree 실험으로 해결됐다고 보지 않음

## 미해결 항목

본문에 넣어야 할 미확인 사실은 없습니다. 다음 항목은 의도적으로 주장하지
않습니다.

- 실제 Orca 앱에서 몇 개의 agent까지 안정적으로 실행되는지
- 병렬 실행이 단일 agent보다 얼마나 빠르거나 저렴한지
- 특정 모델 조합이 항상 더 좋은 결과를 내는지
- 팀·기업 환경의 보안 적합성

## 출처 메모

공식 문서의 핵심 내용을 `artifacts/source-snapshot.md`에 조사일과 한계와
함께 보존했습니다. 기능·메뉴·기본값은 업데이트가 빠르므로 발행 직전 공식
문서를 다시 확인해야 합니다.
