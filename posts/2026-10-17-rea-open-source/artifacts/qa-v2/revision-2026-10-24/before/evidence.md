# 근거: REA란? AI로 앱의 작동 원리를 알아내는 오픈소스 도구

기준일은 2026-10-17 KST이며 조사 주체는 Codex입니다. 사용자 요청에 따라 비개발자 대상의 예시 중심 설명으로 수정했습니다. 이전 글과 source pass는 artifacts/qa-v2/history/revision-1/에 보존했습니다.

## 현재 본문의 주장

| ID | 주장 | 일차 출처와 보존 자료 | 판정과 한계 |
|---|---|---|---|
| C01 | REA는 AI가 실제 앱을 조사하고 설명·재구현에 사용할 자료를 받도록 연결합니다. | https://github.com/morluto/rea ; artifacts/sources/README.md | 공식 설명입니다. 독립 AI 모델이나 범용 노코드 앱으로 쓰지 않습니다. |
| C02 | 깊은 실행 파일 분석에는 별도 엔진이 필요합니다. | https://rea.tools/faq/ ; website--public--faq--index.html | Hopper·Ghidra·IDA 등의 역할을 별도 분석 도구로 풉니다. 모든 앱이 같은 조건으로 분석되지 않습니다. |
| C03 | Windows 계산기 % 사례는 200+10%=220, 200×10%=20입니다. | https://rea.tools/#calculator ; website--public--index.html | REA 4.1.0, Calculator 11.2508.4.0 x64의 프로젝트 측 사례입니다. 숫자는 본문 첫 예시에서 한 번 설명하고 다른 계산기로 일반화하지 않습니다. 새 계산기 화면도 공식 페이지의 결과물입니다. |
| C06 | Notes의 내보내기는 다운로드 폴더의 notes.csv에 번호와 제목을 씁니다. | https://rea.tools/first-investigation/ ; website--public--first-investigation--index.html ; https://rea.tools/get-started/ | 원문은 id·title 열과 path.join(app.getPath('downloads'), 'notes.csv')를 제시합니다. 일반 프로그램 저장 위치로 일반화하지 않습니다. 파일 쓰기 실패의 전달 경로를 후속 질문으로 제안합니다. |
| C09 | 설치는 공식 배포처의 안내에서 시작합니다. | https://rea.tools/get-started/ ; website--public--get-started--index.html ; package.json ; registry-latest.json | 이번 본문은 설치 절차를 약속하지 않습니다. CLI 명령·doctor·Node 버전은 제외하고 공식 문서로 연결합니다. 이전 조사 자료는 보존합니다. |
| C10 | REA는 MIT로 공개되지만 외부 도구 이용권과 분석 대상 권한은 별개입니다. | https://github.com/morluto/rea/blob/main/LICENSE ; https://github.com/morluto/rea/blob/main/DISCLAIMER.md | 라이선스 검사 우회·보호된 코드 및 자산 복제를 지원하지 않는다는 프로젝트 원칙을 귀속합니다. 일반 법률 판단을 하지 않습니다. |
| C11 | 분석은 로컬에서 이루어지나 결과는 에이전트와 모델 제공자 정책의 적용을 받습니다. | https://rea.tools/faq/#sharing ; website--public--faq--index.html | 사내·고객 자료의 전송 조건을 확인하도록 설명하며 무전송·완전 오프라인으로 표현하지 않습니다. |
| C12 | 웹 분석은 비공개 서버 코드 획득을 뜻하지 않으며 원래 주석·이름의 완전 복원도 보장하지 않습니다. | FAQ What code does REA return?, README 원본 소스 복원 질문 | 전체 앱 복제를 약속하지 않습니다. 파일·코드 위치를 조사할 수 있는 범위로 기대를 한정합니다. |
| C13 | 공룡 게임의 속도 규칙을 조사해 속도 조절이 가능한 작은 게임을 만들었습니다. | https://rea.tools/examples/dino-lab/ ; website--public--examples--dino-lab--index.html | 공식 사례는 REA 4.1.0·Chrome 150으로 wayou Chromium-derived HTTP 웹판을 조사했습니다. 크롬 내장 오프라인 게임을 직접 분석했다고 쓰지 않습니다. 새 게임에서 그림·점프·충돌은 새 교육용 코드이며 속도 규칙만 재현합니다. |
| C14 | 개념 설명과 특정 프로그램의 실제 동작 확인을 구별하면 REA의 필요성을 판단할 수 있습니다. | C01·C03·C06·C13에서 도출한 dev.log 자체 판단 틀입니다. | 일반 AI가 프로그램을 절대 분석하지 못한다고 쓰지 않습니다. REA만 가능한 독점 능력이 아니라 이 도구의 사용 목적을 구별합니다. |
| C15 | AI와 대화하며 사용하는 방식에는 로컬 파일을 읽고 도구를 실행하는 개발용 AI 및 REA 연결이 필요합니다. | https://rea.tools/first-investigation/ ; https://rea.tools/get-started/ ; FAQ | 공식 예제 관람과 직접 분석 준비를 구분합니다. 비개발자에게 설정·결과 검증까지 무조건 쉽다고 약속하지 않습니다. AI 없이 CLI로 사용하는 별도 방식도 있으므로 모든 분석에 AI가 필수라고 쓰지 않습니다. |

