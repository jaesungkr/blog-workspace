# 근거 지도: Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Git 저장소 하나는 main worktree 하나와 linked worktree 여러 개를 가질 수 있고, 서로 다른 branch를 동시에 checkout할 수 있음 | 공식 | 확인 | Git `git-worktree` 공식 문서 DESCRIPTION | bare 저장소와 submodule superproject는 별도 제약이 있음 |
| C02 | `git worktree add -b <branch> <path> <start-point>`는 새 branch를 만들고 지정 폴더에 checkout함 | 공식+Codex 실행 | 확인 | Git 공식 문서 OPTIONS, E01 | 경로와 branch가 이미 연결돼 있으면 Git의 안전장치가 거부할 수 있음 |
| C03 | linked worktree는 object database와 일반 branch·tag ref를 공유하지만 각자 `HEAD`, `index`, 작업 파일을 가짐 | 공식 | 확인 | Git 공식 문서 COMMANDS·REFS·DETAILS | pseudo ref와 `refs/bisect`, `refs/worktree`, `refs/rewritten`은 worktree별 예외이며 완전한 환경 격리가 아님 |
| C04 | 두 linked worktree에서 서로 다른 파일을 수정하면 각 `git status`에는 자기 변경만 나타나고 main은 깨끗하게 유지됨 | Codex 실행 | 확인 | E02, `worktree-test-2026-08-21.log` | 작은 fixture의 두 파일을 한 번씩 바꾼 결과 |
| C05 | 각 변경을 독립 commit한 뒤 main에서 차례로 merge하자 둘 다 정상 병합됨 | Codex 실행 | 확인 | E03, 실행 로그와 graph 캡처 | 서로 다른 파일 수정 한 사례이며 모든 병합의 성공을 뜻하지 않음 |
| C06 | 두 branch가 같은 `index.html` 버튼 줄을 서로 다르게 바꾸자 두 번째 merge가 exit code 1과 content conflict를 반환함 | Codex 실행 | 확인 | E04, `UU index.html`, `--diff-filter=U` 결과 | 의도적으로 만든 한 줄 충돌 반례 |
| C07 | linked worktree 제거는 `git worktree remove`를 쓰며 clean하지 않으면 기본 제거가 거부됨 | 공식+Codex 실행 | 확인 | Git 공식 문서 `remove`, E05 | `--force`는 변경 손실 위험이 있어 기본 절차에서 권하지 않음 |
| C08 | 폴더를 수동 삭제해 metadata가 남았을 때 `git worktree prune`이 stale 정보를 정리하며 `--dry-run`으로 먼저 확인 가능 | 공식 | 확인 | Git 공식 문서 `prune`, `--dry-run` | 수동 이동은 `repair`가 필요한 다른 문제일 수 있음 |
| C09 | worktree는 운영체제 권한, 네트워크, 공유 DB, 포트, 홈 디렉터리 자격 증명을 격리하지 않음 | Git 구조 해석 | 확인 | C03의 분리 범위와 Git 문서 DETAILS에서 도출 | 보안 샌드박스 성능을 직접 시험한 결과가 아님 |
| C10 | Codex 앱은 새 작업에서 `Worktree`와 시작 branch를 선택하면 worktree를 만들며, CLI는 별도 worktree 디렉터리에서 실행할 수 있음 | 공식+로컬 실행 구조 | 확인 | OpenAI Codex Worktrees 공식 문서, 로컬 `codex-cli 0.148.0-alpha.9` 확인 | 앱은 기본 detached HEAD 흐름이며 이 글의 수동 branch 생성과 별도 경로임 |
| C11 | 단계별 터미널 이미지는 실제 로그의 명령과 핵심 출력을 재조판했으며 실제 Terminal 앱 화면 자체는 아님 | Codex 실행 | 확인 | HTML 렌더 소스, raw PNG, SHA-256 | 임시 경로·색상·제목·줄바꿈을 공개용으로 편집함 |

## 직접 검증 설계

