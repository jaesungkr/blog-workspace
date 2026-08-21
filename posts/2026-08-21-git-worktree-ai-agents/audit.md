# 최종 감사: Git worktree 사용법 - Claude Code·Codex의 작업 폴더를 안전하게 나누는 방법

## 현재 수명주기

- 상태: `reviewing`
- 로컬 원고·미디어·밝은/어두운 테마 미리보기: 완료
- 아직 `ready`가 아닌 이유: Tistory CDN URL 매핑, 원격 바이트 검증, 독립 최종 페이지 검수가 없음
- 권한 경계: 사용자가 Tistory 임시 글 생성·저장을 명시적으로 허용하지 않았으므로 원격 초안이나 미디어 업로드를 만들지 않음

## 구조와 독자

- [x] 제목 앞부분이 검색 의도 `Git worktree 사용법`에서 시작합니다.
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤 독자가 겪는 같은 폴더 변경 혼재 장면을 제시했습니다.
- [x] 첫 5-6문장 안에 `에이전트 하나에 worktree 하나`와 merge 충돌의 한계를 함께 밝혔습니다.
- [x] branch와 worktree의 차이를 첫 명령보다 먼저 설명했습니다.
- [x] `clean main -> add -b -> agent별 검증·commit -> main merge -> remove` 사슬이 보입니다.
- [x] 직접 실험의 작은 fixture와 일반 운영 추천의 범위를 구분했습니다.
- [x] 기본 선택과 예외를 직접 제시했습니다. 파일·검증이 독립적이면 병렬, schema·lockfile·rename은 주의합니다.

## 근거와 독창성

- [x] Git 명령의 의미는 공식 문서, Claude Code의 바로가기는 공식 문서, 분리·병합·충돌 결과는 Codex 실행으로 구분했습니다.
- [x] macOS 26.5.2, Git 2.53.0, 2026-08-21 KST의 테스트 입력·판정·원시 로그를 보존했습니다.
- [x] 서로 다른 파일의 정상 병합과 같은 줄의 content conflict를 같은 fixture에서 재현했습니다.
- [x] Codex가 실행한 작업을 사용자의 개인 경험으로 쓰지 않았습니다.
- [x] worktree가 보안 권한·네트워크·포트·DB를 격리하지 않는 경계를 밝혔습니다.
- [x] 실제 Terminal 앱 캡처가 아니라 원문 로그를 재조판한 화면임을 첫 화면 전에 밝혔습니다.
- 원자료: `artifacts/run/run-worktree-test.sh`, `artifacts/run/worktree-test-2026-08-21.log`, `artifacts/captures/terminal-shots.html`, `artifacts/captures/raw/`

## 제목·문체 폴리싱

- 비교 표본(슬러그·상태): `2026-08-21-github-beyond-git` ready, `2026-08-10-vercel-deployment-guide` ready, `2026-08-10-bluetooth-headset-audio-quality` ready, `2026-08-02-github-stacked-pull-requests` ready, `2026-07-28-wsl-containers-without-docker-desktop` ready
- 같은 하위 카테고리 표본이 부족할 때의 대체 기준: 해당 없음
- 검색 판단: 실제 검색량 자료가 아닌 현재 검색 결과와 기존 인기글을 바탕으로 한 정성 판단. 넓은 검색어를 앞에 두고 Claude Code·Codex라는 사용 장면을 뒤에 둠
- 대표 제목·소제목 변경: `worktree가 실제로 나누는 것`을 `branch만 만들 때와 무엇이 다를까`로, `병합이 끝난 worktree 정리하기`를 `commit과 병합을 확인한 뒤 지우기`로 바꿈
- 대표 문단 연결 수정: 한 문장에 묶였던 정상 병합과 충돌 재현을 두 문장으로 나눔. `.env` 준비와 포트·DB 격리를 별도 문단으로 분리함
- 삭제한 빈 문구 또는 반복: `핵심은 같습니다`, `중요한 점은`, 반복적인 `다만`을 직접 행동 문장으로 교체함
- 보존 확인한 핵심 사실: Git 명령, 테스트 환경·주체·결과, 공식 URL, 실패 조건, 표의 판단값, 미디어 의미
- 남은 문체·근거 위험: 제품 버전별 실행 UI를 설명하는 글이 아니므로 Claude Code와 Codex의 설치·계정 절차는 범위 밖으로 남김
- 폴리싱 전 분석: generic-heading 2, stock phrase 2, 70자 초과 문장 2
- 폴리싱 후 분석: generic-heading 0, stock phrase 0, 70자 초과 문장 1

## 대표 이미지

- [x] 최종 이미지를 전체 크기로 열어 확인했습니다.
- [x] 320px 너비 썸네일과 240px 정사각 crop에서 두 폴더와 분기 그래프가 남는지 확인했습니다.
- [x] Git의 commit graph와 분리된 작업 폴더라는 주제 단서가 제목 없이도 인식됩니다.
- [x] 로고·워터마크·제품 UI 모사·내장 문구가 없습니다.
- [x] 독립 `dev-log-hero-validation` 검수에서 `pass`를 받았습니다.

