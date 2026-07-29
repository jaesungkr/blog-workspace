# 근거 지도: SkillOpt 사용법: 에이전트의 반복 실수를 스킬로 고치는 방법

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 `공식`, `독립 검증`, `벤더 주장`, `사용자 제공`, `Codex 실행`,
`추정`, `구조 예시`처럼 실제 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | SkillOpt는 동결한 대상 모델의 가중치 대신 자연어 스킬 문서를 최적화함 | 공식 | 확인 | 논문 §1·§3, 공식 README·문서 | "파인튜닝 대체"는 모든 작업의 동등한 성능을 뜻하지 않음 |
| C02 | 롤아웃 -> 반영 -> 병합 -> 선택 -> 수정 -> 검증 순서로 동작함 | 공식 + 소스 확인 | 확인 | 논문 §3, `docs/guide/training-loop.md`, `skillopt/engine/trainer.py` | 실제 환경 어댑터에 따라 롤아웃·채점 구현은 달라짐 |
| C03 | 텍스트 학습률은 한 단계에서 적용할 최대 편집 수이며 기본값은 4, cosine 스케줄 최솟값은 2임 | 공식 + 소스 확인 | 확인 | 논문 실험 설정, `configs/_base_/default.yaml` | 설정값이며 보편적인 최적값은 아님 |
| C04 | 기본 논문식 게이트는 selection 점수가 현재보다 엄격히 높을 때만 후보를 채택하고 동점은 거절함 | 공식 + Codex 실행 | 확인 | 논문 §3.5·§4.2, `evaluate_gate`, 게이트 경계 실행 | `evaluation.use_gate: false`면 강제 채택 가능. 현재 main의 slow update 기본값은 별도 주의 필요 |
| C05 | 거절한 편집은 같은 epoch의 후속 반영에 부정적 피드백으로 쓰임 | 공식 + 소스 확인 | 확인 | 논문 §3.5, Microsoft Research 글, trainer의 rejected-step buffer | 배포되는 스킬에는 버퍼 자체가 포함되지 않음 |
| C06 | 배포 산출물은 `best_skill.md`이며 대상 모델 추론 때 옵티마이저 호출을 추가하지 않음 | 공식 | 확인 | 논문 초록·§3.7, README | 스킬 텍스트 자체의 컨텍스트 토큰은 추가됨 |
| C07 | 논문은 6개 벤치마크·7개 대상 모델·3개 실행 방식의 52개 평가 셀에서 모두 최고 또는 공동 최고라고 보고함 | 저자 보고 | 확인 | arXiv v2 초록·표 1·2 | 독립 재현이 아니라 저자 실험이며 셀별 표본·벤치마크 범위를 벗어나 일반화할 수 없음 |
| C08 | 논문은 GPT-5.5에서 no-skill 대비 평균 +23.5p(직접 채팅), +24.8p(Codex), +19.1p(Claude Code)를 보고함 | 저자 보고 | 확인 | arXiv v2 초록·§1 | 전체 유료 실험은 이 글에서 재현하지 않음 |
| C09 | 6개 GPT-5.5 사례의 최종 스킬은 379~1,995 토큰이고 채택 편집은 1~4개임 | 저자 보고 + 저장소 확인 | 확인 | 논문 표 6, `ckpt/*/gpt5.5_skill.md` | 저장소 단어 수와 논문 tokenizer의 토큰 수는 같은 단위가 아님 |
| C10 | 같은 6개 사례의 훈련 토큰은 20.8M~213.8M임 | 저자 보고 | 확인 | 논문 표 6 | 공급자 가격·병렬성·캐시 여부에 따라 실제 비용과 시간은 달라짐 |
| C11 | 논문은 신뢰할 수 있는 자동 검증이나 채점 신호, held-out split이 필요하다고 제한을 밝힘 | 공식 | 확인 | 논문 Appendix B | 주관적인 작업에는 사람 또는 별도 모델 평가 설계가 더 필요함 |
| C12 | PyPI 최신 공개 버전은 0.2.0이고 Python 3.10 이상을 요구함 | 공식 + 패키지 메타데이터 | 확인 | v0.2.0 릴리스, `pyproject.toml` | 2026-07-29 기준이며 main에는 이후 미출시 기능이 포함됨 |
| C13 | 연구 엔진과 SkillOpt-Sleep은 별도 진입점·설정·안전 경계를 가짐 | 공식 | 확인 | `docs/index.md`, `docs/sleep/README.md` | Sleep은 preview이며 실제 세션 데이터의 외부 전송 경계를 검토해야 함 |
| C14 | 현재 커밋의 전체 테스트는 기본 macOS 임시 경로에서 555 pass·6 skip·2 fail, `/private/tmp` 재실행에서 557 pass·6 skip임 | Codex 실행 | 확인 | `artifacts/test-log.md` | 실제 모델 API와 전체 논문 벤치마크를 호출하지 않는 저장소 테스트 범위 |
| C15 | 기본 임시 경로의 2개 실패는 `/var/...`와 실제 경로 `/private/var/...` 비교 때문에 Superpowers overlay 경로가 작업공간 밖으로 잘못 판정된 경우임 | Codex 실행 + 소스 분석 | 확인 | pytest traceback, `skillopt_sleep/adapters/superpowers.py:721` | 현재 macOS 환경의 경로 별칭 사례이며 다른 OS에서는 재현되지 않을 수 있음 |
| C16 | 테스트를 빼먹는 가상 에이전트에서 문제를 훈련 20건·선택 10건·시험 10건으로 나누고, 현재 스킬 6/10, 테스트 확인 후보 8/10, 동점 후보 6/10으로 채택·거절을 설명함 | 구조 예시 | 확인 | C02의 편집 흐름과 C04의 엄격한 점수 상승 게이트를 단순화해 구성 | 문제 수와 점수 모두 실제 SkillOpt 실행·공식 벤치마크·Codex 측정값이 아니며 본문에서 가상 예시로 명시 |
| C17 | 연구 엔진으로 새 업무를 최적화하려면 사용자가 초기 스킬, train/selection/test 데이터, 실행·채점 어댑터, 대상·옵티마이저 모델 설정을 준비해야 함 | 공식 + 소스 확인 | 확인 | `docs/guide/first-experiment.md`, `docs/guide/new-benchmark.md`, `EnvAdapter`, `scripts/train.py` | 내장 벤치마크는 어댑터를 제공하지만 사용자 고유 업무는 연결 코드를 직접 구현해야 함 |
| C18 | 연구 엔진은 `best_skill.md`와 함께 config, summary, history, 후보 스킬, 단계별 실행 기록을 결과 디렉터리에 저장함 | 공식 + 소스 확인 | 확인 | `docs/guide/first-experiment.md`, `skillopt/engine/trainer.py` | 파일 구성은 버전과 설정에 따라 일부 달라질 수 있으며 자동 배포를 뜻하지 않음 |
| C19 | SkillOpt-Sleep은 일반 요청 중 자동 작동하지 않고 별도 run/schedule 뒤 제안을 staging하며 사용자가 adopt해야 반영함 | 공식 | 확인 | `docs/sleep/README.md`의 one-night 흐름과 CLI | preview 기능이며 실제 세션 데이터 전송 경계와 공급자 비용을 별도로 검토해야 함 |

