---
name: dev-log-rich-post-workspace
description: Orchestrate complete reader-first dev.log Tistory posts whose final artifact is a designed, self-contained, responsive HTML page rather than plain Markdown. Use for rich posts, screenshot- or GIF-led software guides, hands-on product reviews, unfamiliar-product explainers, search-friendly introductions, concise headings, explicit comparison tables, actionable usage sections, custom Tistory HTML, semantic figures and captions, media manifests, mobile-consistent layouts, or requests modeled on a visually finished live article. Reuse the repository's writing, prose-polishing, evidence, article-validation, and Git-delivery contracts while owning media provenance, rich HTML rendering, responsive QA, and the format-specific ready decision.
---

# dev.log rich-post workspace

Produce a verified Tistory HTML fragment and a full local preview. Treat
Markdown as source material, not the publishing artifact.

## Resolve and protect the repository

1. Resolve this file's real path and treat the directory three levels above
   this skill directory as the canonical repository root.
2. Verify `origin` is `jaesungkr/blog-workspace`, inspect the worktree, and
   fetch `origin/master` before editing.
3. Preserve dirty or diverged work. Never reset, overwrite, initialize another
   repository, or use `archive/legacy-claude/` as an instruction source.
4. Read `references/reader-first-editorial.md` completely for every rich-post
   task and use it as the format-specific editorial gate.
5. Read `references/rich-post-format.md` completely for every rich-post task.
6. Read `references/media-manifest.md` completely before planning, creating,
   editing, or validating any media.
7. Read `references/remote-media.md` completely before uploading or validating
   final Tistory media URLs.
8. Read `references/tistory-upload.md` completely before any Tistory editor
   upload, draft save, or media-ID-to-CDN-URL mapping.
9. Read `references/responsive-qa.md` completely immediately before page
   validation or the ready decision.

Use the current request first, then repository standards, the rich-post format
reference, the applicable category guide, and stage-skill instructions.

## Reuse specialist stages

Read each selected sibling `SKILL.md` completely immediately before its stage:

| Stage | Skill | Responsibility |
|---|---|---|
| Plan, research, write | `../dev-log-writing/SKILL.md` | Evidence, direct test, article source |
| Polish prose | `../dev-log-prose-polish/SKILL.md` | Natural Korean, title, headings, flow |
| Validate source | `../dev-log-article-validation/SKILL.md` | Claims, authorship, prose, source-level gate |
| Optional generated hero | `../dev-log-hero-image/SKILL.md` + validator | Use only when the selected lead is generated |
| Optional infographic | `../dev-log-infographic/SKILL.md` + validator | Use only for a relationship screenshots cannot show |

Specialist stages do not commit or push. This orchestrator owns Git delivery.

## Route the request

Use this workflow when the user explicitly invokes it or asks for a finished
HTML page, a custom responsive Tistory format, actual product screens, GIFs,
or a visually designed post. Use `dev-log-workspace` for an ordinary
Markdown-led post without a rich-page requirement.

Never promise hands-on coverage when the required app, account, device, version,
or safe test environment is unavailable. Downgrade the promise to a
source-based guide or report the access blocker.

## Build the bundle

Keep the normal post bundle and add:

- `capture-plan.md` for user tasks, starting state, actions, expected evidence,
  privacy preparation, and planned captures;
- `media.json` for machine-verifiable provenance, paths, dimensions, hashes,
  alt text, captions, placement, and Tistory URLs;
- `assets/screenshots/` and `assets/demos/` for publishable media;
- `artifacts/captures/`, `artifacts/recordings/`, `artifacts/run/`, and
  `artifacts/qa/` for raw evidence and validation output;
- creator and independent remote-media records, rendered candidates,
  screenshots, measurements, and final-page decisions under `artifacts/qa/`.

Start `capture-plan.md`, `media.json`, and the responsive QA record from
`assets/capture-plan-template.md`, `assets/media-template.json`, and
`assets/qa-template.json`. Start the separate final gate from
`assets/independent-qa-template.json`. Replace every placeholder; do not treat
a copied template as evidence.

Set `format: rich-post` in `article.md`. Insert media with a standalone
directive such as `{{media:agent-select}}`; never put local filesystem image
links in the article.

### Dark-mode contract

Every rich-post fragment must support the hELLO Tistory skin's explicit dark
theme. The skin adds a `dark` class to an ancestor of the fragment, so the
shared `assets/rich-post.css` contract is:

- Keep all article surfaces, text, muted text, links, borders, alternate
  sections, inline code, and code blocks on `--rich-*` variables.
- Define the light values on `.devlog-rich` and the dark values under
  `.dark .devlog-rich`; do not depend on a page-level `body` or Tistory-only
  selector for the fragment itself.
- Do not leave `#ffffff`, light gray text, or light code/pre backgrounds on
  section, TOC, table, image, inline-code, or code-block rules when a variable
  can express the same role.