- 질문: worktree 두 개가 작업 중 파일 변경을 분리하는지, 다른 파일의 변경은 정상 merge되고 같은 줄의 변경은 충돌하는지, 안전한 제거가 가능한지
- 실행 주체: Codex
- 환경과 확인 시점: macOS 26.5.2, Git 2.53.0, 2026-08-21 KST
- 입력: `index.html`과 `README.md`가 있는 새 저장소, 분리 수정 patch 2개, 같은 줄 충돌 patch 2개
- 전처리 또는 표현: `main`에서 두 linked worktree를 만든 뒤 각 patch를 별도 폴더에 적용함. 공개 캡처의 임시 절대 경로는 `~/worktree-demo`로 바꿈
- 비교·판정 규칙: 각 worktree와 main의 `git status`, merge 종료 상태, `git diff --name-only --diff-filter=U`, 최종 `git worktree list`를 관찰함
- 성공 기준: 분리 수정 단계에서 main은 clean, 서로 다른 파일의 두 merge는 성공, 같은 줄의 두 번째 merge는 non-zero와 unresolved path 1개, 제거 후 linked worktree 0개
- 반복 횟수와 표본 크기: 전체 시나리오 2회 실행. 첫 실행에서 공개 경로 치환 결함을 발견해 스크립트를 수정했고, 두 번째 실행을 근거 로그로 채택함
- 보존할 원자료: `artifacts/run/run-worktree-test.sh`, `fixture/`, `patches/`, `worktree-test-2026-08-21.log`, `artifacts/captures/terminal-shots.html`, raw PNG 7장

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 깨끗한 main에서 linked worktree 2개 생성 | main, `feat/home-copy`, `docs/agent-rule` 세 폴더가 같은 시작 commit에서 생성됨 | `artifacts/run/worktree-test-2026-08-21.log` | `git worktree add -b` 한 방식 |
| E02 | Claude 폴더는 `index.html`, Codex 폴더는 `README.md` 수정 | 각 status에는 자기 파일 1개만 표시되고 main은 clean | 같은 로그와 `04-isolated-status-v3.png` | 서로 다른 파일을 수정한 작은 fixture |
| E03 | 두 branch를 main에 순서대로 `--no-ff` merge | 두 merge 모두 성공했고 graph에 두 branch commit과 merge commit이 남음 | 같은 로그와 `05-merge-graph-v3.png` | 자동 테스트는 없는 정적 파일 예시 |
| E04 | 두 branch가 같은 버튼 문구 줄 수정 | 두 번째 merge exit code 1, `UU index.html`, unresolved path 1개 | 같은 로그와 `06-conflict-boundary-v3.png` | 같은 줄 text conflict 반례 |
| E05 | merge abort 뒤 두 linked worktree 제거 | 최종 list에 main만 남고 `prune --dry-run` 출력 없음 | 같은 로그와 `07-cleanup-v5.png` | clean linked worktree 제거 경로 |

## 실패와 반례

- 첫 실행에서 macOS의 `/tmp -> /private/tmp` 경로 해석 때문에 공개 로그 치환 결과가 `/private~/worktree-demo`로 나타났습니다. `pwd -P`로 실제 임시 루트를 고정한 뒤 두 번째 실행에서 수정됐습니다.
- worktree 두 개가 같은 줄을 다르게 바꾼 실험에서는 작업 중 서로의 변경을 보지 않았지만 main 병합 때 충돌했습니다.
- worktree 분리만으로 동일한 개발 서버 포트, 외부 데이터베이스, lockfile, 공용 캐시, 환경 변수와 운영체제 권한이 분리된다고 일반화하면 안 됩니다.

## 미해결 항목

- 없음. submodule superproject와 worktree별 설정은 본문 범위에서 제외하고 제한으로만 밝힘

## 출처 메모

- Git 공식 문서: https://git-scm.com/docs/git-worktree
- OpenAI Codex Worktrees 공식 문서: https://developers.openai.com/codex/environments/git-worktrees
- 기존 dev.log Orca 글: https://dop3n.tistory.com/entry/Orca-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%97%AC%EB%9F%AC-CLI-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%EB%A5%BC-%EC%9B%8C%ED%81%AC%ED%8A%B8%EB%A6%AC%EB%A1%9C-%EB%B3%91%EB%A0%AC-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
