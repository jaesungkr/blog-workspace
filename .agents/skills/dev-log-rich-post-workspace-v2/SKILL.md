---
name: dev-log-rich-post-workspace-v2
description: Create complete dev.log Tistory rich posts with a staged v2 workflow that freezes the evidence-backed source before remote media work, uses conditional capture and viewport gates, performs one independent light/dark final-page approval, and produces paste-ready responsive HTML with Git delivery. Use only when the user explicitly invokes v2 or asks for the faster source-freeze rich-post workflow; use the original dev-log-rich-post-workspace for existing v1 bundles or when v1 is explicitly requested.
---

# dev.log rich-post workspace v2

Produce a reader-first Tistory fragment and full preview without repeating the
same editorial and browser approval. Keep the original rich-post skill and its
artifacts untouched.

## Protect the repository

1. Resolve this skill's real path and use the directory three levels above it
   as the repository root.
2. Read the repository `AGENTS.md`, inspect the worktree, verify the expected
   origin, and fetch `origin/master` before editing.
3. Preserve dirty or diverged work. Never reset, overwrite, initialize another
   repository, or edit `.agents/skills/dev-log-rich-post-workspace/` as part of
   a v2 task.
4. Use `format: rich-post-v2`, `media.json` version 2, `workflow-v2.json`, and
   `artifacts/qa-v2/`. Never write v2 evidence under the v1 QA paths.

This skill is explicit-invocation only so it can coexist with v1. Do not
silently migrate an existing `format: rich-post` bundle.

## Load only the current stage

Read `references/workflow-v2.md` for every v2 task. Then load just in time:

- before source approval: `references/source-freeze-v2.md`;
- before final media or Tistory URL work: `references/media-release-v2.md`;
- immediately before browser QA: `references/final-page-qa-v2.md`;
- immediately before ready, Git, and handoff: `references/delivery-v2.md`.

Use the repository writing, prose-polishing, and article-validation skills for
their owning stages. Run article validation as a source-level gate before the
freeze; do not rerun its editorial interrogation after browser QA. Use the
separate hero and infographic creator/validator skills only when routed.

## Route the work

Record the decision in `workflow-v2.json` before research.

- Choose `standard-rich` for a source-based article with static media.
- Choose `evidence-rich` for direct product use, experiments, GIFs, or a
  capture-led promise.
- Turn on generated hero, infographic, 390px, 768px, GIF, and second remote
  fetch only when the corresponding risk exists.
- Never claim hands-on work when the required app, account, device, version,
  or safe environment is unavailable. Narrow the promise instead.

Create a new bundle with:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/init_bundle_v2.py \
  <slug> --title "<title>" --category "<category>" \
  --subcategory "<subcategory>" --profile standard-rich
```

Inspect and replace every template placeholder. Do not treat an empty template
as evidence.

## Build and freeze the source

1. Plan one primary reader, the retained message, easiest start, required
   claims, honest test boundary, media role, and conditional gates.
2. Research unstable, niche, source-sensitive, or high-stakes claims before
   drafting. Prefer primary and official sources.
3. Capture raw evidence during research only when the route requires it. Keep
   secrets out of raw files; recapture instead of blurring them later.
4. Draft around evidence with `plain identity -> ordinary use -> easiest start
   -> evidence boundary`. Keep comparison rules, prerequisites, exact entry
   points, and limitations explicit.
5. Run one structural revision and one prose-polish stage.
6. Hand the still-`reviewing` bundle to an independent source reviewer. Return
   substantive defects to writing and surface defects to prose polish until it
   passes.
7. Record the freeze:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/record_source_pass_v2.py \
  posts/YYYY-MM-DD-slug --by "<actual independent source reviewer>"
```

Keep lifecycle `reviewing`. Treat the record as the internal source freeze.
Any material source edit invalidates it and all later page evidence.

## Finalize media and preflight locally

Complete `media.json` with local publication files, provenance, rights,
dimensions, hashes, alt text, captions, placement, and claim IDs. Create
`capture-plan.md` only for first-party, simulated, or GIF media.

Run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/check_rich_post_v2.py \
  posts/YYYY-MM-DD-slug
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/render_rich_post_v2.py \
  posts/YYYY-MM-DD-slug --output-dir posts/YYYY-MM-DD-slug/artifacts/qa-v2/preflight
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/render_rich_post_v2.py \
  posts/YYYY-MM-DD-slug --preview-theme dark \
  --output-dir posts/YYYY-MM-DD-slug/artifacts/qa-v2/preflight-dark
```

The creator inspects the local page as a preflight, not as a manual approval.
Fix layout and media defects now. If text must change, return to the source
stage and write a new source pass.

## Bind remote media

Print and bind the deterministic queue with `tistory_media_map_v2.py`. Receive
URLs from the user or upload to a confirmed unpublished draft only with
explicit authority. Never click publish.

Record one remote baseline with `remote_media_v2.py record`. Run
`remote_media_v2.py verify` only when the route requires a second fetch. A
missing session, mapping, authority, or successful fetch leaves the article at
`reviewing`.

## Run one final page gate

Prepare canonical remote light and dark candidates:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/prepare_final_qa_v2.py \
  posts/YYYY-MM-DD-slug
```

One independent reviewer captures both themes with
`capture_rich_qa_v2.py --mode final-light` and `--mode final-dark`. Use the
required 1280 and 360 profiles. Add the conditional flags selected in
`workflow-v2.json` to both commands.

Inspect the entire exact page and fill only the human fields in
`artifacts/qa-v2/final-measurements.json`. Save focused component evidence only
for an observed failure, a new component, or a routed risk. Do not create a
separate screenshot for every repeated table or list.

Persist the only manual page approval with `record_final_page_v2.py`. Do not
reopen the editorial gate here. A genuine source defect returns the bundle to
writing and invalidates the current candidate.

## Decide ready and deliver

Read `references/delivery-v2.md`, then run `finalize_rich_post_v2.py` with the
current task's user-facing output path. Add `--require-second-fetch` when
routed. The finalizer must restore `reviewing` on failure.

Run repository-wide tests only when skills, scripts, templates, CSS, or
standards changed. Inspect the exact diff, stage only task files, commit, fetch
and integrate without force, rerun affected checks, push to `origin/master`,
and verify the remote commit.

Make the byte-identical `<slug>-tistory-fragment.txt` the primary handoff and
state the Tistory title separately. The user always pastes, previews, toggles
the real hELLO theme, and publishes. After the user supplies the live URL,
validate desktop and mobile before setting `published`.

## Completion

A v2 rich post is complete only when the source pass, validated local media,
resolved remote URLs, required remote observation, exact remote light/dark
candidate, one independent final-page record, strict final render, focused Git
delivery, verified remote commit, and byte-identical paste file pass. Never
accept an unresolved claim, unsupported hands-on statement, local media path,
placeholder, duplicate H1, unreadable mobile evidence, hidden table content,
stale gate, or known visual defect.
