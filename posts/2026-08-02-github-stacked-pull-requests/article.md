---
title: "GitHub Stacked Pull Request 사용법, 큰 변경을 작은 PR로 쌓는 순서"
slug: github-stacked-pull-requests
date: 2026-08-02
category: "Log"
subcategory: "개발 · 디지털"
status: ready
format: rich-post
tags: [GitHub, Stacked Pull Request, 스택 PR, GitHub CLI, 코드 리뷰]
summary: "GitHub Stacked Pull Request의 구조와 public preview 범위, gh stack으로 시작하는 순서, 레이어별 리뷰와 bottom-up 병합 규칙을 공식 화면과 함께 정리합니다."
hero_image: assets/screenshots/github-changelog-hero.jpg
published_url: ""
sources:
  - https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
  - https://docs.github.com/en/pull-requests/get-started/about-stacked-prs
  - https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart
  - https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests
  - https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests
  - https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests
  - https://github.com/github/gh-stack
---

안녕하세요. dev.log입니다.

기능 하나가 커질수록 pull request(PR)도 함께 커집니다. 리뷰를 쉽게 하려고 여러 PR로 나누면 또 다른 일이 생깁니다. 첫 PR이 합쳐질 때까지 기다리거나, 서로 의존하는 브랜치의 base와 rebase를 계속 관리해야 합니다.

GitHub Stacked Pull Request는 이 두 가지 수고를 줄이는 기능입니다. 큰 변경은 의존 순서대로 연결된 작은 PR이 됩니다. 각 PR은 따로 리뷰하고, 스택 전체의 순서와 병합은 GitHub가 함께 관리합니다. [2026년 7월 30일 public preview](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)가 시작됐고 웹·CLI·모바일·API에서 사용할 수 있습니다.

가장 쉬운 출발점은 push 권한이 있는 테스트 저장소에서 두 레이어만 연결해 보는 것입니다. GitHub.com의 `Create stack`이나 공식 `gh stack` Quickstart로 시작할 수 있습니다. public preview가 순차 배포 중이어서 저장소에 UI가 아직 보이지 않을 수 있습니다.

2026년 8월 2일 Codex가 GitHub 공식 변경 로그를 브라우저로 열어 출시 화면, CLI 생성 흐름, stack map, 병합 UI를 캡처했습니다. 사용자의 저장소에서 기능을 켜거나 실제 PR을 만들고 병합하지는 않았습니다. 명령과 동작은 GitHub 공식 문서를 바탕으로 정리한 출처 기반 안내입니다.

{{media:github-changelog-hero}}

### 스택 PR은 브랜치 사다리

Stacked pull request는 같은 저장소 안에서 의존 순서대로 연결한 PR 두 개 이상을 뜻합니다. 맨 아래 PR은 보통 `main`을 향하고, 그 위 PR은 바로 아래 PR의 브랜치를 base로 삼습니다.

```text
frontend      -> PR #3 (base: api-endpoints)  <- top
api-endpoints -> PR #2 (base: auth-layer)
auth-layer    -> PR #1 (base: main)           <- bottom
main
```

인증 구조가 있어야 API를 만들 수 있고, API가 있어야 화면을 붙일 수 있다고 가정해 보겠습니다. 이 변경은 `auth -> api -> frontend` 순서로 쌓습니다. PR #3에는 전체 기능이 아니라 `frontend`와 `api-endpoints` 사이에서 추가된 내용만 나타납니다. 리뷰 범위는 작아지고, 의존 순서는 그대로 남습니다.

기존 방식과 비교하면 GitHub가 새로 맡는 역할이 더 분명해집니다.

| 방식 | 리뷰 단위 | 의존 관계와 rebase | 어울리는 상황 |
|---|---|---|---|
| 하나의 큰 PR | 전체 변경 하나 | 단순하지만 PR이 커집니다. | 변경이 작고 한 번에 이해할 수 있을 때 |
| 수동 종속 PR | 작은 PR 여러 개 | base 변경과 연쇄 rebase를 직접 관리합니다. | 기존 도구나 별도 규칙이 이미 있을 때 |
| GitHub Stacked PR | 레이어별 작은 PR | stack map, 아래 변경을 위 브랜치에 차례로 다시 얹는 연쇄 rebase, 일부·전체 병합을 GitHub와 `gh stack`이 지원합니다. | 앞 변경에 의존하면서도 다음 작업을 계속해야 할 때 |

