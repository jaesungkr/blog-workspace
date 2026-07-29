---
name: dev-log-article-validation
description: Independently validate written dev.log post bundles and rendered Tistory HTML. Use for editorial review, evidence and authorship checks, Korean sentence quality, metadata and lifecycle status, blog.py checks, Tistory rendering, mobile table or code layout, repository regression tests, or ready-state decisions. Validate the article separately from hero and infographic quality and do not perform Git delivery.
---

# dev.log article validation

Act as an independent gate for the written post and its rendered HTML.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory.
2. Read `standards/editorial-standard.md` and
   `standards/category-guides.md` completely.
3. Read every file in the target post bundle that affects publication.
4. Read applicable category-specific guides.
5. Treat existing checkmarks as claims to verify, not evidence.

## Source audit

Read the article from greeting to closing and verify:

- title and headings match search intent, repository syntax, and the applicable
  category-specific title pattern; their sequence follows this post's actual
  event or argument and does not rely on reusable labels alone;
- the opening gives context and the retained conclusion early;
- a new or materially revised Bible-character opening uses a short,
  character-specific bridge before its canonical passage, remains clear to a
  reader who missed earlier installments, and carries one passage-grounded
  observation or question into the body without an abrupt greeting-to-quote
  jump or a complete answer in the setup;
- any scripture used for that opening matches the named translation and
  immediate context, follows the applicable quotation format, and introduces
  no motive, emotion, or missing action that the passage does not state;
- unfamiliar terms, methods, metrics, and labels appear before dependent
  results;
- the full explanation or decision chain is present;
- recommendations state their scope, evidence, exceptions, and limitations;
- claims map to `evidence.md` and primary sources where needed;
- Codex-run work is not presented as the user's personal experience;
- the first-party contribution is verifiable;
- headings pass the subject-substitution test unless a conventional label
  genuinely improves navigation;
- each paragraph seam carries a concrete cause, consequence, contrast, time,
  example, question, or deliberate reset instead of a connector-only bridge;
- 존대어, Korean sentence hygiene, paragraph flow, sentence rhythm, tables,
  emphasis, and closing follow the editorial standard;
- prose polishing did not change numbers, sources, code, tables, test
  authorship, uncertainty, or limitations and did not invent human signals;
- unresolved facts, TODOs, invented details, and unsupported certainty are
  absent;
- image decisions, validator results, placement, alt text, and remaining risks
  are honestly recorded in `audit.md`.

Report `revision_required` with exact evidence when a defect exists. Return
evidence, method, or explanation-structure defects to the writing stage and
title, heading, opening-bridge flow, rhythm, or empty-prose defects to the
prose-polishing stage. Return an unsupported opening scene, quotation, or
textual question to the writing stage. Rerun prose polish after any material
writing revision, then rerun the full affected audit.

## Automated and rendered validation

For each changed post run:

```bash
python3 scripts/blog.py check <post-directory>
python3 scripts/blog.py render <post-directory>
```

Inspect the actual rendered Tistory HTML at a natural reading width. Verify
heading rhythm, paragraphs, table wrapping, code scrolling, links, and intended
manual image positions.

When scripts, templates, standards, or skills change, also run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/blog.py check --all
```

When a skill changes, run the skill-creator `quick_validate.py` against every
affected skill and confirm `agents/openai.yaml` still matches its purpose.

## Ready decision

Set `status: ready` only when:

- the article source and rendered HTML pass;
- `dev-log-hero-validation` records `pass`;
- `dev-log-infographic-validation` records `pass` or `not_applicable`;
- the audit contains observed review evidence and no known material defect.

Otherwise keep `reviewing`. Record each finding as
`problem -> revision -> re-verification`.

## Handoff

Return the commands, results, rendered artifact, remaining risks, and stage
result (`pass` or `revision_required`) to `dev-log-workspace`. Do not create
images, commit, or push.
