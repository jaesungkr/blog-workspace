#!/usr/bin/env python3
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


SERVING_GRAMS = 150


def main() -> None:
    source = Path(__file__).with_name("greek_yogurt_ranges.csv")
    factor = Decimal(SERVING_GRAMS) / Decimal(100)
    with source.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    print(f"Assumed serving: {SERVING_GRAMS} g")
    print("Source scope: range across 17 products, purchased October 2025")
    print("Caution: minima and maxima for different metrics may be different products.")
    for row in rows:
        minimum = Decimal(row["min"]) * factor
        maximum = Decimal(row["max"]) * factor
        unit = row["unit_per_100g"]
        if row["metric"] in {"energy", "price"}:
            rendered_min = f"{minimum.quantize(Decimal('1'), rounding=ROUND_HALF_UP):,}"
            rendered_max = f"{maximum.quantize(Decimal('1'), rounding=ROUND_HALF_UP):,}"
        else:
            rendered_min = f"{minimum.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)}"
            rendered_max = f"{maximum.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)}"
        print(f"{row['metric']}: {rendered_min}–{rendered_max} {unit}")


if __name__ == "__main__":
    main()
