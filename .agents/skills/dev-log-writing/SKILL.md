---
name: dev-log-writing
description: Plan, research, draft, and structurally revise Korean Tistory articles in the dev.log repository. Use for topic planning, briefs, evidence maps, source research, original tests, article Markdown, metadata, evidence-backed explanation, or substantive editorial revisions. This stage hands a reviewing candidate to the prose polisher and then the independent article validator; it does not create images or perform Git delivery.
---

# dev.log writing

Produce the evidence-complete written post bundle. Leave the focused
title-heading-flow pass, image creation, final validation, commit, and push to
their owning skills.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory and work there.
2. Read `standards/editorial-standard.md` and
   `standards/category-guides.md` completely.
3. Read `standards/blog-memory.md` for topic discovery, full-post planning,
   traffic strategy, AdSense work, or portfolio review.
4. Read the applicable Reflections guide when needed.
5. Inspect the whole target bundle and all user-supplied material.

## Maintain the bundle

Create a new bundle when necessary:

```bash
python3 scripts/blog.py new <slug> --title "<title>" \
  --category "<parent>" --subcategory "<child>"
```

Use:

- `brief.md` for the reader, search intent, retained message, prerequisites,
  explanation chain, first-party value, limitations, likely questions, and
  infographic decision.
- `evidence.md` for claim, source, status, basis, limitation, test design, raw
  results, failures, and unresolved facts.
- `article.md` for publishable Markdown and lifecycle metadata.
- `audit.md` for observed editorial review findings.
- `artifacts/` for sources, logs, scripts, screenshots, and raw outputs.

Follow `planning -> researching -> drafting -> reviewing`. Do not set `ready`;
the article validator owns that transition.

## Write the post

1. Classify by the promise to the reader, not a noun in the topic.
2. Apply the current category name and any category-specific public-title
   pattern from the applicable guide. Keep series labels and episode order out
   of the title when that guide requires a modifier-led title.
3. Establish in `brief.md`:
   - one reader and search intent;
   - one sentence the reader should retain;
   - a familiar anchor and every prerequisite;
   - for a Bible-character article, the opening's canonical passage, the short
     character-specific bridge that prepares it, and the single textual
     question or tension that will carry into the body;
   - the complete input-to-result or decision chain;
   - a verifiable first-party contribution;
   - the strongest limitation or counterargument;
   - likely non-specialist follow-up questions;
   - the scope of any ranking or recommendation;
   - whether an infographic materially reduces reading effort, the relationship
     it would show, and its exact placement.
4. Research unstable, niche, high-stakes, or source-sensitive claims before
   drafting. Prefer primary and official sources.
5. If appropriate and no first-party result exists, run a reproducible
   experiment Codex can actually perform. Record Codex as the actor.
6. Draft Tistory-compatible Markdown. Keep metadata in frontmatter and the
   publishable article below it. For a new or materially revised
   Bible-character opening, follow the applicable guide's sequence: standard
   greeting -> one or two natural bridge sentences -> compact scripture block
   or passage-grounded scene -> one concrete observation or question -> modest
   article promise. Keep the bridge useful to readers who did not see the
   previous installment, and do not invent scene details to make it vivid.
7. Revise once for structure and evidence, then establish clear baseline Korean,
   consistent 존대어, sentence hygiene, and source-grounded voice. Do not force
   the recent title skeleton, a uniform paragraph size, or a bold takeaway for
   every section; `dev-log-prose-polish` owns the focused final prose pass.
8. Repair missing terms and methods before the results that depend on them.
9. Update the source-level portions of `audit.md` from the actual files, then
   set the article to `reviewing`.

## Evidence integrity

- Never invent a test, personal experience, quotation, statistic, source,
  sermon statement, or scripture.
- Distinguish user reports, Codex-run work, official claims, independent
  verification, estimates, and structural examples.
- Preserve inputs, environment, judging rule, representative raw output, and at
  least one failure or limitation for original tests.
- Attach sources and measurement context near supported claims.
- Omit unresolved claims from a ready candidate.
- Apply the substitution test: if another blog name could replace `dev.log`
  without weakening the post, strengthen the evidence, judgment, or series
  connection.

## Handoff

Return a `reviewing` bundle with no unresolved publishable claim to
`dev-log-prose-polish`, then `dev-log-article-validation`. Report the changed
files, evidence limitations, infographic gate decision, and any issue the prose
polisher or article validator must inspect. Do not create or validate images,
set `ready`, commit, or push.