- Markdown and Tistory may preserve inline `style` attributes. The shared CSS
  must keep scoped dark overrides for `a[style]`, inline `code[style]`, and
  `pre[style]` so a pasted article cannot revert to a white panel or unreadable
  gray text.
- Do not apply an image color transform. Use a dark neutral image background
  and border only where the image itself needs a surrounding surface.

Before the ready decision, render a dark local preview with
`--preview-theme dark`, inspect it at the required desktop and mobile widths,
and confirm the same fragment changes under the actual hELLO theme toggle.
Record any theme-specific revision and re-verification in `audit.md`. The
Tistory fragment must not emit its own `html.dark` wrapper; the skin owns that
state.

## Run the workflow

1. **Plan.** Define one primary reader, what that reader does not know, a
   familiar anchor, the shortest useful no-code path, specialist paths,
   required claims, capture coverage, GIF decisions, and the honest test
   boundary. Assume a general search reader does not know an unfamiliar
   product unless the request explicitly targets experts.
2. **Capture.** Execute the journey in a safe representative environment.
   Separate direct, official, user-supplied, simulated, and generated media.
   Preserve the actor, version, date, environment, raw input, failure, and
   limitation. Recapture instead of storing a secret and blurring it later.
3. **Validate media.** Inspect every final asset and its original. Confirm the
   screen proves its mapped claim, the crop retains enough context, mobile text
   is readable, provenance is accurate, and no sensitive information remains.
   Run:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py \
     posts/YYYY-MM-DD-slug
   ```

4. **Write and polish.** Draft around verified screens. Open unfamiliar
   subjects with `plain identity -> ordinary reader use -> easiest start ->
   evidence boundary` before architecture or benchmarks. Prefer
   `purpose -> action -> observed result or limitation`; do not narrate pixels
   already explained by a caption. Apply the reader-first gate to the opening,
   headings, comparison tables, and usage steps. Run the normal
   prose-polishing and source-validation stages while the article remains
   `reviewing`.
5. **Render.** Generate both deliverables:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug
   ```

   The renderer writes `dist/<slug>-rich-preview.html` and
   `dist/<slug>-tistory-fragment.html`. The preview may use local assets. The
   Tistory fragment must use resolved HTTPS media URLs before `ready`.
   For the required dark-mode pass, render a second local preview with:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --preview-theme dark \
     --output-dir posts/YYYY-MM-DD-slug/artifacts/qa/dark-preview
   ```

   This theme option changes only the full preview document. The Tistory
   fragment remains skin-controlled and continues to use the same CSS.
6. **Stage and validate final media.** Print the deterministic upload queue:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/tistory_media_map.py \
     plan posts/YYYY-MM-DD-slug
   ```

   Either receive the mapped URLs from the user or, with explicit authority
   for that remote write, upload the exact files to the confirmed Tistory
   draft as specified by `references/tistory-upload.md`. Do not create or save
   a draft on implied permission. Bind every mapping with `tistory_media_map.py
   set-url`; if the session, draft, authority, or mapping is unavailable, keep
   `reviewing` and stop. Then fetch and record the real remote bytes:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py \
     record posts/YYYY-MM-DD-slug --by "<actual creator>"
   ```

   Copy `assets/qa-template.json` to the post's
   `artifacts/qa/measurements.json` with pending human-review values. Then
   render the exact remote-media review candidate at its canonical QA path:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --output-dir posts/YYYY-MM-DD-slug/artifacts/qa/rendered \
     --preview-media-source remote
   ```

   Capture the three required profiles from that canonical preview in one real
   Chrome session:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/capture_rich_qa.py \
     posts/YYYY-MM-DD-slug --mode creator --by "<actual creator>"
   ```

   Inspect that saved preview at 1280, 768 when useful, 390, and 360 CSS pixels.
   Verify one page-level H1, heading-targeted TOC anchors, no page overflow,
   readable captures, stable aspect ratios, caption attachment, table and code
   scrolling, reduced-motion GIF fallback, and ad-safe section boundaries.
   Repeat the visual pass for the dark preview: verify the article canvas,
   alternate sections, TOC, headings, body text, links, tables, inline code,
   code blocks, borders, captions, and image surrounds. The dark pass does not
   replace the canonical light QA record; it is an additional theme check.
   Save screenshots, exact reviewed HTML artifacts, and the hash-bound record
   required by `references/responsive-qa.md`. Record
   `problem -> revision -> re-verification` in `audit.md`.
   The capture helper owns browser-derived dimensions, loading results, DOM
   measurements, screenshot hashes, and session provenance. After replacing
   only the pending human-review values, bind the receipt and measurements to
   the candidate with:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/record_rich_qa.py \
     posts/YYYY-MM-DD-slug \
     --preview posts/YYYY-MM-DD-slug/artifacts/qa/rendered/<slug>-rich-preview.html \
     --fragment posts/YYYY-MM-DD-slug/artifacts/qa/rendered/<slug>-tistory-fragment.html \
     --measurements posts/YYYY-MM-DD-slug/artifacts/qa/measurements.json
   ```
