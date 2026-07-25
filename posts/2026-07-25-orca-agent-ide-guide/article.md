---
title: "Orca 사용법 - 여러 CLI 에이전트를 워크트리로 병렬 실행하는 방법"
slug: orca-agent-ide-guide
date: 2026-07-25
category: "Log"
subcategory: "AI 개념 · 실전"
status: ready
tags: [Orca, CLI 에이전트, AI 코딩 에이전트, Git worktree, Codex, Claude Code, 개발 도구]
summary: "Orca가 여러 CLI 코딩 에이전트를 Git worktree로 격리하는 원리와 장점, 설치부터 첫 병렬 세션·diff 검토까지의 사용법, 권한과 병합 충돌의 한계를 정리합니다."
hero_image: assets/orca-worktree-hero.png
published_url: ""
sources:
    - https://www.onorca.dev/docs
    - https://www.onorca.dev/docs/install
    - https://www.onorca.dev/docs/first-session
    - https://www.onorca.dev/docs/model/worktrees
    - https://www.onorca.dev/docs/agents/supported
    - https://www.onorca.dev/docs/agents/codex
    - https://www.onorca.dev/docs/agents/custom-cli
    - https://www.onorca.dev/docs/review/commit-push
    - https://www.onorca.dev/docs/cli/overview
    - https://www.onorca.dev/docs/telemetry
    - https://github.com/stablyai/orca
---

안녕하세요. dev.log입니다.

Codex나 Claude Code를 한 터미널에서 잘 쓰다가 두 개를 동시에 실행하면 문제가 달라집니다. 같은 브랜치의 파일을 서로 고치고, 한쪽이 설치한 의존성이나 만든 임시 변경 때문에 다른 쪽 테스트가 흔들릴 수 있습니다. **Orca의 핵심은 에이전트를 많이 띄우는 화면이 아니라, 작업마다 독립된 Git worktree를 주고 결과를 diff로 비교하는 운영 방식입니다.** 처음부터 다섯 개를 켜기보다 에이전트 두 개와 명확한 성공 조건으로 시작하는 편이 좋습니다.

이번 글에서는 여러 CLI 코딩 에이전트를 한 프로젝트 안에서 관리하는 `stablyai/orca`를 다룹니다. 설치와 메뉴 흐름은 2026년 7월 25일 공식 문서를 기준으로 확인했고, Orca가 격리에 사용하는 Git worktree의 효과와 한계는 작은 저장소에서 Codex가 직접 재현했습니다. Orca 앱의 성능이나 AI 모델 품질을 직접 비교한 사용 후기는 아니라는 범위도 먼저 밝혀 둡니다.

### 1. Orca의 정확한 역할

