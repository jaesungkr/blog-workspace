# 캡처 계획: 스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기

## 독자 과업

- 주요 독자와 모른다고 가정할 내용: `SKILL.md`를 관리하지만 SkillOpt에
  스킬 파일 하나만 넣으면 자동으로 좋은 문장으로 바뀐다고 생각하는 개발자
- 익숙한 기준: 담당자와 마감일을 자주 빼먹는 회의록 정리
- 글을 읽은 뒤 완료할 작업: 현재 스킬, 반복 작업 사례, 성공 기준이 각각
  왜 필요한지 이해하고 `run`·`status`·`adopt`를 구분한 뒤 공식 mock
  PASS를 확인
- 시작 상태와 전제 조건: 터미널, Git, Python 3.10 이상
- 비개발자 경로: 해당 없음. 현재 공식 제품은 명령줄 개발 도구
- 확장 경로: `skillopt-sleep dry-run`으로 수집 범위를 확인한 뒤 실제
  backend와 `--target-skill-path`를 지정해 제안을 검토함에 저장
- 가장 짧은 성공 경로: 회의록 예시 이해 -> 소스 clone -> Python 3.12
  가상환경 -> editable install -> 공식 mock -> PASS
- 시험하지 않는 범위: 회의록 예시의 실제 실행, 개인 세션, real backend,
  실제 `adopt`, 연구 엔진 학습, 실제 LLM 성능

## 사용법 경계

- 작동 관계: 현재 스킬 + 작업 사례 + 성공 기준 -> 수정 후보 ->
  별도 사례 검사 -> 검토함 -> 사용자 adopt
- 공식 확인 명령: `python -m skillopt_sleep.experiments.run_experiment
  --persona researcher --assert-improves`
- 계정·비용 조건: 공식 mock에는 API Key와 모델 비용이 없음. Git과
  Python 3.10 이상 필요
- 문서 링크: `https://microsoft.github.io/SkillOpt/docs/guideline.html`,
  `https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md`,
  `https://microsoft.github.io/SkillOpt/docs/reference/cli.html`
- 가장 흔한 실패: Python 3.9 이하는 설치가 거절됨. Python 3.10 이상으로
  가상환경을 다시 만들고, 최신 `main`이 달라졌다면 commit `7da46ae`로
  돌아감
- 비용 오해: 실제 backend의 `dry-run`은 저장과 반영만 막으며 provider
  호출과 비용은 막지 않음. 비용 없는 점검은 `--backend mock`

## 실행 환경

- 실행 주체: Codex
- 확인일: 2026-07-30
- 환경: macOS 26.5.2 arm64, Python 3.12.13, Google Chrome 150
- 소스: Microsoft SkillOpt commit
  `7da46ae693ee0329b80225c0128a37d65db10e9e`, package metadata 0.2.0
- 네트워크: 공개 소스 clone과 Python package 설치에만 사용. mock
  실행은 provider 호출 없음
- 개인정보: 개인 세션과 API credential을 사용하지 않음

## 주장과 화면

| 주장 ID | 독자 행동·관찰 | 필요한 증거 | 자산 ID | 성공 기준 |
|---|---|---|---|---|
| C01·C10·C15 | 무엇을 입력하면 무엇이 제안되고 파일은 언제 바뀌는지 이해 | official source + 명시된 구조 예시 | `skillopt-meeting-notes-flow` | 입력 3가지, 수정 후보, 별도 사례 검사, adopt를 한 흐름으로 구분 |
| C02·C03·C05 | 공식 no-API 실험을 실행하고 PASS의 범위를 이해 | first-party log + source | 해당 없음 | 설치·제어 흐름 확인과 실제 스킬 성능을 혼동하지 않음 |
| C07·C08·C09 | 실제 프로젝트 전에 dry-run 경계를 확인 | official source | 해당 없음 | mock/real backend와 project/target path를 혼동하지 않음 |

## 제작 순서

| 순서 | 시작 상태 | 행동 | 완료 상태 | 자산 역할 | 비고 |
|---|---|---|---|---|---|
| 1 | 공식 소스 clone | Python 3.12 환경에 설치하고 mock 실행 | PASS 원시 로그 | evidence | `artifacts/run/mock-experiment.txt` 보존 |
| 2 | 회의록 구조 예시 | 입력 3가지와 세 수정 규칙을 HTML/CSS로 조판 | 가상 예시 infographic | lead | 실제 제품 UI·실행 결과로 표현하지 않음 |
| 3 | v1 후보 | 입력 문서와 후보 문서의 겹침 확인 | revision required | validation | 높이·문구·연결선 수정 |
| 4 | v2~v4 | 문서 높이와 연결선, 모바일 글자 크기 수정 | v5 1080×1350 | lead | headline 20px, primary 15px, support 12px, caveat 11.3px equivalent |

## GIF 판단

- 시간 변화가 핵심인가: 아니요. 입력에서 후보와 adopt까지의 관계는 한 장의
  정적 흐름도가 더 빠르게 설명함
- GIF·poster: `not_applicable`

## 개인정보와 권한

- 제거할 값: 없음. 가상 회의록 예시이며 개인 경로·계정·세션이 없음
- 외부 전송·결제·로그인: 소스와 package 다운로드 외에는 없음
- 출처·권리: SkillOpt 메커니즘은 공식 문서, 회의록 문구와 결정적
  HTML/CSS 조판은 dev.log 원본
- 사용자가 직접 하거나 승인할 단계: Tistory 이미지 업로드와 CDN URL
  매핑, 최종 게시. 실제 개인 프로젝트의 real backend와 `adopt`
