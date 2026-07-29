"""Reproduce SkillOpt's strict validation-gate boundary without model calls."""

from skillopt.evaluation.gate import evaluate_gate


for candidate_score in (0.49, 0.50, 0.51):
    result = evaluate_gate(
        candidate_skill=f"candidate-{candidate_score}",
        cand_hard=candidate_score,
        current_skill="current",
        current_score=0.50,
        best_skill="best",
        best_score=0.50,
        best_step=0,
        global_step=1,
    )
    print(
        f"candidate={candidate_score:.2f} "
        f"action={result.action} "
        f"current={result.current_score:.2f} "
        f"best={result.best_score:.2f}"
    )
