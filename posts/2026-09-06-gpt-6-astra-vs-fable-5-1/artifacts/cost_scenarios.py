"""Illustrative token bills; no API requests or model evaluations."""
from decimal import Decimal as D
from pathlib import Path
import json

SCENARIOS = [
    dict(id="fresh_100k", fresh=100000, cached=0, output=10000),
    dict(id="cache_hit_100k", fresh=10000, cached=100000, output=10000),
    dict(id="long_300k", fresh=300000, cached=0, output=10000),
]

def bill(s, model):
    long_input = model == "astra" and s["fresh"] + s["cached"] > 272000
    input_rate = D(20 if long_input else 10)
    cached_rate = D(2 if long_input else 1) if model == "astra" else D("0.25")
    output_rate = D(75 if long_input else 50)
    return (D(s["fresh"]) * input_rate + D(s["cached"]) * cached_rate
            + D(s["output"]) * output_rate) / D(1000000)

if __name__ == "__main__":
    result = {
        "actor": "Codex local Decimal calculation",
        "date": "2026-09-06",
        "basis": "Standard rates and fixed illustrative token counts; no actual model calls.",
        "exclusions": ["initial cache write", "tool charges", "tax", "discounts"],
        "output_definition": "All billable output including reasoning",
        "rows": [{**s, "astra_usd": str(bill(s, "astra")),
                  "fable_usd": str(bill(s, "fable"))} for s in SCENARIOS],
    }
    out = Path(__file__).with_name("cost-results.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(out.read_text())
