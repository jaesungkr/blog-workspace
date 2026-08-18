# 최종 감사: Xirp, 여러 AI 코딩 에이전트를 한곳에서 관리하는 스포티파이 개발 도구

## 현재 상태

- lifecycle: `ready`
- route: `standard-rich`
- source stage: 작성·v2 문체 밀도 수정·일반 문장 다듬기·독립 source review 통과, source freeze 기록 완료
- media stage: 공식 화면 3장 로컬 검증·Tistory CDN 연결·remote baseline 통과
- final page stage: 1280px·360px light/dark 로컬 preflight와 독립 final-page QA 통과

## 독자 계약과 글의 척추

- 독자가 겪는 장면: 여러 터미널·저장소·브랜치에서 AI 코딩 세션을 동시에 돌리며 작업 상태를 놓침
- 독자가 모르는 것: Xirp의 정체, Portal 의존 여부, worktree와 transcript 공유 범위
- 한 명의 독자: 두 개 이상의 AI 코딩 에이전트나 세션을 관리하는 macOS 개발자
- 기본 권장: 여러 로컬 세션이 문제라면 Xirp 단독으로 시작하고, 조직 문서·소유권·이전 세션 공유가 필요할 때만 Portal을 연결함
- 유용한 결과: 독자는 `기존 터미널 / Xirp 단독 / Xirp+Portal / 도입 보류` 중 자신의 시작점을 고를 수 있음
- 제외한 내용: 직접 사용 후기, 성능·비용·코드 품질 벤치마크, Portal 계약 가격, Windows·Linux 우회 설치
- 글의 척추: 세션이 흩어지는 제약 때문에 최소 도입 범위를 먼저 고르고, 로컬 프로젝트·worktree·상태 표시를 확인한 뒤 조직 맥락이 필요할 때만 Portal로 넓힘

## 최근 글과 제목·소제목 비교

같은 `Log > AI 개념 · 실전`에서 최근 완료 글 5개를 비교했습니다.

| slug | 상태 | 비교 이유 |
|---|---|---|
| `unsloth-desktop-guide` | ready | 낯선 베타 데스크톱 앱을 비전문가에게 설명하는 동일한 글 형태 |
| `grok-bot-guide` | ready | 신제품의 정체·첫 사용·비용 경계를 다루는 가이드 |
| `iphone-claude-instead-of-siri` | ready | 준비 조건과 실패 지점을 앞세운 절차 글 |
| `skillopt-agent-skill-optimizer` | ready | 에이전트 도구의 역할과 적합한 작업을 판정하는 글 |
| `prompt-injection-document-test` | ready | 실험 범위와 보안 경계를 제목·소제목에 명시한 글 |

- 제목 판단: 최근 글의 `키워드 사용법 - 설명` 골격을 반복하지 않고, 제품명 뒤에 정체·해결 대상·만든 주체를 자연스럽게 붙임
- 검색량 근거: 별도 검색량 도구를 쓰지 않은 정성 판단이며 트래픽을 약속하지 않음
- Orca 글과의 중복 점검: `orca-agent-ide-guide`는 worktree 격리의 직접 실험이 중심이고, 이번 글은 Xirp의 로컬·Portal 경계와 베타 도입 판단이 중심임

## 제목과 소제목 strip

| 표면 | 독자 역할 | 검토 결과 |
|---|---|---|
| 제목 | identify | Xirp가 AI 코딩 세션 관리 도구라는 정체를 전제 없이 밝힘 |
| 여러 에이전트의 세션을 한곳에 모으는 앱 | identify | 지원 에이전트·지속 터미널·CLI 설정 소유권을 설명함 |
| 처음에는 Portal 없이 시작하기 | choose | 최소 도입 범위와 4갈래 결정표를 제시함 |
| 프로젝트를 등록하고 첫 세션 열기 | act | 준비 조건, main checkout과 worktree의 차이, 병렬 수정 시 기본 선택, 다섯 단계 실행을 제공함 |
| 병렬 작업은 worktree로 분리하기 | act | 독립 작업 배분, merge 충돌 한계, 권한 경계를 설명함 |
| Grid view에서 기다리는 세션 찾기 | verify | 상태 표시를 읽고 불일치 시 changelog를 확인하게 함 |
| 팀의 조직 지식은 Portal로 연결하기 | decide | Xirp 단독과 Portal 연결의 기능 경계를 비교함 |
| Xirp 설치 전 확인할 베타 제한 | verify | 플랫폼·배포·로컬 코드·transcript·버전 경계를 묶음 |
| Xirp가 잘 맞는 개발자 | decide | 세션 수와 조직 맥락으로 최종 시작점을 정함 |