- 최종 파일: `assets/graphics/git-worktree-hero-v1.png`
- 크기·SHA-256: 1672×941, `b46c46d09978d364e4c1c222ab5d28915fe91c5252e904328fe45b7f40fbe039`
- 권장 위치: opening 결론 바로 뒤
- 한국어 alt: 하나의 Git 저장소에서 두 개의 작업 폴더와 커밋 경로가 갈라졌다가 검토 지점에서 다시 만나는 편집 이미지
- 주제 인식 단서: commit node가 이어진 물리적 branch rail, 서로 다른 두 작업 폴더, 오른쪽 검토·합류 지점
- 최종 생성 프롬프트 기록: 프리미엄 기술 캠페인용 편집 still life. 하나의 어두운 Git 저장소 블록에서 commit-node 경로 두 개가 갈라져 서로 다른 물리적 작업 폴더를 지나 오른쪽 검토 지점에서 다시 만나는 장면. 따뜻한 중성 배경, 정교한 종이·금속 재질, 넓은 여백, 절제된 Git orange accent, cinematic soft light. 텍스트·로고·UI·코드 화면·사람·로봇 금지. 썸네일에서도 두 폴더와 분기 구조가 남도록 구성.
- 독립 검수 메모: full·320 thumbnail 통과. 240 square crop은 양끝 일부를 자르지만 핵심 두 폴더와 branch graph는 유지. 종이의 작은 생성 흔적은 비중요 영역이라 수정 불필요.

## 보조 인포그래픽

- 판단: `1장`
- 판단 이유: 하나의 저장소가 공유하는 값과 세 worktree가 따로 가지는 값을 명령만으로는 빠르게 구분하기 어려움
- [x] 장식이 아니라 `공유 vs 분리`라는 한 관계를 설명합니다.
- [x] branch와 worktree의 차이를 설명한 직후에 배치했습니다.
- [x] C03·C06과 문구를 대조했습니다.
- [x] 전체 1080px와 Chrome 실제 360 CSS px 표시를 확인했습니다.
- [x] 독립 `dev-log-infographic-validation` 검수에서 v3가 `pass`를 받았습니다.

| 최종 파일 | 유형 | 해결하는 독자 질문 | 권장 위치 | 한국어 alt | 문구·수치 근거 |
|---|---|---|---|---|---|
| `assets/graphics/worktree-map-infographic-v5.png` | 원리 | 무엇을 공유하고 무엇을 폴더마다 나누는가 | `branch만 만들 때와 무엇이 다를까` 설명 뒤 | 하나의 Git 저장소와 main·Claude·Codex 세 폴더의 연결 구조도 | C03, C06 |

- 크기·SHA-256: 1080×1080, `1578139934f1ad79e0478513b2ada5979644e73cc23ee11872c5129439c8df61`
- 360px 환산: 제목 20.7px, 주요 라벨 15.3px, 폴더 내부 12.0px, 공유 라벨 12.0px, 충돌 주의문 11.0px
- 실제 360px 증거: `artifacts/infographic/worktree-map-v5-mobile-360.png`, display 360×360, natural 1080×1080, document client/scroll 360/360
- 독립 검수: 한글 깨짐·잘림·텍스트와 선 충돌 없음. 1초 관계 테스트와 framed-poster 테스트 통과

## 단계별 화면

- 최종 후보: v3 화면 5장, `03-list-worktrees-v4.png`, `07-cleanup-v5.png`의 총 7장
- 각 크기: 720×800px, 본문 720 CSS px, 360px 페이지에서 실제 표시 320×355.3px
- 원문성: `worktree-test-2026-08-21.log`에서 선택한 명령과 핵심 출력을 재조판함. 임시 절대 경로, 색상, 제목, 줄바꿈을 공개용으로 편집했고 화면별 처리 내역을 `media.json`에 기록함
- v1 반려 이유: 1200×720 가로형이 360px에서 축소될 때 명령 글자가 작아짐
- v3 선택 이유: 세로형 캔버스와 22–24px 터미널 글자로 바꾸고 commit graph 탭과 글자를 보정함
- 로컬 브라우저 시각 확인: add, merge graph, conflict 화면을 360px figure 단위로 열어 명령·성공·오류 문구와 캡션이 읽힘
- 개인정보: 실제 홈 경로, 계정, remote, token 없음

## 로컬 반응형·테마 검토

