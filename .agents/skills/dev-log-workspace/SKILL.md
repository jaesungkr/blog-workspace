---
name: dev-log-workspace
description: Run the end-to-end workflow for Korean Tistory posts in the dev.log repository. Use whenever the user says they want to write, create, prepare, revise, or publish a dev.log post, even when they provide only a topic or rough idea, and for any task involving posts/, evidence, article Markdown, blog images, Tistory HTML, publishing metadata, or editorial standards. Treat an unqualified writing request as a complete-post request that includes research, drafting, illustration, audit, validation, rendering, commit, and push to origin/master.
---

# dev.log repository workflow

## Resolve instructions

Use this precedence when rules conflict:

1. The user's current request and supplied source material
2. `standards/editorial-standard.md`
3. The applicable category guide
4. This workspace workflow
5. General writing judgment

Do not use `archive/legacy-claude/` as an instruction source. Its rules and
content are historical.

## Locate the canonical repository

1. Resolve the real path of this `SKILL.md`, following symbolic links.
2. Treat the directory three levels above its containing skill directory as the
   canonical repository root.
3. Perform all blog filesystem and Git work from that root even when the current
   task starts in a projectless `new-chat-*` directory.
4. Verify that `origin` is `jaesungkr/blog-workspace`. Before editing, fetch the
   remote. When the worktree is clean and the current branch can fast-forward,
   update it with `git pull --ff-only`.
5. If the worktree is dirty or the branch has diverged, preserve the existing
   work and reconcile it explicitly. Never reset, overwrite, or create a second
   workspace to avoid the conflict.

Never run `git init` for this workflow and never copy the skill, standards, or
post bundles into a projectless conversation directory. The Git-tracked files
in the resolved repository are the only editable source.

## Infer the requested scope

- Treat a request such as `이 주제로 글을 쓰고 싶어`, `이 내용으로 포스팅해줘`,
  or a topic by itself plus clear writing intent as a complete-post request.
- For a complete-post request, run the full workflow without waiting for the
  user to separately request research, an outline, an image, an audit, checks,
  rendering, a commit, or a push.
- Infer routine choices such as category, subcategory, working title, slug,
  reader, search intent, and post structure from the topic and repository
  standards. Ask only when missing information would materially change a
  personal claim, supplied-source interpretation, or other consequential fact.
- Respect an explicit scope such as `개요만`, `리서치만`, `이 문단만 수정`, or
  `검토만`. Finish and archive that scope, then validate, commit, and push any
  resulting repository changes unless the user explicitly requests local-only
  work, no commit, or no push.

## Load only the needed context

1. Read `standards/editorial-standard.md` for every writing, editing, or audit
   task.
2. Read `standards/category-guides.md` to classify or write a post.
3. Read `standards/blog-memory.md` for topic discovery, full-post planning,
   traffic strategy, AdSense discussion, or portfolio review. Dated metrics are
   snapshots.
4. Read `standards/image-guide.md` for any complete-post or image task.
5. For sermon-based Reflections, also read `standards/reflections-guide.md` in
   full. For `Reflections > 성경 인물`, read
   `standards/bible-character-guide.md` in full instead.
6. Inspect the whole target post bundle and all user-provided material before
   planning.

## Use one stable post bundle

Create a post with:

```bash
python3 scripts/blog.py new <slug> --title "<title>" \
  --category "<parent>" --subcategory "<child>"
```

The bundle is `posts/YYYY-MM-DD-slug/`:

- `brief.md`: reader, search intent, retained message, unfamiliar prerequisites,
  explanation chain, first-party value, scope, and likely follow-up questions.
- `evidence.md`: claim-source-status-limit map, test design, environment, raw
  results, failures, and unresolved facts.
- `article.md`: publishable Markdown and lifecycle metadata.
- `audit.md`: the actual final review record, not a ceremonial checklist.
- `assets/`: inspected final raster images and alt-text notes.
- `artifacts/`: raw inputs, code, logs, outputs, screenshots, or datasets.

