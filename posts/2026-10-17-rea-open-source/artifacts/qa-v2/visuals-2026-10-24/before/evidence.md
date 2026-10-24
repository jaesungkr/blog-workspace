# 근거: REA 사용법: 메모 앱 분석으로 확인한 기능과 한계

기준일은 2026-10-24 KST입니다. 실제 실행 주체는 Codex입니다. 사용자 지시에 따라 본문에는 수행 주체를 별도 공개하지 않고 중립적인 실험 서술을 사용하며, 사용자의 개인 경험으로 바꾸지 않습니다. 원고는 과거의 공식 사례 소개에서 자체 CLI 분석과 함수 검증 중심으로 개편했습니다. 과거 기획·원고·근거·미디어는 artifacts/qa-v2/revision-2026-10-24/before/에 보존합니다.

## 일차 출처

- 프로젝트: https://github.com/morluto/rea
- 첫 실습 및 공식 예제: https://rea.tools/first-investigation/
- 예제 ZIP: https://rea.tools/examples/notes-example.zip
- 저장 처리 코드: https://rea.tools/examples/notes-electron/main.js
- 준비물·CLI·MCP 경로: https://rea.tools/get-started/
- 분석 대상·별도 엔진·자료 처리: https://rea.tools/faq/
- 라이선스: https://github.com/morluto/rea/blob/main/LICENSE
- 실행 배포본 메타데이터: https://registry.npmjs.org/rea-agents/6.7.0

공식 웹 문서는 웹 도구로 2026-10-24에 확인했습니다. 웹 시작 안내는 npm 6.4.0을 언급했으나 npm 공식 registry의 latest는 6.7.0이었으므로 실제 실행 버전을 6.7.0으로 고정했습니다. 최신이라는 문구나 버전 간 우열을 본문에 넣지 않습니다. registry 응답은 registry-latest.json에 보존했습니다.

## 확보·실행 경로

모든 신규 자료의 경로 접두사는 artifacts/qa-v2/revision-2026-10-24/입니다.

1. 공식 ZIP의 단순 HTTP 요청은 403이었고, 공식 실습 페이지의 Download example ZIP 링크를 Codex in-app browser에서 정상 다운로드했습니다. 브라우저 경고나 인증을 우회하지 않았습니다.
2. notes-example.zip 원본과 안전한 상대경로 검사 후 압축을 푼 fixture/notes-example/ 6개 파일을 보존했습니다. fixture-sha256.json에 각 파일의 SHA-256이 있습니다.
3. npm의 rea-agents@6.7.0을 npx로 실행했습니다. setup 또는 MCP 등록, 사용자 설정 변경은 하지 않았습니다. 환경은 environment.json, 실제 명령과 종료 코드는 rea-invocation.json, 분석 stdout은 rea-analysis.json, 진행 stderr는 rea-analysis.stderr.txt입니다.
4. 실행 명령은 `npx -y rea-agents@6.7.0 analyze-javascript-application <fixture 절대경로> --format json --full-output`입니다. 본문의 ./notes-example은 독자가 압축을 푼 상위 폴더에서 실행하는 동등한 상대경로입니다. CLI 도움말도 원본 파일로 보존했습니다.
5. 분석 JSON과 원본 코드의 파일·행 위치를 직접 대조했습니다. 사람이 읽을 요약은 analysis-summary.json입니다. 자연어 AI 답변이 REA 원출력인 것처럼 쓰지 않습니다.
6. verify-csv.cjs에서 입력별 예상 문자열을 실행 전에 고정했습니다. 수정하지 않은 원본 toCsv를 호출한 실제 결과는 csv-results.json, Python 표준 csv.reader로 재해석한 결과는 csv-roundtrip.json입니다. verify-roundtrip.py로 재실행할 수 있습니다.

## 주장과 검증