PR 개수가 많다고 좋은 스택이 되는 것은 아닙니다. 한 레이어가 독립적으로 리뷰할 만한 작업인지, 위 레이어가 아래 레이어에 실제로 의존하는지를 먼저 봐야 합니다. 서로 독립적인 변경이라면 각각 `main`을 향하는 일반 PR이 더 단순합니다.

### 웹과 CLI 두 출발점

웹에서는 첫 PR을 평소처럼 만든 뒤, 두 번째 PR의 base를 첫 PR의 브랜치로 정하고 `Create stack`을 선택할 수 있습니다. 이미 base 관계가 맞는 열린 PR들이 있다면 GitHub가 스택으로 연결하라는 배너를 보여 줄 수도 있습니다. 화면에서 만드는 정확한 순서는 GitHub의 [웹 생성 문서](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)에서 확인할 수 있습니다.

반복해서 스택을 만들고 로컬 브랜치를 오갈 때는 공식 `gh stack` 확장이 더 짧습니다. GitHub의 [Quickstart](https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart)에 적힌 시작 조건은 다음과 같습니다.

- GitHub CLI `2.90.0` 이상
- Git `2.20` 이상
- `gh auth login`으로 인증된 상태
- 브랜치를 push할 수 있는 같은 GitHub 저장소

