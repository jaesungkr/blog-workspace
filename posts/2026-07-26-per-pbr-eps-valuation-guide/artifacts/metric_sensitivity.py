#!/usr/bin/env python3
"""Calculate deterministic PER/PBR/EPS sensitivity scenarios for the post."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    label: str
    share_price: float
    net_income: float
    equity: float
    shares: float
    changed_input: str
    limitation: str


SCENARIOS = (
    Scenario(
        "S1",
        "기준",
        10,
        100,
        500,
        100,
        "없음",
        "비교 기준",
    ),
    Scenario(
        "S2",
        "일회성 손상",
        10,
        20,
        420,
        100,
        "순이익 100→20, 자기자본 500→420",
        "손상의 세금·회계 효과를 단순화",
    ),
    Scenario(
        "S3",
        "자사주 매입",
        10,
        100,
        300,
        80,
        "자기자본 500→300, 주식 수 100→80",
        "매입 시점·주가 반응·세금을 고정",
    ),
    Scenario(
        "S4",
        "경기 호황",
        10,
        200,
        600,
        100,
        "순이익 100→200, 자기자본 500→600",
        "호황 이익의 지속 기간을 예측하지 않음",
    ),
)


def calculate(scenario: Scenario) -> dict[str, str]:
    eps = scenario.net_income / scenario.shares
    bps = scenario.equity / scenario.shares
    per = scenario.share_price / eps if eps > 0 else None
    pbr = scenario.share_price / bps if bps > 0 else None
    return {
        "scenario_id": scenario.scenario_id,
        "label": scenario.label,
        "share_price": f"{scenario.share_price:.2f}",
        "net_income": f"{scenario.net_income:.2f}",
        "equity": f"{scenario.equity:.2f}",
        "shares": f"{scenario.shares:.2f}",
        "eps": f"{eps:.2f}",
        "bps": f"{bps:.2f}",
        "per": f"{per:.2f}" if per is not None else "N/A",
        "pbr": f"{pbr:.2f}" if pbr is not None else "N/A",
        "changed_input": scenario.changed_input,
        "limitation": scenario.limitation,
    }


def main() -> None:
    output_path = Path(__file__).with_name("metric-sensitivity-results.csv")
    rows = [calculate(scenario) for scenario in SCENARIOS]
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=rows[0].keys(),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(
            row["scenario_id"],
            row["label"],
            f'EPS={row["eps"]}',
            f'PER={row["per"]}',
            f'PBR={row["pbr"]}',
        )


if __name__ == "__main__":
    main()
