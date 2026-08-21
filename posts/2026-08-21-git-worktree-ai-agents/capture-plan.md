# 캡처 계획: Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법

## 독자 과업

- 주요 독자와 이 독자가 모른다고 가정할 내용: Git branch와 commit은 쓰지만 linked worktree의 분리 범위를 모르는 AI 코딩 도구 사용자
- 낯선 주제를 설명할 익숙한 기준: 한 책상을 두 사람이 같이 쓰지 않고, 각자 같은 설계도의 복사본을 펼친 독립 책상을 쓰는 방식
- 글을 읽은 뒤 완료할 작업: main을 깨끗하게 확인하고 에이전트별 worktree를 만든 뒤 각 폴더에서 작업·commit·merge·정리
- 시작 상태와 전제 조건: Git이 설치된 로컬 저장소, 기준 branch, 터미널 2개, 설치·로그인된 에이전트 CLI
- 비개발자가 시작할 가장 쉬운 경로: 해당 없음. Git CLI를 쓰는 개발자용 글이며 명령마다 의미와 결과를 먼저 설명함
- 개발자·API·자체 배포로 확장할 경로: shell alias나 Orca 같은 관리 도구로 생성·상태 확인을 자동화
- 가장 짧은 성공 경로: `status -> worktree add -b -> list -> 각 폴더에서 agent 실행 -> commit -> main merge -> remove`
- 이 글이 시험하지 않는 범위: agent 모델 성능, 보안 격리, submodule superproject, remote push와 PR 생성

## 비교와 사용법

- 비교 대상과 개수: 같은 폴더 터미널 2개와 linked worktree 2개
- 점수·순위 판정 규칙: 순위 없음. 변경 노출, branch·HEAD 분리, merge 결과를 관찰함
- 벤더 자료와 독립 검증의 경계: Git 명령 의미는 공식 문서, 실제 분리·병합·충돌 결과는 Codex 실행
- 실제 시작 명령: `git status --short --branch`, `git worktree add -b <branch> <path> <start-point>`
- 멤버십·결제·API Key·운영체제 조건: Git은 무료. Claude Code와 Codex의 설치·계정 조건은 각 서비스에 따르며 본문은 Git 절차만 검증함
- 정확한 명령: `git worktree add -b`, `git worktree list`, `git merge --no-ff`, `git worktree remove`, `git worktree prune --dry-run`
- 대표 첫 과제: 한 worktree는 `index.html` 문구, 다른 worktree는 `README.md` 운영 규칙 수정
- 공식 문서 링크: https://git-scm.com/docs/git-worktree
- 가장 흔한 실패와 조건별 복구 방법: branch가 이미 다른 worktree에서 checkout된 오류는 새 branch 이름을 사용. unclean remove 거부는 변경을 확인·commit·stash한 뒤 재시도. 수동 삭제 metadata는 `prune --dry-run`으로 먼저 확인

## 실행 환경

- 실행 주체: Codex
- 확인일: 2026-08-21 KST
- OS·브라우저·기기: macOS 26.5.2, Apple silicon Mac
- 제품·앱 버전: Git 2.53.0, Google Chrome 140 계열, Node.js 24.19.0
- 계정·네트워크 조건: 로컬 임시 저장소, remote와 계정 없음
- 테스트 데이터와 개인정보 준비: 공개용 fixture만 사용. 임시 절대 경로는 캡처에서 `~/worktree-demo`로 치환

## 주장과 화면

| 주장 ID | 독자 행동·관찰 | 필요한 증거 | 자산 ID | 성공 기준 |
|---|---|---|---|---|
| C02 | 시작 branch와 새 folder를 함께 생성 | direct log image | baseline, add-worktrees | branch·path·start point가 보임 |
| C03 | 세 worktree의 path와 branch 확인 | direct log image + infographic | list-worktrees, worktree-map | main과 두 linked worktree가 구분됨 |
| C04 | 각 폴더의 변경이 서로 섞이지 않음 | direct log image | isolated-status | 두 linked status와 clean main이 한 화면에 보임 |
| C05 | 서로 다른 파일 변경의 정상 merge | direct log image | merge-graph | 두 branch commit과 merge graph가 보임 |
| C06 | 같은 줄 변경의 merge conflict | direct log image | conflict-boundary | `CONFLICT`, `UU`, 파일명이 보임 |
| C07 | clean linked worktree 제거 | direct log image | cleanup | main만 남고 dry-run이 clean |
| C01-C03 | 한 repository에서 분리·공유되는 경계 | generated concept + deterministic infographic | git-worktree-hero, worktree-map | hero는 개념만, infographic은 정확한 구조만 설명 |

## 캡처 순서

| 순서 | 시작 상태 | 행동 | 완료 상태 | 자산 역할 | 비고 |
|---|---|---|---|---|---|
| 1 | 깨끗한 main | Git version과 status 확인 | 기준점 확인 | action | 실제 로그 재구성 |
| 2 | main | linked worktree 2개 생성 | branch·folder 2쌍 | action | 실제 로그 재구성 |
| 3 | worktree 3개 | list 실행 | path·branch 지도 | result | 실제 로그 재구성 |
| 4 | 두 linked worktree | 서로 다른 파일 수정 | main clean | result | 실제 로그 재구성 |
| 5 | 두 branch commit | main에서 차례로 merge | 두 변경 합쳐짐 | result | 실제 로그 재구성 |
| 6 | 같은 줄 수정 branch 2개 | 차례로 merge | 두 번째 content conflict | error | 실제 로그 재구성 |
| 7 | abort 후 clean worktree | remove와 prune dry-run | main만 남음 | result | 실제 로그 재구성 |

## 미관 이미지 판단

- 대표 이미지는 실제 UI 증거가 아니라 `하나의 Git 뿌리 -> 분리된 두 작업 경로 -> 검토 후 재결합`을 표현하는 생성형 편집 이미지로 제작함
- 대표 이미지를 명령·성공 결과의 증거로 사용하지 않으며 `origin: generated`, `role: lead`로 기록함
- 단계별 캡처 사이에 장식 이미지를 추가로 끼우지 않음. 구조 이해에는 결정적 조판의 보조 인포그래픽 한 장을 사용함
- 화면 증거와 미관 이미지가 각각 `무엇을 증명하는가`와 `어떤 분위기·개념을 전달하는가`를 캡션에서 구분함

## GIF 판단

- 정지 화면으로 의미가 손실되는가: 아니요. 명령과 완료 상태가 중요하며 시간 흐름은 정적 순서가 더 명확함
- 시작·핵심 동작·완료 상태: 7장의 정적 sequence로 대체
- 실제 GIF 길이(5초 이하): 해당 없음
- 정적 poster 자산 ID: 해당 없음
- poster가 같은 GIF에서 추출됐는가: 해당 없음
- 모바일에서 읽힐 crop: 터미널 이미지는 720×800px 세로형으로 조판해 360 CSS px에서도 가로 스크롤 없이 읽히게 함

## 개인정보와 권한

- 캡처 전에 제거할 값: 실제 사용자 홈 경로, 실제 저장소 이름, 계정·token·remote URL
- 외부 전송·결제·로그인·OTP 여부: 없음
- 공식 자료의 출처·라이선스: Git 공식 문서는 링크와 짧은 해설만 사용
- 사용자가 직접 해야 하는 단계: Tistory 업로드와 최종 게시
