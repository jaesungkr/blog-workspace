# 기획: Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법

## 분류와 독자

- 상위 카테고리: `Log`
- 하위 카테고리: `개발 · 디지털`
- 한 명의 독자: Git의 `branch`, `commit`, `merge`는 써 봤지만 Claude Code와 Codex를 같은 저장소에서 동시에 실행하면 변경이 섞일까 걱정되는 개발자
- 검색 의도: `git worktree 사용법`, `git worktree add`, `Claude Code Codex 동시 사용`, `AI 코딩 에이전트 충돌 방지`를 검색해 폴더를 분리하고 결과를 안전하게 합치는 전체 순서를 알고 싶음
- 독자가 이미 아는 것: 터미널에서 Git 저장소로 이동하고 `git status`와 `git commit`을 실행하는 수준. linked worktree, per-worktree HEAD와 index는 모를 수 있음

## 글의 중심

- 독자가 기억할 한 문장: AI 에이전트 하나에 worktree 하나를 배정하면 작업 중 파일 덮어쓰기는 막을 수 있지만, 같은 줄을 바꾼 브랜치의 merge 충돌까지 사라지지는 않습니다.
- 낯선 주제를 붙잡아 줄 익숙한 장면: Claude Code가 기능을 만들고 있는 폴더에서 Codex에게 문서 수정을 맡겼다가 `git status`에 두 작업의 변경이 한꺼번에 나타나는 상황
- 가장 쉬운 시작: 깨끗한 `main`에서 에이전트별 새 브랜치와 인접 폴더를 `git worktree add -b` 한 번으로 함께 만듦
- 이 글이 답하지 않는 범위: Claude Code와 Codex의 코딩 성능 비교, Orca·Xirp 같은 관리 앱의 전체 기능, submodule이 포함된 superproject의 다중 checkout, 운영체제 권한이나 네트워크 격리
- 가장 정직한 한계 또는 반론: worktree는 파일 폴더와 per-worktree Git 상태를 분리할 뿐 보안 샌드박스가 아니며, 공유 포트·데이터베이스·환경 변수·같은 줄의 merge 충돌은 별도로 관리해야 함

## dev.log만의 근거

- first-party contribution: Codex가 macOS 26.5.2와 Git 2.53.0에서 임시 저장소를 만들고 `main + linked worktree 2개`의 분리 수정, 정상 병합, 같은 줄 수정의 충돌, 안전한 제거까지 재현함
- 실제 실행 주체: `Codex`
- 보존할 원자료: 재현 스크립트, 초기 fixture, 네 개의 patch, 전체 stdout 로그, 이를 읽기 좋게 재구성한 단계별 터미널 캡처 7장
- 기존 글 또는 시리즈 연결: 인기글 `Orca 사용법 - 여러 CLI 에이전트를 워크트리로 병렬 실행하는 방법`의 기초 Git 계층을 독립 실행 가능한 글로 확장함
- 다른 블로그 이름으로 바꿔도 성립하는 부분: 일반 명령 설명만으로는 성립하므로 성공 사례와 같은 줄 충돌 반례를 같은 fixture에서 재현하고 정확한 원자료를 함께 보존함

## 설명 순서

| 순서 | 독자가 먼저 알아야 할 것 | 다음 내용과의 연결 |
|---|---|---|
| 1 | 같은 폴더의 두 터미널은 같은 미완성 파일을 본다 | 에이전트마다 물리적인 작업 폴더를 나눌 이유 |
| 2 | worktree는 한 저장소에서 여러 브랜치를 서로 다른 폴더에 동시에 checkout한다 | `add -b`, `list`, 각 폴더에서 에이전트 실행 |
| 3 | 서로 다른 파일의 변경은 독립적으로 commit한 뒤 merge할 수 있다 | 직접 실험의 정상 병합 결과 |
| 4 | 같은 줄 수정은 마지막 merge에서 충돌한다 | 작업 분할 기준과 실패 복구 |
| 5 | 깨끗한 linked worktree만 제거하고 branch 삭제는 별도로 판단한다 | 안전한 정리와 운영 체크리스트 |

## 중앙 방법의 판단 사슬

`깨끗한 기준 브랜치 -> 작업별 브랜치와 폴더 생성 -> 각 에이전트를 해당 폴더에서 실행 -> worktree별 status·test·commit -> main에서 하나씩 merge·검증 -> linked worktree 제거`

## 독자 질문 지도

| 질문 | 본문 답 |
|---|---|
| worktree는 branch와 무엇이 다른가 | branch는 commit을 가리키고 worktree는 그 branch의 실제 파일 폴더와 개별 HEAD·index를 가짐 |
| 폴더를 복사하는 것과 무엇이 다른가 | 하나의 repository metadata와 object database를 공유하며 Git이 linked worktree 관계를 추적함 |
| Claude Code와 Codex는 어디에서 실행하나 | 각 linked worktree로 이동한 별도 터미널에서 실행함 |
| worktree가 merge 충돌도 없애나 | 작업 중 파일 노출은 분리하지만 같은 줄 변경의 merge 충돌은 남음 |
| 언제 지우나 | 변경을 commit하고 병합·보존 여부를 확인한 뒤 `git worktree remove` 사용 |
| 폴더를 Finder에서 그냥 지워도 되나 | 권장하지 않으며 이미 지웠다면 `git worktree prune --dry-run`으로 먼저 확인 |

## 이미지 설계

- 증거 이미지: 직접 실행 로그 기반 터미널 캡처 7장. 시작점, 생성, 목록, 분리된 변경, 병합 그래프, 같은 줄 충돌, 정리를 각각 증명함
- 아이코닉 이미지: Git의 하나의 뿌리에서 두 작업 경로가 분리되고 검토 지점에서 다시 만나는 장면을 물리적 메타포로 표현한 생성형 hero 1장
- 보조 인포그래픽 결정: `1장`
- 한눈에 보여 줄 관계: 하나의 Git 저장소가 object database와 일반 branch·tag ref를 공유하면서 main·Claude·Codex 세 폴더에 서로 다른 HEAD·index·작업 파일을 둠
- 글이나 표만으로 충분하지 않은 이유: `공유되는 것`과 `폴더별로 분리되는 것`의 경계를 명령만으로 이해하기 어려움
- 유형: `원리`
- 핵심 설명 뒤 권장 위치: `worktree가 실제로 나누는 것` 절 뒤

## 제목 후보

1. Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법
2. Git worktree 사용법 - AI 코딩 에이전트마다 독립 폴더 만드는 순서
3. Claude Code·Codex 동시 사용, Git worktree로 변경 섞임 막기

- 선택 제목: `Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법`
- 선택 이유: 검색어를 맨 앞에 두고, worktree가 실제로 해결하는 범위를 `작업 폴더 분리`로 정확히 제한함
