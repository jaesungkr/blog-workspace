#!/usr/bin/env python3
"""Recalculate Qwen3.8-Max ranks from the vendor's published comparison table."""

from __future__ import annotations

import csv
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "sources" / "qwen38-article.json"
CSV_OUT = ROOT / "qwen38-single-score-ranks.csv"
JSON_OUT = ROOT / "qwen38-audit-summary.json"
REPORT_OUT = ROOT / "qwen38-audit-report.md"


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self.current_table: list[list[str]] | None = None
        self.current_row: list[str] | None = None
        self.current_cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == "table":
            self.current_table = []
        elif tag == "tr" and self.current_table is not None:
            self.current_row = []
        elif tag in {"th", "td"} and self.current_row is not None:
            self.current_cell = []

    def handle_data(self, data: str) -> None:
        if self.current_cell is not None:
            self.current_cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"th", "td"} and self.current_cell is not None:
            value = " ".join("".join(self.current_cell).split())
            assert self.current_row is not None
            self.current_row.append(html.unescape(value))
            self.current_cell = None
        elif tag == "tr" and self.current_row is not None:
            assert self.current_table is not None
            if self.current_row:
                self.current_table.append(self.current_row)
            self.current_row = None
        elif tag == "table" and self.current_table is not None:
            self.tables.append(self.current_table)
            self.current_table = None


def parse_score(value: str) -> float | None:
    value = value.strip()
    if value in {"", "--", "—"} or "/" in value:
        return None
    match = re.fullmatch(r"-?\d+(?:\.\d+)?%?", value)
    if not match:
        return None
    return float(value.rstrip("%"))


def main() -> None:
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    parser = TableParser()
    parser.feed(payload["data"]["content"])

    table = next(
        rows
        for rows in parser.tables
        if rows
        and "Qwen3.8-Max" in rows[0]
        and "Qwen3.7-Max" in rows[0]
        and "GPT5.6 Sol (max)" in rows[0]
    )
    header = table[0]
    target_index = header.index("Qwen3.8-Max")
    previous_index = header.index("Qwen3.7-Max")

    rows_out: list[dict[str, object]] = []
    skipped_rows: list[str] = []
    section = ""
    for row in table[1:]:
        if len(row) == 1:
            section = row[0]
            continue
        if len(row) != len(header):
            skipped_rows.append(row[0] if row else "<empty>")
            continue
        scores = [parse_score(value) for value in row[1:]]
        target_score = parse_score(row[target_index])
        previous_score = parse_score(row[previous_index])
        if target_score is None:
            skipped_rows.append(row[0])
            continue
        available = [score for score in scores if score is not None]
        rank = 1 + sum(score > target_score for score in available)
        leaders = [
            header[index]
            for index in range(1, len(header))
            if parse_score(row[index]) == max(available)
        ]
        rows_out.append(
            {
                "section": section,
                "benchmark": row[0],
                "qwen38_score": target_score,
                "qwen37_score": previous_score,
                "qwen38_rank": rank,
                "compared_models": len(available),
                "leader": " / ".join(leaders),
                "qwen38_beats_qwen37": (
                    previous_score is not None and target_score > previous_score
                ),
            }
        )

    rank_counts: dict[str, int] = {}
    for row in rows_out:
        key = str(row["qwen38_rank"])
        rank_counts[key] = rank_counts.get(key, 0) + 1

    summary = {
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_title": payload["data"]["title"],
        "models": header[1:],
        "single_score_rows": len(rows_out),
        "skipped_composite_or_unparseable_rows": skipped_rows,
        "rank_counts": rank_counts,
        "qwen38_beats_qwen37_rows": sum(
            bool(row["qwen38_beats_qwen37"]) for row in rows_out
        ),
        "qwen38_leader_rows": sum(int(row["qwen38_rank"]) == 1 for row in rows_out),
    }

    fieldnames = [
        "section",
        "benchmark",
        "qwen38_score",
        "qwen37_score",
        "qwen38_rank",
        "compared_models",
        "leader",
        "qwen38_beats_qwen37",
    ]
    with CSV_OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    JSON_OUT.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    report = [
        "# Qwen3.8-Max vendor-table recalculation",
        "",
        f"- Source: {summary['source_title']}",
        f"- Source SHA-256: `{summary['source_sha256']}`",
        f"- Compared models: {', '.join(summary['models'])}",
        f"- Single-score rows: {summary['single_score_rows']}",
        f"- Rank counts: {summary['rank_counts']}",
        f"- Rows beating Qwen3.7-Max: {summary['qwen38_beats_qwen37_rows']}",
        f"- Rows tied for or holding first place: {summary['qwen38_leader_rows']}",
        "",
        "Composite cells containing two scores were excluded instead of choosing one metric after the fact.",
        "All scores come from the vendor-authored Qwen release table; this is a structural recalculation, not an independent benchmark rerun.",
        "",
        "| Section | Benchmark | Qwen3.8 | Qwen3.7 | Rank | Row leader |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in rows_out:
        report.append(
            "| {section} | {benchmark} | {qwen38_score:g} | {qwen37_score:g} | {qwen38_rank}/{compared_models} | {leader} |".format(
                **row
            )
        )
    REPORT_OUT.write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
