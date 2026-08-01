# 캡처 계획: GitHub Stacked Pull Request 사용법, 큰 변경을 작은 PR로 쌓는 순서

## 독자 과업

- 주요 독자와 이 독자가 모른다고 가정할 내용: 종속 PR을 수동으로 유지해 본 개발자이며 GitHub의 새 stack 객체와 병합 규칙은 모른다고 가정합니다.
- 낯선 주제를 설명할 익숙한 기준: 하나의 큰 PR과 base가 연결된 여러 PR
- 글을 읽은 뒤 완료할 작업: 기능이 자신의 저장소에 맞는지 판단하고 테스트 저장소에서 첫 두 레이어 스택을 시작합니다.
- 시작 상태와 전제 조건: Git 2.20+, GitHub CLI 2.90.0+, `gh auth login`, 같은 저장소에 branch push 권한
- 비개발자가 시작할 가장 쉬운 경로: 해당 없음. Git 브랜치와 PR을 다루는 개발자 기능입니다. 웹 UI만으로도 만들 수 있지만 Git 기본 지식은 필요합니다.
- 개발자·API·자체 배포로 확장할 경로: GitHub website, `gh stack`, Mobile, Webhooks, REST API, GraphQL
- 가장 짧은 성공 경로: 확장 설치 -> `gh stack init` -> 첫 커밋 -> `gh stack add` -> 둘째 커밋 -> `gh stack submit` -> GitHub stack map 확인
- 이 글이 시험하지 않는 범위: 사용자 계정의 실제 rollout 상태, 조직 ruleset, CI 비용, conflict, merge queue, 실제 병합

## 비교와 사용법

- 비교 대상과 개수: 거대 단일 PR, 수동 종속 PR, GitHub Stacked PR의 세 가지 흐름
- 점수·순위 판정 규칙: 순위를 매기지 않고 리뷰 단위, 의존성 표시, rebase 부담, 지원 한계를 비교합니다.
- 벤더 자료와 독립 검증의 경계: 기능 동작은 GitHub 공식 문서를 근거로 하며, Codex는 공개 변경 로그의 화면과 문서 일치만 확인했습니다.
- 실제 시작 URL·앱·메뉴·명령: `https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart`, `gh extension install github/gh-stack`
- 멤버십·결제·API Key·운영체제 조건: 별도 결제 조건은 공식 quickstart에 적혀 있지 않습니다. GitHub 인증과 push 가능한 저장소가 필요합니다.
- 정확한 모델명·모델 ID·명령: 모델 해당 없음. `github/gh-stack`, `gh stack init`, `gh stack add`, `gh stack submit`, `gh stack view`
- 대표 첫 과제 또는 프롬프트: auth layer와 api layer로 나뉜 두 브랜치 스택
- 공식 문서 링크: Changelog, About, Quickstart, Creating, Managing, `github/gh-stack`
- 가장 흔한 실패와 조건별 복구 방법: 기능이 보이지 않으면 preview rollout 여부를 확인합니다. cross-fork와 GitHub Desktop은 지원하지 않습니다. server rebase는 unsigned이므로 signed commit 요구 저장소는 CLI rebase를 사용합니다.

## 실행 환경

- 실행 주체: Codex
- 확인일: 2026-08-02
- OS·브라우저·기기: macOS, Codex 인앱 브라우저, 기본 1280×720 viewport
- 제품·앱 버전: GitHub Changelog 공개 웹페이지. GitHub Stacked PR은 public preview 상태
- 계정·네트워크 조건: 로그인이 필요 없는 공개 페이지. GitHub 계정 변경이나 저장소 쓰기는 수행하지 않았습니다.
- 테스트 데이터와 개인정보 준비: 공개 공식 페이지만 사용했습니다. 개인정보·비공개 저장소·토큰은 캡처하지 않았습니다.

## 주장과 화면

| 주장 ID | 독자 행동·관찰 | 필요한 증거 | 자산 ID | 성공 기준 |
|---|---|---|---|---|
| C01 | 출시 상태와 대표 UI 확인 | screenshot | `github-changelog-hero` | 날짜, public preview 제목, stack merge UI가 보입니다. |
| C05 | CLI 생성 흐름 확인 | screenshot | `github-stack-workflow` | `gh stack init`, `add`, `submit` 안내가 보입니다. |
| C03 | 레이어별 리뷰 구조 확인 | screenshot | `github-review-map` | frontend, api, auth 레이어가 stack map에 보입니다. |
| C06 | 여러 레이어 병합 UI 확인 | screenshot | `github-merge-stack` | 세 레이어와 `Merge stack 3`가 보입니다. |

## 캡처 순서

| 순서 | 시작 상태 | 행동 | 완료 상태 | 자산 역할 | 비고 |
|---|---|---|---|---|---|
| 1 | 공식 변경 로그 첫 화면 | 페이지 로드 후 viewport 캡처 | 제목과 대표 merge UI 확보 | lead | 원본 전체 화면 보존, 본문용 crop |
| 2 | `Create stacks` 구간 | 데모 영상이 유효 프레임을 표시할 때 캡처 | CLI 명령이 읽히는 프레임 확보 | action | 검은 초기 프레임 폐기 |
| 3 | `Review each layer independently` 구간 | stack map 이미지가 보이도록 스크롤 후 캡처 | PR 레이어 구조 확보 | concept | 공식 예시 UI |
| 4 | 병합 데모 구간 | `Merge stack 3` 프레임 캡처 | 전체 병합 상태 확보 | result | 공식 예시 UI |

## GIF 판단

- 정지 화면으로 의미가 손실되는가: 아니요. 생성, 리뷰, 병합의 핵심 상태는 정지 화면 네 장으로 설명할 수 있습니다.
- 시작·핵심 동작·완료 상태: 해당 없음
- 실제 GIF 길이(5초 이하): 해당 없음
- 정적 poster 자산 ID: 해당 없음
- poster가 같은 GIF에서 추출됐는가: 해당 없음
- 모바일에서 읽힐 crop: 독립 검토 뒤 CLI 520×340, stack map 440×260, 병합 박스 520×240으로 더 좁게 다시 crop했습니다.

## 개인정보와 권한

- 캡처 전에 제거할 값: 없음. 공개 GitHub 공식 페이지이며 계정 정보가 보이지 않습니다.
- 외부 전송·결제·로그인·OTP 여부: 없음
- 공식 자료의 출처·라이선스: GitHub 공식 Changelog 공개 페이지. 기능 설명을 위한 화면 인용이며 source URL과 캡처 시점을 기록합니다.
- 사용자가 직접 해야 하는 단계: Tistory 미디어 업로드, 최종 HTML 붙여넣기, 미리보기 확인, 공개 발행