- 원래 소제목 `macOS 베타에서 확인할 네 가지`는 숫자형 탐색 훅보다 행동이 분명하도록 `Xirp 설치 전 확인할 베타 제한`으로 바꿈
- 문장형 대비 소제목, `A가 아니라 B` 소제목, 범용 `정리·구조·활용` 소제목은 없음

## v2 문체·밀도 수정

### analyzer 전후

| 항목 | 수정 전 | 수정 후 |
|---|---:|---:|
| heading | 8 | 8 |
| generic-heading signal | 0 | 0 |
| 평균 문장 길이 | 39.0자 | 35.7자 |
| 50자 초과 문장 | 23 | 12 |
| 70자 초과 문장 | 4 | 0 |
| 추상명사 밀도 | 5.1/1000 한글 | 3.4/1000 한글 |
| 교정 대비 frame | 3.6/1000 한글 | 1.1/1000 한글 |

숫자는 통과 점수가 아니라 검토 목록으로만 사용했습니다.

### 대표 수정

- `새 AI 모델이 아니라 ... macOS 앱`을 `여러 ... macOS 앱`과 `모델을 새로 제공하지는 않습니다`로 분리해 상투적인 대비 frame을 제거함
- 첫 본문 절에서 제품 정체를 다시 설명하던 문장을 지우고 지원 에이전트와 지속 터미널이라는 새 정보부터 시작함
- `Xirp가 에이전트를 대신 제공하는 것은 아닙니다`를 삭제하고 모델·로그인·권한의 실제 소유자를 직접 밝힘
- 로컬 기능 한 문장에 기능 목록이 몰려 있던 부분을 두 문장으로 나눔
- `기준은 단순합니다`를 삭제하고 독립 작업에 worktree를 하나씩 준다는 행동부터 제시함
- 결론에서 제품 정체를 세 번째로 반복하던 문단을 삭제하고 동시에 관리하는 세션 수라는 최종 판단만 남김
- Codex 대기 상태 오류를 막연히 `여러 차례 수정`이라고 쓰지 않고 v0.14.0·v0.15.0으로 특정함

### 문단별 새 정보와 소유 절

| 소유 절 | 새 정보·행동 | 뒤 절의 반복 처리 |
|---|---|---|
| 도입부 | plain identity와 `단일 세션=기존 터미널`, `복수 세션=Xirp 단독` 기본값 | 결론은 다음 행동 한 문장만 제시 |
| 세션을 한곳에 모으는 앱 | 지원 에이전트·지속 터미널·native CLI 설정·Spotify 36,000회 벤더 집계 | Portal·설치 절에서 다시 설명하지 않음 |
| Portal 없이 시작하기 | 4갈래 도입 결정표 | 결론은 표 전체를 재진술하지 않음 |
| 첫 세션 열기 | 준비 조건, main checkout과 새 worktree의 차이, 병렬 수정 시 기본 선택, 화면에서 고를 값 | media caption은 버튼 순서만 보조 |
| worktree 분리 | 독립 작업별 worktree 배분, 의존 작업의 merge 충돌, 권한 경계 | 첫 세션 절의 checkout 정의와 선택 규칙을 반복하지 않음 |
| Grid view | hooks 상태·알림·상태 오판 changelog | 베타 절에서는 보안 버전만 다룸 |
| Portal 연결 | Workspace·Catalog·MCP, Workspace에서 시작한 Claude Code·Codex 세션의 수동 기록 업로드 | 베타 절은 공유 데이터의 위험만 남김 |
| 베타 제한 | OS·독점 배포·업로드 범위·v0.15.1 | 결론에서 제한 목록을 반복하지 않음 |

## 보존한 사실과 경계

- 지원 에이전트: Claude Code, Codex, Gemini
- 지원 플랫폼: 현재 베타는 macOS 전용
- 현재 확인 버전: 2026-08-18 공식 changelog의 v0.15.1
- 벤더 집계: 36,000회가 넘는 내부 세션, 독립 성능 수치로 해석하지 않음
- Xirp는 각 에이전트의 모델·자격 증명·권한을 번역하거나 대신 소유하지 않음
- 로컬 프로젝트 등록만으로 코드가 Portal에 업로드되지 않음
- 세션 기록 업로드는 Portal Workspace에서 시작한 Claude Code·Codex 세션으로 제한됨
- 업로드 기록에는 대화·도구 호출·파일 변경·경로가 포함될 수 있고 자동 비밀정보 제거가 없음
- 별도 worktree는 작업 중 파일을 분리하지만 merge 충돌·공유 외부 상태·권한을 자동 해결하지 않음
- 직접 앱을 사용하거나 성능을 측정했다는 문장을 쓰지 않음

## 공식 미디어 판단

