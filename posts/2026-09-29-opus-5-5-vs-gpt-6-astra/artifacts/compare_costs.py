#!/usr/bin/env python3
"""Reproduce the token-cost examples used in the Opus 5.5 comparison."""

import json


RATES = {
    "opus_5_5": {"input": 4.0, "cache_read": 0.20, "output": 20.0},
    "gpt_6_astra": {"input": 10.0, "cache_read": 1.0, "output": 50.0},
    "fable_5_1": {"input": 10.0, "cache_read": 0.25, "output": 50.0},
}


SCENARIOS = {
    "standard_bundle": {"input": 1.0, "cache_read": 0.0, "output": 0.2},
    "cache_heavy_agent": {"input": 2.0, "cache_read": 20.0, "output": 1.0},
    "single_300k_prompt": {"input": 0.3, "cache_read": 0.0, "output": 0.05},
}


def cost(model: str, scenario: str) -> float:
    rates = dict(RATES[model])
    usage = SCENARIOS[scenario]
    if model == "gpt_6_astra" and scenario == "single_300k_prompt":
        rates["input"] *= 2
        rates["cache_read"] *= 2
        rates["output"] *= 1.5
    return round(sum(usage[key] * rates[key] for key in usage), 2)


def main() -> None:
    output = {
        scenario: {model: cost(model, scenario) for model in RATES}
        for scenario in SCENARIOS
    }
    output["standard_bundle_savings_vs_astra_percent"] = round(
        (1 - output["standard_bundle"]["opus_5_5"]
         / output["standard_bundle"]["gpt_6_astra"]) * 100,
        1,
    )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
