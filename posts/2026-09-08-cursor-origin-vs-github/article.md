---
title: "Github vs. Cursor Origin, 코드 저장소 비교"
slug: cursor-origin-vs-github
date: 2026-09-08
category: "Log"
subcategory: "개발 · 디지털"
status: ready
format: rich-post-v2
tags: [Cursor Origin, Cursor, GitHub, Git 저장소, AI 코딩 에이전트, 코드 호스팅]
summary: "GitHub와 Cursor Origin이 공유하는 Git 저장소 기능부터 협업·AI 에이전트의 차이까지 비교합니다. GitHub 미러가 동기화하는 데이터와 남겨 두는 데이터를 구분하고 프로젝트별 선택을 제안합니다."
hero_image: assets/cursor-origin-official-og.jpg
published_url: ""
sources:
    - https://cursor.com/ko/origin
    - https://cursor.com/docs/origin
    - https://cursor.com/docs/origin/create-repository
    - https://cursor.com/docs/origin/mirror-github
    - https://cursor.com/docs/origin/integrations
    - https://cursor.com/docs/origin/settings
    - https://cursor.com/docs/api/origin
    - https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
    - https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
    - https://docs.github.com/en/actions/reference
    - https://docs.github.com/en/packages
    - https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
    - https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository
    - https://github.com/features/copilot/agents
    - https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
    - https://www.instagram.com/p/DdAinVJk37q/
---

안녕하세요. dev.log입니다.

Cursor에서 코드를 작성하고 GitHub에 올리는 개발자라면, Cursor가 자체 저장소 서비스까지 만든 이유가 궁금할 만합니다. **Cursor Origin**은 코드와 변경 이력을 보관하고, 수정 내용을 검토해 합치는 코드 호스팅 서비스입니다. GitHub와 기본 역할은 같지만 Cursor의 AI 에이전트와 저장소를 함께 관리하도록 연결한 점이 눈에 띕니다.

이미 GitHub에서 프로젝트를 운영하고 있다면 저장소를 서둘러 옮길 필요는 없습니다. GitHub를 계속 쓰면서 Origin에도 코드와 리뷰를 동기화할 수 있기 때문입니다. 선택을 가르는 것은 코드를 저장할 수 있느냐보다, 프로젝트의 협업과 자동화를 어디에서 운영하느냐입니다.

{{media:cursor-origin-lead}}

### 두 서비스가 공유하는 Git 저장소

