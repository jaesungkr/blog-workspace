#!/usr/bin/env python3
"""Summarize the manually coded hiccup source matrix.

This script measures explicit coverage across selected public medical sources.
It does not grade clinical evidence quality.
"""

from __future__ import annotations

import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "hiccup-source-matrix.csv"
SOURCE_COLUMNS = ("asan", "mayo", "nhs", "msd", "statpearls", "cochrane")
ALLOWED = {"yes", "partial", "not_addressed"}


def main() -> None:
    with INPUT.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    print(f"matrix={INPUT.name}")
    print(f"claims={len(rows)}")
    print(f"sources={len(SOURCE_COLUMNS)}")
    print(f"cells={len(rows) * len(SOURCE_COLUMNS)}")
    print("claim_id\tyes\tpartial\tnot_addressed\tclaim")

    for row in rows:
        values = [row[source] for source in SOURCE_COLUMNS]
        unknown = sorted(set(values) - ALLOWED)
        if unknown:
            raise ValueError(f"{row['claim_id']}: unexpected values {unknown}")
        print(
            "\t".join(
                (
                    row["claim_id"],
                    str(values.count("yes")),
                    str(values.count("partial")),
                    str(values.count("not_addressed")),
                    row["claim"],
                )
            )
        )


if __name__ == "__main__":
    main()
