# dev.log workspace guidance

## Mission

This repository is the working archive for the Korean Tistory blog `dev.log`.
The editorial identity is **추측 대신 검증(Tested, not guessed)**. A polished
summary of public sources is not enough: monetized posts need a reproducible
test, artifact, dataset, log, screenshot, observation, or explicit decision
framework that belongs on this blog.

## Start every blog task here

- Use the repository skill at `.agents/skills/dev-log-workspace/SKILL.md`.
- Treat that Git-tracked skill as the only editable copy. For global Codex
  discovery, link it with `scripts/link_codex_skill.sh`; do not maintain a
  separate copied skill under `~/.codex/skills/`.
- Treat `standards/` as the editorial source of truth.
- Read `standards/editorial-standard.md` for every writing or editing task.
- Read only the additional category, image, memory, or Reflections guide that
  the repository skill routes you to.
- Inspect the complete post bundle and user-provided material before planning.
- Do not finish a complete dev.log post in a projectless scratch directory.
  Create or update its bundle in this repository, run the checker, commit the
  completed bundle, and push it to `origin/master` unless the user explicitly
  requests local-only work or the push is blocked.

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
- Do not reintroduce rigid legacy rules such as a fixed character count, a
  mandatory number of headings, a mandatory table, or a generic disclaimer.
- Do not auto-publish. Rendering stops at paste-ready HTML; the user publishes
  in Tistory and supplies the final URL.
- A Git push to this workspace is part of the archive workflow and is not a
  Tistory publication. Keep `status: ready` until the user supplies the live
  Tistory URL.
- Do not mark a post `ready` or `published` while TODOs, unresolved evidence,
  missing first-party value, or a missing final image remain.

## Definition of done

A complete-post request is done only when the article has passed the applicable
editorial audit, strong claims have evidence and limitations, first-party value
is visible, the final image exists and has placement/alt text recorded, the
workspace checker passes, and remaining uncertainty is reported plainly.