- 미리보기: `dist/git-worktree-ai-agents-rich-preview.html`
- 다크 미리보기: `artifacts/qa/dark-preview/git-worktree-ai-agents-rich-preview.html`
- 브라우저: Chrome 151.0.7922.172, 세션 `b7e88519-92fe-419c-913e-fe09caec185a`
- 실측 기록: `artifacts/qa/local-browser-qa.json`
- [x] 1280×900, 390×844, 360×800에서 document client width와 scroll width가 일치합니다.
- [x] 모든 프로필에서 H1이 하나이며 9개 이미지가 positive natural dimensions로 로드됐습니다.
- [x] 360px 밝은·어두운 전체 페이지와 각 figure를 직접 열어 확인했습니다.
- [x] 표 2개는 360px에서 wrapper 320px, scroll width 620px, `overflow-x:auto`로 페이지가 아닌 표 내부에서 스크롤됩니다.
- [x] 코드 블록은 페이지 폭을 늘리지 않고 필요한 블록만 내부 스크롤됩니다.
- [x] 360px의 표 2개와 넘치는 코드 블록을 밝은·어두운 테마에서 `scrollLeft=0`과 최댓값으로 각각 캡처해 양끝 열·명령을 확인했습니다.
- [x] 다크 모드의 본문, 링크, inline code, code block, 표, 캡션, 이미지 surround 대비가 유지됩니다.
- 한계: 이 기록은 로컬 미디어를 사용한 보조 검수입니다. Tistory CDN 원격 자산과 최종 fragment를 묶는 공식 creator QA가 아닙니다.

## 수정 이력

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | 직접 실행 로그 | macOS `/tmp` 실제 경로 때문에 공개 치환이 `/private~/worktree-demo`로 남음 | `pwd -P` 기준으로 치환하고 전체 시나리오 재실행 | 두 번째 로그 PASS, 공개 경로 정상 |
| 2 | 터미널 v1 | 1200×720 이미지를 모바일에서 줄이면 명령이 작음 | 720×800 세로형 v2, graph 22px·짧은 탭의 v3 생성 | 360px figure에서 명령·출력 판독 가능 |
| 3 | 인포그래픽 v1 | 라벨과 connector가 겹침 | 위치를 분리한 v2 생성 | 겹침 제거 |
| 4 | 인포그래픽 v2 | 제목 아래 보조 문장이 도식을 반복 | 보조 문구 삭제, 제목 여백 조정한 v3 생성 | 독립 전체·360px 검수 PASS |
| 5 | 원고 폴리싱 | 범용 소제목 2개, stock phrase 2개, 긴 문장 | 질문형 원리 소제목·행동형 정리 소제목, 문장 분리 | analyzer generic 0, stock 0 |
| 6 | 로컬 브라우저 QA | 첫 측정에서 lazy image가 아래에서 로드되지 않음 | 이미지마다 scroll·load 완료를 기다린 뒤 전체 재캡처 | 여섯 프로필 모두 미로드 이미지 0 |
| 7 | 독립 원고·출처 검수 | Codex 앱 흐름, refs 공유 범위, clean 판정, 실행 주체와 편집 화면 표현이 넓거나 부정확 | 공식 Worktrees 흐름 추가, ref 예외·branch header 조건·Codex 주체·선택 로그 표현으로 한정 | 독립 source-level 재검수 PASS |
| 8 | list·cleanup 화면 | 터미널 안 편집 주석과 번역된 PASS가 실제 출력처럼 보임 | list 주석 삭제 v4, cleanup 영문 원문 복원과 탭 보정 v5 | 360px 밝은·어두운 판독·로그·hash 독립 재검수 PASS |
| 9 | 인포그래픽 v3-v5 | refs 표현이 넓고 v4 공유 라벨이 360px에서 11.3px | 일반 branch·tag ref로 한정하고 v5에서 원본 36px로 복원 | 독립 전체·360px 검수 PASS |

## 검사와 남은 위험

- 검사 명령: `python3 scripts/blog.py check posts/2026-08-21-git-worktree-ai-agents`
- 검사 결과: 대상 글과 저장소 전체 50개 글 모두 오류 0, 경고 0
- rich 검사: `check_rich_post.py` pass, media 9 · directives 9, 9개 자산 모두 `validated`
- 회귀 테스트: `57 passed, 66 subtests passed`
- 스킬 검사: `quick_validate.py .agents/skills/dev-log-rich-post-workspace` -> `Skill is valid!`
- Tistory 미디어: 사용자가 제공한 최종 CDN URL 9개를 media ID별로 연결하고, creator·independent 두 차례의 원격 바이트 검증을 통과함
- creator responsive QA: Chrome 151, 세션 `5f128593-b0f4-4709-976a-ada7898421dc`, 1280×900·390×844·360×800 모두 pass
- independent final-page QA: Chrome 151, 별도 세션 `39bc35e1-cf24-4c0c-ae03-ad316d7306cb`, 9개 figure와 표·코드 좌우 스크롤, 밝은·어두운 테마 모두 pass
- 공개 미디어 문구: alt·caption·최종 fragment에서 `생성 이미지`, `제공 이미지`, `편집 이미지` 같은 제작 방식 라벨을 제거하고 독립 재검수함. 출처·권리·처리 이력은 `media.json`과 내부 audit에만 보존함
- 남은 위험: 실제 Tistory 스킨과 광고 삽입 위치는 사용자의 최종 붙여넣기 미리보기에서만 확인 가능함
- 사람이 티스토리에서 확인할 항목: 실제 스킨의 표·코드 좌우 스크롤, 캡션 간격, 광고가 소제목과 figure를 분리하지 않는지, 최종 게시 전 카테고리·태그
- 최종 종료 판단: 원격 미디어와 독립 final-page 검수를 모두 통과해 `ready`로 승인함. 최종 게시 버튼은 사용자가 누름
