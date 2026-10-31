---
name: dev-log-rich-post-workspace-v2
description: Create and publish complete dev.log Tistory rich posts after the author approves the specific article and asks to publish. Freeze an evidence-backed Korean source, validate media and responsive light/dark layouts before publication, then use the Codex in-app browser to attach native Tistory images, enter the article, publish, and record the resulting URL with Git delivery. Post-publication visual checks belong to the author unless requested. Use when explicitly invoked, requested as a source-freeze workflow, or selected by the repository AGENTS.md; use the original rich-post skill for existing v1 bundles.
---

# dev.log rich-post workspace v2

Produce a reader-first article and publish it through the Codex in-app browser
after the author approves that article and asks to publish. Keep the original
rich-post skill and its artifacts untouched.

After publication, confirm only the successful publish result and article URL.
The author handles post-publication checks. Do not run additional desktop/mobile,
image, layout, theme, or title/cover-contrast checks or automatic visual repairs
unless the author explicitly requests them. Keep the pre-publication gates.

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

This is the repository's default complete-post workflow when selected by
`AGENTS.md`. Outside that repository, require explicit invocation or a request
for this workflow; keep the global implicit-invocation policy unchanged. Do
not silently migrate an existing `format: rich-post` bundle.

## Preserve the canonical article format

Always render publication HTML with this skill's `render_rich_post_v2.py` and
finalizer. Do not substitute a custom `build_preview.py`, hand-written HTML,
or another Markdown converter, even if the prose matches. The canonical
`.devlog-rich` article, section spacing/backgrounds, automatic TOC (two or more
major sections), table wrappers, media wrappers and theme variables are part
of the approved blog format. Keep preview and submitted fragment tied to the
actual renderer/CSS hashes. A source revision called “v2” is not proof that
this workflow was used.

Use Markdown `>` for copyable request/input examples and attributed quotations;
all such blockquotes receive the same neutral light/dark box treatment. This
is presentation, not automatic classification as a command: keep context and
attribution in the prose, never add a “prompt” label to quotations. Ordinary
explanation stays in paragraphs; executable code stays in fenced code blocks.
Do not copy the default box CSS into new `assets/post.css` files. Existing
article overrides remain historical, and scoped exceptions are allowed only
for an observed issue. Check the canonical-template and prompt-box gate in
`references/final-page-qa-v2.md` before publishing. Workflow changes do not
republish old articles or authorize rewriting approved prose to satisfy lint.

## Direct specialist dependencies

Load these stages directly; no base workspace orchestrator is required.

| Stage | Skill |
|---|---|
| Write | [dev-log-writing](../dev-log-writing/SKILL.md) |
| Polish prose | [dev-log-prose-polish](../dev-log-prose-polish/SKILL.md) |
| Validate source | [dev-log-article-validation](../dev-log-article-validation/SKILL.md) |
| Create a routed hero | [dev-log-hero-image](../dev-log-hero-image/SKILL.md) |
| Validate a routed hero | [dev-log-hero-validation](../dev-log-hero-validation/SKILL.md) |
| Validate a routed infographic | [dev-log-infographic-validation](../dev-log-infographic-validation/SKILL.md) |

Run writing, prose polish, then source validation. Rerun
`dev-log-prose-polish` before article validation after a material source
revision. `references/infographic-v2.md` owns the v2 infographic creator
selection. Specialist stages do not commit or push; this orchestrator owns
Git delivery.