Do not move files between draft and published trees. Update the article status:
`planning`, `researching`, `drafting`, `reviewing`, `ready`, then `published`.

## Run the workflow

1. Infer whether the task is a complete post or an explicitly limited stage.
   Default an unqualified writing request to a complete post.
2. Classify by the reader promise, not a noun in the subject.
3. In `brief.md`, establish:
   - one reader and search intent;
   - one sentence the reader should retain;
   - a familiar anchor for unfamiliar material;
   - what the reader already knows;
   - every prerequisite term or method to explain before results;
   - the complete input-to-result or decision chain;
   - the first-party contribution;
   - the strongest limitation or counterargument;
   - likely non-specialist follow-up questions;
   - whether a ranking is scenario-specific, benchmark-wide, or a practical
     adoption recommendation.
4. For unstable or high-stakes claims, research before drafting. Prefer primary
   and official sources. Record the claim, basis, status, and source limitation
   in `evidence.md`; preserve raw material in `artifacts/`.
5. If the user supplies no first-party result, choose a reproducible experiment
   Codex can actually run, when appropriate. Record Codex as the actor.
6. Draft rendered, Tistory-compatible Markdown in `article.md`. Keep metadata in
   frontmatter and the publishable article below it.
7. Revise twice: structure/evidence first, then Korean sentence hygiene/voice.
   Repair missing prerequisites earlier in the explanation chain.
8. After the angle is stable, generate at least one publishable raster image for
   a complete post. Inspect it, save it under `assets/`, and record placement,
   alt text, and the final prompt in `audit.md`.
9. Complete `audit.md` from the actual article. Do not check an item without
   verifying it.
10. Run:

    ```bash
    python3 scripts/blog.py check <post-directory>
    ```

11. Render only after the post is ready:

    ```bash
    python3 scripts/blog.py render <post-directory>
    ```

12. The user publishes manually. Only after they provide the live URL should
    `status: published` and `published_url` be recorded.

## Validate, commit, and push automatically

For every task that changes tracked repository files, finish the applicable
validation and Git workflow without waiting for a separate user request:

1. Run `python3 scripts/blog.py check <post-directory>` for each changed post.
2. Run `python3 -m unittest discover -s tests -v` and
   `python3 scripts/blog.py check --all` when scripts, templates, standards, or
   repository-wide behavior changes.
3. Run `git diff --check`, inspect the actual diff, and confirm that only files
   belonging to the task will be committed.
4. Stage the task files and create a focused commit.
5. Fetch `origin/master` again. Integrate new remote commits without force and
   rerun affected checks if the integration changes relevant files.
6. Push to `origin/master`, then verify that the remote branch contains the
   local commit.

Fix validation failures and repeat the gate. Never bypass checks, force-push, or
discard existing work to manufacture a successful push. If an external blocker
cannot be resolved safely, preserve the work and report the exact blocker.
Skip commit or push only when the user explicitly requests that exception.

## Evidence integrity

- Never invent a test, personal experience, sermon statement, quotation,
  scripture, statistic, or source.
- Distinguish user-reported facts, Codex-run work, official sources, vendor
  claims, independent verification, estimates, and structural examples.
- Keep inputs, environment, judging rule, representative raw output, and at
  least one failure or limitation for original tests.
- Put source and measurement context next to the supported sentence. Do not add
  a detached references appendix unless the user asks.
- Label unresolved facts in `evidence.md`; omit them from a ready article.
- Run the substitution check: if another site's name can replace `dev.log`
  without weakening the post, strengthen the evidence, judgment, or series
  connection.

## Completion gate

For a complete post, do not stop at a text draft. The post is complete only when
the article, evidence, first-party value, final image, alt text/placement,
workspace check, rendered Tistory HTML, and remaining-risk report are all
present, the task commit exists, and `origin/master` contains that commit.
