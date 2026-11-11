# Evidence — 2026-11-11
## E1 공식 사양
https://developers.openai.com/api/docs/models/gpt-6-astra
Astra input $10/output $50 per 1M, context1050000/output128000. >272K input: whole request input/cache2x output1.5x.
https://platform.claude.com/docs/en/models/fable-5-2/overview
Fable input8/output40, context1M/output128000; API default high/apps medium.
https://www.anthropic.com/claude-fable-and-mythos-5-2
Released Nov9; Mythos verified orgs. Vendor table FrontierCode2.0 Fable49.1 xhigh/Astra42.8; FrontierSWE v2 69.9/65.5; AutomationBench51.4/41.4. Highest effort unless marked.
https://openai.com/index/gpt-6-astra/ Astra most demanding model; latest Sol is distinct.
## E2 independent AA v5.0.1
https://artificialanalysis.ai/models/gpt-6-astra 57/$6.24/23.0min max
https://artificialanalysis.ai/models/claude-fable-5-2-medium 56/$3.80/7.9min
https://artificialanalysis.ai/models/claude-fable-5-2-high 62/$9.08/17.5min
https://artificialanalysis.ai/models/claude-fable-5-2 65/$26.54/44.4min
All Fable Default Fallback. Weighted average benchmark task cost and duration; not normal chat bill. Ratios26.54/6.24=4.2532. Reader example100K input/10K output Fable1.2 Astra1.5 dollars, no cache/tools, billable reasoning included.
## E3 Arena
https://arena.ai/leaderboard/code/webdev Chrome confirmed Nov11: Fable xHigh1/1836±22/994; Opus Max2/1814±12/4187; Astra Max5/1764±9/8425.
https://arena.ai/leaderboard/chat/text displayNov9: Fable5.2 absent; AstraMax41/1474±6/18315.
https://arena.ai/leaderboard/agent displayNov8: Fable5.2 absent; AstraMax5/14.24%±2.03%/15520sessions.
https://arena.ai/blog/agent-arena-methodology net improvement causal estimate relative baseline not success rate.
Cloud Chrome tab1 direct screenshot viewed; file export blocked EROFS workspace/tmp. No screenshot file delivered.
## E4 plans
https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
Pro launch window ends11/16 23:59PT, normally usage credits. API distinct from subscription.

| ID | 본문 주장 | 출처·조건 | 한계 |
|---|---|---|---|
| C-comparison | Fable5.2와 Astra 비교 | E1~E4 | 대표이미지는 모델 상징, 성능 증거 아님 |
| C-benchmark | 공식 코딩·업무 표 | E1 Anthropic 동일표 | vendor reported |
