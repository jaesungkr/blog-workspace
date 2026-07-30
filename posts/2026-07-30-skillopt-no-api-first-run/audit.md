# 감사: 스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기

## 현재 후보

- lifecycle: `reviewing`
- format: `rich-post`
- primary reader: SkillOpt를 처음 실행하는 `SKILL.md` 사용자
- direct test actor: Codex
- candidate scope: API 키 없는 official mock acceptance test와 실제
  프로젝트로 넘어가기 전 안전 경계

## 사용자 피드백에서 바꾼 중심

| 기존 글의 문제 | 새 구조 | 확인 기준 |
|---|---|---|
| 가상 버그 수정 예시가 첫 행동을 대신함 | 실제 복사 가능한 명령을 첫 절에 배치 | 독자가 설치부터 PASS 확인까지 순서대로 따라갈 수 있음 |
| 논문 성능·토큰·테스트 수치가 주제를 압도함 | 새 글은 직접 실행한 12-task mock 결과만 사용 | 모든 숫자가 독자의 첫 실행을 설명함 |
| 연구 엔진과 Sleep 설명이 길고 진입점이 늦음 | 두 경로를 한 표로 나누고 mock→dry-run→real run 순서를 제시 | 목적별 명령과 준비물이 바로 보임 |
| 가상 6/10→8/10이 실제처럼 먼저 보임 | 0.3333→1.0 원시 실행과 mock 한계를 같은 절에서 설명 | 실제 LLM 개선으로 오독할 수 없음 |
| 설치 명령이 글 후반에 있음 | clone·version pin·venv·install·run을 첫 절에 배치 | prerequisites와 복구 조건이 명령 근처에 있음 |
| 공식 mock의 숫자와 규칙을 설명해도 SkillOpt의 입력과 출력이 보이지 않음 | 숫자와 내부 규칙을 공개 본문·현재 미디어에서 제거하고 회의록 가상 예시로 교체 | `현재 스킬 + 작업 사례 + 성공 기준 -> 후보 -> 별도 검사 -> adopt`를 처음 읽는 독자가 설명할 수 있음 |

## 미디어 기록

- current lead:
  `assets/infographics/skillopt-meeting-notes-flow-v5.png`
- origin: 설명용 simulated diagram. 실제 제품 UI·실행 결과가 아님
- type: input -> candidate -> validation -> adoption process
- reader question: 현재 `SKILL.md` 외에 무엇이 필요하고 실제 파일은 언제
  바뀌는가?
- placement: `회의록 스킬을 고친다고 가정해 보기` 절의 후보 검증 설명 뒤
- dimensions: 1080×1350
- sha256: `63dcdcff3de815800a0ca7725fb9beba9eed99b4f0f035e6cbd2865e1ffc0398`
- editable source:
  `artifacts/infographics/skillopt-meeting-notes-flow-v5.html`
- raw PNG:
  `artifacts/captures/raw/skillopt-meeting-notes-flow-v5.png`
- production: 가상 회의록 입력·후보·검사·반영을 정확한 한국어로
  HTML/CSS 결정 조판. 생성형 이미지와 가상 제품 UI를 사용하지 않음
- alt: 현재 SKILL.md와 반복 작업 사례, 성공 기준으로 회의록 스킬 수정
  후보를 만들고 별도 사례 검사 뒤 adopt하는 흐름
- copy map: 입력과 후보 문구는 C15의 명시된 구조 예시, run/status/adopt
  경계는 C10의 공식 CLI·README에 대응
- 360px equivalent type: headline 20.0px, primary 15.0px,
  support 12.0px, caveat 11.3px
- headline zone: 255/1350 = 18.9%
- type-scale check: 모든 역할과 headline zone PASS
- infographic stage: creator full-raster inspection과 type-scale PASS.
  독립 검수에서 full raster와 정확한 360 CSS px 표시, 글리프·연결선·충돌·
  타입 스케일·하단 고지까지 PASS하여 `validated`
- previous assets: mock 점수 lead와 실제 규칙 infographic은 사용자
  피드백에 따라 현재 `media.json`과 공개 본문에서 제외. 파일은 감사 이력으로
  보존하며 현재 후보로 취급하지 않음