Apply the [direct-statement rule](references/editorial-voice-v2.md#direct-statements-without-rhetorical-reversals)
to titles, headings, body, captions, and closing before source freeze. State
the fact or judgment directly; remove invented rebuttals, defensive caveats,
generic self-testing endings, and unsolicited product-switching advice. The
source reviewer must enforce these criteria even for a single occurrence.
Also apply the [concrete-predicate rule](references/editorial-voice-v2.md#concrete-predicates-instead-of-abstract-nominal-judgments):
replace unnecessary nominal labels such as `도입 판단의 첫 조건입니다` with
the actual action or supported judgment, including in the closing.

## Load only the current stage

Read `references/workflow-v2.md` for every v2 task. Then load just in time:

- before drafting, materially revising, or polishing the source:
  `references/editorial-voice-v2.md`;
- before source approval: `references/source-freeze-v2.md`;
- before final media or Tistory URL work: `references/media-release-v2.md`;
- before Tistory editor access or publication:
  `references/tistory-publication-v2.md`;
- immediately before browser QA: `references/final-page-qa-v2.md`;
- immediately before ready, Git, and handoff: `references/delivery-v2.md`.

Use the repository writing, prose-polishing, and article-validation skills for
their owning stages. Run article validation as a source-level gate before the
freeze; do not rerun its editorial interrogation after browser QA. Use the
separate hero creator/validator only when routed. For a routed infographic,
read [references/infographic-v2.md](references/infographic-v2.md), select
`max-txt2img` or `diagram-design` for the reader's question, and hand every
publication raster to
[../dev-log-infographic-validation/SKILL.md](../dev-log-infographic-validation/SKILL.md).
Use [../max-txt2img/SKILL.md](../max-txt2img/SKILL.md) for generated explanatory
illustrations. Resolve `diagram-design` from the active skill catalog for
precise HTML/SVG diagrams. These are both supported v2 creator routes; neither
replaces independent validation. Do not modify their global installation or
profiles as a side effect of writing an article.

## Route the work

Record the decision in `workflow-v2.json` before research.

- Choose `standard-rich` for a source-based article with static media.
- Choose `evidence-rich` for direct product use, experiments, GIFs, or a
  capture-led promise.
- Turn on generated hero, infographic, 390px, 768px, GIF, and second remote
  fetch only when the corresponding risk exists.
- For a procedural software guide, record the reader-friction screenshot
  decision in `workflow-v2.json` and `brief.md`; do not wait until the finished
  prose to decide whether the reader needs a UI landmark.
- For an unfamiliar product, model, or technical concept, default to a
  non-specialist reader unless the user explicitly names an expert audience.
  Treat prior knowledge as a prerequisite only when the brief and title make
  that scope explicit.
- For a recommendation or benefit explainer aimed at non-specialists, record
  the situation the reader already recognizes, what the reader does not yet
  know, one intended reader, one plain recommendation, its useful consequence,
  and details that the article will deliberately leave out. Do not frame the
  title around a folk association, search behavior, nutrient, mechanism, or
  feature that the intended reader may not know.
- Actively plan supporting visuals while outlining, especially for unfamiliar
  concepts, multi-step processes, data transformations, and handoffs between
  people or tools. Evaluate `max-txt2img` and `diagram-design` before deciding
  prose is sufficient. Record the question, message, placement, and selected
  creator in `brief.md` and the existing `decision_note`; do not add schema
  fields. A useful diagram is part of the normal workflow, not an optional
  extra that waits for the author to ask. Keep a short reason when omitted;
  do not enforce an image count or turn every list into a diagram.
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

1. Plan one primary reader, the retained message, easiest start, first-screen
   answer, opening movement, heading-only action or decision path, required
   claims, honest test boundary, media role, and conditional gates. The opening
   movement should name a concrete moment in which the reader meets the topic,
   the question or tension that arises there, the useful answer or action, and
   the evidence boundary that explains why the distinction matters. Treat this
   as narrative logic rather than a sentence quota, and never invent a personal
   anecdote to supply the scene. For a recommendation or
   benefit explainer, also lock the reader's recognizable situation, knowledge
   baseline, plain recommendation, useful consequence, and excluded detail in
   `brief.md`; do not broaden the audience after research reveals more facts.
   For an unfamiliar subject,
   make the public title and first screen independently answer what it is, what
   ordinary problem it solves, and why the intended reader would use it. A
   navigation-count hook such as `볼 화면 3곳` cannot substitute for the
   subject's plain identity unless the user explicitly requests a screen-led
   guide for readers who already know the product.
   For a procedural guide, map the steps where a first-time reader may fail to
   locate the entry point, choose the right field or value, or recognize the
   success/error state. Select a screenshot only for those friction points.
   Two to five screenshots is a useful range for a normal guide, not a quota;
   zero or more than five is valid when the recorded reader need justifies it.
   Each selected screenshot must answer a different concrete question, and
   every excluded obvious screen needs a short redundancy or upload-cost reason.
   For a disease, cause, prevention, or another broad explainer, also lock the
   questions created by the title and opening, then name adjacent topics the
   article will exclude. Typical questions may include what causes the subject,
   whether it applies personally, what can realistically change the outcome,
   which popular claims are overstated, and when professional help is needed.
   Use only the questions this title creates; do not turn the example into a
   fixed health outline. A category guide sets safety and evidence rules, not
   the article's public structure. Apply repository title and heading syntax to
   planning candidates as well; public titles and headings must not end in
   `~다`, including polite `~습니다` forms.
2. Research unstable, niche, source-sensitive, or high-stakes claims before
   drafting. Prefer primary and official sources.
3. Capture raw evidence during research only when the route requires it. Keep
   secrets out of raw files; recapture instead of blurring them later.
4. Draft around evidence with `plain identity -> ordinary use -> easiest start
   -> evidence boundary`. This is an information order, not a four-paragraph
   template. After the greeting, prefer a concrete reader situation such as a
   choice at a meal, shop, settings screen, or failed task when it belongs to
   the subject. Let the competing expectation or confusion arise from that
   situation, give the practical answer before background detail, and use the
   next turn to explain the evidence boundary. Do not open with an abstract
   summary of search results when a truthful everyday decision is available,
   and do not manufacture momentum with `결론부터 말하면`. Do not announce
   the article with `이번 글에서는`, promise to explain it `차근차근`, or
   front-load a defensive process note when the same boundary can sit beside
   the affected claim. Keep comparison rules,
   prerequisites, exact entry points, and limitations explicit. For
   troubleshooting or procedural intent, put the first safe action or default
   choice before the lead visual and TOC, then order headings by the reader's
   actual next decisions. Keep a generic non-test boundary in the brief,
   evidence, and audit rather than publishing a self-disqualifying sentence
   such as `앱을 설치하거나 실제 학습을 실행하지 않았으므로 ... 확인하지
   못했습니다`. Preserve honesty by narrowing the title and promise, omitting
   unsupported hands-on or performance claims, attributing vendor claims, and
   placing a specific limitation beside the claim it changes. Publish a test
   boundary only when it materially changes the reader's decision or the user
   explicitly asks for methodology disclosure.
   For a recommendation or benefit explainer, lead with `recognizable situation
   -> plain recommendation and useful consequence -> practical use -> mechanism
   and evidence -> material safety boundary`. Name the everyday effect before
   asking a non-specialist to interpret a nutrient, metric, feature, or internal
   mechanism. Start a simple lifestyle explainer with three stage-level jobs:
   why it fits, how to choose or use it, and who needs a material caution. Add
   another section only when it changes a real reader decision. Keep one
   representative number or comparison in the prose when it is enough; move
   supporting detail to a table or `evidence.md` instead of repeating it.
   Keep consequential safety and exception language beside the affected advice,
   but do not grow a standalone limitations section when one precise boundary
   closes the claim.
   Run a topic-link test on every practical section. If its advice could be
   pasted unchanged into a generic wellness, productivity, safety, or buyer
   guide, either explain the subject-specific causal or decision link with
   evidence or remove it. Broadly helpful advice does not earn space merely
   because it may benefit the same audience. The title-created questions, not
   the source's full list of adjacent recommendations, own the outline.
5. Before polishing individual sentences, apply the REA-calibrated
   [comprehension and natural-Korean pass](references/editorial-voice-v2.md#comprehension-before-sentence-polish).
   A reader must understand the task, its purpose, the input or subject, who
   did what, and the result before encountering implementation details or a
   secondary check. If that chain is missing, return to writing and reorder or
   remove material; synonym changes cannot repair the structure. Then run the
   full voice-and-density revision in
   `references/editorial-voice-v2.md` before the normal prose-polish stage. It
   has six required surfaces: the reader-benefit contract, opening movement,
   heading strip, AI-template sentence frames, paragraph-level new information,
   and repeated claim or action ownership. For broad explainers, the audit must
   also record the title-created question map, excluded adjacent topics, and
   topic-link test decisions.
   The normal prose-polish stage does not replace this pass. Finish every new
   or materially revised source with the
   [final connected-Korean read](references/editorial-voice-v2.md#final-connected-korean-read)
   as the last writing step, after structure and density edits. Record actual
   paired-sentence/paragraph before-and-after evidence (or a justified unchanged
   passage), not merely “polished”.
   Run the analyzer before and after as an inventory, never a score. A zero
   signal count does not pass a heading, paragraph, or article. Record the
   heading rewrites, representative deletions or merges, ownership decisions,
   protected facts and caveats, and unresolved concerns in `audit.md`.
6. Hand the still-`reviewing` bundle to an independent source reviewer. The
   reviewer must first cold-read `article.md` without the prior approvals or
   audit conclusions, describing how adjacent thoughts connect under the
   final connected-Korean gate, including separate first-screen and
   title-plus-headings-only passes. For an experiment or software explainer,
   have the reviewer state from the article alone what was supplied, what each
   tool found, what was checked separately, and why that check belongs here.
   Return the article if those answers require the brief or prior conversation.
   Then the reviewer reads the brief,
   evidence, audit, `references/editorial-voice-v2.md`, and
   `references/source-freeze-v2.md`. Return the source when a heading sounds
   like a compressed explanatory sentence, joins separate decisions for
   symmetry, or relies on `A가 아니라 B`; when the opening contains a generic
   roadmap; when a paragraph only previews, recaps, or repeats; or when the
   central choice appears after background. For a non-specialist article about
   an unfamiliar subject, also return a title or first screen that assumes the
   reader already knows the subject, leads with internal process boundaries,
   or reaches usage steps before stating the plain identity and ordinary use.
   For a non-specialist recommendation or benefit explainer, return a source
   when the title assumes the reader already connects the subject with the
   problem; when the first screen names nutrients, metrics, features, or
   mechanisms before the useful consequence; when several audiences or
   benefits compete without one recommendation; when evidence detail hides the
   recommendation; or when defensive caveats occupy more attention than the
   bounded claim they qualify. Do not remove a material medical, legal,
   financial, security, or operational warning to satisfy density.
   Also return an opening that merely inventories rumors, features, search
   results, or source findings before pivoting with `결론부터 말하면`; one that
   gives a practical answer but then restates it as a slogan; or one whose
   opening scene could introduce an unrelated subject without changing the
   action. Return substantive defects to writing and surface defects to prose
   polish until it passes.
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

Place each instructional screenshot immediately after the step it clarifies.
The surrounding prose must say where the reader is, what to inspect or enter,
and what action follows; a caption alone is not the instruction. Prefer an
official screenshot for source-based explanation and a first-party capture
only when the article honestly claims direct product use. Do not add a screen
that merely repeats an already obvious button or list.

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

If a wide UI screenshot becomes unreadable at 360 CSS pixels, use the optional
validated `mobile_scroll_width` media field and a clear caption instruction so
only the screenshot scrolls horizontally. Do not make lead art or ordinary
images scroll.

## Author approval and browser media binding

Present the complete local article and publication images for the author's
review. Keep `reviewing` until the author confirms the specific article and
asks to publish, for example `이대로 올리자`. Record the actual instruction and
approved source/media hashes in `artifacts/qa-v2/author-publication-approval.json`
as described in `references/tistory-publication-v2.md`. This author approval is
distinct from the independent source pass. Once it exists, continue through
image upload, editor entry, preview, final publish, and publication confirmation
without asking for the same permission again.

Use the Codex in-app browser, including for login and file upload. Print the
media queue with `tistory_media_map_v2.py plan` for Codex's upload checklist.
Upload each validated local asset in the target editor and capture the native
`[##_Image|..._##]` code that Tistory generates. Bind that exact code with
`set-embed --embed-file ... --url ...`; the URL is an observed preview/live
address for byte verification, not the publication source. Set
`publication_mode: codex-browser` in `workflow-v2.json` for this release.
Do not infer an attachment code by rewriting a CDN URL.

Record one remote baseline with `remote_media_v2.py record` and the routed
second fetch. New browser releases require native attachment blocks for every
media item. The fragment preserves them; local and remote previews use normal
images for inspection. Check the exact native fragment in Tistory's own
preview before publication. A missing login, attachment, approval, or valid
fetch keeps the article at `reviewing` with a concrete resumption point.

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

After the final gates pass, enter the byte-identical
`<slug>-tistory-fragment.txt` in the target Tistory editor. Check the exact
native attachment result, title, category, public URL, and real hELLO light/dark
preview; publish under the recorded author approval. Confirm publication from
the browser's success state or matching post-list entry, read the article URL,
and set `published`. Do not open the public page for additional visual QA.
Return that URL as the primary handoff, with the exact TXT as a backup. If a
completion screenshot is needed, use the observed success state without a new
inspection pass. Finish Git delivery for
the publication evidence and lifecycle update as well.

## Completion

A v2 rich post is complete only when the source pass, validated local media,
resolved remote URLs, required remote observation, exact remote light/dark
candidate, one independent final-page record, strict final render, focused Git
delivery, verified remote commit, byte-identical submitted file, author
publication approval, and confirmed publication with its resulting URL. Routine
post-publication visual QA is not a completion gate. A reviewed draft without
author publication approval is a review handoff, not a published post. Never
accept an unresolved claim, unsupported hands-on statement, local media path,
placeholder, duplicate H1, unreadable mobile evidence, hidden table content,
stale gate, known visual defect, a fluent article whose purpose or actual work
cannot be explained by its intended reader, an unmotivated test or diagram,
generic opening roadmap, abstract
result-summary opening, canned `결론부터 말하면` pivot, sentence-shaped
contrast heading, paragraph without new reader value, full takeaway repeated
across sections, a specialist-assuming title for a non-specialist reader, a
recommendation title that assumes an unknown folk association or search habit,
an unexplained nutrient or mechanism before its useful consequence, competing
target readers, evidence detail that hides the recommendation, or a generic
public disclaimer that lowers trust without changing the reader's decision.

