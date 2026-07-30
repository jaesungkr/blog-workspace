#!/usr/bin/env python3
"""Recalculate a small Kimi K3 evidence summary from official snapshots."""

from __future__ import annotations

import csv
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "run"
README_PATH = SOURCES / "kimi-k3-readme.md"
HF_MODEL_PATH = SOURCES / "huggingface-model-blobs.json"

MODELS = (
    "Kimi K3",
    "Claude Fable 5",
    "GPT-5.6 Sol",
    "Claude Opus 4.8",
    "GPT-5.5",
    "GLM-5.2",
)


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []
        elif tag == "br" and self._cell is not None:
            self._cell.append(" ")

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._row is not None and self._cell is not None:
            value = re.sub(r"\s+", " ", "".join(self._cell)).strip()
            self._row.append(value)
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None


def read_official_benchmark_rows() -> list[dict[str, object]]:
    parser = TableParser()
    parser.feed(README_PATH.read_text(encoding="utf-8"))

    section = ""
    coding_rows: list[dict[str, object]] = []
    for row in parser.rows:
        if len(row) == 1 and row[0] in {
            "Reasoning & Knowledge",
            "Coding",
            "Agentic",
            "Vision",
        }:
            section = row[0]
            continue
        if section != "Coding" or len(row) != 7:
            continue
        benchmark = row[0]
        if benchmark == "Benchmark":
            continue
        values: list[float] = []
        for raw in row[1:]:
            match = re.search(r"-?\d+(?:\.\d+)?", raw)
            if not match:
                raise ValueError(f"Missing numeric value for {benchmark}: {raw!r}")
            values.append(float(match.group(0)))
        if len(values) != len(MODELS):
            raise ValueError(
                f"Expected {len(MODELS)} scores for {benchmark}, found {len(values)}"
            )
        ordering = sorted(
            range(len(values)),
            key=lambda index: (-values[index], index),
        )
        kimi_rank = ordering.index(0) + 1
        coding_rows.append(
            {
                "benchmark": benchmark,
                "kimi_k3": values[0],
                "kimi_rank": kimi_rank,
                "leader": MODELS[ordering[0]],
                "leader_score": values[ordering[0]],
                "scores": dict(zip(MODELS, values)),
            }
        )
    return coding_rows


def read_weight_summary() -> dict[str, object]:
    payload = json.loads(HF_MODEL_PATH.read_text(encoding="utf-8"))
    shards = [
        item
        for item in payload["siblings"]
        if re.fullmatch(r"model-\d{5}-of-\d{6}\.safetensors", item["rfilename"])
    ]
    total_bytes = sum(int(item["size"]) for item in shards)
    return {
        "repository": payload["id"],
        "revision": payload["sha"],
        "last_modified": payload["lastModified"],
        "shard_count": len(shards),
        "total_bytes": total_bytes,
        "decimal_tb": round(total_bytes / 1_000_000_000_000, 3),
        "binary_tib": round(total_bytes / (1024**4), 3),
    }


def write_outputs(
    coding_rows: list[dict[str, object]],
    weights: dict[str, object],
) -> None:
    ranks = {rank: 0 for rank in range(1, 7)}
    for row in coding_rows:
        ranks[int(row["kimi_rank"])] += 1

    summary = {
        "basis": "MoonshotAI/Kimi-K3 official README and Hugging Face model metadata",
        "coding_benchmark_count": len(coding_rows),
        "kimi_k3_rank_distribution": {str(rank): count for rank, count in ranks.items()},
        "weight_files": weights,
        "limitations": [
            "Vendor-reported benchmark table, not an independent rerun.",
            "Scores may use different agent harnesses and fallback or cyberguard behavior.",
            "Shard size is storage metadata, not measured inference memory.",
        ],
    }
    (OUTPUTS / "audit-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    with (OUTPUTS / "coding-benchmark-ranks.csv").open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            ["benchmark", "kimi_k3_score", "kimi_rank", "leader", "leader_score"]
        )
        for row in coding_rows:
            writer.writerow(
                [
                    row["benchmark"],
                    row["kimi_k3"],
                    row["kimi_rank"],
                    row["leader"],
                    row["leader_score"],
                ]
            )

    report_lines = [
        "# Kimi K3 공식 자료 재계산 결과",
        "",
        f"- 코딩 벤치마크 행: {len(coding_rows)}개",
        f"- Kimi K3 1위: {ranks[1]}개",
        f"- Kimi K3 2위: {ranks[2]}개",
        f"- Kimi K3 3위: {ranks[3]}개",
        (
            f"- 공개 모델 샤드: {weights['shard_count']}개, "
            f"합계 {weights['decimal_tb']} TB ({weights['binary_tib']} TiB)"
        ),
        "",
        "## 코딩 벤치마크별 위치",
        "",
        "| 벤치마크 | Kimi K3 | 순위 | 공식 표의 1위 |",
        "|---|---:|---:|---|",
    ]
    for row in coding_rows:
        report_lines.append(
            f"| {row['benchmark']} | {row['kimi_k3']:.1f} | "
            f"{row['kimi_rank']}위 | {row['leader']} ({row['leader_score']:.1f}) |"
        )
    report_lines.extend(
        [
            "",
            "## 해석 제한",
            "",
            "- Moonshot AI가 공개한 표를 다시 계산한 결과이며 독립 벤치마크가 아닙니다.",
            "- 모델별 하네스와 fallback·cyberguard 조건이 완전히 같지 않습니다.",
            "- 샤드 합계는 저장 용량이며 실제 추론 메모리를 측정한 값이 아닙니다.",
            "",
        ]
    )
    (OUTPUTS / "audit-report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )


def main() -> int:
    coding_rows = read_official_benchmark_rows()
    if len(coding_rows) != 9:
        print(
            f"Expected 9 coding benchmarks, found {len(coding_rows)}",
            file=sys.stderr,
        )
        return 1
    weights = read_weight_summary()
    if weights["shard_count"] != 96:
        print(
            f"Expected 96 model shards, found {weights['shard_count']}",
            file=sys.stderr,
        )
        return 1
    write_outputs(coding_rows, weights)
    print("Kimi K3 evidence audit: pass")
    print(
        "coding ranks "
        f"1st={sum(row['kimi_rank'] == 1 for row in coding_rows)} "
        f"2nd={sum(row['kimi_rank'] == 2 for row in coding_rows)} "
        f"3rd={sum(row['kimi_rank'] == 3 for row in coding_rows)}"
    )
    print(
        f"weights {weights['shard_count']} shards, "
        f"{weights['decimal_tb']} TB ({weights['binary_tib']} TiB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