- GIF: `not_applicable`

## 문제 -> 수정 -> 재검증

| 회차 | 발견한 문제 | 수정 | 재검증 |
|---|---|---|---|
| 1 | 최초 1600×900 lead의 터미널 세부 문자와 첫 1200×1200 후보의 하단 지표 라벨이 350 CSS px에서 작음 | 1200×1200 정사각형으로 바꾸고 명령을 한 줄로 줄인 뒤, 지표를 세로 배치하고 라벨을 40px·값을 54px로 확대 | 390px local preview에서 `모델 토큰 0`, `채택 편집 2`, `유해한 규칙 BLOCKED`가 줌 없이 읽힘. 최종 remote 360·390px 재확인 필요 |
| 2 | system Python 3.9 가상환경에서 package 설치가 실패 | Python 3.12 새 가상환경으로 다시 설치하고 본문에 3.10 이상 조건·복구 추가 | 동일 commit의 mock experiment exit 0, PASS |
| 3 | `dry-run`이 비용 없는 모드로 오해될 수 있음 | mock과 real backend를 별도 표로 분리하고 real dry-run의 호출·비용 가능성을 명시 | 공식 README·CLI reference와 대조 |
| 4 | `--project`만 주면 대상 스킬까지 자동 선택하는 것처럼 읽힐 수 있음 | `--target-skill-path`의 별도 책임과 예시 경로 교체 필요를 명시 | 공식 guideline·CLI reference와 대조 |
| 5 | `mock`·backend·acceptance test·fixture·night가 첫 독자에게 설명 없이 이어짐 | 첫 사용 위치에서 시험 모드·실행 방식·인수 테스트·고정 예제·학습 회차로 풀어 씀 | 명령과 수치, 연구 엔진·Sleep의 경계는 그대로 보존 |
| 6 | `먼저 5분 실습`은 설치 네트워크에 따라 지키기 어려운 시간 약속이며, `mock과 실제 실행의 경계`는 범용적인 제목 | `API 키 없이 첫 실행`, `dry-run도 모델 비용이 생기는 조건`으로 바꿈 | 제목과 소제목만 읽어도 실행 -> 점수 해석 -> 경로 선택 -> 실제 연결 -> 비용 경계 -> 과제 선택 순서가 보임 |
| 7 | Python 3.10 조건이 일반적인 오류 안내로만 남아 실제 검증의 실패가 드러나지 않음 | Codex의 Python 3.9 설치 거절과 3.10 이상 재생성 조건을 본문에 연결 | `evidence.md`의 실패 로그와 Python 3.12 성공 결과를 대조 |
| 8 | 설치 예시는 Python 3.12로 고정됐는데 본문은 3.10 이상과 Windows 활성화만 설명해 복사 경로가 맞지 않음 | macOS·Linux와 Windows PowerShell 명령을 분리하고, 3.10·3.11 사용자는 명령의 버전 번호를 바꾸도록 명시 | Python 3.12 명령은 직접 실행 결과와 대조하고 최소 지원 버전은 package metadata와 대조 |
| 9 | 설치 후에도 현재 디렉터리가 SkillOpt clone이라 `--project "$PWD"`가 독자의 프로젝트를 가리키지 않음 | `dry-run` 전에 자신의 프로젝트 루트로 이동하고 `$PWD`를 확인하는 단계를 추가 | 상대 target path와 project scope가 같은 프로젝트 루트를 기준으로 해석됨을 CLI help·guideline과 대조 |
| 10 | 경로 비교 표와 캡션에 loader·adapter·staging·replay·fixture가 첫 설명 없이 등장함 | 문제를 읽는 코드, 실행·채점 연결 코드, 검토함, 과제 재실행 방식, 고정 예제로 바꿈 | 처음 읽는 독자가 표와 캡션만 보고도 준비물을 구분할 수 있는지 문장 검토 |
| 11 | 사용자가 SkillOpt가 원본 스킬을 실제로 바꾸는지, 제안만 하는지 구분하기 어려움 | 도입과 새 절에 `run` 제안 저장 -> `status` 확인 -> `adopt` 실제 반영을 분리하고 공식 mock의 정확한 두 규칙 diff를 추가 | C10·C14, CLI help, mock 재실행 결과와 대조. `--auto-adopt`는 opt-in으로 유지 |
| 12 | 첫 인포그래픽 시안에서 하단 반영 순서와 주의 문구가 캔버스 밖으로 밀리고 겹침 | 패널 너비·세로 간격·하단 copy를 줄이고 v2·v3로 재조판 | 전체 흐름이 1080×1350 안에 들어오지만 v3의 중앙 연결어가 두 줄로 좁게 보임 |
| 13 | v3의 중앙 `검증 통과`가 좁은 연결부에서 두 줄로 갈라져 모바일 판독이 약함 | v4에서 `검증`으로 줄이고 45px primary label로 확대 | 360px equivalent 15.0px, 연결어와 화살표가 양쪽 파일 영역을 침범하지 않음. 독립 시각 검수 필요 |
| 14 | v4가 실제 후보 규칙을 축약하면서 `<answer>...</answer>`의 뒤쪽 태그와 `in the exact form` 문구가 빠짐 | v5에서 공식 mock 로그의 두 후보 문장을 그대로 복원하고 줄바꿈만 조정 | 원시 로그·C14와 대조해 영문 대소문자와 구두점까지 일치. 1080×1350 전체 이미지에서 잘림·겹침이 없고 모바일 환산 글자 크기 기준을 모두 통과. 독립 시각 검수 필요 |
| 15 | 새 설명의 `다만` 도입이 방어적으로 들리고, 점수·연결 절의 제목만으로 범위와 선행 행동이 충분히 드러나지 않음 | 조건을 직접 말하는 도입으로 바꾸고 `12개 고정 예제`, `세션 범위부터 확인`을 제목에 넣음. 공급자 전송 문장은 두 문장으로 나눔 | 명령·수치·URL·실행 주체·제안과 반영 경계를 다시 대조했으며 내용 불변. 문체 분석에서 generic heading 신호가 2개에서 0개로 줄었는지 재확인 |
| 16 | `adopt` 표가 검토함에 반영할 후보가 없는 경우까지 파일이 바뀌는 것처럼 읽힐 수 있음 | `후보가 있으면`, `통과한 후보가 있으면` 조건을 실제 파일 열에 명시 | 고정 commit의 staging·adopt·`auto_adopt=False` 제어 흐름과 다시 대조 |
| 17 | 독립 인포그래픽 검수 환경에 브라우저 런타임이 없고 로컬 `file://` 접근도 정책상 차단됨 | full raster·확대 영역·정확한 문구·타입 스케일을 독립 검수하고 브라우저 게이트를 분리 기록 | raster/source PASS. publish/raw SHA-256 일치, 잘림·겹침·저대비·글리프 오류 없음. untouched 360 CSS px browser gate는 미완료이므로 `validated`로 올리지 않음 |
| 18 | 사용자가 숫자와 내부 규칙을 읽고도 SkillOpt가 무엇을 입력받아 무엇을 바꾸는지 이해하기 어려움 | 공개 본문에서 내부 규칙과 점수 절을 제거하고 회의록 스킬의 현재 문서·반복 사례·성공 기준·수정 후보를 추가 | 본문 검색에서 해당 내부 규칙과 점수 0건. 공식 mock은 설치 PASS 확인으로만 축소 |
| 19 | 새 회의록 infographic v1에서 입력 문서가 서로 가리고 후보 문서가 상단 설명과 겹침 | v2에서 입력 문서를 겹치지 않게 배치하고 후보 높이 고정 | 입력 두 번째 줄과 마지막 후보 규칙이 일부 박스 밖으로 밀려 추가 수정 필요 |
| 20 | v2의 입력·후보 문구가 고정 높이를 넘음 | v3에서 문구를 짧게 줄이고 문서 높이·작업 영역을 확대 | 모든 문구가 1080×1350 안에 들어오며 잘림·겹침 없음 |
| 21 | v3의 하단 연결선이 `run`·`adopt` 글자에 너무 가까움 | v4에서 연결선을 단계 원형 표식의 중심으로 이동 | 선과 글자 사이 clear zone 확보 |
| 22 | v4 support copy의 360px 환산 크기가 기준 아래 | v5에서 headline 60, primary 45, support 36, caveat 34px로 조정하고 문서 높이 확대 | 360px equivalent 20.0·15.0·12.0·11.3px, headline zone 18.9% 모두 PASS. full raster에서 잘림·겹침 없음 |
| 23 | 첫 회의록 제목이 가정 행위만 말하고, 예시 절에서 아직 설명하지 않은 연구 엔진 산출물이 먼저 나옴 | 제목을 `입력과 수정 후보`로 바꾸고 연구 엔진 문장을 뒤의 두 경로 절에만 남김. 가상 예시 고지도 한 문장으로 합침 | 제목만 읽어도 절의 역할이 보이며, 독자는 회의록 흐름을 끝낸 뒤 두 실행 경로를 만남 |
| 24 | 독립 출처 검수에서 `run`·`status`가 후보가 없는 실행까지 후보 파일을 보여 주는 것처럼 읽히고, 폐기한 arXiv·점수 PNG가 공개 `assets/`에 남아 있음을 발견 | `run`은 최신 보고서를 항상 저장하고 통과 후보가 있을 때 후보 파일도 저장한다고 수정. `status`도 최신 보고서와 조건부 후보를 표시한다고 수정. 폐기 PNG 3개는 `artifacts/archive/deprecated-public-assets/`로 이동 | 독립 출처 재검수 PASS. 공개 article·media·assets에서 arXiv·0.3333·1.0000 검색 0건, 공개 assets에는 현재 회의록 PNG 1개만 남음 |
| 25 | 로컬 `file://` 미리보기의 브라우저 캡처가 Browser URL 정책으로 차단됨 | 정책을 우회하지 않고 렌더된 HTML 구조·목차 앵커·반응형 CSS·이미지 경로·크기·해시를 정적으로 검사 | H1 1개, H2·목차 7개와 앵커 전부 일치, 이미지 1080×1350·publish 해시 일치, 금지 문자열과 로컬 절대 경로 0건 |
| 26 | `작업 사례`만으로는 독자가 결과 파일 하나를 넘기면 되는지, 요청·결과·판정 기준까지 필요한지 구분하기 어려움 | 도입에 `현재 스킬 + 사용자가 남긴 과거 작업 기록 + 잘됐는지 판단할 기준 -> 후보 -> 다른 사례 테스트 -> adopt` 문장을 그대로 추가하고, 과거 작업 기록의 범위를 요청·결과·잘된 점과 잘못된 점으로 설명 | 회의록 입력 표와 한 줄 흐름까지 같은 용어로 맞춤. 독립 출처 재검수에서 세션 기록 범위·held-out gate·조건부 staging·status·adopt 설명 모두 PASS |
| 27 | 티스토리 HTML에는 이미지 CDN 주소가 없어 붙여넣기 직전에 자리표시자를 바꿔야 했음 | 사용자가 업로드해 준 `skillopt-meeting-notes-flow` CDN URL을 매니페스트에 연결하고 remote media record를 생성 | CDN GET 200, PNG 1080×1350, remote preview의 이미지 로드와 1280·390·360 문서 폭·목차·H1 구조 PASS. 실제 CDN PNG도 전체 래스터로 재확인 |
| 28 | 티스토리 미리보기에서 교차 회색 섹션이 제목보다 앞쪽부터 넓게 보이며, 빈 회색 박스처럼 읽힘 | 이 글에 `section_backgrounds: plain`을 지정해 섹션의 교차 배경을 끔. 코드 블록·표의 회색 표면은 유지 | 원격 미디어를 넣은 rich fragment를 다시 렌더해 모든 본문 section에 `is-alt` 클래스가 없음을 확인. 사용자가 보낸 티스토리 캡처의 문제 위치와 비교 |

