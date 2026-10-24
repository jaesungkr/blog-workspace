"""Arithmetic illustration only; no model calls or measured bills."""
import json
from decimal import Decimal
from pathlib import Path

usage = {"input_tokens": 100_000, "billable_output_tokens": 10_000}
rates = {"argon_intro": ("2", "10"), "argon_december": ("4", "20"), "astra_standard": ("10", "50")}
costs = {}
for name, (input_rate, output_rate) in rates.items():
    costs[name] = str((Decimal(usage["input_tokens"]) * Decimal(input_rate)
                       + Decimal(usage["billable_output_tokens"]) * Decimal(output_rate)) / Decimal(1_000_000))
result = {"kind": "arithmetic_scenario_not_api_test", "actor": "Codex", "as_of": "2026-10-25",
          "usage": usage, "cost_usd": costs,
          "equal_token_intro_price_ratio": str(Decimal("10") / Decimal("2")),
          "aa_observed_task_cost": {"argon_high": "1.99", "astra_max": "3.26"},
          "aa_observed_cost_ratio": str(Decimal("3.26") / Decimal("1.99")),
          "exclusions": ["cache", "tools", "batch/flex", "fast", "retries"],
          "assumptions": ["billable output includes thinking tokens", "input below Astra 272K surcharge"]}
Path(__file__).with_name("cost-results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
