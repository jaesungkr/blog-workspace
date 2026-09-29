from decimal import Decimal
import json


SCENARIOS = [
    {"id": "short", "input_tokens": 100_000, "output_tokens": 20_000},
    {"id": "long", "input_tokens": 500_000, "output_tokens": 50_000},
]

PRICES = {
    "Claude Sonnet 5.5": {"input": Decimal("2"), "output": Decimal("10")},
    "GPT-6 Sol": {
        "input": Decimal("2"),
        "output": Decimal("10"),
        "long_input": Decimal("4"),
        "long_output": Decimal("15"),
        "long_threshold": 272_000,
    },
    "Claude Opus 5.5": {"input": Decimal("4"), "output": Decimal("20")},
}


def calculate(model, scenario):
    price = PRICES[model]
    is_long_sol = model == "GPT-6 Sol" and scenario["input_tokens"] > price["long_threshold"]
    input_rate = price["long_input"] if is_long_sol else price["input"]
    output_rate = price["long_output"] if is_long_sol else price["output"]
    total = (
        Decimal(scenario["input_tokens"]) / Decimal(1_000_000) * input_rate
        + Decimal(scenario["output_tokens"]) / Decimal(1_000_000) * output_rate
    )
    return {"input_rate": str(input_rate), "output_rate": str(output_rate), "total_usd": str(total)}


result = {
    "assumption": "Each model bills the same input and output token counts; cache, tools, discounts, and regional processing are excluded.",
    "scenarios": [
        {**scenario, "models": {model: calculate(model, scenario) for model in PRICES}}
        for scenario in SCENARIOS
    ],
}

print(json.dumps(result, ensure_ascii=False, indent=2))
