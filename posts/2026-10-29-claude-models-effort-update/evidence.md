# Evidence / claim map

Checked: 2026-10-29 UTC
Research packet: research-facts.md
Draft: article-draft.md

## Claims

| ID | Claim | Primary source | Scope / treatment |
| --- | --- | --- | --- |
| C1 | Featured current models are Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1 | https://platform.claude.com/docs/en/models/overview | Confirmed live; model choice examples are editorial applications of official roles, not measured results. |
| C2 | Haiku fastest/repetitive tasks; Sonnet speed/intelligence; Opus complex knowledge/coding; Fable demanding reasoning | https://platform.claude.com/docs/en/models/overview | Table simplifies official positioning. Opus recommendation distinguished from author's speed-oriented Sonnet option. |
| C3 | All four latest models support low/medium/high/xhigh/max | https://platform.claude.com/docs/en/build-with-claude/effort | Applies only to named current models, not all older versions. |
| C4 | Effort influences work/verification as well as thinking | https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code | Code-specific file/test example; not guaranteed outcome. |
| C5 | Model vs effort diagnostic | https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code | Framed as a starting point, not deterministic rule; first ensure test request/environment permits work. |
| C6 | App model selector next to send; Effort menu; Default label; next-response change | https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings | Official prose; screenshots must not be described as actual app control if only documentation. |
| C7 | Latest four models cannot disable Thinking in Claude app | https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings | Explicit app scope; API exceptions not generalized. |
| C8 | Code Opus/Sonnet/Haiku 5.5 defaults medium, /model and /effort controls | https://code.claude.com/docs/en/model-config | User overrides not described as default. |
| C9 | Sonnet 5.5 API default high; Opus/Haiku 5.5 API medium | https://platform.claude.com/docs/en/build-with-claude/effort | API invocation without explicit effort only. |
| C10 | Max can overthink/diminishing returns; effort calibrated per model | https://code.claude.com/docs/en/model-config#choose-an-effort-level | No unsupported multiplier or identical compute assumption. |
| C11 | Fable requires usage credits on Pro | https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan | Avoid claiming all paid subscriptions include same access or unlimited use. |

| C12 | Opus 5.5 same workout-app request, four reported Effort times and Low/Max outputs | https://claude.dev/blog/spending-your-effort/ | Published example: Low 1.5 min, Medium 4, High 11, Max 67; xhigh not reported; screenshots are official demos, not our tests. |

## Sources and observations

Writer directly opened and inspected model overview, effort API docs, Help app settings, Code model config, and official model/effort selection article. Research agent independently verified sources and old-article browser auditor inspected original. Latest source packet records Fable plan specifics.

## Old content removed

Browser audit reports old post 2026-06-18: Haiku4.5/Sonnet4.6/Opus4.8 and obsolete Fable access situation, inconsistent benchmark versions/arithmetic, always-high default, low=no-thinking implication, max 5–10x blanket multiplier, MAX_THINKING_TOKENS and thinking-off general advice. Draft removes rather than patches these sections.

## Independent review

Pending research_claude_effort_refresh review of article-draft.md. Do not mark source_review_done or publish before findings are addressed.

## Media evidence

Requested assets: claude-models-official and claude-effort-official. Actual capture agent is collecting source URL, inspection, dimensions/hash, provenance. Exact manifest pending capture results; do not invent tistory_url.

### Independent source review — 2026-10-29

Research reviewer read the complete final draft and visually inspected both screenshots. Body fact review: **PASS**. SHA-256: `dff805666d921d6b6c31a75b5ea49dfccb90f00315b3cca20cb634c7f9045a6c`. Models, Effort support, app Thinking scope, Code/API defaults, Fable Pro credits and conditional model-versus-effort guidance match the verified official sources. One media-caption correction required: explicitly label the model screenshot **Claude API 기준**, because it includes API prices and default effort. Full record: `source-review.json`. No publication performed.

Caption fix verified at 2026-10-29T06:15:40Z. Final independent source review: **PASS**, with unchanged draft hash.

## 2026-10-29 follow-up: observed Effort example

C12 — Source: https://claude.dev/blog/spending-your-effort/ (2026-09-25, Thariq Shihipar). Same Opus 5.5, underspecified personal fitness and workout tracker app. Published labels: low 1.5 min / medium 4 min / high 11 min / max 67 min. Low log and simple graph; higher effort adds details; max heat chart. One example, not an average-speed benchmark; xhigh not reported for this example. No monetary-cost claims added, no equal-runtime/harness assumption beyond published source. Writer directly inspected source lines 64–70. New subsection about 144 Korean space-separated words. Prior source freeze invalidated by addition; independent review pending.

### Effort example update independent review — 2026-10-29 07:06 UTC

Body PASS. Same Opus 5.5, task and 4 reported time values verified against https://claude.dev/blog/spending-your-effort/ (2026-09-25). Original does not disclose xhigh for this example. Draft explicitly avoids average-speed generalization. Low and Max feature descriptions match the original, and Medium/High features are not invented. Detailed research: `effort-comparison-research.md`. Current reviewed hash: `76156db95dbf8b6eb29c2da31e2dd2d18b771266630bce556422d5ca40ece9c2`. New example media, if added, requires final provenance/caption inspection.

Final Effort enhancement source/media review PASS — 2026-10-29T07:11:30Z. Independently viewed Low and Max screenshots: labels/times match, Low log/chart visible, Max Progress graph/menu visible. Heatmap is correctly attributed to original article, not claimed visible in this capture. Final reviewed article SHA-256: `fc99617f9eab1ffcc82385208d616d3cf9fdb7fd8572ac5e37fddfa295f050d8`.
