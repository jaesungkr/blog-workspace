---
name: dev-log-writing
description: Plan, research, draft, and revise Korean Tistory articles in the dev.log repository. Use for topic planning, briefs, evidence maps, source research, original tests, article Markdown, metadata, editorial revisions, or any request focused on the written content of a dev.log post. This stage hands a reviewing candidate to the independent article validator and does not create images or perform Git delivery.
---

# dev.log writing

Produce the written post bundle. Leave image creation, final validation, commit,
and push to their owning skills.

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
2. Establish in `brief.md`:
   - one reader and search intent;
   - one sentence the reader should retain;
   - a familiar anchor and every prerequisite;
   - the complete input-to-result or decision chain;
   - a verifiable first-party contribution;
   - the strongest limitation or counterargument;
   - likely non-specialist follow-up questions;
   - the scope of any ranking or recommendation;
   - whether an infographic materially reduces reading effort, the relationship
     it would show, and its exact placement.
3. Research unstable, niche, high-stakes, or source-sensitive claims before
   drafting. Prefer primary and official sources.
4. If appropriate and no first-party result exists, run a reproducible
   experiment Codex can actually perform. Record Codex as the actor.
5. Draft Tistory-compatible Markdown. Keep metadata in frontmatter and the
   publishable article below it.
6. Revise once for structure and evidence, then again for natural Korean,
   consistent 존대어, sentence hygiene, and voice.
7. Repair missing terms and methods before the results that depend on them.
8. Update the source-level portions of `audit.md` from the actual files, then
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

Return a `reviewing` bundle with no unresolved publishable claim. Report the
changed files, evidence limitations, infographic gate decision, and any issue
the article validator must inspect. Do not create or validate images, set
`ready`, commit, or push.