## 현재 검수 결과

- 이전 prose·article pass는 이번 opening 변경으로 historical 상태가 됨
- current article: writing revision·prose polish complete, independent source
  validation PASS
- current infographic: creator full-raster·type-scale PASS, independent
  full-raster·360 CSS px validation PASS
- current bundle check: `blog.py` 오류 0·경고 0, rich-post PASS
- current remote media: creator fetch PASS. CDN 응답은 PNG 1080×1350이며
  `artifacts/qa/remote-media.json`에 기록
- current render: CDN URL이 들어간 preview·Tistory fragment 재생성,
  user-facing `.txt`와 fragment SHA-256 일치. 회차 28 뒤 creator Chrome
  capture도 1280·390·360에서 이미지 로드·문서 폭·목차·H1 구조 PASS
- current article browser QA: creator remote Chrome capture에서 1280·390·360
  모두 이미지 로드·문서 폭·목차·H1 구조 PASS. 전체 페이지의 human
  readability record와 independent QA는 pending

## 제목·소제목·문체 폴리싱

- 비교한 최근 완성 글:
  `prompt-injection-document-test`(ready),
  `orca-agent-ide-guide`(ready),
  `ccshare-manycode-guide`(ready),
  `wsl-containers-without-docker-desktop`(ready),
  `duckdb-guide`(ready)
