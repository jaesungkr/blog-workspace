# SkillOpt 로컬 검증 로그

## 고정 입력과 환경

- 실행일: 2026-07-29
- 저장소: `https://github.com/microsoft/SkillOpt`
- 커밋: `8304e6c3eceae36bc595e58a34b4a422ae6b2d4f`
- 커밋 시각: `2026-07-28T09:34:13Z`
- 운영체제: macOS 26.5.2 (25F84), Darwin 25.5.0 arm64
- Python: 3.12.13
- pytest: 9.1.1
- 설치: 격리 가상환경에서 `python -m pip install -e ".[dev]"`

## 전체 테스트 1차

명령:

```bash
/private/tmp/skillopt-venv-20260729/bin/python -m pytest -q
```

결과:

```text
2 failed, 555 passed, 6 skipped in 15.86s
```

실패한 항목:

```text
tests/test_superpowers_scenarios.py::TestOverlayIntegration::test_skill_copied_to_correct_path
tests/test_superpowers_scenarios.py::TestOverlayIntegration::test_source_checkout_unchanged
```

두 항목 모두 `skillopt_sleep/adapters/superpowers.py:721`에서
`ValueError: Skill path ... escapes workspace ...`로 끝났습니다.
traceback의 작업공간은 `/var/folders/...`였고, `skill_dir.resolve()` 결과는
같은 위치의 실제 경로인 `/private/var/folders/...`였습니다. 비교 대상 가운데
하나만 정규화해 안전한 하위 경로를 외부 경로로 잘못 판단한 사례입니다.

## 전체 테스트 2차

macOS 경로 별칭을 제거하기 위해 임시 루트를 실제 경로로 지정하고 같은 테스트를
다시 실행했습니다.

```bash
TMPDIR=/private/tmp \
  /private/tmp/skillopt-venv-20260729/bin/python -m pytest -q
```

결과:

```text
557 passed, 6 skipped in 12.98s
```

## 검증 게이트 경계

`artifacts/gate_probe.py`와 같은 입력을 현재 소스에서 실행했습니다.

```text
candidate=0.49 action=reject current=0.50 best=0.50
candidate=0.50 action=reject current=0.50 best=0.50
candidate=0.51 action=accept_new_best current=0.51 best=0.51
```

현재 점수보다 낮은 후보뿐 아니라 동점 후보도 거절하고, 엄격히 높은 후보만
새 최선으로 채택했습니다.

공식 게이트 단위 테스트:

```bash
/private/tmp/skillopt-venv-20260729/bin/python -m pytest tests/test_gate.py -q
```

```text
22 passed in 0.01s
```

## 해석 제한

- 저장소의 자동 테스트와 순수 게이트 함수를 확인했습니다.
- 모델 API를 호출하는 논문 벤치마크 52개 셀은 재현하지 않았습니다.
- `6 skipped`는 현재 의존성과 실행 환경에서 선택적으로 건너뛴 항목입니다.
- `/private/tmp` 재실행 성공은 기본 macOS 경로 판정 문제를 없앤 조건이며,
  1차 실패를 없었던 일로 만들지 않습니다.
