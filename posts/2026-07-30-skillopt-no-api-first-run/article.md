---
title: "스킬 최적화 방법 - SkillOpt를 API 키 없이 직접 돌려보기"
slug: skillopt-no-api-first-run
date: 2026-07-30
category: "Log"
subcategory: "AI 개념 · 실전"
status: reviewing
format: rich-post
section_backgrounds: plain
tags: [SkillOpt, SkillOpt 사용법, 스킬 최적화, SKILL.md, Codex, Claude Code, AI 에이전트]
summary: "SkillOpt가 현재 SKILL.md와 사용자가 남긴 과거 작업 기록, 성공 기준으로 수정 후보를 만들고 검증한 뒤 adopt에서 실제 파일에 반영하는 과정을 회의록 예시로 설명합니다."
hero_image: assets/infographics/skillopt-meeting-notes-flow-v5.png
published_url: ""
sources:
  - https://github.com/microsoft/SkillOpt
  - https://microsoft.github.io/SkillOpt/docs/guideline.html
  - https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md
  - https://microsoft.github.io/SkillOpt/docs/reference/cli.html
  - https://github.com/microsoft/SkillOpt/blob/main/skillopt_sleep/experiments/run_experiment.py
---

안녕하세요. dev.log입니다.

Codex나 Claude Code에 같은 일을 맡길 때마다 같은 실수가 반복될 수 있습니다. 그때마다 `SKILL.md`에 규칙을 한 줄씩 보태면 당장은 나아져도, 새 규칙이 다른 작업을 망가뜨리는지는 알기 어렵습니다.