- 같은 하위 카테고리 표본: 삭제 예정인 기존 SkillOpt 글은 새 후보의 비교
  기준에서 제외했습니다. 같은 `AI 개념 · 실전`의 완성 글이 충분하지 않아,
  실행 명령과 직접 검증을 중심에 둔 `개발 · 디지털` tutorial 네 편으로
  다섯 편을 채웠습니다.
- 제목 판단: 최근 기술 글에 `검색어 - 설명` 골격이 반복됐지만, 이번 제목은
  사용자가 직접 제안한 `스킬 최적화 방법 - SkillOpt`의 방향을 우선했습니다.
  뒤 문구는 넓은 설명 대신 이 글만의 행동인 `API 키 없이 직접 돌려보기`로
  제한했습니다. 검색량 자료를 사용한 판단은 아닙니다.
- private spine: `SKILL.md`와 결과 파일 하나만 넣으면 자동 첨삭될 것으로
  기대한 독자가 회의록 예시에서 현재 스킬·사용자가 남긴 과거 작업 기록·
  성공 기준이 함께 필요하다는 점을 이해하고, 공식 mock은 설치 점검으로만
  사용하기로 했습니다.
- 보호한 불변값: commit `7da46ae`, Python 3.12.13, Python 3.9 설치 실패,
  0 model tokens, harmful edit blocked, 명령·URL·표 값·Codex 실행 주체,
  검증하지 않은 범위를 바꾸지 않았습니다. 공개 본문에서 제거한 mock 내부
  수치는 원시 로그에만 보존합니다.
- 대표 수정: `먼저 5분 실습`의 확인하지 않은 시간 약속을 제거했고,
  `acceptance test`와 `fixture`를 독자가 바로 이해할 한국어로 풀었습니다.
  `run`·`status`·`adopt` 설명은 한 문장에 세 판단을 넣지 않고 검토 순서대로
  나눴습니다.
- 사용자 후속 질문 반영: `스킬을 실제로 바꾸는가, 제안하는가`를 도입의
  결론으로 올렸습니다. 이어진 이해도 피드백에 따라 mock 내부 규칙과 점수
  절을 제거하고, 회의록 가상 예시의 입력·후보·검사·adopt를
  코드·표·인포그래픽으로 같은 의미가 되도록 맞췄습니다.

## 남은 게이트

- creator human readability decision과 `rich-post.json` 기록
- second independent remote media fetch
- independent responsive QA와 final-page record
- lifecycle `ready`
- URL mapping 반영 focused Git commit and origin/master push

사용자가 직접 업로드한 CDN URL만 매핑했습니다. 티스토리 편집·붙여넣기·
최종 공개는 사용자가 수행하며, independent remote/page QA 전까지는
`reviewing`을 유지합니다.