| ID | 질문 | 로컬 파일 | 검증 |
|---|---|---|---|
| `xirp-home` | 앱의 정체와 첫 입력 지점 | `assets/xirp-home-official-v1.png` | 1800×1153, 원본 화면 확인, 해시 일치 |
| `xirp-new-session` | 목표·에이전트·worktree 선택 위치 | `assets/xirp-new-session-official-v1.png` | 1800×1153, 760px 모바일 스크롤 지정, 해시 일치 |
| `xirp-grid-view` | 여러 세션의 상태 확인 위치 | `assets/xirp-grid-view-official-v1.png` | 1800×1153, 916px 모바일 스크롤 지정, 해시 일치 |

- 원본 CDN 응답은 `artifacts/media-candidates/`에 JPEG로 보존함
- 엄격한 저장소 파서와 호환되도록 크롭·주석 없이 PNG로 무손실 변환함
- 인포그래픽: 없음. Xirp 단독과 Portal의 차이는 3열 표가 더 정확하고 짧음
- 생성 hero: 없음. 공식 홈 화면이 제품 정체를 직접 보여 줌

## 현재 검사와 남은 위험

- `analyze_prose.py`: 수정 전·후 실행 완료. 수정 후 평균 35.7자, 50자 초과 12개, generic heading 0, stock phrase 0, 70자 초과 문장 0
- `check_rich_post_v2.py`: 로컬 source/media 검사 통과, media 3·directive 3
- 독립 source reviewer: 4차 검토에서 알려진 source-level 결함 없음으로 통과, `artifacts/qa-v2/source-pass.json` 기록 완료
- local preflight: 1280×900과 360×780에서 light/dark 확인. H1 1개, figure 3개, 전체 페이지 가로 넘침 없음
- mobile overflow: 760px·916px 화면과 620px 표는 각각 지정된 스크롤 컨테이너 안에서만 가로 스크롤함
- media load: 공식 화면 3장 모두 1800×1153으로 로드되고 깨진 이미지 없음
- remote media: 사용자가 돌려준 세 Tistory CDN URL을 각 stable media ID에 고정하고 baseline GET 통과
- final-page QA: 독립 reviewer `/root/xirp_source_review`가 1280×900·360×800 light/dark를 확인. H1 1개, 목차 target 8개, page overflow 0, remote image 3개 로드
- fragment QA: H1 0, placeholder 0, local path 0
- 최종 상태: paste-ready fragment 생성 완료, lifecycle `ready`; 실제 공개 URL 확인 전까지 `published`로 바꾸지 않음

## 독립 source review 이력

| 회차 | 판정 | 문제 | 반영한 수정 | 재검증 |
|---|---|---|---|---|
| 1 | revision_required | Portal 기록 업로드가 모든 에이전트에 가능한 것처럼 읽힘 | 표와 본문을 `Portal Workspace에서 시작한 Claude Code·Codex 세션`으로 제한하고 evidence C07도 수정 | 2차 독립 검토 대기 |
| 1 | revision_required | 첫 세션 선택 전에 main checkout과 worktree 차이가 설명되지 않음 | 첫 절차 앞에 기존 작업 폴더와 별도 브랜치·작업 폴더의 차이, 병렬 수정 시 기본 선택을 추가 | 2차 독립 검토 대기 |
| 1 | revision_required | MCP와 transcript가 뜻풀이 없이 등장함 | 첫 표에서 MCP 약어를 제거하고 Portal 절에서 연결 규격을 설명, transcript를 `세션 기록`으로 먼저 소개 | 2차 독립 검토 대기 |
| 1 | revision_required | 결론이 도입부와 결정표, Portal 판단을 반복함 | 결론을 로컬 프로젝트 하나와 새 worktree 하나를 여는 다음 행동 한 문장으로 축소 | 2차 독립 검토에서 통과 |
| 2 | revision_required | 첫 세션 앞 worktree 뜻풀이와 병렬 작업 절 첫 문단이 같은 원리·행동을 반복함 | 병렬 작업 절의 반복 문단을 삭제하고 독립 작업·병합 충돌 한계부터 시작 | 3차 독립 검토에서 원문 통과, audit 소유 절 갱신 요구 |
| 2 | revision_required | 감사 기록의 analyzer 수치가 1차 수정 뒤 원문과 맞지 않음 | 현재 최종 원문으로 analyzer를 다시 실행하고 전후 표를 갱신 | 3차 독립 검토에서 통과 |
| 3 | revision_required | audit가 checkout 격리 소유 절을 삭제 전 구조로 기록함 | checkout/worktree 정의와 기본 선택은 첫 세션 절, 배분·merge 충돌·권한은 worktree 절로 갱신 | 4차 독립 검토에서 통과 |
| 4 | pass | 알려진 source-level 결함 없음 | 추가 원고 수정 없음 | 독립 reviewer `/root/xirp_source_review`, source freeze 기록 허용 |
