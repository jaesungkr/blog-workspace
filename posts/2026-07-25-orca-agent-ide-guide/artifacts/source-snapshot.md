# Orca 공식 자료 조사 스냅샷

- 조사일: 2026-07-25
- 조사 주체: Codex
- 대상: `stablyai/orca`와 `onorca.dev` 공식 문서
- 범위: 제품 정의, 설치, worktree 구조, 첫 3-agent 세션, 지원 에이전트,
  권한 기본값, Codex 연동, custom CLI, diff 검토, CLI, 개인정보·텔레메트리
- 직접 Orca 앱 설치·UI 실행: 하지 않음
- 직접 실행 범위: Orca가 병렬 격리의 기반으로 사용하는 Git worktree
  메커니즘과 병합 충돌

## 확인한 공식 문서와 핵심 근거

1. https://www.onorca.dev/docs
   - Orca는 여러 AI 코딩 에이전트를 나란히 실행하는 데스크톱 IDE임
   - 작업마다 Git worktree, 에이전트 터미널, 브라우저 탭을 둠
   - Orca 자체는 모델, Git 대체물, 호스팅 VPS가 아님

2. https://www.onorca.dev/docs/install
   - macOS, Windows, Linux용 데스크톱 앱 제공
   - macOS Homebrew 명령:
     `brew install --cask stablyai/orca/orca`
   - 첫 실행에서 홈 디렉터리 접근을 요청하고 `~/.claude`, `~/.codex`,
     Ghostty 설정 가져오기를 제안함

3. https://www.onorca.dev/docs/first-session
   - 저장소 추가 -> worktree 생성 -> agent 선택 -> 같은 작업을 여러
     worktree에서 실행 -> split pane -> diff 비교 -> commit/push 흐름

4. https://www.onorca.dev/docs/model/worktrees
   - worktree마다 별도 브랜치, 디스크의 파일, 에이전트 터미널을 가짐
   - 기준 ref는 보통 `origin/main`
   - 일반 Git 명령을 그대로 사용할 수 있음
   - worktree 삭제 시 확인 뒤 디렉터리와 브랜치를 함께 제거함

5. https://www.onorca.dev/docs/agents/supported
   - Codex, Claude Code, OpenCode 등 여러 CLI agent를 기본 지원
   - custom CLI도 추가 가능
   - 기본 실행 인자에 각 에이전트의 권한 우회·full autonomy 플래그를
     채워 둠
   - Settings -> Agents -> Agent Permissions에서 Manual로 전환 가능

6. https://www.onorca.dev/docs/agents/codex
   - Codex를 먼저 설치하고 터미널에서 로그인해야 함
   - Orca는 `~/.codex`의 계정·자격 정보를 읽고 선택한 worktree를
     현재 작업 디렉터리로 Codex를 실행함

7. https://www.onorca.dev/docs/agents/custom-cli
   - Settings -> Agents -> Add custom agent에서 이름, 실행 파일 또는
     명령, 기본 인자, 선택적 startup hook을 설정함
   - OSC title을 내보내지 않는 custom agent도 터미널로는 작동하지만
     상태 점이 표시되지 않을 수 있음

8. https://www.onorca.dev/docs/review/commit-push
   - diff에서 파일 또는 hunk별 stage, commit, push, review 생성을 지원
   - 일반 Push에서 자동 force-push하지 않음
   - 저장소의 pre-commit hook을 그대로 실행함

9. https://www.onorca.dev/docs/cli/overview
   - 데스크톱 앱에 포함된 `orca` CLI는 Settings -> Experimental -> CLI에서
     등록
   - `command -v orca`, `orca status --json`으로 확인
   - worktree, terminal, file, browser, automation 명령 제공

10. https://www.onorca.dev/docs/telemetry
    - 공식 설명상 파일 내용, 프롬프트, agent 출력, terminal 출력, repo·branch
      이름은 전송하지 않음
    - 익명 제품 사용 이벤트는 전송할 수 있음
    - 앱 설정, `DO_NOT_TRACK=1`, `ORCA_TELEMETRY_DISABLED=1`로 비활성화 가능

11. https://github.com/stablyai/orca
    - 공개 저장소, MIT License
    - 공식 README는 병렬 worktree, terminal split, diff annotation,
      GitHub·Linear, SSH worktree, mobile companion 등을 소개함

## 출처 해석 한계

- 위 기능 설명과 개인정보 처리 설명은 프로젝트 공식 자료이므로 벤더 자체
  설명입니다.
- 기능과 메뉴는 업데이트가 잦아 이후 버전에서 달라질 수 있습니다.
- Orca 앱 UI의 안정성, 성능, 실제 사용량 절감은 이번 조사에서 독립적으로
  측정하지 않았습니다.
- 타사 CLI agent가 처리하는 코드·프롬프트의 보존 정책은 Orca 텔레메트리
  정책과 별개입니다.