CSV는 행과 열 형태의 데이터를 저장하는 텍스트 형식이며 스프레드시트에서 열 수 있다는 안정적인 기본 정의로 풉니다. 입력 번호나 메모 내용을 새로 측정한 것처럼 쓰지 않습니다. 코드와 역공학도 사례가 무엇을 하는지 이해시키는 기본 정의로 소개합니다.

## 설명 예시와 실제 결과의 구별

- 계산기와 공룡의 요청 문구는 공식 프롬프트를 바탕으로 dev.log가 쉽게 풀어 쓴 요청 예시입니다. 저자의 실행 기록·대화·인용문이 아닙니다.
- 계산기 % 결과, 새 계산기 화면, 공룡의 속도 조절 게임, Notes 저장 경로는 프로젝트 측 자료입니다. Codex나 사용자가 실제 분석한 성과로 쓰지 않습니다.
- 오래된 프로그램의 계산 규칙을 새 프로그램에서 맞추는 용도는 재구현 결과에서 도출한 적용 예시입니다. 임의의 업무 사례에 성공한 사실을 만들지 않습니다.
- 메모 파일 위치를 알고 싶다는 상황은 '가정해 보겠습니다'로 표시한 설명 예시입니다. 실제 사용자의 장애나 저자의 경험이 아닙니다.
- 자체 기여는 개념 질문/실제 프로그램 질문 구분, 파일·코드 위치 대조, 동일 입력의 결과 비교라는 시작 기준입니다. 전체 사례를 다시 요약하는 표는 중복이므로 제거했습니다.

## 조사 방법과 한계

공식 GitHub main 커밋 0c7b6d834af2d044b23196e0e522cc2468327a1e의 문서·웹 원문을 artifacts/sources/에 보존했습니다. 이번 추가 자료는 dino-lab과 first-investigation의 HTML입니다. 웹 도구에서도 공식 홈페이지·FAQ·시작 안내 및 두 예제의 현재 내용을 재확인했습니다.

REA 설치, MCP 등록, 실제 상용 앱 분석, 게임 조작 또는 프로그램 수정은 하지 않았습니다. artifacts/verify_distribution.py와 distribution-check.json은 이전 턴에 Codex가 GitHub 및 npm 메타데이터를 비교한 결과이며 런타임 기능 검증이 아닙니다.

Instagram 원문은 웹 제한 및 브라우저 관리자 정책 확인 실패로 읽지 못했습니다. 게시물의 문구나 사례를 인용하지 않습니다. 이전 로컬 file:// 미리보기도 CUA URL 정책에서 거절되었으며 다른 브라우저·raw CDP·headless 방식으로 우회하지 않습니다. 화면 검사 통과를 기록하지 않습니다.

## 이미지

C01에 대응하는 공식 social-card.svg의 1200×630 PNG입니다. 실제 UI·새 분석 성과를 보여주는 이미지가 아닙니다. 원본 자산 검토와 MIT 라이선스 보존 기록은 lead-review.md에 있으며 360px 페이지 표시 검증과 구별합니다. 이번 수정에서는 alt·caption만 비개발자에게 쉬운 문장으로 바꿨고 이미지 바이트는 변경하지 않았습니다.

원본 및 source_url은 media.json에 있습니다. Copyright (c) 2026 morluto와 LICENSE 전문을 PNG 메타데이터 및 assets/REA-LICENSE.txt에 보존했습니다. 생성 hero는 not_applicable입니다. 사용자 요청으로 supporting infographic 두 장을 C01·C03·C13·C15에 근거해 추가합니다.

## 설명 그림의 주장과 경계

- 계산기 과정 그림의 AI 질문·REA 조사·AI 제작은 C01·C03·C15를 시각화합니다. 표시할 220은 공식 계산기 덧셈 % 사례의 결과이며 가상의 측정 수치가 아닙니다. 코드를 실제 글자처럼 꾸며 원본 코드로 오해하게 만들지 않습니다.
- 공룡 변경 그림은 C13의 기존 웹 게임 속도 변화와 새 작은 게임의 속도 조절만 비교합니다. '속도 규칙만 재현'을 이미지에 포함해 원본 전체 복원 오해를 막습니다. 색상·캐릭터 그림은 설명을 위한 것이고 실제 앱 캡처가 아닙니다.
- 실화면처럼 보이는 이미지나 성능·성공률·복제 보장 문구를 생성하지 않습니다. 공식 사례를 설명하는 개념 그림의 origin은 generated, role은 concept입니다.
- 정확한 표시 문자열은 artifacts/qa-v2/infographic/copy-map.json 및 각 영문 prompt에 고정합니다. 최종 생성 뒤 실제 크기·hash·검토 결과를 별도 generation record에 기록합니다.