[SkillOpt](https://github.com/microsoft/SkillOpt)는 이 과정을 테스트가 있는 문서 수정처럼 다룹니다. 현재 스킬을 과거 작업 기록과 함께 살펴보고 수정 후보를 만듭니다. 별도로 남겨 둔 사례에서는 후보를 적용한 결과가 실제로 나아졌는지 확인합니다.

한 문장으로 정리하면 이렇습니다.

> **현재 스킬 + 사용자가 남긴 과거 작업 기록 + 잘됐는지 판단할 기준**을 SkillOpt에 넘기면, 수정 후보를 만들고 다른 사례로 테스트합니다. 통과한 후보는 검토함에 두며, 사용자가 adopt해야 실제 스킬에 반영됩니다.

여기서 과거 작업 기록은 결과 파일 하나만 뜻하지 않습니다. 사용자가 무엇을 요청했고, 에이전트가 어떤 결과를 냈으며, 무엇이 잘됐고 무엇이 잘못됐는지 확인할 수 있어야 합니다. 이 정보가 없으면 SkillOpt도 어느 방향으로 고쳐야 할지 판단하기 어렵습니다.

SkillOpt-Sleep에서는 이 승인 절차가 `run`, `status`, `adopt`로 나뉩니다. `run`은 검토 보고서를 남기고, 검증을 통과한 후보가 있으면 함께 보관합니다. `status`는 최근 보고서와 후보가 있을 경우 그 내용을 보여 줍니다. 사용자가 `adopt`를 실행해야 대상 `SKILL.md`가 실제로 바뀝니다.

### 회의록 스킬로 보는 입력과 수정 후보

아래 회의록은 작동 방식을 풀어 보기 위해 만든 가상 예시이며, 직접 실행한 결과는 아닙니다.

현재 회의록 스킬에 다음 한 줄만 있다고 가정해 보겠습니다.

```text
 # 회의록 정리

회의 내용을 짧고 명확하게 요약한다.
```

그런데 여러 회의록을 정리하는 동안 같은 문제가 반복됐습니다.

- 결정된 내용과 앞으로 할 일이 섞입니다.
- 할 일의 담당자가 빠집니다.
- 마감일을 알 수 없는데 날짜를 추측합니다.

이때 SkillOpt가 판단에 사용하는 재료는 세 가지입니다.

| 입력 | 회의록 예시에서는 |
|---|---|
| 현재 스킬 | `회의 내용을 짧고 명확하게 요약한다` |
| 사용자가 남긴 과거 작업 기록 | 회의 요청과 결과에서 반복된 담당자 누락, 항목 혼합, 날짜 추측 |
| 성공 기준 | 항목 구분, 담당자 표시, 날짜가 없으면 `미정` |

이 자료를 바탕으로 다음과 같은 수정 후보를 만들 수 있습니다.

```diff
 # 회의록 정리

 회의 내용을 짧고 명확하게 요약한다.

+ 결정사항과 할 일을 별도 항목으로 구분한다.
+ 모든 할 일에 담당자와 마감일을 표시한다.
+ 마감일이 확인되지 않으면 날짜를 추측하지 말고 '미정'이라고 쓴다.
```

후보를 만들었다고 바로 좋은 규칙으로 인정하지는 않습니다. 수정에 직접 쓰지 않은 다른 회의록에도 적용해 담당자 누락과 날짜 추측이 줄었는지 검사합니다. 결과가 나아진 후보만 검토함에 남기고, 그렇지 않으면 거절합니다.

{{media:skillopt-meeting-notes-flow}}

이 흐름을 한 줄로 줄이면 다음과 같습니다.

```text
현재 SKILL.md + 사용자가 남긴 과거 작업 기록 + 성공 기준
→ 수정 후보
→ 별도 사례로 검사
→ 검토함
→ 사용자가 adopt
```

### 제안이 실제 SKILL.md가 되는 시점

SkillOpt-Sleep에서 제안과 반영은 서로 다른 단계입니다. 기본 설정에서는 검증을 통과해도 원본을 바로 덮어쓰지 않습니다.

| 명령 | 하는 일 | 대상 SKILL.md |
|---|---|---|
| `run` | 세션에서 과제를 만들고 후보를 검증한 뒤 최신 보고서를 검토함에 저장. 통과한 후보가 있으면 후보 파일도 함께 저장 | 바뀌지 않음 |
| `status` | 가장 최근 검토 보고서와, 있을 경우 수정 후보를 표시 | 바뀌지 않음 |
| `adopt` | 검토함의 후보를 백업 후 실제 파일에 반영 | 후보가 있으면 바뀜 |
| `run --auto-adopt` | 검증을 통과한 후보를 자동 반영 | 통과한 후보가 있으면 바뀜, 사용자가 켠 경우만 |

회의록 예시의 후보가 검증을 통과했다고 가정해 보겠습니다. `run` 뒤에는 보고서와 후보가 검토함에 남고, `status`로 그 내용을 확인할 수 있습니다. 사용자가 후보를 읽고 `adopt`했을 때 비로소 위 세 규칙이 대상 `SKILL.md`에 들어갑니다.

### API 키 없이 첫 실행

필요한 것은 Git과 Python 3.10 이상입니다. 먼저 설치된 버전을 확인하세요.

글과 같은 소스를 재현하려고 2026년 7월 30일의 커밋 `7da46ae`를 고정했습니다.

macOS와 Linux에서는 다음 명령을 사용합니다. 글에서 검증한 버전은 Python 3.12입니다. Python 3.10이나 3.11만 설치돼 있다면 첫 명령의 이름을 `python3.10` 또는 `python3.11`로 바꾸면 됩니다.

```bash
python3.12 --version
git clone https://github.com/microsoft/SkillOpt.git
cd SkillOpt
git checkout 7da46ae693ee0329b80225c0128a37d65db10e9e

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Windows PowerShell에서는 Python Launcher로 같은 버전을 지정합니다.

```powershell
py -3.12 --version
git clone https://github.com/microsoft/SkillOpt.git
Set-Location SkillOpt
git checkout 7da46ae693ee0329b80225c0128a37d65db10e9e

py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

Python 3.10이나 3.11을 쓰려면 두 곳의 `3.12`를 설치된 버전으로 바꾸세요.

설치가 끝나면 [공식 SkillOpt-Sleep 안내](https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md)에 있는 재현용 실험을 실행합니다. 같은 입력에서는 같은 결과가 나오는 명령입니다.

```bash
python -m skillopt_sleep.experiments.run_experiment \
  --persona researcher \
  --assert-improves
```

Codex가 새 Python 3.12 환경에서 실행했을 때 마지막에 다음 문구가 출력됐습니다.

```text
PASS: nightly consolidation improves held-out score
AND gate blocks regressions.
```

이 `PASS`는 수정 후보를 만들고, 별도 사례로 검사하고, 나쁜 후보를 거절하는 프로그램의 연결 상태가 정상이라는 뜻입니다. 사용자의 실제 스킬이 좋아졌다는 성능 점수는 아닙니다.

이 명령은 API 키나 모델 토큰을 쓰지 않습니다. 설치 단계에서 Python 패키지는 내려받지만, 실험 자체는 외부 모델에 프롬프트를 보내지 않습니다. 개인 `SKILL.md`도 수정하지 않습니다.

이번 검증에서도 시스템 Python 3.9로 만든 첫 가상환경은 설치가 거절됐습니다. `python --version`으로 3.10 이상인지 확인하고 가상환경을 다시 만들면 됩니다. 최신 `main`에서 결과가 달라졌다면 위 커밋으로 돌아와 같은 조건에서 확인할 수 있습니다.

### SkillOpt의 두 실행 경로

공식 문서에서 `SkillOpt`와 `SkillOpt-Sleep`은 목적과 준비물이 다릅니다. 이름은 비슷하지만 같은 명령의 쉬운 모드와 어려운 모드가 아닙니다.

| 경로 | 무엇을 입력하나 | 무엇을 얻나 | 먼저 준비할 것 |
|---|---|---|---|
| 연구 엔진 | 초기 스킬, 학습·선택·최종 검사 문제 | `best_skill.md`, 점수와 이력 | 문제를 읽는 코드, 실행·채점 연결 코드, 대상·옵티마이저 모델 |
| SkillOpt-Sleep | 지원하는 코딩 에이전트의 지난 세션 | 검토함에 임시 저장된 스킬·메모리 제안 | 세션 범위, 과제를 다시 실행할 방식, 대상 스킬 경로 |

앞에서 실행한 명령은 두 번째 경로에 포함된 공식 인수 테스트입니다. 인수 테스트는 빈 관리 블록에서 수정 후보를 만들고 검증 게이트를 통과시키는 흐름을 확인합니다. 독자의 실제 파일을 수정하거나 연구 논문의 전체 훈련을 축소 재현하지는 않습니다. SkillOpt-Sleep도 논문의 `skillopt/` 패키지에 직접 의존하지 않으며, 검증 게이트를 따로 포함한 preview 기능입니다.

내장 벤치마크가 아닌 회사 업무를 연구 엔진에 붙이려면 일이 더 많습니다. 문제를 train·selection·test로 나누고, 에이전트가 낸 결과를 점수로 바꾸는 코드를 작성해야 합니다. 실제 업무를 수행할 대상 모델과 스킬 문장을 고칠 옵티마이저 모델도 정해야 합니다. 자동 채점이 어려운 업무라면 이 준비가 최적화 자체보다 더 중요합니다.

### 내 SKILL.md 연결 전에 세션 범위부터 확인

실제 세션을 건드리기 전에 수집 범위부터 확인하는 순서가 좋습니다. 아래 명령은 최근 Codex 세션을 대상으로 흐름만 점검합니다.

먼저 SkillOpt 저장소에서 나와, 고치려는 스킬이 있는 프로젝트 루트로 이동합니다. 앞에서 활성화한 가상환경은 그대로 둡니다.

```bash
cd /path/to/your-project
```

Windows PowerShell에서는 `Set-Location C:\path\to\your-project`처럼 입력합니다. 이제 `$PWD`가 SkillOpt 저장소가 아니라 자신의 프로젝트를 가리키는지 확인한 뒤 실행하세요.

```bash
skillopt-sleep dry-run \
  --project "$PWD" \
  --source codex \
  --backend mock \
  --lookback-hours 72 \
  --max-sessions 5 \
  --max-tasks 3
```

PowerShell에서는 다음처럼 각 줄 끝에 백틱을 붙입니다.

```powershell
skillopt-sleep dry-run `
  --project "$PWD" `
  --source codex `
  --backend mock `
  --lookback-hours 72 `
  --max-sessions 5 `
  --max-tasks 3
```

`--backend mock`은 외부 모델 공급자를 호출하지 않습니다. `dry-run`은 결과를 검토함에 임시 저장하거나 스킬에 반영하지 않습니다. 다만 로컬 상태 디렉터리에 진단용 근거 로그가 생길 수 있으므로, 그 파일도 세션 자료처럼 다루는 편이 좋습니다.

실제 모델로 후보를 만들 준비가 됐다면 대상 스킬 경로를 명시합니다. 아래 경로는 예시이므로 자신의 프로젝트 경로로 바꿔야 합니다.

```bash
skillopt-sleep run \
  --project "$PWD" \
  --source codex \
  --backend codex \
  --target-skill-path .agents/skills/my-skill/SKILL.md \
  --max-sessions 5 \
  --max-tasks 3 \
  --progress

skillopt-sleep status --project "$PWD"
```

PowerShell에서는 다음과 같이 실행합니다.

```powershell
skillopt-sleep run `
  --project "$PWD" `
  --source codex `
  --backend codex `
  --target-skill-path .agents/skills/my-skill/SKILL.md `
  --max-sessions 5 `
  --max-tasks 3 `
  --progress

skillopt-sleep status --project "$PWD"
```

`--project`는 어떤 프로젝트의 세션과 상태를 볼지 정합니다. 어느 `SKILL.md`를 고칠지는 자동으로 정하지 않으므로 `--target-skill-path`를 따로 적어야 합니다.

`run`도 기본적으로 제안을 임시 보관할 뿐입니다. 먼저 `status`에서 수정 내용과 근거를 읽습니다. 별도 테스트까지 통과한 뒤에만 `skillopt-sleep adopt --project "$PWD"`를 실행하세요. 처음부터 예약 실행이나 `--auto-adopt`를 켤 이유는 없습니다.

### dry-run도 모델 비용이 생기는 조건

`dry-run`이라는 이름만 보고 비용이 없다고 생각하기 쉽습니다. 하지만 비용과 외부 전송을 가르는 것은 `dry-run`이 아니라 backend입니다.

| 확인 항목 | `mock` backend | `codex` 같은 실제 backend |
|---|---|---|
| 모델 호출 | 없음 | 있음 |
| 확인할 수 있는 것 | 수집·편집·게이트의 제어 흐름 | 선택한 모델이 과제를 다시 실행한 결과와 수정 후보 |
| `dry-run`의 효과 | 임시 저장·반영 없음 | 임시 저장·반영은 없지만 호출과 비용은 발생 가능 |
| 품질 해석 | 실제 스킬 향상 근거가 아님 | 미리 떼어 둔 검사 사례의 범위 안에서만 해석 |

[공식 데이터 경계 설명](https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md#how-it-works)에 따르면 수집 자체는 로컬에서 읽기 전용으로 진행됩니다. 실제 모델을 쓰면 세션에서 추린 내용과 파생 과제가 선택한 모델 공급자에게 전송될 수 있습니다. 과제를 다시 실행한 내용과 반영 프롬프트도 전송 대상에 포함될 수 있습니다. 비밀정보처럼 보이는 문자열을 가리는 기능이 있어도 모든 외부 프롬프트가 안전하다고 보장하지는 않습니다.

따라서 첫 실전은 공개하거나 폐기해도 되는 작은 프로젝트가 좋습니다. 민감한 저장소에서는 task file을 먼저 만들고 내용을 검토·수정한 뒤 실제 backend에 넘기는 절차가 필요합니다. 게이트는 점수 하락을 줄이는 장치이지, 개인정보나 보안을 대신 검사하는 경계가 아닙니다.

### 어떤 스킬부터 고칠까

SkillOpt에 잘 맞는 첫 과제는 화려한 작업보다 판정이 분명한 반복 업무입니다.

- 같은 종류의 요청이 여러 세션에서 반복됩니다.
- 성공 여부를 테스트, 파일 비교, JSON schema, 정답 형식처럼 일관되게 확인할 수 있습니다.
- 편집에 쓴 사례와 별도로 검사할 사례를 남길 수 있습니다.
- 세션 일부가 provider로 전송돼도 문제가 없는 범위를 고를 수 있습니다.

예를 들어 “커밋 제목을 명령형으로 쓰기”, “코드 수정 뒤 관련 테스트 실행하기”, “응답을 정해진 JSON 형태로 끝내기”가 첫 후보가 될 수 있습니다. 반대로 문체 취향, 한 번뿐인 기획, 정답이 계속 바뀌는 업무는 점수부터 흔들립니다. 이때는 최적화 명령보다 무엇을 성공으로 볼지 먼저 정해야 합니다.

가장 짧은 시작은 위 공식 mock 실험에서 `PASS`를 확인하는 것입니다. 그다음 반복 실수 하나를 고르고, 성공 조건을 한 문장으로 적어 보세요. 이 조건을 자동으로 검사할 수 있을 때 비로소 실제 세션의 작은 `dry-run`으로 넘어갈 준비가 된 것입니다.
