"""Reproduce a fixed-token price illustration; this does not run any model."""
from decimal import Decimal
import json

INPUT_TOKENS = 100_000
OUTPUT_TOKENS = 10_000
RATES = {
    "GPT-6.1 Sol": ("2", "10"),
    "Claude Opus 5.5": ("4", "20"),
    "GPT-6 Astra": ("10", "50"),
    "Claude Fable 5.1": ("10", "50"),
}

print(json.dumps({
    "actor": "Codex",
    "observation_date": "2026-09-30",
    "method": "fixed token counts multiplied by standard USD rates per million tokens",
    "input_tokens": INPUT_TOKENS,
    "output_tokens": OUTPUT_TOKENS,
    "exclusions": ["cache", "tool fees", "retries", "speed modes", "regional premiums", "subscription limits"],
    "limitation": "Actual token usage differs by model; this is arithmetic, not an inference benchmark.",
    "rows": [{
        "model": model,
        "input_rate": i,
        "output_rate": o,
        "example_usd": str((Decimal(INPUT_TOKENS) * Decimal(i) + Decimal(OUTPUT_TOKENS) * Decimal(o)) / Decimal(1_000_000)),
    } for model, (i, o) in RATES.items()],
}, ensure_ascii=False, indent=2))