[Origin 공식 문서](https://cursor.com/docs/origin)에서 말하는 `git forge`는 Git 저장소에 코드 탐색과 리뷰 같은 협업 기능을 더한 서비스입니다. GitHub도 여기에 해당합니다. Git 명령에서 원격 저장소의 별칭으로 쓰는 `origin`과 Cursor의 제품명 Origin은 구분해야 합니다.

Origin에서도 저장소를 내려받는 `clone`, 변경 내용을 보내는 `push`, 최신 내용을 가져오는 `pull`을 그대로 사용합니다. 수정안을 올려 검토받고 합치는 Pull Request(PR)도 지원합니다. 코드를 보관하고 리뷰하는 기본 작업 때문에 Git 사용법을 새로 배울 필요는 없습니다.

아래는 2026년 9월 8일 공식 문서에 공개된 기능을 같은 항목으로 비교한 표입니다. Origin은 현재 초기 베타입니다.

| 비교 항목 | GitHub | Cursor Origin |
|---|---|---|
| Git 저장소 | Git 명령, 브랜치·태그·변경 이력 | 동일한 기본 Git 작업 지원 |
| 코드 탐색과 리뷰 | 코드 검색, PR 생성·검토·병합 | 코드 검색, PR 생성·검토·병합 |
| 업무와 토론 | Issues·Projects·Discussions | 현재 문서에 대응 기능이 명시되지 않음 |
| 자동화 연결 | GitHub Actions와 외부 앱 | Cursor Automations, Vercel·Depot·Buildkite |
| 저장소 공개 범위 | 공개 또는 비공개 | 팀 내부용 Internal 또는 권한을 지정하는 Private |
| 이용 조건 | Free에서도 공개·비공개 저장소 제공 | Pro·Teams·Enterprise에서 순차 제공, Free 제외 |

Origin의 [저장소 생성 문서](https://cursor.com/docs/origin/create-repository)는 Internal과 Private을 안내합니다. 누구나 코드를 보고 기여하는 공개 오픈소스가 목적이라면, 현재는 공개 저장소를 제공하는 GitHub가 맞습니다.

### GitHub에 함께 쌓이는 협업 기록

프로젝트를 운영하다 보면 코드 외에도 할 일, 버그 신고, 논의와 배포 설정이 쌓입니다. [GitHub의 협업 기능](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)은 이런 정보를 저장소와 연결합니다. Issues에는 버그와 작업을 기록하고, Discussions에서는 질문과 의견을 나누며, Projects에서는 작업과 PR을 표·보드·로드맵으로 관리합니다.

자동화도 저장소 선택에 영향을 줍니다. [GitHub Actions](https://docs.github.com/en/actions/reference)는 코드를 올렸을 때 빌드·테스트·배포를 실행할 수 있습니다. Packages는 배포할 패키지를 보관하고, Pages는 정적 웹사이트를 제공합니다. 코드만 다른 곳에 복사해도 이 설정과 운영 방식까지 옮겨지는 것은 아닙니다.

[GitHub의 보안 도구](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository)는 사용하는 라이브러리의 취약점, 코드의 보안 문제, 실수로 올린 비밀값을 찾는 작업도 맡습니다. Dependabot, code scanning, secret scanning 등이 여기에 해당하며 이용 조건은 플랜과 저장소 공개 범위에 따라 다릅니다. Origin의 현재 공개 문서에서는 Packages·Pages나 이와 같은 보안 제품 구성이 확인되지 않습니다. 이를 Origin에 보안 기능이 전혀 없다는 뜻으로 읽어서는 안 됩니다.

### AI 에이전트를 연결하는 방식

Origin은 Cursor에서 에이전트에게 맡긴 작업을 저장소 생성부터 PR까지 연결합니다. [Origin 통합 문서](https://cursor.com/docs/origin/integrations)에 따르면 클라우드 에이전트가 저장소를 내려받아 코드를 수정하고, 변경 사항을 올려 PR을 만들 수 있습니다. Cursor Automations를 연결하면 일정에 맞추거나 코드가 올라오고 PR이 열리는 시점에 에이전트를 실행할 수도 있습니다.

GitHub에서도 [Copilot 클라우드 에이전트](https://github.com/features/copilot/agents)에 작업을 맡길 수 있습니다. [Claude와 Codex 같은 타사 에이전트](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents)도 Issue와 PR에 연결됩니다. 타사 에이전트 기능은 현재 공개 미리보기이며 유료 Copilot 플랜이 필요합니다. 사람이 Issue로 일을 맡기고, 에이전트가 만든 PR을 검토한 뒤 수정 의견을 전달하는 식입니다.

따라서 AI 에이전트의 유무만으로 두 서비스를 나누기는 어렵습니다. Cursor의 에이전트와 자동화를 주로 쓴다면 Origin의 연결 방식을 살펴볼 만합니다. GitHub에 작업과 리뷰가 모여 있다면 그곳에서 에이전트를 쓰는 방법도 있습니다. Cursor Automations 자체도 연결된 GitHub 저장소를 대상으로 실행할 수 있으므로, 에이전트를 쓰기 위해 반드시 Origin으로 이전해야 하는 것은 아닙니다.

### GitHub 저장소를 연결하는 미러

두 서비스를 함께 쓰는 방법이 **미러링**입니다. GitHub 저장소를 Origin에 복사하고 이후 변경 사항도 동기화하는 기능입니다. [Origin의 미러 문서](https://cursor.com/docs/origin/mirror-github)에 따르면 GitHub가 계속 원본으로 남고, Origin에서 코드를 찾거나 PR을 다룰 수 있습니다.

동기화되는 대상은 코드, Git 이력, 브랜치와 태그입니다. PR은 양방향으로 반영되며 Origin 저장소로 보낸 push도 GitHub에 전달됩니다. 반면 Issues와 GitHub Actions의 워크플로·비밀값은 Origin으로 이전되지 않습니다. 자동 빌드·테스트(CI)도 GitHub에서 계속 실행합니다.

연결하려면 Origin 이용 권한, 저장소 소유 계정이나 조직에 연결된 Cursor GitHub App, 대상 저장소의 GitHub 관리자 권한이 필요합니다. 조건을 갖췄다면 [코드베이스 화면](https://cursor.com/codebase)에서 `Sync from GitHub`를 선택하고 저장소를 지정합니다. 연결 상태는 저장소의 `Settings → General`에서 확인합니다.

같은 설정의 `Detach from GitHub`를 실행하면 동기화가 끝나고 Origin 쪽 저장소가 독립됩니다. 이후 Origin에 보낸 변경 사항은 GitHub로 전달되지 않으며, 기존 GitHub 저장소는 그대로 남습니다. 두 곳을 계속 연결하려는 목적이라면 미러 상태를 유지해야 합니다.

### 프로젝트에 맞는 선택

저장소를 바꿔야 할 이유가 있는지부터 판단하면 선택이 단순해집니다. 다음은 기능 비교를 바탕으로 정리한 도입안이며, 속도나 에이전트 성능의 순위는 아닙니다.

| 프로젝트 상황 | 권장 선택 | 먼저 확인할 점 |
|---|---|---|
| 공개 오픈소스이거나 GitHub의 업무·배포·보안 기능에 의존함 | GitHub 유지 | 필요한 에이전트 기능을 기존 저장소에 연결할 수 있는지 |
| 기존 코드를 Origin에서도 탐색하고 PR을 다루고 싶음 | GitHub 원본 + Origin 미러 | 관리자 권한과 PR 동기화 상태 |
| 새 비공개 프로젝트에서 Cursor 에이전트 중심으로 개발함 | Origin 단독 호스팅 시험 | 필요한 외부 앱과 팀 권한이 지원되는지 |

Origin 단독 호스팅을 시험한다면 베타의 제약도 함께 확인해야 합니다. [외부 앱 설정](https://cursor.com/docs/origin/settings)에 나온 Vercel·Depot·Buildkite 중 Depot과 Buildkite는 Origin이 원본인 저장소에서만 작동합니다. 저장소 주소에서 소유자에 해당하는 코드베이스 이름은 베타 중 변경할 수 없고, [Origin API](https://cursor.com/docs/api/origin) 역시 변경될 수 있습니다. 사내 자동화를 연결할 계획이라면 인증, 웹훅과 브랜치 보호 등 필요한 기능을 먼저 점검해야 합니다.

Origin을 도입할 이유가 생겼다면 중요도가 낮은 저장소 하나로 시작해 보세요. 실제 리뷰 과정에서 동기화가 잘 맞는지, 필요한 자동화가 돌아가는지 확인하면 됩니다. 그 결과가 팀의 작업을 줄여 주는지까지 확인한 뒤 사용 범위를 넓혀도 늦지 않습니다.
