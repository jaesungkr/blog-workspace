# dev.log workspace guidance

## Mission

This repository is the working archive for the Korean Tistory blog `dev.log`.
The editorial identity is **추측 대신 검증(Tested, not guessed)**. A polished
summary of public sources is not enough: monetized posts need a reproducible
test, artifact, dataset, log, screenshot, observation, or explicit decision
framework that belongs on this blog.

## Start every blog task here

- Use `.agents/skills/dev-log-rich-post-workspace-v2/SKILL.md` as the default
  orchestrator for new complete posts and revisions of v2 posts. This
  repository instruction selects v2 even when the user does not name a skill.
- Continue existing `format: rich-post` bundles with
  `.agents/skills/dev-log-rich-post-workspace/SKILL.md` unless the user asks
  to migrate them. Do not silently convert a v1 bundle to v2.
- For a limited request such as research, prose editing, or image review,
  load only the owning specialist and its applicable validator. Respect an
  explicit request for a plain Markdown artifact.
- The selected orchestrator loads writing, prose-polishing, image creation,
  and validation skills directly. It owns the media manifest, responsive QA,
  publication handoff, and Git delivery; no additional base orchestrator is
  required.
- Treat every Git-tracked `.agents/skills/dev-log-*` directory as the only
  editable copy. For global Codex discovery, link all of them with
  `scripts/link_codex_skill.sh`; do not maintain copied skills under
  `~/.codex/skills/`.
- Treat `standards/` as the editorial source of truth.
- Read `standards/editorial-standard.md` for every writing or editing task.
- Read only the additional category, image, memory, or Reflections guide that
  the selected stage skill routes you to.
- Treat `standards/image-art-direction.md` as the Git-tracked source of truth
  for public-facing blog image quality. A built-in or globally installed image
  skill is an execution dependency, not the canonical blog standard.
- Inspect the complete post bundle and user-provided material before planning.
- Treat an unqualified request to write about a topic as an end-to-end
  complete-post request. Do not stop at research, an outline, or a text draft
  unless the user explicitly limits the scope.
- Do not finish a complete dev.log post in a projectless scratch directory.
  Create or update its bundle in this repository, pass every independent gate
  required by the selected format, render the ready article, commit the
  completed bundle, push it to `origin/master`, and verify the remote commit
  unless the user explicitly requests local-only work or the push is blocked.

## Repository model

- One post lives in `posts/YYYY-MM-DD-slug/`.
- Keep `brief.md`, `evidence.md`, `article.md`, `audit.md`, `assets/`, and
  `artifacts/` together. Do not split drafts and published posts into separate
  trees.
- Track lifecycle in `article.md` frontmatter:
  `planning -> researching -> drafting -> reviewing -> ready -> published`.
- Preserve original test inputs, outputs, screenshots, and logs in
  `artifacts/`. Never present a Codex-run test as the author's personal test.
- Store generated publishable images in `assets/`. A complete post needs at
  least one inspected final image.
- `archive/legacy-claude/` is read-only historical material. Do not treat it as
  verified evidence or a current template.
- `dist/` is disposable Tistory HTML and is not tracked.

## Useful commands

```bash
python3 scripts/blog.py new my-post --title "제목" --category Log --subcategory "개발 · 디지털"
python3 scripts/blog.py check posts/YYYY-MM-DD-my-post
python3 scripts/blog.py check --all
python3 scripts/blog.py render posts/YYYY-MM-DD-my-post
python3 -m unittest discover -s tests -v
```

Use Python's standard library only. When changing scripts, run the full unit
test suite and `python3 scripts/blog.py check --all`.

## Non-negotiables

- Never invent facts, quotations, scripture, sermon claims, first-person
  experience, test results, or sources.
- Research current, medical, financial, legal, product, pricing, benchmark, or
  other unstable claims before drafting. Prefer primary and official sources.
- Keep body prose in consistent Korean honorific style. Titles and headings
  must not end in `~다`.
- Do not reintroduce rigid legacy rules such as a fixed character count,
  uniform paragraph or sentence lengths, a mandatory number or shape of
  headings, a bold-emphasis quota, a mandatory table, or a generic disclaimer.
- For `dev-log-rich-post-workspace-v2`, follow its
  author-approved direct-publication workflow. After the author approves the
  specific article and says to publish (for example, `올리자`), Codex uses the
  Codex in-app browser to attach images, enter the approved article, preview,
  publish, and verify the live page. Drafting alone is not publication approval.
  Other workflows stop at paste-ready HTML unless the user instructs otherwise.
- Retain a user-facing `<slug>-tistory-fragment.txt` file containing only the
  exact publication HTML. For direct v2 publication, the live article URL is
  the primary final link and the exact submitted TXT is the backup. Other
  workflows make the TXT primary.
- A Git push to this workspace is part of the archive workflow and is not a
  Tistory publication. Keep `status: ready` until the live Tistory page is
  verified; direct v2 publication obtains that URL from the successful browser
  publication instead of requiring the author to send it.
- Do not mark a post `ready` or `published` while TODOs, unresolved evidence,
  missing first-party value, or a missing final image remain.

## Definition of done

A complete-post request is done only when the prose-polishing stage has removed
reusable title, heading, and paragraph-flow templates without changing the
evidence, the article validator passes, strong claims have evidence and
limitations, first-party value is visible, paste-ready HTML is rendered, the
task is committed, `origin/master` contains that commit, and remaining
uncertainty is reported plainly. A standard post also requires a validated hero
and an infographic pass or `not_applicable`. A `rich-post` instead requires a
validated lead visual, resolved media manifest, full preview and Tistory
fragment, two verified CDN fetches, and separate creator and independent
responsive inspection at the required desktop and mobile profiles; a generated
lead still requires the hero validator.