확장은 공개 [github/gh-stack 저장소](https://github.com/github/gh-stack)의 명령으로 설치합니다.

```bash
gh extension install github/gh-stack
```

두 레이어짜리 스택을 만드는 최소 흐름은 아래와 같습니다.

```bash
gh stack init auth-layer

git add .
git commit -m "Add authentication layer"

gh stack add api-endpoints

git add .
git commit -m "Add API endpoints"

gh stack submit

gh stack view
```

`gh stack submit`은 각 브랜치를 원격에 push하고, 올바른 base를 가진 PR을 만든 뒤 GitHub의 stack으로 연결합니다. 브랜치만 먼저 올리고 싶다면 `gh stack push`를 따로 쓸 수 있습니다.

{{media:github-stack-workflow}}

이 단계는 push와 PR 생성을 포함하므로 처음에는 업무 저장소보다 테스트 저장소가 안전합니다. 기존 브랜치를 가져오거나 중간 레이어를 재배치하는 명령은 나중에도 배울 수 있습니다. 첫 시도에서는 `init -> add -> submit -> view`만 확인해도 스택의 흐름이 보입니다.

### 레이어별 diff와 stack map

일반적인 종속 PR도 base를 아래 브랜치로 잡으면 현재 레이어의 diff만 볼 수 있습니다. GitHub Stacked PR은 여기에 한 가지를 더합니다. 여러 PR을 하나의 stack 객체로 묶고, 연결 순서를 UI와 병합 규칙에 드러냅니다.

PR 상단에는 현재 레이어 번호가 표시되고, merge box의 stack map에는 모든 PR과 상태가 나옵니다. 리뷰어는 자신이 보는 변경이 인증, API, 화면 가운데 어느 단계인지 확인한 뒤 해당 레이어만 검토할 수 있습니다. 서로 다른 리뷰어가 여러 레이어를 병렬로 보는 것도 가능합니다.

{{media:github-review-map}}

`main`의 보호 규칙도 그대로 남습니다. GitHub [공식 개요](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)는 bottom PR의 base branch를 기준으로 삼습니다. 여기에 설정된 branch protection이 stack의 각 PR에 적용됩니다. CODEOWNERS 승인과 required check도 모든 레이어가 충족해야 합니다.

### 병합은 bottom-up

Stacked PR은 [전체, 일부, 개별 병합](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests)을 지원합니다. 순서는 bottom-up입니다. 아래 레이어가 위 레이어의 전제이기 때문입니다.

- top PR을 병합하면 준비된 아래 PR까지 함께 병합합니다.
- 중간 PR을 병합하면 그 아래 레이어도 함께 들어갑니다.
- 중간보다 위에 남은 PR은 열린 상태를 유지합니다. base가 자동으로 바뀌고(retarget), 새 base에 맞춰 rebase됩니다.
- bottom PR 하나만 먼저 병합한 뒤 나머지 stack을 계속 진행할 수도 있습니다.

{{media:github-merge-stack}}

공식 데모의 `Merge stack 3`는 세 레이어가 모두 준비된 상태입니다. 버튼은 top PR에 있지만 커밋 기록은 아래 PR부터 하나씩 병합한 것과 같은 순서를 지킵니다.

rebase에는 한 가지 주의가 있습니다. GitHub 웹에서 실행하는 server-side cascading rebase는 새 커밋에 서명하지 않습니다. signed commit을 요구한다면 [관리 문서](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests)의 안내처럼 로컬에서 `gh stack rebase`를 실행해야 합니다. 이어서 `gh stack push`로 올리면 기존 Git 서명 설정을 따를 수 있습니다.

### 지원 범위에서 걸리는 조건

현재 공개 미리보기는 모든 GitHub 워크플로를 지원하지 않습니다. [공식 지원 범위](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)를 실제 선택 기준으로 바꾸면 다음과 같습니다.

| 상황 | 판단 | 이유 |
|---|---|---|
| 큰 기능을 의존 단계로 나눌 수 있음 | 잘 맞습니다. | 아래 작업을 기다리지 않고 다음 레이어를 진행할 수 있습니다. |
| AI agent가 연속된 작업을 많이 만듦 | 검토할 가치가 큽니다. | 작업 하나를 PR 레이어 하나로 대응시키기 쉽습니다. |
| 변경들이 서로 독립적임 | 일반 PR이 낫습니다. | 스택 의존성을 만들 이유가 없습니다. |
| 외부 fork에서 연속 PR을 보냄 | 현재는 맞지 않습니다. | 모든 branch가 같은 저장소에 있어야 하며 cross-fork stack은 지원하지 않습니다. |
| GitHub Desktop만 사용함 | 바로 시작하기 어렵습니다. | GitHub Desktop은 현재 Stacked PR을 지원하지 않습니다. 웹이나 CLI가 필요합니다. |
| signed commit이 필수임 | CLI rebase를 권합니다. | 웹의 server-side rebase 커밋은 서명되지 않습니다. |
| merge queue가 필수임 | 저장소에서 먼저 확인해야 합니다. | 7월 30일 발표 기준 지원이 수 주에 걸쳐 순차 배포 중입니다. |

특히 마지막 항목은 문서만 보고 활성화됐다고 단정하면 안 됩니다. 기능 자체도 public preview라 바뀔 수 있고, merge queue 통합은 별도 rollout 상태를 가집니다. 버튼이 보이지 않는다면 로그아웃이나 재설치부터 하기보다 해당 저장소의 preview 노출과 조직 정책을 먼저 확인해야 합니다.

### 테스트 저장소에서 시작할 순서

처음부터 실제 기능 브랜치를 여러 개 옮기기보다 다음 순서가 안전합니다.

1. push 권한이 있는 테스트 저장소에서 GitHub CLI와 Git 버전을 확인합니다.
2. `github/gh-stack` 확장을 설치하고 두 레이어만 만듭니다.
3. `gh stack view`와 GitHub의 stack map에서 base 순서가 같은지 확인합니다.
4. 각 PR의 diff가 해당 레이어만 포함하는지 살펴봅니다.
5. branch protection과 required check가 모든 레이어에서 동작하는지 확인합니다.
6. merge queue와 signed commit을 쓴다면 실제 업무 도입 전에 별도 검증합니다.

첫 스택을 만들고 나면 이 기능의 쓰임이 분명해집니다. 거대한 PR을 무조건 잘게 자르는 도구가 아니라, **의존하는 변경을 작은 리뷰 단위로 유지하면서 그 연결까지 GitHub 안에서 관리하는 도구**입니다.

공식 문서의 빠른 시작은 [Quickstart for stacked pull requests](https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart)에서 확인할 수 있습니다. public preview의 배포 상태와 변경점은 [GitHub Changelog](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)를 함께 확인하는 편이 좋습니다.
