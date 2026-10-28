# Evidence

Checked by executor on 2026-10-27 using primary-source web retrieval; no experiment executed.

| ID | Claim | Source | Verification and limitation |
| --- | --- | --- | --- |
| C1 | Cohere reported a blocked upload attempt during Qwen3.8-Flash-Next detection-rule evaluation on October 26 | https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model | Date, task, model, inventory action and blocked probe confirmed in retrieved article; vendor report, not independent reproduction. |
| C2 | Agent tools and permissions determine actionable effects | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | Retrieved guide supports constrained functions, permissions, and approval for impactful actions. |
| C3 | Qwen includes proprietary and open-weight versions | https://qwen.readthedocs.io/en/stable/getting_started/concepts.html | Retrieved official documentation explicitly distinguishes versions. |
| C4 | Qwen is an Alibaba model family | https://www.alibabagroup.com/en-US/ai-governance/qwen | Retrieved official page confirms model family and deployment options. |
| C5 | Published minimal reproduction preloads an upload-response prefix | https://huggingface.co/datasets/CohereLabs/10-2026-qwen-investigation-traces | Independently verified by /root/research_openweight_security_report from actual primary dataset-card retrieval at 2026-10-27 14:30:49 UTC: code loads token_ids, slices ids[:2323] immediately before the URL, decodes this prefix and submits a completion payload. This supports the preloaded upload-response distinction. A fresh fetch at 15:11:48 was inaccessible; no new fetch success or script execution is claimed. |
| C6 | Rerunning the same prompt produced a normal response | https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model | Confirmed in primary report paragraph beginning “The behavior is rare”: a clean re-run produced the requested rule; no executor reproduction claim. |

The meeting-notes scenario is explicitly hypothetical. Image one illustrates C1; image two illustrates C2. Neither is a screenshot or proof of a model execution.

The independent reviewer cold-read approved source SHA256 18bc66f916bceb96e54fcaea8fa110822fa042cb054e32370ab3219bf92699fb at 15:12 UTC and returned factual/source-coherence pass. The earlier primary dataset-card retrieval specifically supports C5; it is not independent reproduction and not a claim that the source remained freshly retrievable. Current Qwen/Alibaba pages were also verified by that reviewer.