## 직접 검증 설계

- 질문: 현재 SkillOpt 소스의 자동 테스트가 격리된 macOS 환경에서 통과하는지,
  핵심 게이트가 하락·동점·상승 후보를 문서대로 처리하는지 확인함
- 실행 주체: Codex
- 환경과 확인 시점: 2026-07-29, Apple Silicon arm64, macOS 26.5.2
  (25F84), Python 3.12.13, pytest 9.1.1
- 입력: `microsoft/SkillOpt` main 커밋
  `8304e6c3eceae36bc595e58a34b4a422ae6b2d4f`와 공식 `tests/`
- 전처리 또는 표현: `/private/tmp/skillopt-venv-20260729` 가상환경에
  `python -m pip install -e ".[dev]"`로 현재 소스와 개발 의존성을 설치함
- 비교·판정 규칙: pytest 종료 코드 0을 전체 통과로 봄. 게이트는 현재 점수
  0.50에서 후보 0.49·0.50·0.51을 한 번씩 넣어 action과 보존 점수를 확인함
- 성공 기준: 전체 테스트 실패 0개, 게이트가 0.49와 0.50을 거절하고 0.51만
  `accept_new_best`로 채택함
- 반복 횟수와 표본 크기: 전체 테스트 2회(기본 temp, 명시적 `/private/tmp`),
  게이트 경계 3개와 공식 `tests/test_gate.py` 22개
