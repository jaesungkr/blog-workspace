# Preserved benchmark failure

- Actor: Codex
- Environment: macOS arm64, Python 3.9, DuckDB 1.4.5
- Input: 5,000,000 synthetic rows exported from one DuckDB table to CSV and
  Zstandard-compressed Parquet
- Query: July date filter, `SUM(amount)`, and `COUNT(*)` grouped by region
- Expected: identical result rows from the two file formats
- Actual: the equality assertion failed on the first measured Parquet run

Representative output:

```text
CSV     ('region_00', 20476966.870000023, 41097)  revenue type: DOUBLE
Parquet ('region_00', Decimal('20476966.87'), 41097)  revenue type: DECIMAL(38,2)
RuntimeError: result mismatch for parquet on run 1
```

Cause: CSV has no embedded schema, so automatic detection read `amount` as
`DOUBLE`. Parquet retained the source `DECIMAL(12,2)` schema. The benchmark
query was corrected to cast `amount` to `DECIMAL(12,2)` before aggregation.
This failure is retained because it demonstrates why production CSV reads
should pin important types instead of assuming format-equivalent schemas.
