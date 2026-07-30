# SkillOpt source snapshot

- Checked at: 2026-07-30
- Repository: https://github.com/microsoft/SkillOpt
- Commit: `7da46ae693ee0329b80225c0128a37d65db10e9e`
- Commit time: `2026-07-30T04:57:41+08:00`
- Commit subject: `Merge PR #182: harvest Claude Skill tool invocations`
- Package version in `pyproject.toml`: `0.2.0`
- Python requirement: `>=3.10`

## Primary files checked

- `docs/guideline.html`
- `docs/sleep/README.md`
- `docs/reference/cli.md`
- `skillopt_sleep/experiments/run_experiment.py`
- `skillopt_sleep/experiments/personas.py`
- `skillopt_sleep/consolidate.py`
- `skillopt_sleep/backend.py`
- `pyproject.toml`

## Directly verified boundaries

- The deterministic command defaults to `backend=mock`.
- The researcher fixture contains 12 exact-answer tasks.
- The experiment assigns a held-out split with seed 42 and begins from an empty managed skill.
- `--assert-improves` exits nonzero unless the held-out score rises.
- For the mock backend it also exits nonzero unless the gate blocks the known harmful rule.
- The mock backend reports zero model tokens and makes no provider calls.
- A real SkillOpt-Sleep backend can send transcript-derived prompts and derived tasks to the selected provider.
- A real-backend `dry-run` suppresses staging and adoption, but it does not suppress provider calls or spend.
- Stateful proposals are staged for review; `adopt` is a separate action.

## Article scope

The article uses the deterministic experiment as a safe first run. It does not
claim that the result measures a reader's own skill, that a real LLM improved,
or that the paper's paid benchmark suite was reproduced.
