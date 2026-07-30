# 기획: 스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기

## 분류와 독자

- 상위 카테고리: `Log`
- 하위 카테고리: `AI 개념 · 실전`
- 한 명의 독자: Codex나 Claude Code에서 `SKILL.md`를 관리하지만
  SkillOpt가 무엇을 입력받고 무엇을 바꾸는지 모르는 개발자
- 독자가 모른다고 가정할 내용: 스킬 파일만으로는 최적화할 수 없다는 점,
  사용자가 남긴 과거 작업 기록과 성공 기준의 역할, 제안과 실제 파일 반영의 차이,
  연구 엔진과 SkillOpt-Sleep의 차이
- 검색 의도: `스킬 최적화 방법`, `SkillOpt 사용법`, `SkillOpt 실행`을
  검색해 작동 방식을 이해하고 API 키 없는 첫 명령을 실행
- 익숙한 기준: 담당자와 마감일을 빠뜨리는 회의록 정리
- 가장 쉬운 시작: 회의록 가상 예시로 입력과 출력을 이해한 뒤 공식 mock의
  PASS 확인

## 글의 중심

- 독자가 기억할 한 문장: SkillOpt는 현재 `SKILL.md`만 첨삭하는 도구가
  아니라 사용자가 남긴 과거 작업 기록과 성공 기준으로 수정 후보를 만들고, 별도 사례에서
  검증한 뒤 사용자가 `adopt`할 때 실제 파일에 반영하는 도구
- 첫 이해: 현재 스킬 + 사용자가 남긴 과거 작업 기록 + 잘됐는지 판단할 기준
  -> 수정 후보 ->
  별도 사례 검사 -> 검토함 -> adopt
- 첫 행동: commit 고정 -> 가상환경 설치 -> 공식 mock 실행 -> PASS 확인
- 직접 관찰: Codex가 commit `7da46ae`를 Python 3.12.13 새 가상환경에
  설치해 mock 제어 흐름의 PASS, harmful edit 차단, model token 0을 확인
- 가장 큰 오해: `SKILL.md` 하나만 던지면 무료로 알아서 좋은 문장으로
  고쳐 준다고 생각하는 것
- 가장 중요한 실전 경계: real-backend `dry-run`도 provider 호출과 비용이
  발생할 수 있으며, `--project`와 `--target-skill-path`는 역할이 다름
- 이 글이 시험하지 않는 범위: 실제 개인 세션, real backend, `adopt`,
  회의록 예시의 실제 실행, 연구 엔진 학습과 논문 성능

## 설명 순서

| 순서 | 독자가 이해하거나 하는 일 | 다음 내용과의 연결 |
|---|---|---|
| 1 | 회의록 예시에서 입력 세 가지 확인 | SkillOpt의 정체를 먼저 이해 |
| 2 | 수정 후보와 별도 사례 검사 확인 | 무조건적인 문서 첨삭과 구분 |
| 3 | `run`·`status`·`adopt` 구분 | 실제 파일이 바뀌는 시점 확인 |
| 4 | API 키 없는 공식 명령 실행 | 설치와 제어 흐름만 안전하게 점검 |
| 5 | 연구 엔진과 Sleep 구분 | 자신의 목적에 맞는 경로 선택 |
| 6 | mock dry-run으로 세션 범위 점검 | provider 호출 전 안전 경계 확인 |
| 7 | 첫 최적화 과제 선택 | 반복성·채점 가능성·데이터 안전성 판단 |

## 입력에서 결과까지

회의록 설명용 예시는 다음 관계만 보여 줍니다.

`현재 회의록 SKILL.md + 회의 요청·결과에서 반복된 담당자 누락 + 항목 구분·미정 표시
같은 성공 기준 -> 세 규칙의 수정 후보 -> 수정에 쓰지 않은 회의록으로 검사
-> 검토함 -> 사용자 adopt`

실제 SkillOpt-Sleep 경로는 다음과 같습니다.

`지원 에이전트의 로컬 세션 -> 반복 과제 추출 -> 선택 backend로 과제 재실행
및 채점 -> 제한된 범위의 수정 후보 -> 별도 검사 -> 검토함 -> 사용자 adopt`

## 근거와 first-party 가치

- 실행 주체: Codex
- 실행일: 2026-07-30
- 고정 commit: `7da46ae693ee0329b80225c0128a37d65db10e9e`
- 실행 환경: macOS 26.5.2 arm64, Python 3.12.13, 새 virtualenv
- 원자료: `artifacts/run/mock-experiment.txt`
- 출처 대조: `artifacts/source-snapshot.md`
- 직접 확인한 것: 설치 성공, 공식 mock PASS, harmful edit 차단,
  model token 0
- 실패 또는 제한: system Python 3.9 가상환경은 `>=3.10` 요구 조건 때문에
  설치가 거절됨. Python 3.12로 다시 만든 뒤 성공

## 미디어 판단

- lead visual: 필요. “무엇을 넣으면 무엇이 나오는가”와
  `run -> 검사 -> adopt`를 글보다 빠르게 보여 줌
- reader question: 현재 `SKILL.md` 외에 무엇이 필요하며, 수정 후보는
  언제 실제 파일에 반영되는가?
- type: 회의록 가상 예시를 사용한 input -> candidate -> validation ->
  adoption process
- placement: `회의록 스킬로 보는 입력과 수정 후보` 절의 후보 검증 설명 뒤
- provenance: 설명용 simulated diagram. 실제 제품 UI나 직접 실행 결과로
  제시하지 않음
- additional image: 없음. 이전 mock 점수 이미지와 실제 규칙 이미지는
  사용자의 이해를 방해해 현재 미디어 목록에서 제거
- GIF: `not_applicable`

## 제목 후보

1. 스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기
2. SkillOpt 사용법 - SKILL.md가 실제로 바뀌는 과정
3. SkillOpt 첫 실행 - 스킬과 과거 작업 기록을 함께 넣는 이유

선택 이유: 사용자가 제안한 `스킬 최적화 방법 - SkillOpt` 감각을 유지하고,
API 키 없는 실행이라는 구체적 행동을 제목에서 드러냅니다.
