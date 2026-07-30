# 근거 지도: 스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기

## 주장별 상태

| ID | 본문 주장 | 유형 | 상태 | 근거 | 한계 |
|---|---|---|---|---|---|
| C01 | SkillOpt는 모델 가중치 대신 외부 자연어 스킬을 실행 기록과 held-out validation으로 최적화함 | 공식 | 확인 | 공식 저장소 README·guideline | 모든 작업에서 성능 향상을 보장하지 않음 |
| C02 | 공식 deterministic experiment는 mock backend로 API 키 없이 실행 가능함 | 공식 + Codex 실행 | 확인 | `docs/sleep/README.md`, `run_experiment.py`, 실행 로그 | SkillOpt-Sleep acceptance test이며 연구 엔진 훈련 재현이 아님 |
| C03 | commit `7da46ae`의 공식 mock 실행에서 PASS, 0 model tokens, harmful edit blocked를 관찰함 | Codex 실행 | 확인 | `artifacts/run/mock-experiment.txt` | 공식 고정 예제 한 번의 결정적 실행 |
| C05 | mock의 PASS는 실제 LLM이나 사용자 스킬의 품질 향상 근거가 아님 | 공식 + 소스 해석 | 확인 | README의 mock 경계, `run_experiment.py` docstring | 제어 흐름과 gate safety만 검증 |
| C06 | package는 Python 3.10 이상을 요구함 | 공식 + 설치 관찰 | 확인 | `pyproject.toml`, Python 3.9 설치 실패, Python 3.12 성공 | 최신 release와 main 기능 경계는 바뀔 수 있음 |
| C07 | SkillOpt 연구 엔진과 SkillOpt-Sleep은 별도 입력·산출물·패키지 경계를 가짐 | 공식 | 확인 | guideline, Sleep README | Sleep은 preview |
| C08 | mock backend는 provider 호출이 없지만 real-backend dry-run은 호출과 비용이 발생할 수 있음 | 공식 | 확인 | Sleep README, CLI reference | 실제 비용은 선택 backend와 모델에 따라 다름 |
| C09 | `--project`는 범위를 정하고 대상 스킬은 `--target-skill-path`로 따로 지정해야 함 | 공식 | 확인 | guideline, CLI reference | 경로는 프로젝트마다 다름 |
| C10 | Sleep `run`은 기본적으로 제안을 staging하며 `adopt`가 별도임 | 공식 | 확인 | Sleep README, CLI reference | `--auto-adopt`는 사용자가 명시적으로 켤 수 있음 |
| C11 | real backend는 session-derived excerpts·tasks·prompts를 provider로 보낼 수 있고 redaction은 완전한 비밀 보장을 하지 않음 | 공식 | 확인 | Sleep README data boundary | backend별 격리와 전송 범위가 다름 |
| C12 | held-out gate는 측정한 과제의 회귀를 줄일 뿐 보안 경계가 아님 | 공식 | 확인 | guideline data/privacy section | 약한 verifier는 잘못된 목표를 최적화할 수 있음 |
| C13 | 연구 엔진의 새 업무에는 초기 스킬, split 데이터, 실행·채점 adapter, 대상·옵티마이저 모델이 필요함 | 공식 | 확인 | first-experiment·new-benchmark docs | 내장 benchmark는 일부 연결 코드를 제공 |
| C15 | 회의록 스킬의 현재 문서·과거 요청과 결과·성공 기준·수정 후보·검사 흐름은 SkillOpt 작동 방식을 풀어 쓴 설명용 가상 예시임 | 구조 예시 | 확인 | 본문에서 가상 예시로 명시, C01·C10의 공식 흐름에 맞춰 구성 | 직접 실행 결과나 제품 UI가 아님 |

## 직접 검증

- 질문: 일반 독자가 provider credential 없이 SkillOpt의 스킬 편집과
  held-out gate 흐름을 실제 명령으로 확인할 수 있는가?
- 실행 주체: Codex
- 확인일: 2026-07-30
- OS: macOS 26.5.2 arm64
- Python: 3.12.13
- source: Microsoft SkillOpt commit
  `7da46ae693ee0329b80225c0128a37d65db10e9e`
- 설치: 새 virtualenv에서 `python -m pip install -e .`
- 명령: `python -m skillopt_sleep.experiments.run_experiment --persona
  researcher --assert-improves --json`
- 성공 기준: exit 0, `improved: true`, `gate_blocks_harmful: true`,
  `tokens_used: 0`
- 관찰: PASS, `improved: true`, harmful edit blocked, 0 model tokens,
  wall time 0.04초
- 원자료: `artifacts/run/mock-experiment.txt`

## 실패와 복구

- 첫 시도: `/usr/bin/python3`로 새 가상환경을 만들었고 Python 3.9.6이라
  `Package 'skillopt' requires a different Python: 3.9.6 not in '>=3.10'`
  오류가 발생했습니다.
- 복구: 설치된 Python 3.12.13으로 가상환경을 다시 만들고 같은 commit을
  editable install했습니다.
- 결과: 설치 성공 뒤 official mock experiment가 exit 0으로 통과했습니다.
- 본문 반영: Python 3.10 이상 전제와 version 확인 복구 조건을 실행 단계
  바로 뒤에 배치했습니다.

## 해석하지 않는 범위

- model token 0은 mock experiment에만 해당합니다.
- 실제 Codex 세션 harvesting, provider 전송, 비용, staging, adopt는
  실행하지 않았습니다.
- 회의록 예시는 입력과 출력의 관계를 이해시키기 위한 구조 예시입니다.
  실제 SkillOpt가 만든 수정안이나 검증 결과로 해석하지 않습니다.
- 논문의 연구 엔진 benchmark와 저자 보고 성능을 재현하지 않았습니다.
- private session을 사용하지 않았으므로 privacy claim은 공식 문서 경계만
  전달합니다.

## 공식 출처

- https://github.com/microsoft/SkillOpt
- https://microsoft.github.io/SkillOpt/docs/guideline.html
- https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md
- https://microsoft.github.io/SkillOpt/docs/reference/cli.html
- https://github.com/microsoft/SkillOpt/blob/main/skillopt_sleep/experiments/run_experiment.py