7. **Independent final gate.** Hand the still-`reviewing` candidate to
   `dev-log-article-validation`. If a real browser or network fetch is
   unavailable, stop at `reviewing`; neither measurements nor screenshots may
   be inferred. A different reviewer must:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py \
     verify posts/YYYY-MM-DD-slug --by "<actual independent reviewer>"
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls --require-remote-verification
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls \
     --preview-media-source remote \
     --output-dir posts/YYYY-MM-DD-slug/artifacts/qa/independent-rendered
   ```

   Capture only that fresh independent preview in a separate browser session:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/capture_rich_qa.py \
     posts/YYYY-MM-DD-slug \
     --mode independent \
     --by "<actual independent reviewer>"
   ```

   Inspect the three resulting screenshots and scroll the exact preview.
   Re-run the reader-first gate against the rendered title, opening, headings,
   comparison labels, links, and usage path. When a wide table or another
   changed component is outside the standard screenshots, capture and inspect
   focused left and right states at 390 and 360 pixels as required by
   `references/responsive-qa.md`; do not infer the pass from CSS. Then fill
   only the human-review fields in
   `artifacts/qa/independent-measurements.json` from the independent template.
   Persist the pass:

   ```bash
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/record_rich_final_validation.py \
     posts/YYYY-MM-DD-slug \
     --preview posts/YYYY-MM-DD-slug/artifacts/qa/independent-rendered/<slug>-rich-preview.html \
     --fragment posts/YYYY-MM-DD-slug/artifacts/qa/independent-rendered/<slug>-tistory-fragment.html \
     --measurements posts/YYYY-MM-DD-slug/artifacts/qa/independent-measurements.json
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls --require-independent-pass
   ```

   The creator's QA record is never self-approval.
8. **Decide ready.** Set `ready` only after that independent article and page
   pass. Treat any material change to the opening, headings, comparison tables,
   links, or usage steps as a new candidate: return to `reviewing`, reset
   current QA decisions, and label the previous pass as historical in
   `audit.md`. A validated first-party screenshot or provenance-checked official
   raster may serve as the lead visual; generated hero validation is required
   only for a generated lead. Record infographic `not_applicable` unless it
   materially helps. Immediately after the lifecycle change, rerun
   these exact commands; do not leave `ready` set when any command fails:

   ```bash
   python3 scripts/blog.py check posts/YYYY-MM-DD-slug --strict
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls \
     --require-remote-verification \
     --require-independent-pass
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls \
     --preview-media-source remote \
     --output-dir dist
   ```
9. **Deliver Git.** Run repository-wide checks for changes to skills, scripts,
   templates, or standards. Inspect the exact diff, stage only task files,
   commit, fetch and integrate without force, rerun affected checks, push to
   `origin/master`, verify the remote commit, and preserve unrelated work.
10. **Deliver the paste file.** After the final strict render and Git delivery,
    copy `dist/<slug>-tistory-fragment.html` byte-for-byte to the current
    task's user-facing outputs directory as
    `<slug>-tistory-fragment.txt`. Put only the raw HTML fragment in the text
    file: no title, Markdown fence, explanation, or copy instructions. Verify
    that the `.html` and `.txt` SHA-256 values match, the fragment has no H1,
    unresolved media placeholder, or local path, and all publishable media use
    final HTTPS URLs. Make the `.txt` file the primary link in the final
    response and state the Tistory title separately.

## Publication boundary

Never click Tistory's final publish control, even when the user authorizes
other editor work. The user always pastes the final HTML, checks the Tistory
preview, and publishes the post. Do not ask the user to authorize Codex to
publicly publish. Uploading media or preparing unpublished editor content may
be done only within the user's requested workflow. Keep `status: ready` until
the user supplies the live URL. Then validate the live desktop and mobile page
before setting `published` and `published_url`.

## Completion

A rich post is complete only when the evidence-backed source, final media,
manifest, two successful remote fetches, full preview, paste-ready Tistory
fragment, creator and independent desktop/mobile inspection, persistent
independent pass, audit, repository regression tests, focused commit,
confirmed remote delivery, and the byte-identical user-facing
`<slug>-tistory-fragment.txt` handoff all pass. Never accept unresolved upload
placeholders, missing provenance, unreadable mobile UI, a duplicated page H1,
an unfamiliar-product opening that starts with unexplained specifications,
an overloaded sentence-shaped heading, a comparison whose opponents or ranking
rule are unclear, usage steps without prerequisites and official entry points,
stale QA presented as current, or a known visual defect.