- 보존할 원자료: `artifacts/test-log.md`, `artifacts/gate_probe.py`,
  `artifacts/source-notes.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 기본 macOS 임시 경로로 전체 pytest | 555 pass, 6 skip, 2 fail | `artifacts/test-log.md` | 실패는 Superpowers overlay 통합 테스트 두 개의 경로 판정 |
| E02 | `TMPDIR=/private/tmp`로 같은 커밋·같은 테스트 재실행 | 557 pass, 6 skip, exit 0 | `artifacts/test-log.md` | 저장소 자동 테스트 범위. 실제 API 벤치마크 아님 |
| E03 | 현재 0.50, 후보 0.49·0.50·0.51 | reject, reject, accept_new_best | `artifacts/gate_probe.py`, `artifacts/test-log.md` | pure function인 핵심 게이트 경계 |
| E04 | 공식 게이트 단위 테스트 | 22 pass, exit 0 | `artifacts/test-log.md` | hard·soft·mixed 점수와 상태 불변식 |
| E05 | README·논문·문서·config·checkpoint 대조 | 구조, 기본값, 논문 수치, 버전 차이 확인 | `artifacts/source-notes.md` | 저자 보고 성능은 독립 재현으로 올리지 않음 |

## 실패와 반례

- 실패한 입력: 별도 `TMPDIR` 지정 없이 전체 pytest를 실행하면
  `TestOverlayIntegration` 두 항목이 실패함
- 예상과 달랐던 결과: Python `TemporaryDirectory`가 전달한 작업공간은
  `/var/folders/...`였지만 `skill_dir.resolve()`는 `/private/var/folders/...`를
  반환했습니다. 한쪽만 정규화한 `is_relative_to(workspace)` 비교가 안전한
  하위 경로를 밖으로 잘못 판정했습니다.
- 재검증: 임시 루트를 실제 경로인 `/private/tmp`로 지정한 뒤 같은 전체 테스트가
  557 pass·6 skip으로 끝났습니다. 제품의 핵심 게이트 22개도 별도로 통과했습니다.
- 일반화하면 안 되는 범위: 자동 테스트 통과는 논문의 52개 성능 셀, 실제
  API 비용, 사용자 데이터셋의 채점 품질, SkillOpt-Sleep의 개인 세션 보안을
  검증한 결과가 아닙니다.

## 미해결 항목

- 없음. 전체 논문 재현과 실제 Sleep 사용은 본문에서 검증하지 않은 범위로
  명확히 구분합니다.

## 출처 메모

- 공식 저장소: https://github.com/microsoft/SkillOpt
  - README, 설치법, 코드, 테스트, config, checkpoint의 1차 출처
- 공식 문서: https://microsoft.github.io/SkillOpt/docs/
  - 연구 엔진과 Sleep 구분, 설치·첫 실험·학습 루프
- arXiv v2: https://arxiv.org/abs/2605.23904
  - 방법, 실험 수치, 비용, limitations
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/
  - 연구팀의 쉬운 설명과 공식 발표
- v0.2.0 릴리스: https://github.com/microsoft/SkillOpt/releases/tag/v0.2.0
  - PyPI 버전과 SkillOpt-Sleep 추가 범위

긴 원문을 복사하지 않고, 본문 주장 옆에 필요한 링크와 한계를 함께 둡니다.