| ID | 본문 주장 | 근거 | 한계 |
|---|---|---|---|
| C01 | REA는 프로그램 조사를 돕는 오픈소스 분석 도구입니다. | 공식 README·FAQ, MIT 고지 | 독립 언어모델이나 완전 복제 도구로 표현하지 않습니다. |
| C16 | Node 지원 범위는 ^22.19.0 또는 ^24.11.0 또는 >=26.0.0이며, macOS arm64, Node.js 26.0.0, npm 11.12.1, REA 6.7.0으로 CLI 분석을 실행했습니다. | registry-latest.json의 engines, environment.json, rea-invocation.json, 실제 --help | MCP 연결이나 Electron GUI 사용 후기와 구별합니다. |
| C17 | 예제는 6파일이며 JavaScript 4개, parse_failures 0, 요청 처리 연결 1개입니다. | rea-analysis.json의 ok, data.normalized_result.statistics, summary.ipc.paired_renderer_transmissions | REA 결과의 개수이며 정확도 점수·범용 성능 평가가 아닙니다. |
| C18 | renderer → preload → main → csv 경로로 내보내기를 처리합니다. | REA graph의 notes:export 채널·handler 및 원본 renderer.js:1-4, preload.js:3-5, main.js:8-12, csv.js:1-9 | 그래프가 연결한 부분과 소스 직접 읽기를 함께 사용했습니다. 실행 시 도달성·권한·저장 성공은 검증하지 않았습니다. |
| C19 | downloads/notes.csv에 id,title 내용을 쓰도록 코드에 지정되어 있습니다. | main.js:8-12, csv.js 전체 및 공식 첫 실습 | 실제 시스템 다운로드 폴더에 파일을 쓴 결과가 아닙니다. |
| C20 | 다섯 입력이 예상 문자열과 일치하고 원래 값으로 재해석됐습니다. | verify-csv.cjs, csv-results.json, csv-roundtrip.json | 표본은 plain, comma-and-quotes, korean, embedded-newline, empty-list 각 1회이며 Excel 등 외부 앱에서 열지는 않았습니다. |
| C21 | 작은 예제는 직접 읽어도 저장 경로를 확인할 수 있고, REA는 관계 및 위치를 정리합니다. | 6개 원본 파일의 수동 대조, REA graph observation 위치 | 통제된 두 AI 세션의 A/B 비교를 하지 않았습니다. 속도·정확도 향상 주장이나 표를 만들지 않습니다. |
| C22 | JavaScript 소스 정적 분석과 깊은 native 실행 파일 분석의 준비물이 다릅니다. | FAQ 분석 섹션, get-started, 이번 실험 | 소스 없는 모든 앱을 단순 명령 하나로 분석한다고 쓰지 않습니다. |
| C23 | 서버 비공개 소스나 원래 주석·이름의 완전 복원을 보장하지 않습니다. | FAQ What code does REA return? | 분석한 자료를 넘어선 성과를 약속하지 않습니다. |
| C24 | REA MIT와 외부 AI/분석 도구 비용, 모델 데이터 정책은 별개입니다. | LICENSE, FAQ sharing, provider 준비 안내 | 가격·일반 법률 판단을 하지 않습니다. |

## 예상 값과 판정 기준

다섯 입력 각각에서 실제 toCsv 출력이 고정 예상 문자열과 정확히 같아야 합니다. Python csv.reader로 읽었을 때 첫 행은 ['id','title'], 나머지 행은 입력의 id와 title을 그대로 가져야 통과입니다. 5/5가 두 조건을 모두 통과했습니다.

- plain: `{id:1,title:'First note'}`
- comma-and-quotes: `{id:1,title:'Hello, "REA"'}`; 공식 실습 입력입니다.
- korean: `{id:2,title:'서울, "메모"'}`; 자체 추가 입력입니다.
- embedded-newline: `{id:3,title:'첫째 줄\n둘째 줄'}`; 실제 LF를 포함한 자체 추가 입력입니다.
- empty-list: `[]`; 자체 추가 입력입니다.

위의 두 첫 일반/공식 입력과 추가 입력을 합쳐 총 다섯 경우입니다. 출력 전체는 csv-results.json에 있습니다. Node 함수 실행은 CSV 문자열만 만들며, Electron 앱을 띄우거나 사용자의 실제 메모·다운로드 파일을 읽지 않습니다.

## 실패·측정 한계

- 도구 실행 자체는 성공했습니다. parse 실패·오류를 만들어 내지 않습니다.
- 코드를 읽은 정적 관계이며 실제 Electron IPC 도달성이나 저장 완료를 증명하지 않습니다. 분석 결과 자체도 runtime 미검증 제한을 포함합니다.
- 원본에는 파일 쓰기 실패를 화면으로 전달하는 후속 조사 여지가 있으며, 오류 UI를 실행 검증했다고 쓰지 않습니다.
- CLI 분석 1회와 각 입력의 함수 결과 확인만 있습니다. 속도 수치는 본문에서 제외합니다.
- 모델명·추론 설정·독립 대화 조건을 통제한 비교가 없으므로 '일반 AI보다 정확하다'고 쓰지 않습니다.
- 기존 계산기·게임 사례의 생성 그림은 유지하지 않습니다. 글의 주장을 뒷받침하는 실행 화면으로 오해될 수 있기 때문입니다.

## 미디어

공식 social-card.svg를 원본 크기 1200×630으로 래스터화한 기존 rea-official-lead.png를 유지합니다. sha256 f368346a7e2a4dd5101d9762ad3f86d0a3df604d303cae98ad5b8bc4549e6078입니다. MIT 고지는 assets/REA-LICENSE.txt 및 원본 PNG 메타데이터에 있습니다. 로컬 원본 이미지를 열어 텍스트·관계·출처를 확인했고, 직접 분석 화면으로 소개하지 않습니다. 본문에는 공식 자료라는 caption과 MIT 고지를 유지합니다.

새 그림·이미지 편집은 없습니다. 로컬 1280/360 light/dark preflight 이후 author review handoff를 제공합니다. 기존 Tistory URL·게시일·카테고리는 수정 발행 때 유지하며, 구체 후보 승인 전에는 원격 staging이나 공개 글 수정을 하지 않습니다.
