from __future__ import annotations

import json
import os
import platform
import statistics
import sys
import time
from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "events.csv"
PARQUET_PATH = ROOT / "events.parquet"
RESULT_PATH = ROOT / "benchmark-results.json"
ROW_COUNT = 5_000_000
REPEATS = 7

QUERY_TEMPLATE = """
SELECT
    region,
    SUM(CAST(amount AS DECIMAL(12, 2))) AS revenue,
    COUNT(*) AS event_count
FROM '{path}'
WHERE event_date BETWEEN DATE '2025-07-01' AND DATE '2025-07-31'
GROUP BY region
ORDER BY region
"""


def timed_query(connection: duckdb.DuckDBPyConnection, path: Path):
    started = time.perf_counter()
    rows = connection.execute(QUERY_TEMPLATE.format(path=path)).fetchall()
    elapsed = time.perf_counter() - started
    return elapsed, rows


def main() -> None:
    connection = duckdb.connect()
    connection.execute("SET threads = 4")
    connection.execute(
        f"""
        CREATE OR REPLACE TABLE events AS
        SELECT
            i AS event_id,
            DATE '2025-01-01' + CAST(i % 365 AS INTEGER) AS event_date,
            'region_' || LPAD(CAST(i % 10 AS VARCHAR), 2, '0') AS region,
            'category_' || LPAD(CAST(i % 100 AS VARCHAR), 3, '0') AS category,
            CAST(1 + (hash(i) % 5) AS INTEGER) AS quantity,
            CAST((100 + (hash(i * 17) % 99_900)) / 100.0 AS DECIMAL(12, 2)) AS amount
        FROM range({ROW_COUNT}) AS t(i)
        ORDER BY event_date, event_id
        """
    )
    connection.execute(f"COPY events TO '{CSV_PATH}' (HEADER, DELIMITER ',')")
    connection.execute(
        f"""
        COPY events TO '{PARQUET_PATH}'
        (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 100000)
        """
    )

    # Warm up both readers once, then alternate the measured order.
    timed_query(connection, CSV_PATH)
    timed_query(connection, PARQUET_PATH)

    timings = {"csv": [], "parquet": []}
    expected_rows = None
    for run in range(REPEATS):
        order = (("csv", CSV_PATH), ("parquet", PARQUET_PATH))
        if run % 2:
            order = tuple(reversed(order))
        for label, path in order:
            elapsed, rows = timed_query(connection, path)
            timings[label].append(elapsed)
            if expected_rows is None:
                expected_rows = rows
            elif rows != expected_rows:
                raise RuntimeError(f"result mismatch for {label} on run {run + 1}")

    csv_size = CSV_PATH.stat().st_size
    parquet_size = PARQUET_PATH.stat().st_size
    result = {
        "actor": "Codex",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "environment": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": sys.version.split()[0],
            "duckdb": duckdb.__version__,
            "cpu_count": os.cpu_count(),
            "duckdb_threads": 4,
        },
        "dataset": {
            "rows": ROW_COUNT,
            "columns": 6,
            "sort_order": ["event_date", "event_id"],
            "csv_bytes": csv_size,
            "parquet_bytes": parquet_size,
            "parquet_compression": "zstd",
            "parquet_row_group_size": 100000,
        },
        "query": (
            "July date filter, then exact-decimal SUM(amount) and COUNT(*) "
            "grouped by 10 regions"
        ),
        "measurement": {
            "warmup_runs_per_format": 1,
            "measured_runs_per_format": REPEATS,
            "alternating_order": True,
            "csv_seconds": timings["csv"],
            "parquet_seconds": timings["parquet"],
            "csv_median_seconds": statistics.median(timings["csv"]),
            "parquet_median_seconds": statistics.median(timings["parquet"]),
            "median_speedup_csv_over_parquet": (
                statistics.median(timings["csv"])
                / statistics.median(timings["parquet"])
            ),
            "result_rows": expected_rows,
        },
        "limitations": [
            "Synthetic, date-sorted local dataset rather than a general benchmark.",
            "Warm-cache measurements on one Apple Silicon machine.",
            "CSV and Parquet results depend on schema, compression, sort order, storage, and query shape.",
        ],
    }
    RESULT_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
