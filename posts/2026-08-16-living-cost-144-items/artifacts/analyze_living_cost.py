#!/usr/bin/env python3
"""Reproduce the dev.log analysis of KOSIS living-cost items.

Input is the UTF-8 CSV downloaded from KOSIS table DT_1J22005 after adding
2025.07 to the default 2026.02-2026.07 view. The public ranking uses the
year-over-year change from July 2025 to July 2026.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import median


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "kosis-living-price-index-2025-07_2026-07.csv"
RANKING = HERE / "living-cost-144-analysis.csv"
CATEGORY_SUMMARY = HERE / "living-cost-category-summary.csv"
SUMMARY = HERE / "living-cost-analysis-summary.json"

AGGREGATES = {
    "총지수",
    "생활물가지수",
    "식품",
    "식품 이외",
    "전월세",
    "생활물가 이외",
    "전·월세포함 생활물가지수",
}

# KOSIS DT_1J22005 publishes the 144 detailed items in this fixed order.
# Counts match the official appendix: 61+20+4+8+6+5+10+7+2+5+7+9=144.
CATEGORY_SEGMENTS = [
    ("식료품·비주류음료", 61),
    ("주류", 3),
    ("외식", 20),
    ("담배", 1),
    ("의류·신발", 8),
    ("주거·공공요금", 6),
    ("가정용품", 5),
    ("보건", 10),
    ("교통", 7),
    ("통신", 2),
    ("오락·문화", 5),
    ("교육", 7),
    ("기타 생활서비스", 9),
]


def change_rate(old: float, new: float) -> float:
    return (new / old - 1.0) * 100.0


def main() -> None:
    with SOURCE.open(encoding="utf-8-sig", newline="") as source_file:
        raw_rows = list(csv.DictReader(source_file))

    aggregate_rows = {row["품목별"]: row for row in raw_rows if row["품목별"] in AGGREGATES}
    item_rows = [row for row in raw_rows if row["품목별"] not in AGGREGATES]
    expected_count = sum(count for _, count in CATEGORY_SEGMENTS)
    if len(item_rows) != expected_count:
        raise ValueError(f"Expected {expected_count} detailed items, found {len(item_rows)}")

    categories: list[str] = []
    for category, count in CATEGORY_SEGMENTS:
        categories.extend([category] * count)

    analyzed = []
    for row, category in zip(item_rows, categories):
        july_2025 = float(row["2025.07"])
        july_2026 = float(row["2026.07"])
        analyzed.append(
            {
                "item": row["품목별"],
                "category": category,
                "index_2025_07": july_2025,
                "index_2026_07": july_2026,
                "yoy_pct": change_rate(july_2025, july_2026),
            }
        )

    analyzed.sort(key=lambda row: (-row["yoy_pct"], row["item"]))
    for rank, row in enumerate(analyzed, start=1):
        row["rank"] = rank

    with RANKING.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=["rank", "item", "category", "index_2025_07", "index_2026_07", "yoy_pct"],
        )
        writer.writeheader()
        for row in analyzed:
            writer.writerow(
                {
                    **row,
                    "index_2025_07": f'{row["index_2025_07"]:.2f}',
                    "index_2026_07": f'{row["index_2026_07"]:.2f}',
                    "yoy_pct": f'{row["yoy_pct"]:.2f}',
                }
            )

    category_rows = []
    for category, _ in CATEGORY_SEGMENTS:
        rows = [row for row in analyzed if row["category"] == category]
        rates = [row["yoy_pct"] for row in rows]
        top = max(rows, key=lambda row: row["yoy_pct"])
        category_rows.append(
            {
                "category": category,
                "count": len(rows),
                "median_yoy_pct": median(rates),
                "rising_count": sum(rate > 0 for rate in rates),
                "five_percent_plus_count": sum(rate >= 5 for rate in rates),
                "top_item": top["item"],
                "top_item_yoy_pct": top["yoy_pct"],
            }
        )

    with CATEGORY_SUMMARY.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=category_rows[0].keys())
        writer.writeheader()
        for row in category_rows:
            writer.writerow(
                {
                    **row,
                    "median_yoy_pct": f'{row["median_yoy_pct"]:.2f}',
                    "top_item_yoy_pct": f'{row["top_item_yoy_pct"]:.2f}',
                }
            )

    def aggregate_rate(name: str) -> float:
        row = aggregate_rows[name]
        return change_rate(float(row["2025.07"]), float(row["2026.07"]))

    summary = {
        "source_table": "KOSIS DT_1J22005 생활물가지수(2020=100)",
        "source_updated": "2026-08-04",
        "comparison": "2025-07 to 2026-07",
        "detailed_item_count": len(analyzed),
        "overall_cpi_yoy_pct": round(aggregate_rate("총지수"), 2),
        "living_cpi_yoy_pct": round(aggregate_rate("생활물가지수"), 2),
        "living_food_yoy_pct": round(aggregate_rate("식품"), 2),
        "living_nonfood_yoy_pct": round(aggregate_rate("식품 이외"), 2),
        "rising_item_count": sum(row["yoy_pct"] > 0 for row in analyzed),
        "rising_item_share_pct": round(
            sum(row["yoy_pct"] > 0 for row in analyzed) / len(analyzed) * 100.0, 1
        ),
        "falling_item_count": sum(row["yoy_pct"] < 0 for row in analyzed),
        "unchanged_item_count": sum(row["yoy_pct"] == 0 for row in analyzed),
        "five_percent_plus_count": sum(row["yoy_pct"] >= 5 for row in analyzed),
        "top_15": [
            {"rank": row["rank"], "item": row["item"], "category": row["category"], "yoy_pct": round(row["yoy_pct"], 2)}
            for row in analyzed[:15]
        ],
        "bottom_10": [
            {"rank": row["rank"], "item": row["item"], "category": row["category"], "yoy_pct": round(row["yoy_pct"], 2)}
            for row in analyzed[-10:]
        ],
        "method_limit": "Detailed-item ranks and category medians are unweighted diagnostics. Official aggregate indices apply expenditure weights; individual household bills also depend on purchase quantity, brand, region, and discounts.",
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
