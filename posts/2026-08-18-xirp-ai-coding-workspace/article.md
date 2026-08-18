---
title: "Xirp, 여러 AI 코딩 에이전트를 한곳에서 관리하는 스포티파이 개발 도구"
slug: xirp-ai-coding-workspace
date: 2026-08-18
category: "Log"
subcategory: "AI 개념 · 실전"
status: ready
format: rich-post-v2
tags: [Xirp, AI 코딩 에이전트, Codex, Claude Code, Gemini CLI, Spotify]
summary: "Xirp가 여러 AI 코딩 세션과 Git worktree를 어떻게 한곳에서 관리하는지, Portal 없이 시작하는 방법과 베타에서 확인할 제한을 정리합니다."
hero_image: assets/xirp-home-official-v1.png
published_url: ""
sources:
    - https://xirp.spotify.com/
    - https://xirp.spotify.com/join-beta
    - https://backstage.spotify.com/docs/xirp
    - https://backstage.spotify.com/docs/xirp/getting-started
    - https://backstage.spotify.com/docs/xirp/projects
    - https://backstage.spotify.com/docs/xirp/sessions
    - https://backstage.spotify.com/docs/xirp/xirp-and-portal
    - https://backstage.spotify.com/docs/xirp/faq
    - https://backstage.spotify.com/docs/xirp/changelog
    - https://portal.spotify.com/blog/introducing-xirp
---

안녕하세요. dev.log입니다.

AI 코딩 도구를 하나만 쓸 때는 터미널 하나면 충분합니다. Codex로 구현하고 Claude Code로 검토하며 Gemini CLI를 다른 저장소에서 돌리기 시작하면 이야기가 달라집니다. 어느 세션이 작업 중인지, 어떤 브랜치를 쓰는지, 어디에서 답을 기다리는지 찾는 일이 늘어납니다.

**Xirp는 여러 AI 코딩 에이전트의 세션과 Git 작업 공간을 한곳에서 관리하는 macOS 앱**입니다. 코드를 생성할 모델을 새로 제공하지는 않습니다. Mac에서 두 개 이상의 에이전트나 세션을 병렬로 쓴다면 Portal 연결 없이 로컬 기능부터 시험해 보는 것이 가장 가벼운 시작입니다. 한 에이전트와 한 세션만 쓴다면 기존 터미널을 유지해도 충분합니다.

{{media:xirp-home}}

### 여러 에이전트의 세션을 한곳에 모으는 앱