[Orca 공식 문서](https://www.onorca.dev/docs)는 이 제품을 여러 AI 코딩 에이전트를 나란히 실행하는 데스크톱 IDE로 설명합니다. IDE가 사람의 편집기·터미널·디버거를 한곳에 모았다면, Orca는 여기에 에이전트별 작업공간과 상태, 결과 검토 흐름을 더한 **ADE(Agent Development Environment)**에 가깝습니다.

여기서 CLI 에이전트는 터미널 명령으로 실행하는 코딩 도구입니다. Codex, Claude Code, OpenCode처럼 저장소의 파일을 읽고 수정하며 테스트도 실행하는 프로그램을 떠올리면 됩니다. Orca 자체가 새로운 AI 모델을 제공하는 것은 아닙니다. 이미 설치하고 로그인한 에이전트와 각 서비스의 구독을 한 화면에서 운영합니다.

Orca의 기본 흐름은 다음처럼 이어집니다.

> Git 저장소와 기준 브랜치 → 작업별 worktree·브랜치 → CLI 에이전트 실행 → 테스트와 diff 비교 → 채택할 변경만 commit·push → 나머지 worktree 정리

Git worktree는 한 저장소의 여러 브랜치를 서로 다른 폴더에 동시에 checkout하는 Git 기능입니다. 일반 브랜치 전환은 한 작업 폴더의 내용을 계속 바꾸지만, worktree는 작업 A와 작업 B의 실제 파일 폴더를 따로 둡니다. Orca는 이 구조에 에이전트 터미널, 편집기, 브라우저, diff 검토 화면을 묶습니다.

### 2. 터미널 여러 개와 다른 지점

터미널 창만 두 개 열어도 프로세스는 병렬로 실행됩니다. 그러나 두 터미널의 현재 작업 디렉터리가 같다면 파일 상태도 같습니다. 에이전트 A가 파일을 수정하는 순간 에이전트 B도 그 변경을 보게 되고, 아직 완성되지 않은 코드 위에서 테스트하거나 추가 수정을 시작할 수 있습니다.

Orca의 차이는 프로세스 수가 아니라 **변경 상태의 경계**에 있습니다.

| 비교 항목 | 같은 폴더의 터미널 분할 | Orca의 worktree 분리 |
|---|---|---|
| 작업 파일 | 두 agent가 공유 | 작업별 별도 폴더 |
| Git 브랜치 | 전환 시 서로 영향 | worktree별 별도 브랜치 |
| 미완성 변경 | 다른 agent에게 즉시 노출 | 해당 worktree 안에 유지 |
| 결과 비교 | 직접 경로·상태를 추적 | 기준 ref와 diff로 검토 |
| 정리 | stash·복원·브랜치 전환 필요 | 채택·보관·삭제를 작업 단위로 처리 |

[공식 worktree 문서](https://www.onorca.dev/docs/model/worktrees)에 따르면 각 worktree는 자체 브랜치, 디스크의 파일, 에이전트 터미널을 가집니다. 기준이 되는 ref는 보통 `origin/main`이고, 필요하면 다른 브랜치나 특정 commit에서 시작할 수 있습니다. Orca 밖의 터미널에서 `git status`, `git rebase`, `git cherry-pick` 같은 일반 Git 명령을 그대로 써도 됩니다.

### 3. Orca의 실질적인 장점

첫 번째 장점은 작업 중 파일 충돌을 줄이는 것입니다. 에이전트마다 독립된 폴더가 있으므로 한쪽의 미완성 변경이 다른 쪽 실행 환경에 바로 섞이지 않습니다. 같은 버그에 서로 다른 해결법을 시도시키거나, 기능 구현과 테스트 보강을 나누기에 적합합니다.

두 번째 장점은 결과를 대화가 아니라 코드로 비교하게 만든다는 점입니다. 어느 에이전트가 더 자신 있게 설명했는지가 아니라 테스트 통과 여부, 변경 범위, diff의 복잡도, 유지보수성을 보고 선택할 수 있습니다. [Orca의 commit·push 문서](https://www.onorca.dev/docs/review/commit-push)는 파일 또는 hunk 단위 stage, 저장소의 pre-commit hook 실행, 일반 push에서 자동 force-push를 하지 않는 흐름을 설명합니다.

세 번째 장점은 여러 실행의 상태를 한곳에서 확인하는 것입니다. 에이전트가 작업 중인지, 입력을 기다리는지, 끝났는지를 worktree별로 볼 수 있고 split pane에서 여러 터미널을 함께 배치할 수 있습니다. 다만 custom CLI가 OSC title이라는 터미널 상태 신호를 보내지 않으면 상태 점은 표시되지 않을 수 있습니다. 이 경우에도 터미널 자체는 정상적으로 작동한다고 [custom CLI 문서](https://www.onorca.dev/docs/agents/custom-cli)는 설명합니다.

마지막으로 특정 모델에 묶이지 않습니다. 기본 목록에 없는 CLI도 `Settings → Agents → Add custom agent`에서 이름, 실행 파일이나 명령, 기본 인자, 선택적 startup hook을 등록할 수 있습니다. **하나의 모델을 고르는 도구라기보다 서로 다른 에이전트를 같은 Git 검토 규칙 아래 두는 도구**라는 표현이 더 정확합니다.

### 4. worktree 격리 재현 결과

공식 설명만 요약하면 worktree가 실제로 어디까지 해결하는지 놓치기 쉽습니다. 그래서 macOS Darwin 25.5.0 arm64와 Git 2.53.0 환경에서 임시 저장소를 만들고, 같은 기준 commit에서 `agent-a`와 `agent-b` worktree를 생성했습니다.

기준 파일은 `config.txt` 한 개입니다. 기준 checkout에는 `mode=base`, A에는 `mode=agent-a`, B에는 `mode=agent-b`를 기록했습니다. 성공 기준은 기준 checkout이 깨끗한 상태를 유지하면서 두 worktree가 서로 다른 내용과 각자의 수정 상태를 보이는지였습니다.

| 작업 위치 | 파일 내용 | `git status --short` |
|---|---|---|
| 기준 checkout | `mode=base` | clean |
| `agent-a` worktree | `mode=agent-a` | `M config.txt` |
| `agent-b` worktree | `mode=agent-b` | `M config.txt` |

**작업 중 격리는 예상대로 성공했습니다.** A와 B가 같은 경로의 파일을 다르게 수정했지만 서로의 파일을 덮어쓰지 않았고, 기준 checkout도 변하지 않았습니다. 실험 스크립트와 전체 출력은 글 번들의 `artifacts/`에 보존했습니다.

이어서 두 변경을 각각 commit하고 A를 먼저 기준 브랜치에 merge한 뒤 B를 merge했습니다. 두 브랜치가 같은 줄을 서로 다르게 바꿨기 때문에 두 번째 merge는 exit code 1과 `CONFLICT (content)`를 반환했고, 파일에는 conflict marker 3개가 생겼습니다.

이 반례가 중요합니다. **worktree는 에이전트가 일하는 동안 파일 상태를 격리하지만, 서로 충돌하는 두 설계를 자동으로 화해시키지는 않습니다.** Orca의 diff 비교와 채택 판단이 부가 기능이 아니라 병렬 작업의 마지막 필수 단계인 이유입니다.

### 5. 잘 맞는 작업과 맞지 않는 작업

Orca는 모든 코딩 작업을 무조건 병렬화하는 도구가 아닙니다. 작업 사이의 의존성이 약하고, 결과를 같은 기준으로 채점할 수 있을 때 효과가 큽니다.

| 작업 상황 | 추천 | 이유 |
|---|---|---|
| 같은 버그에 해결법 두 가지 시도 | 적합 | 같은 테스트로 diff와 결과 비교 가능 |
| UI 시안 두 가지 구현 | 적합 | 화면·접근성·테스트 기준으로 하나를 선택 |
| 기능 구현과 독립 테스트 작성 | 조건부 적합 | 인터페이스를 먼저 고정해야 함 |
| 백엔드 변경 뒤 프런트엔드 연결 | 순차 작업 우선 | 앞 단계 API가 바뀌면 뒤 작업이 재작업 |
| 여러 agent가 같은 lockfile·설정 줄 수정 | 분할 재설계 | 병합 충돌 가능성이 큼 |
| Git을 쓰지 않는 작은 일회성 작업 | 기존 CLI 우선 | worktree·검토 비용이 이점보다 큼 |

가장 좋은 첫 과제는 “서로 다른 방법으로 같은 실패 테스트를 고치고, 통과한 결과 중 작은 diff를 선택하세요”처럼 독립성과 판정 기준이 함께 있는 작업입니다. 반대로 “프로젝트 전체를 알아서 개선하세요”는 각 에이전트가 다른 목표를 만들기 쉬워 비교하기 어렵습니다.

에이전트 수는 두 개로 시작하는 편이 좋습니다. 세 번째 실행부터는 선택지가 하나 늘지만, 토큰·CPU·메모리뿐 아니라 사람이 읽어야 할 diff도 하나 늘어납니다. 병렬화의 상한은 실행 가능한 에이전트 수보다 **검토자가 같은 날 책임 있게 확인할 수 있는 변경 수**로 정하는 편이 안전합니다.

### 6. 설치 전 준비

Orca를 설치하기 전에 Git 저장소와 사용할 CLI 에이전트를 먼저 준비합니다. 예를 들어 Codex를 쓴다면 Codex를 설치한 뒤 일반 터미널에서 한 번 로그인해야 합니다. [Codex 연동 문서](https://www.onorca.dev/docs/agents/codex)에 따르면 Orca는 로컬 `~/.codex`의 계정 정보를 읽고 선택한 worktree를 현재 작업 디렉터리로 삼아 Codex를 실행합니다.

준비 상태는 다음 순서로 확인하면 됩니다.

1. 프로젝트가 Git 저장소이고 기준 브랜치와 remote가 올바른지 확인합니다.
2. 미커밋 변경을 정리하거나 보존해 깨끗한 기준점을 만듭니다.
3. 사용할 Codex·Claude Code·OpenCode 등의 CLI를 각각 설치합니다.
4. 일반 터미널에서 각 CLI를 실행해 로그인과 기본 동작을 확인합니다.
5. 프로젝트의 설치·테스트·lint 명령을 짧은 문서로 정리합니다.

macOS에서는 [공식 설치 문서](https://www.onorca.dev/docs/install)의 Homebrew 명령을 사용할 수 있습니다.

```bash
brew install --cask stablyai/orca/orca
```

macOS, Windows, Linux용 설치 파일을 공식 다운로드 페이지나 GitHub Releases에서 받을 수도 있습니다. 첫 실행에서는 저장소를 추가하기 위한 홈 디렉터리 접근을 요청하고, `~/.claude`, `~/.codex`, Ghostty 터미널 설정을 가져올지 제안합니다. 설치 경로와 메뉴는 업데이트될 수 있으므로 실제 설치 시점의 공식 문서를 함께 확인하는 편이 좋습니다.

### 7. 권한 설정부터 확인할 이유

저장소를 추가하기 전에 `Settings → Agents`의 권한 모드를 확인해야 합니다. [공식 지원 agent 문서](https://www.onorca.dev/docs/agents/supported)에 따르면 Orca는 기본 지원 agent의 새 실행에 권한 우회 또는 full autonomy 인자를 미리 채웁니다. 예를 들어 Codex에는 승인과 sandbox를 우회하는 인자, Claude Code에는 permission prompt를 건너뛰는 인자가 사용될 수 있습니다.

worktree를 보안 샌드박스로 이해하면 안 됩니다. worktree가 분리하는 대상은 checkout된 작업 파일과 브랜치입니다. agent 프로세스가 가진 운영체제 권한, 홈 디렉터리의 자격 증명, 네트워크, 공용 데이터베이스, Docker daemon까지 자동으로 격리하지는 않습니다.

**처음에는 `Settings → Agents → Agent Permissions`를 Manual로 바꾸고 필요한 동작만 허용하는 방식을 권합니다.** 자동 실행이 꼭 필요하다면 테스트용 저장소와 최소 권한 계정, 별도 환경 변수, 삭제 가능한 데이터베이스부터 사용합니다. production 배포, 결제, 이메일 발송, 인프라 삭제처럼 되돌리기 어려운 명령은 worktree 안에 있다는 이유만으로 자동 승인하면 안 됩니다.

개인정보 설정도 분리해서 봐야 합니다. [Orca 텔레메트리 문서](https://www.onorca.dev/docs/telemetry)는 코드·프롬프트·에이전트 출력·터미널 출력·저장소 이름을 제품 텔레메트리로 보내지 않고, 익명 사용 이벤트는 수집할 수 있다고 설명합니다. 앱 설정이나 `DO_NOT_TRACK=1`, `ORCA_TELEMETRY_DISABLED=1`로 이를 끌 수 있습니다. 다만 실제 코드를 처리하는 Codex나 Claude Code의 데이터 정책은 Orca 텔레메트리와 별도로 확인해야 합니다.

### 8. 첫 병렬 세션 사용법

[공식 첫 세션 안내](https://www.onorca.dev/docs/first-session)의 흐름을 실무용으로 다듬으면 다음과 같습니다.

1. 왼쪽 사이드바에서 `Add Repo`를 눌러 로컬 Git 저장소를 추가합니다.
2. 저장소 설정에서 기준 ref가 `origin/main` 같은 올바른 브랜치인지 확인합니다.
3. 저장소 옆 `+`를 눌러 `fix-login-a`라는 worktree를 만듭니다.
4. 시작 ref를 고르고 첫 번째 CLI agent를 선택합니다.
5. 같은 시작 ref에서 `fix-login-b`를 만들고 두 번째 agent를 선택합니다.
6. 두 agent에 같은 목표·제약·성공 조건을 전달합니다.
7. split pane과 상태 표시로 진행을 보되, 중간 구현을 서로 복사하지 않습니다.
8. 각 worktree에서 같은 테스트와 lint를 실행합니다.
9. 기준 ref 대비 diff를 열어 결과를 비교합니다.
10. 채택한 branch만 stage·commit·push하고 review를 만듭니다.
11. 남은 worktree는 필요한 기록을 확인한 뒤 archive하거나 삭제합니다.

두 에이전트에 보낼 프롬프트는 같은 문장을 복사하는 것보다 같은 **평가 계약**을 주는 일이 중요합니다.

```text
목표: 로그인 경합 조건으로 실패하는 테스트를 통과시키세요.
범위: auth/ 디렉터리와 관련 테스트만 수정하세요.
성공 조건: 지정한 테스트, 전체 typecheck, lint가 모두 통과해야 합니다.
금지: 의존성 버전 변경, 테스트 삭제, 외부 서비스 호출은 하지 마세요.
결과: 원인, 변경 파일, 실행한 검증, 남은 위험을 10줄 이내로 보고하세요.
```

완료 보고의 문장보다 직접 실행한 테스트와 diff를 우선합니다. 두 결과가 모두 통과했다면 변경 줄 수가 적다는 이유만으로 선택하지 말고, 원인을 실제로 제거했는지와 예외 처리가 명확한지까지 봅니다. 어느 쪽도 기준을 만족하지 못하면 둘을 억지로 섞기보다 실패 로그를 새 worktree의 입력으로 넘기는 편이 추적하기 쉽습니다.

### 9. 포트·의존성·외부 상태 분리

파일 폴더가 나뉘어도 개발 서버의 기본 포트는 같을 수 있습니다. 두 worktree가 모두 `localhost:3000`을 열려고 하면 한쪽이 실패합니다. worktree별로 `3001`, `3002`처럼 포트를 배정하거나 Orca의 작업별 환경 설정에서 명시해야 합니다.

의존성도 확인해야 합니다. 각 worktree가 자체 `node_modules`나 가상환경을 만들면 디스크 사용량과 설치 시간이 늘고, 전역 캐시를 공유하면 속도는 빨라져도 캐시 오염 가능성이 남습니다. 저장소의 setup hook에 설치 명령을 넣기 전에 lockfile과 캐시 정책을 정해 두는 편이 좋습니다.

데이터베이스와 외부 API는 더 조심해야 합니다. 두 에이전트가 같은 개발 DB의 migration이나 같은 테스트 계정을 동시에 바꾸면 Git diff 밖에서 충돌합니다. **병렬 세션의 진짜 격리 단위는 worktree만이 아니라 포트, 환경 변수, 데이터베이스 schema, 클라우드 자격 증명까지 포함해야 합니다.**

### 10. CLI 자동화는 두 번째 단계

GUI 흐름에 익숙해진 뒤에는 Orca에 포함된 `orca` CLI로 worktree와 터미널을 자동화할 수 있습니다. [Orca CLI 문서](https://www.onorca.dev/docs/cli/overview)에 따르면 `Settings → Experimental → CLI`에서 명령을 등록한 뒤 다음처럼 연결 상태를 확인합니다.

```bash
command -v orca
orca status --json
orca worktree ps --json
orca terminal list --json
```

CLI는 worktree 생성·조회, 터미널 입출력, 파일과 diff 열기, 내장 브라우저 제어까지 다룹니다. 자동화에서는 사람이 읽는 화면 텍스트보다 `--json` 결과와 명시적인 worktree selector를 사용하는 편이 안전합니다.

처음부터 자동 dispatch와 자동 merge까지 연결하지 않는 것이 좋습니다. 먼저 수동으로 두 agent를 운영하면서 어떤 성공 조건과 검토 항목이 실제로 통하는지 기록합니다. 반복 가능한 판단 규칙이 생긴 뒤 worktree 생성과 테스트 실행부터 자동화해야 실패했을 때 어디서 잘못됐는지 찾을 수 있습니다.

### 11. 도입 판단

Orca는 “에이전트를 많이 켜면 개발이 빨라진다”는 약속보다 **병렬 시도를 분리하고 비교 가능한 Git 변경으로 바꾸는 도구**로 볼 때 가치가 분명합니다. 같은 문제에 두 접근을 경쟁시키거나 독립 작업을 나누고, 결과를 테스트와 diff로 고르는 팀에 잘 맞습니다.

반대로 하나의 CLI agent로 충분한 짧은 작업, 앞 단계 결과가 계속 바뀌는 순차 작업, Git을 쓰지 않는 프로젝트에는 운영 비용이 더 클 수 있습니다. diff를 검토할 시간과 책임자가 없다면 병렬 실행은 생산성이 아니라 미검토 변경의 양만 늘립니다.

처음 적용할 때는 작은 실패 테스트 하나를 고르고, 같은 기준 ref에서 worktree 두 개만 만드세요. 권한은 Manual로 두고, 두 agent에 같은 성공 조건을 준 뒤 테스트 결과와 diff를 비교합니다. **그 한 번의 검토가 편해졌다면 세 번째 agent를 고민하고, 불편했다면 병렬 수보다 작업 분해와 판정 기준부터 고치는 것이 Orca를 제대로 쓰는 순서입니다.**
