# Qwen3.8-Max vendor-table recalculation

- Source: Qwen3.8-Max: A New Bar for Coding and Cowork
- Source SHA-256: `e49ec2e824d0e2b447080e767f50e86735d59d0344bccf46e770fb2b5da7867a`
- Compared models: Opus4.8, Fable5, GPT5.6 Sol (max), Qwen3.7-Max, Qwen3.8-Max
- Single-score rows: 30
- Rank counts: {'2': 11, '3': 7, '4': 5, '1': 7}
- Rows beating Qwen3.7-Max: 30
- Rows tied for or holding first place: 7

Composite cells containing two scores were excluded instead of choosing one metric after the fact.
All scores come from the vendor-authored Qwen release table; this is a structural recalculation, not an independent benchmark rerun.

| Section | Benchmark | Qwen3.8 | Qwen3.7 | Rank | Row leader |
|---|---|---:|---:|---:|---|
| Coding Agent | Terminal Bench 2.1 | 86.6 | 74.5 | 2/5 | GPT5.6 Sol (max) |
| Coding Agent | SWE-bench Pro | 67.7 | 60.6 | 3/5 | Fable5 |
| Coding Agent | DeepSWE 1.1 | 56.6 | 21.6 | 4/5 | GPT5.6 Sol (max) |
| Coding Agent | NL2Repo-Bench | 55.9 | 47.2 | 2/3 | Opus4.8 |
| Coding Agent | FrontierSWE | 73.5 | 40.7 | 2/4 | Fable5 |
| Coding Agent | MLS-Bench-Lite | 41 | 31.7 | 4/5 | Fable5 |
| Coding Agent | PaperBench | 93 | 64.8 | 1/5 | Qwen3.8-Max |
| Coding Agent | AndroidBench | 75.1 | 56.5 | 2/5 | Fable5 |
| Coding Agent | QwenSWEBench | 80.7 | 63.4 | 3/5 | Fable5 |
| Coding Agent | QwenQoderBench | 58.4 | 36.8 | 3/5 | Fable5 |
| Coding Agent | QwenReactBench | 1724 | 1538 | 2/5 | Fable5 |
| Coding Agent | QwenSVGBench | 1713 | 1499 | 2/5 | GPT5.6 Sol (max) |
| General Agent | CoWorkBench | 74.8 | 64.6 | 2/5 | Fable5 |
| General Agent | WorkSpaceBench | 67.7 | 61.4 | 2/5 | Fable5 |
| General Agent | JobBench | 53.4 | 31.3 | 2/5 | Fable5 |
| General Agent | SkillsBench | 70.2 | 61.2 | 3/5 | GPT5.6 Sol (max) |
| General Agent | Automation-Bench (Pass@1) | 27.3 | 14.2 | 3/5 | GPT5.6 Sol (max) |
| General Agent | Toolathlon Verified (Pass@1) | 72.5 | 49.7 | 4/5 | Fable5 |
| General Agent | WideSearch | 81.9 | 75.2 | 1/4 | Qwen3.8-Max |
| General Agent | HLE w/ tools | 56.2 | 53.5 | 4/5 | Fable5 |
| General Capabilities | GPQA Diamond | 92.6 | 92.4 | 2/5 | GPT5.6 Sol (max) |
| General Capabilities | HLE | 43.6 | 41.4 | 4/5 | Fable5 |
| General Capabilities | IFBench | 82.8 | 79.1 | 1/5 | Qwen3.8-Max |
| General Capabilities | $OneMillion-Bench (expert score) | 52.5 | 44.4 | 3/5 | Fable5 |
| General Capabilities | HealthBench | 60.2 | 54.5 | 1/4 | Qwen3.8-Max |
| General Capabilities | PLawBench | 73.2 | 58.9 | 1/5 | Qwen3.8-Max |
| General Capabilities | PRBench-Legal | 57.6 | 48.5 | 1/5 | Fable5 / GPT5.6 Sol (max) / Qwen3.8-Max |
| General Capabilities | PRBench-Finance | 58.3 | 46.8 | 1/5 | Qwen3.8-Max |
| General Capabilities | MRCR v2 256K (8-needle) | 92.9 | 86.7 | 2/4 | GPT5.6 Sol (max) |
| General Capabilities | LongBench v2 | 66.3 | 65.3 | 3/4 | Opus4.8 |
