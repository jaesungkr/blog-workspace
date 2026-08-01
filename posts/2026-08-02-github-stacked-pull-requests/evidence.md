# 근거 지도: GitHub Stacked Pull Request 사용법, 큰 변경을 작은 PR로 쌓는 순서

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | GitHub는 2026-07-30 Stacked pull requests를 public preview로 발표했습니다. | 공식 + Codex 관찰 | 확인 | GitHub Changelog, 2026-08-02 브라우저 캡처 | 배포가 수일에 걸쳐 진행되어 저장소별 노출 시점이 다를 수 있습니다. |
| C02 | 스택은 같은 저장소의 PR 두 개 이상이며, 첫 PR은 trunk를, 다음 PR은 바로 아래 PR의 브랜치를 base로 삼습니다. | 공식 | 확인 | GitHub Docs `About stacked pull requests` | cross-fork stack은 지원하지 않습니다. |
| C03 | 각 PR은 해당 레이어의 diff만 보여 주며, stack map에서 전체 순서와 상태를 확인할 수 있습니다. | 공식 + Codex 관찰 | 확인 | GitHub Docs, 변경 로그의 PR stack map 캡처 | 실제 사용자 저장소에서 리뷰를 실행하지는 않았습니다. |
| C04 | CLI 시작 조건은 GitHub CLI 2.90.0 이상, Git 2.20 이상, `gh auth login`, push 가능한 저장소입니다. | 공식 | 확인 | GitHub Docs `Quickstart for stacked pull requests` | 향후 preview에서 버전 조건이 바뀔 수 있습니다. |
| C05 | `gh extension install github/gh-stack`으로 확장을 설치하고 `gh stack init`, `add`, `submit`, `view`로 기본 흐름을 실행할 수 있습니다. | 공식 + Codex 관찰 | 확인 | GitHub Docs quickstart, `github/gh-stack` README, 공식 변경 로그의 CLI 영상 프레임 | 이 글에서는 확장을 설치하거나 원격 PR을 만들지 않았습니다. |
| C06 | 전체·일부·개별 병합이 가능하지만 PR은 bottom-up 순서로 병합됩니다. top PR을 병합하면 아래 PR이 함께 병합됩니다. | 공식 + Codex 관찰 | 확인 | GitHub Docs `About`, `Merging`; 변경 로그 병합 UI 캡처 | 실제 병합 결과를 독립 재현하지 않았습니다. |
| C07 | 아래 레이어를 먼저 병합하면 위 레이어는 열려 있고 자동으로 rebase·retarget됩니다. | 공식 | 확인 | GitHub Changelog, GitHub Docs `About stacked pull requests` | 충돌·저장소 정책에 따른 실패는 별도 확인이 필요합니다. |
| C08 | 기존 branch protection, required check, CODEOWNERS 규칙은 스택 레이어에도 적용됩니다. | 공식 | 확인 | GitHub Changelog, GitHub Docs `About stacked pull requests` | 조직별 실제 규칙 구성을 테스트하지 않았습니다. |
| C09 | GitHub website, CLI, Mobile, API에서 사용할 수 있지만 GitHub Desktop과 cross-fork stack은 지원하지 않습니다. | 공식 | 확인 | GitHub Docs `About stacked pull requests` | public preview 중 지원 표면이 바뀔 수 있습니다. |
| C10 | 서버측 rebase 커밋은 서명되지 않으므로 signed commit이 필요한 저장소는 CLI rebase가 적합합니다. | 공식 | 확인 | GitHub Docs `Managing stacked pull requests` | 로컬 서명 설정이 정상이라는 전제가 필요합니다. |
| C11 | 2026-07-30 발표 시점 merge queue 지원은 수 주에 걸쳐 점진 배포 중이었습니다. | 공식 | 확인 | GitHub Changelog | 2026-08-02 이후 배포 상태는 저장소마다 달라질 수 있습니다. |

## 직접 검증 설계

- 질문: 공식 변경 로그 화면이 출시 사실, CLI 생성 흐름, 레이어별 리뷰, stack 병합을 각각 시각적으로 증명하는가?
- 실행 주체: Codex
- 환경과 확인 시점: Codex 인앱 브라우저, macOS, 2026-08-02, 1280×720 기본 viewport
- 입력: 사용자가 제공한 GitHub Changelog URL
- 전처리 또는 표현: 원본 전체 화면을 보존하고, 본문용 자산은 주변 맥락을 남긴 채 중심 영역만 crop했습니다.
- 비교·판정 규칙: 한 자산이 한 주장 역할을 맡고, 360 CSS px 표시에서도 핵심 UI·문구를 식별할 수 있어야 합니다.
- 성공 기준: 제목·날짜·public preview, CLI 명령 흐름, stack map의 레이어, merge stack 버튼이 각각 확인됩니다.
- 반복 횟수와 표본 크기: 페이지 1개, 최종 캡처 4개
- 보존할 원자료: `artifacts/captures/raw/*.jpg`, `assets/screenshots/*.jpg`, `media.json`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 변경 로그 첫 화면 | 2026-07-30 Release, public preview 제목, stack merge UI를 함께 확인했습니다. | `artifacts/captures/raw/github-changelog-hero.jpg` | 출시 페이지의 표시 상태 |
| E02 | `Create stacks` 구간 영상 프레임 | `gh stack init`, `gh stack add`, `gh stack submit` 안내를 확인했습니다. | `artifacts/captures/raw/github-stack-workflow.jpg` | 공식 데모 프레임이며 직접 CLI 실행 결과가 아닙니다. |
| E03 | `Review each layer independently` 구간 | PR 화면 안에서 frontend, api, auth 레이어가 나열된 stack map을 확인했습니다. | `artifacts/captures/raw/github-review-map.jpg` | 공식 예시 UI이며 사용자 저장소 화면이 아닙니다. |
| E04 | 병합 데모 구간 | `Able to merge as a stack`, 3개 레이어, `Merge stack 3` 버튼을 확인했습니다. | `artifacts/captures/raw/github-merge-stack.jpg` | 공식 데모 프레임이며 실제 병합을 수행하지 않았습니다. |

## 실패와 반례

- 실패한 입력: 첫 스크롤 직후 CLI 데모 영상이 검은 프레임으로 캡처됐습니다.
- 예상과 달랐던 결과: lazy-loaded 영상은 화면에 들어온 직후 유효 프레임이 없었습니다.
- 복구: 영상이 로드되고 명령이 보이는 프레임을 다시 캡처했습니다. 검은 프레임은 게시 자산에서 제외했습니다.
- 일반화하면 안 되는 범위: 캡처는 공식 페이지의 데모를 확인한 것이며, 특정 저장소의 권한·CI·충돌·merge queue 동작을 재현한 테스트가 아닙니다.

## 미해결 항목

- 본문에 남길 미확인 사실은 없습니다.
- Tistory CDN URL은 업로드 권한과 대상 draft가 정해지기 전까지 비워 둡니다.

## 출처 메모

- GitHub Changelog: 출시일, public preview, 생성·리뷰·병합 개요, 순차 배포 범위
- GitHub Docs `About`: stack 정의, 지원 표면, 보호 규칙, bottom-up 병합
- GitHub Docs `Quickstart`: 버전·인증·권한 전제, 설치와 기본 명령
- GitHub Docs `Creating`·`Managing`: 웹 생성, 기존 PR 연결, rebase와 signed commit 주의
- `github/gh-stack`: 현재 공개 확장 설치법과 명령 역할
