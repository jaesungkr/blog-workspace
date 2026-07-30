---
name: dev-log-workspace
description: Orchestrate the complete Korean Tistory workflow in the dev.log repository by loading separate skills for writing, prose polishing, hero-image creation, supporting-infographic creation, and independent validation of the article, hero, and infographic. Use for any request involving a complete dev.log post, posts/, evidence, article Markdown, natural Korean prose, titles or headings, blog images, Tistory rendering, editorial standards, publishing metadata, or Git delivery. An unqualified post request includes all stages, validation, commit, and push to origin/master.
---

# dev.log workspace orchestrator

Coordinate the repository and stage skills. Do not duplicate their specialist
instructions here.

## Resolve the repository

1. Resolve this file's real path.
2. Treat the directory three levels above this skill directory as the canonical
   repository root.
3. Work only from that repository, even when the task starts in a projectless
   conversation directory.
4. Verify `origin` is `jaesungkr/blog-workspace`, inspect the worktree, and fetch
   `origin/master` before editing. Fast-forward a clean branch when possible.
5. Preserve dirty or diverged work. Never reset, overwrite, initialize another
   repository, or copy the workflow into a projectless directory.

Use this precedence:

1. Current user request and supplied material
2. Repository standards
3. Applicable category guide
4. Stage skill
5. General judgment

Never use `archive/legacy-claude/` as an instruction source.

## Stage skills

Read each selected sibling `SKILL.md` completely immediately before that stage:

| Stage | Skill | Responsibility |
|---|---|---|
| Write | `../dev-log-writing/SKILL.md` | Brief, research, evidence, article, editorial revision |
| Polish prose | `../dev-log-prose-polish/SKILL.md` | Post-specific title, headings, paragraph flow, and sentence rhythm |
| Validate article | `../dev-log-article-validation/SKILL.md` | Source audit, checks, Tistory render, article QA |
| Create hero | `../dev-log-hero-image/SKILL.md` | One iconic, topic-specific hero candidate |
| Validate hero | `../dev-log-hero-validation/SKILL.md` | Campaign-grade quality and subject-recognition gate |
| Create infographic | `../dev-log-infographic/SKILL.md` | Gate, plan, deterministic layout, final raster candidate |
| Validate infographic | `../dev-log-infographic-validation/SKILL.md` | Text, overlap, connector, crop, and mobile-legibility gate |

Stage skills do not commit or push. This orchestrator owns Git delivery.

## Route the request

If the user explicitly asks for a finished responsive HTML page, actual product
screens, GIF-led explanation, semantic figures, or a visually designed Tistory
post, hand the complete request to
`../dev-log-rich-post-workspace/SKILL.md`. Do not run this orchestrator's
mandatory generated-hero sequence for that profile unless the rich-post
orchestrator selects a generated lead.

Treat a topic plus clear writing intent as a complete-post request. Infer routine
choices such as category, slug, reader, search intent, and structure. Ask only
when missing information would materially change a personal claim, supplied
source interpretation, or another consequential fact.

For a complete post, run:

1. `dev-log-writing`
2. `dev-log-prose-polish`
3. `dev-log-article-validation` for a source-level editorial pass
4. `dev-log-hero-image`
5. `dev-log-hero-validation`, looping back to hero creation until it passes
6. `dev-log-infographic` after the explanation structure is stable
7. `dev-log-infographic-validation` when the gate produced an image, looping
   back to infographic creation until it passes
8. `dev-log-article-validation` again for the ready transition and rendered
   Tistory candidate

Rerun `dev-log-prose-polish` before article validation whenever a writing
revision materially changes the title, headings, paragraph order, or prose.

For an explicitly limited request, load only the owning stage and its validator:

| Request | Required stages |
|---|---|
| Outline or research | Writing + article validation |
| Article edit | Writing + prose polish + article validation |
| Title, headings, flow, natural Korean, or AI-like prose | Prose polish + article validation |
| Hero creation or revision | Hero creation + hero validation |
| Supporting infographic | Infographic creation + infographic validation |
| Review or preflight only | Relevant validator; use all three for a complete post |
| Standards, scripts, or skill change | Article validation repository-wide tests plus every affected specialist validator |

Respect `local only`, `no commit`, or `no push`. Otherwise every tracked change
finishes through the Git delivery gate.

## Handoff contract

- Keep one bundle under `posts/YYYY-MM-DD-slug/`.
- Preserve `brief.md`, `evidence.md`, `article.md`, `audit.md`, `assets/`, and
  `artifacts/` as the shared state between stages.
- Keep the article at `reviewing` while any validator reports
  `revision_required`.
- Set `ready` only after article validation passes, the hero validator passes,
  and the infographic validator passes or records `not_applicable`.
- Record every material issue as
  `problem -> revision -> re-verification` in `audit.md`.
- Record representative prose-polishing decisions and confirm that numbers,
  sources, code, tables, test authorship, and limitations remained intact.
- Do not insert local filesystem image links into `article.md`; the user uploads
  images to Tistory manually.
- Only after the user supplies the live URL set `published` and
  `published_url`.

## Git delivery gate

After all required validators pass:

1. Run `git diff --check` and inspect the actual diff and untracked files.
2. Confirm only task files will be committed.
3. Stage exact files and create a focused commit.
4. Fetch `origin/master` again.
5. Integrate remote changes without force and rerun affected validators when
   integration changes relevant files.
6. Push to `origin/master`.
7. Verify the remote contains the local commit and the worktree is clean.

Never bypass failed validation, force-push, discard unrelated changes, or mark a
post complete with a known editorial, factual, visual, mobile, or placement
defect.

## Final user handoff

After validation, rendering, and Git delivery, copy the exact final Tistory HTML
byte-for-byte to the current task's user-facing outputs directory as
`<slug>-tistory-fragment.txt`. Put only raw paste-ready HTML in the file: no
title, Markdown fence, explanation, or instructions. Verify the `.txt` hash
matches the renderer output, then make the `.txt` file the primary final link
and state the Tistory title separately. The user always pastes, previews, and
publishes it.

## Completion

A complete standard post requires a validated article and evidence record, a
validated hero, an infographic decision and validation when applicable,
rendered Tistory HTML, an honest audit and remaining-risk record, a focused
commit, confirmed presence on `origin/master`, and a byte-identical user-facing
`<slug>-tistory-fragment.txt` handoff. A rich-post request is handed to its own
orchestrator and completion contract.