현재 베타에서 지원하는 에이전트는 Claude Code, Codex, Gemini입니다. [공식 문서](https://backstage.spotify.com/docs/xirp)에 따르면 각 세션은 앱을 닫았다가 다시 열어도 이어지는 지속 터미널로 작동합니다.

모델, 로그인 정보, 추론 설정, 권한과 샌드박스는 각 에이전트의 기존 CLI 설정을 그대로 따릅니다. Xirp 화면에서는 프로젝트, 세션 상태, Git 변경, 파일, `rules`, `skills`를 함께 볼 수 있습니다.

Spotify는 [공식 발표](https://portal.spotify.com/blog/introducing-xirp)에서 내부 엔지니어가 3만6천 회가 넘는 Xirp 세션을 사용했다고 밝혔습니다. 제품이 실제 조직 규모에서 출발했다는 근거는 되지만, 속도나 비용이 얼마나 개선됐는지 독립적으로 검증한 수치는 아닙니다.

### 처음에는 Portal 없이 시작하기

Xirp의 핵심 로컬 기능에는 Spotify Portal이 필요하지 않습니다. 로컬 폴더를 프로젝트로 등록한 뒤 지속 세션과 Git worktree를 만들 수 있습니다. 파일과 `rules`, `skills`, 여러 터미널도 Xirp만으로 볼 수 있습니다.

Portal은 팀의 조직 지식까지 에이전트에 연결할 때 추가하는 선택지입니다. 프로젝트 하나에서 세션 관리가 실제로 편해지는지 확인한 다음 사내 시스템 연동을 검토하세요.

| 지금 필요한 것 | 권장 시작점 | 판단 이유 |
|---|---|---|
| Mac에서 한 에이전트·한 세션만 사용 | 기존 터미널 유지 | 관리 화면을 추가할 이득이 작음 |
| 여러 에이전트나 세션을 병렬 사용 | Xirp 단독 | Portal 없이 지속 세션·worktree·Grid view 사용 가능 |
| 팀의 문서·소유권·이전 세션 공유 | Xirp+Portal | 에이전트가 Workspace와 Software Catalog의 조직 정보를 읽도록 연결 |
| Windows·Linux·서버·SSH 세션 필요 | 도입 보류 | 현재 베타에서 지원하지 않음 |

이 표는 공개 기능과 제한을 바탕으로 만든 도입 결정표입니다. 성능이나 비용을 직접 비교한 순위는 아닙니다.

### 프로젝트를 등록하고 첫 세션 열기

시작 전에 Mac과 지원 에이전트 계정 하나가 필요합니다. [공식 다운로드 페이지](https://xirp.spotify.com/join-beta)에는 Apple silicon과 Intel Mac용 설치 파일이 따로 있습니다. Spotify Technology 계정은 앱 안에서 만들 수 있으며, 개인 Spotify 음악 계정과는 별도입니다. 가입에는 업무용 이메일이 필요합니다.

`main checkout`은 지금 쓰는 작업 폴더를 그대로 사용합니다. 새 worktree는 별도 브랜치와 작업 폴더를 만듭니다. 같은 저장소에서 다른 세션도 파일을 수정한다면 새 worktree를 고르세요.

첫 세션은 다음 순서로 열 수 있습니다.

1. Claude Code, Codex, Gemini 중 사용할 CLI를 설치하고 해당 CLI에서 로그인합니다.
2. Xirp의 `Projects`에서 `Add Project`를 눌러 Mac의 프로젝트 폴더를 등록합니다.
3. 프로젝트 화면에서 `New session`을 열고 결과가 분명한 목표를 적습니다.
4. 사용할 에이전트와 main checkout 또는 새 Git worktree를 고릅니다.
5. `Start`를 누른 뒤 터미널에서 에이전트의 응답과 권한 요청을 확인합니다.

아래 공식 화면에서는 가운데 목표 입력란을 먼저 채우고, 아래쪽 `agent`에서 에이전트를 고릅니다. 왼쪽 아래 worktree 아이콘이 선택됐는지도 확인한 다음 `start`로 넘어가면 됩니다.

{{media:xirp-new-session}}

프로젝트가 Git 저장소가 아니어도 세션과 파일, `rules`, `skills`는 쓸 수 있습니다. 브랜치와 worktree를 포함한 전체 Git 기능을 쓰려면 단일 Git 저장소를 프로젝트로 등록해야 합니다.

### 병렬 작업은 worktree로 분리하기

서로 독립적으로 끝낼 수 있는 작업에는 worktree를 하나씩 줍니다. 같은 파일이나 설계를 함께 바꾸는 작업은 세션을 나눴더라도 마지막에 충돌할 수 있습니다. 이때는 작업 범위부터 쪼개야 합니다.

세션 화면에서는 터미널을 벗어나지 않고 파일과 Git 변경을 확인할 수 있습니다. 에이전트가 끝냈다고 말한 뒤에는 diff를 읽고 테스트 결과를 확인한 다음 커밋하세요. 자동 승인이나 권한 우회 모드는 파일 변경, 셸 명령, 네트워크 호출을 확인 없이 실행할 수 있습니다. 각 에이전트의 샌드박스와 권한 설정은 그대로 유지하는 편이 안전합니다.

### Grid view에서 기다리는 세션 찾기

Session hooks를 켜면 Xirp는 세션을 `Working`, `Idle`, `Waiting`, `Finished or failed` 상태로 구분합니다. Session hooks는 상태 표시와 알림을 위한 연결이며 에이전트의 파일·네트워크 권한은 바꾸지 않습니다.

세션이 여러 개라면 `Cmd+G`로 Grid view를 열고 필요한 터미널을 한 창에 놓을 수 있습니다. 아래 화면의 왼쪽 목록에서 프로젝트별 세션과 `idle` 상태를 확인하고, 주의가 필요한 세션을 선택한 뒤 가운데 터미널에서 이어서 응답합니다.

{{media:xirp-grid-view}}

상태 표시가 실제 터미널과 맞는지도 살펴봐야 합니다. 공식 변경 기록에는 Codex가 작업 중인데 입력 대기로 잘못 표시되던 오류를 v0.14.0과 v0.15.0에서 수정한 내용이 있습니다. 알림이 실제 터미널 상태와 다르면 [최신 변경 기록](https://backstage.spotify.com/docs/xirp/changelog)을 먼저 확인하세요.

### 팀의 조직 지식은 Portal로 연결하기

Portal의 Software Catalog와 Workspace에는 서비스 소유자, 의존 관계, 문서, 기술 결정, 링크, 이전 세션을 모을 수 있습니다. Portal Workspace에서 시작한 적격 세션은 이 조직 맥락을 필요할 때 찾아봅니다. 이때 쓰는 MCP는 에이전트가 외부 도구와 정보를 정해진 방식으로 불러오는 연결 규격입니다.

| 기능 | Xirp 단독 | Xirp+Portal |
|---|---|---|
| 로컬 프로젝트와 지속 터미널 | 가능 | 가능 |
| Git worktree·파일·rules·skills | 가능 | 가능 |
| 카탈로그에서 저장소 찾기 | 불가 | 가능 |
| Workspace 문서·소유권·이전 세션 맥락 | 불가 | 가능 |
| 적격 Workspace 세션 기록 공유 | 불가 | Claude Code·Codex에서 수동 업로드 가능 |

Portal을 연결했다고 모든 로컬 세션에 조직 맥락이 자동으로 들어가지는 않습니다. Workspace나 카탈로그에서 시작한 세션에 관련 맥락이 연결됩니다. 세션 기록(transcript)을 올릴 수 있는 대상은 Portal Workspace에서 시작한 Claude Code·Codex 세션입니다. 사용자가 직접 올려야 팀과 공유됩니다.

### Xirp 설치 전 확인할 베타 제한

Xirp를 설치하기 전에 현재 제한을 확인해야 합니다.

- **운영체제**: 현재 macOS 전용입니다. Windows와 Linux, 서버 배포, SSH 세션 호스팅은 지원하지 않습니다.
- **배포 방식**: 오픈소스가 아닌 Spotify의 독점 소프트웨어이며 베타 중이라 화면과 동작이 빠르게 바뀔 수 있습니다.
- **로컬 코드**: 프로젝트를 등록하거나 Portal을 연결하는 것만으로 로컬 파일이 업로드되지는 않습니다.
- **세션 공유**: 세션 기록을 Portal에 올리면 전체 대화, 도구 호출, 파일 변경, 경로가 포함될 수 있습니다. Xirp가 비밀정보를 자동으로 지우지 않으므로 업로드 전 내용을 직접 검토해야 합니다.

2026년 8월 18일 기준 공식 변경 기록의 최신 표기는 v0.15.1이며, 브라우저 패널의 보안 문제가 수정됐습니다. 설치 후 `Settings` 아래쪽에서 버전과 업데이트 상태를 확인하고, 이전 버전이라면 프로젝트를 열기 전에 업데이트하세요.

### Xirp가 잘 맞는 개발자

Mac에서 세션이 두세 개를 넘기 시작했다면 로컬 프로젝트 하나를 등록하고, 독립 작업 하나를 새 worktree로 열어 보세요.
