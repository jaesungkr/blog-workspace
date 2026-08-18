# 근거 지도: Xirp, 스포티파이가 만든 AI 코딩 세션 관리 앱

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Xirp는 여러 프로젝트에서 Claude Code·Codex·Gemini의 지속 터미널 세션을 실행·관리하는 macOS 앱 | 공식 | 확인 | [Xirp overview](https://backstage.spotify.com/docs/xirp), [FAQ 1.1-1.3](https://backstage.spotify.com/docs/xirp/faq) | 베타의 지원 범위이며 화면과 기능이 바뀔 수 있음 |
| C02 | Portal 없이도 로컬 프로젝트, 지속 세션, worktree, 파일, skills, rules, grid view를 쓸 수 있고 모델·자격 증명·권한은 각 에이전트 설정이 소유함 | 공식 | 확인 | [Xirp overview](https://backstage.spotify.com/docs/xirp), [Getting started](https://backstage.spotify.com/docs/xirp/getting-started), [FAQ 1.4](https://backstage.spotify.com/docs/xirp/faq) | 에이전트 CLI 설치와 로그인은 별도로 필요 |
| C03 | Xirp 프로젝트는 Mac의 폴더이며, 단일 Git 저장소를 등록해야 완전한 Git·worktree 기능을 쓸 수 있음 | 공식 | 확인 | [Projects](https://backstage.spotify.com/docs/xirp/projects) | 비 Git 폴더나 여러 저장소의 상위 폴더는 기능이 제한됨 |
| C04 | 새 세션에서 목표, 에이전트, main checkout 또는 새 worktree, 전경·배경 실행을 고를 수 있음 | 공식 | 확인 | [Sessions](https://backstage.spotify.com/docs/xirp/sessions), [Getting started](https://backstage.spotify.com/docs/xirp/getting-started) | 에이전트별 세부 옵션 지원 범위는 다를 수 있음 |
| C05 | 같은 저장소에서 병렬로 수정할 때 독립 작업별 새 worktree를 쓰면 branch와 checkout이 분리됨 | 공식+Git 구조 해석 | 확인 | [Sessions - Worktrees](https://backstage.spotify.com/docs/xirp/sessions), [Projects - Git](https://backstage.spotify.com/docs/xirp/projects) | 논리적으로 의존하는 작업은 별도 worktree만으로 충돌 위험이 사라지지 않음 |
| C06 | session hooks는 Working·Idle·Waiting·Finished/failed 상태와 알림을 제공하며 Grid view는 여러 터미널을 한 창에 배치함 | 공식 | 확인 | [Sessions](https://backstage.spotify.com/docs/xirp/sessions), [Getting started](https://backstage.spotify.com/docs/xirp/getting-started) | hooks는 추가 파일·네트워크 권한을 주지 않지만 상태 판별은 베타에서 수정될 수 있음 |
| C07 | Portal을 연결하면 카탈로그·Workspace 문서·소유권·자원·이전 세션을 MCP로 가져올 수 있음. 세션 기록 업로드는 Portal Workspace에서 시작한 Claude Code·Codex 세션에서 수동으로 지원됨 | 공식 | 확인 | [Xirp and Portal](https://backstage.spotify.com/docs/xirp/xirp-and-portal), [Getting started - Portal upload](https://backstage.spotify.com/docs/xirp/getting-started), [FAQ 3](https://backstage.spotify.com/docs/xirp/faq) | 직접 만든 로컬 세션에 자동으로 Workspace 맥락이 생기지 않으며 Gemini 세션 업로드는 현재 문서의 지원 조건에 없음 |
| C08 | 프로젝트 등록만으로 로컬 파일이 Portal에 업로드되지는 않지만 transcript 업로드에는 전체 대화·도구 호출·파일 변경·경로가 포함될 수 있고 자동 비밀정보 제거가 없음 | 공식 | 확인 | [FAQ 2.5, 4.2-4.4](https://backstage.spotify.com/docs/xirp/faq), [Sessions](https://backstage.spotify.com/docs/xirp/sessions) | 실제 조직 정책과 Workspace 권한은 각 Portal 설정에 따름 |
| C09 | 현재 베타는 macOS 전용 비공개 소프트웨어이며 Windows·Linux·서버 배포·SSH 세션 호스팅을 지원하지 않고 가입에는 업무용 이메일이 필요함 | 공식 | 확인 | [FAQ 1.2, 1.5, 1.6, 5](https://backstage.spotify.com/docs/xirp/faq) | 지원 범위는 향후 바뀔 수 있음 |
| C10 | 2026-08-18 공식 변경 기록의 최신 표기는 v0.15.1이며 브라우저 패널 보안 문제가 수정됨 | 공식 | 확인 | [Xirp changelog](https://backstage.spotify.com/docs/xirp/changelog) | 글 작성 시점의 버전이며 이후 릴리스가 나올 수 있음 |
| C11 | Spotify는 내부에서 수천 명의 엔지니어가 3만6천 회가 넘는 세션에 Xirp를 사용했다고 밝힘 | 벤더 주장 | 확인 | [Spotify Portal 공식 발표, 2026-08-10](https://portal.spotify.com/blog/introducing-xirp) | 독립 검증되지 않은 Spotify 자체 집계이며 속도·비용 개선 폭은 공개되지 않음 |
| C12 | 공식 다운로드 페이지는 Apple silicon과 Intel Mac용 다운로드, 터미널 설치 명령을 제공함 | 공식 | 확인 | [Get Xirp](https://xirp.spotify.com/join-beta) | 설치 명령은 인터넷의 원격 스크립트를 셸로 실행하므로 다운로드·약관을 먼저 확인하는 편이 안전함 |
| C13 | Spotify Portal은 Backstage 기반의 기업용 내부 개발자 포털로, 서비스·저장소·소유권·문서·API와 도구를 한곳에서 찾게 함 | 공식 | 확인 | [Portal overview](https://backstage.spotify.com/docs/portal), [Portal features](https://backstage.spotify.com/docs/portal/core-features-and-plugins), [Getting started](https://backstage.spotify.com/docs/portal/getting-started) | 개인 프로젝트 관리 앱이나 Spotify 음악 계정이 아니며 실제 구성과 권한은 조직별로 다름 |
| C14 | Orca는 작업마다 별도 Git worktree·브랜치·파일·에이전트 터미널을 두고 생성부터 변경 검토, commit·push·PR, 정리까지 worktree 중심 흐름으로 묶음 | 공식 | 확인 | [Orca overview](https://www.onorca.dev/docs), [Worktrees](https://www.onorca.dev/docs/model/worktrees), [Diff viewer](https://www.onorca.dev/docs/review/diff-viewer) | Xirp와의 속도·비용·코드 품질을 비교한 벤치마크가 아니라 공개 제품 구조의 비교 |
| C15 | Orca는 로컬 외에도 SSH 대상, 자체 Orca 서버, 사용자 소유 클라우드 VM에서 에이전트와 worktree를 실행할 수 있음 | 공식 | 확인 | [Ways to run Orca](https://www.onorca.dev/docs/ways-to-run), [SSH worktrees](https://www.onorca.dev/docs/ssh) | 원격 머신과 클라우드 계정은 사용자가 소유·관리하며 Orca가 관리형 VPS를 제공하는 것은 아님 |
| C16 | 도입 기본값은 `단일 세션=기존 터미널`, `여러 로컬 세션 상태=Xirp 단독`, `worktree별 구현 비교·PR=Orca`, `조직 맥락=Xirp+Portal` | Codex 판단 | 확인 | C01-C09와 C13-C15를 문제별로 재분류한 dev.log 결정표 | 직접 성능 실험이나 비용 비교가 아닌 공식 기능·제약 기반 판단 |

## 직접 검증 설계

- 질문: Xirp를 처음 보는 개발자가 Xirp·Orca·Portal의 역할을 구분하고 자신의 문제에 맞는 시작점을 고를 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: 공개 웹의 Xirp·Spotify Portal·Orca 공식 사이트와 문서, FAQ, 공개 화면, 2026-08-19 KST
- 입력: 지원 운영체제, 에이전트와 세션, Git worktree의 역할, 변경 검토·PR 흐름, Portal 조직 정보, 원격 실행, 데이터 업로드 제한
- 전처리 또는 표현: 기능을 `로컬 세션 상태`, `worktree별 구현 비교`, `조직 맥락`, `실행 위치` 네 문제로 분류
- 비교·판정 규칙: 독자가 실제로 잃고 있는 것이 세션 위치인지, 코드 결과 비교인지, 조직 정보인지, 원격 실행 환경인지에 따라 가장 작은 도구를 선택
- 성공 기준: 각 추천이 하나 이상의 공식 근거와 하나의 명확한 제한을 가짐
- 반복 횟수와 표본 크기: 공식 문서 8개 표면과 제품 공식 화면 3장 교차 확인
- 보존할 원자료: `evidence.md`, `brief.md`, `media.json`, `artifacts/media-candidates/xirp-*-official-source.jpg`, `assets/xirp-*-official-v1.png`

## 결과

| 판단 ID | 조건 | 권장 시작점 | 근거 | 해석 범위 |
|---|---|---|---|---|
| D01 | Mac에서 한 에이전트·한 세션만 사용 | 기존 터미널 유지 | Xirp의 차별 기능은 지속 다중 세션·상태·worktree·grid 관리 | Xirp가 쓸모없다는 뜻이 아니라 추가 관리층의 이득이 작다는 판단 |
| D02 | Mac에서 여러 에이전트나 세션을 병렬 사용 | Xirp 단독 | Portal 없이 핵심 로컬 기능 사용 가능 | 실제 속도·비용 개선은 검증하지 않음 |
| D03 | 여러 에이전트의 구현을 worktree로 분리하고 변경 검토·PR 제출 | Orca | 작업별 worktree와 내장 검토·commit·push·PR 흐름 | 성능 비교가 아니라 작업 모델 기준 선택 |
| D04 | 팀의 소유권·문서·서비스 맥락·이전 세션 공유 필요 | Xirp+Portal | Workspace·Catalog·MCP 맥락과 세션 기록 공유 | Portal 계약·권한·보안 검토 필요 |
| D05 | 원격 서버·SSH·사용자 소유 클라우드 환경에서 실행 | Orca 또는 기존 원격 도구 | Xirp는 현재 미지원, Orca는 공식 원격 실행 경로 제공 | 원격 인프라와 자격 증명은 사용자가 관리 |

## 실패와 반례

- 단일 저장소와 단일 에이전트만 쓰는 사람에게는 세션 관리 UI가 기존 터미널보다 단순하다고 볼 근거가 없음
- 별도 worktree는 파일 checkout을 분리하지만 서로 의존하는 변경의 merge 충돌이나 설계 충돌까지 해결하지 않음
- Xirp와 Orca는 기능 일부가 겹치지만 `세션 상태 관리`와 `worktree별 구현 비교·PR`이라는 중심 문제가 다르며 우열 순위로 표현할 근거가 없음
- Portal 연결이 곧 모든 로컬 세션의 자동 맥락 주입을 뜻하지 않음. Portal Workspace에서 시작한 적격 세션에 해당함
- transcript는 수동 업로드지만 비밀정보를 자동으로 지우지 않으므로 공유 전 검토가 필요함

## 미해결 항목

- 없음. 가격·성능·직접 체험처럼 확인하지 못한 항목은 공개 본문 범위에서 제외함

## 출처 메모

- Spotify 공식 발표의 `3만6천 회 이상 세션`과 특정 changelog 버전은 확인했지만 현재 독자의 선택을 바꾸지 않아 개정 본문에서는 제외함
- Orca 비교는 두 제품의 공개 구조와 지원 흐름을 대조한 정성 판단이며 속도·비용·코드 품질의 우열을 뜻하지 않음
- 공식 문서는 Xirp가 베타이며 화면과 기능이 빠르게 바뀔 수 있다고 명시함. 절차의 버튼 이름보다 독자가 선택할 값과 제약을 중심으로 씀
- 공식 이미지 3장의 원본 JPEG 응답을 `artifacts/media-candidates/`에 보존함. 저장소 파서와 호환되도록 크롭·주석 없이 PNG로 무손실 변환했으며 게시 파일의 출처, 크기, 해시를 `media.json`에 기록함
