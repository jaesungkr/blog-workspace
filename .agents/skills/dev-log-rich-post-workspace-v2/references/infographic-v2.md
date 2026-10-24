# Supporting diagrams and infographics in v2

## Ownership and creator selection

For `format: rich-post-v2`, actively use either of these creator skills when a
visual makes an explanation easier to follow:

- [max-txt2img](../../max-txt2img/SKILL.md): generate a complete raster
  illustration for a concept, mechanism, process, or relationship. Requests
  referring to `max2image` in this workflow use this installed creator.
- `diagram-design`: build a deterministic, self-contained HTML/inline-SVG
  diagram when exact strings, numeric values, labels, or connector geometry
  carry the meaning. Resolve and read its `SKILL.md` from the active skill
  catalog; the current installation is `~/.codex/skills/diagram-design/`.

Both routes hand the exact publication raster to
[dev-log-infographic-validation](../../dev-log-infographic-validation/SKILL.md)
for independent approval. The v2 orchestrator owns route selection, media
registration, source invalidation, final-page QA, and Git delivery. Neither
creator validates its own final work, uploads, publishes, commits, pushes, or
sets the article ready. The hero workflow remains separate.

This replaces v2's earlier max-txt2img-only creator restriction. For the
max-txt2img route, generate the complete image, including the approved labels;
do not silently substitute a text-free layer or HTML layout. For the
explicitly selected diagram-design route, editable HTML/SVG is the intended
production source. Preserve the shared standards' accuracy, scope, spacing,
and actual publication-size readability in both routes. Standard posts and
v1 posts retain their existing creator routing.

For v2 max-txt2img candidates only, this supersedes the deterministic-copy and
generated-illustration-only production clauses in `standards/image-guide.md`,
`standards/image-art-direction.md`, and
`standards/supporting-infographic-guide.md`. Hero-specific campaign or
physical-material preferences do not replace this route's flat infographic
style. The selected diagram-design route retains deterministic copy.

## Plan visuals while outlining

Look for the passages where a reader has to keep several steps, actors,
locations, transformations, or alternatives in mind. Prefer creating a focused
visual there instead of waiting for the author to request more images. This
is a decision based on reading effort, not an image quota.

For each candidate, record the reader question, one retained message,
relationship, evidence claim IDs, intended width, placement, and selected
creator in `brief.md`; summarize the route in the existing `decision_note` of
`workflow-v2.json`. Turn on `infographic` when a supporting visual is selected.
Do not add creator fields to the workflow schema. If prose or a compact table
is clearer, omit the diagram and record a short reason with `not_applicable`
in `audit.md`. Avoid charts that only repeat a list or decorate a paragraph.

| What the reader needs to understand | Creator to consider first |
|---|---|
| A conceptual mechanism or a short process helped by visual motifs | `max-txt2img` |
| Input → analysis → finding, actors and handoffs, or data transformation | Either; choose by illustration value versus precision needs |
| Exact quoted strings, code characters, measured values, schemas, or branching connections | `diagram-design` |

Different figures in one article may use different creators. In the REA case,
the export sequence benefited from a generated process illustration, while
CSV quotation marks required deterministic lettering. Reuse the reasoning,
not those specific figures or an obligatory pair of images. A generated
diagram is an explanation, never evidence that an app was run or a result
measured.

Plan the role and claims before the source freeze; create final media after
the source pass. Provide the selected creator with the approved section,
relevant evidence, exact permitted copy, placement, and existing references.
Do not ask it to illustrate every detail of an entire article. Introduce in
the preceding paragraph why this figure matters to the current question.

## Create with max-txt2img

Follow its source → structure → diagram choice → English prompt validation →
generation → inspection pipeline. Preserve prompt-only, same-prompt
regeneration, and targeted edit requests. A prompt-only result is not final
publication media.

- Use Korean labels for a Korean post unless the author specifies otherwise.
  Keep the exact names, number of stages, order, direction, conditions, and
  values. Use short labels and at most three keywords per component; list all
  permitted visible strings in the prompt.
- Use the approved blog style and a simple, readable illustration. A 16:9
  canvas is a default, not a reason to squeeze essential Korean labels into
  unreadable text. Adapt the layout when the ratio was not fixed by the user.
- Inspect the actual returned raster and respect max-txt2img's one-correction
  budget, including defects found by the independent validator. Preserve each
  attempt. If a defect remains, keep `revision_required`; do not manufacture a
  pass, substitute English or numbers for required Korean, or use another tool
  as an unrecorded way around the failed candidate.

## Create with diagram-design

Read its setup gate and the chosen semantic-pattern/type references before
rendering. Set the audience, content, size, and static layout for the article.
Use Korean-capable fonts for labels and reserve monospace for technical
strings. Follow its complexity, connector, typography, accessibility, and
self-check requirements; do not copy its entire type catalog into the post.

Reuse the project's established approved style instead of reopening an
answered style question. The REA project choice was white, black, and blue;
resolve the relevant marker/profile or documented project choice for the
current task. If no choice exists, follow diagram-design's first-use gate.
Do not overwrite the installed default style guide, saved profile, or unrelated
project configuration merely to style one blog figure.

Keep the self-contained HTML and inline SVG as editable source, then follow
its export reference to create a standalone publication raster. Selecting
this route for a complete Tistory post includes producing that raster. Use
only currently permitted rendering/browser tools; if an export helper cannot
run within those constraints, document the actual allowed export method or
leave a concrete blocker. Do not claim a helper ran when it did not.

Verify exact characters and values against the evidence before and after
export. Preserve any real fallback font, actual pixel dimensions, MIME type,
and bytes. A script self-check cannot establish visual legibility. On a
creator-route change, record the reason and a new candidate, preserve the
failed version, and validate the new raster independently.

## Persist and inspect the publication candidate

Save a versioned raster under the post's `assets/`; never overwrite an earlier
candidate or rename JPEG bytes as PNG. Preserve these records under
`artifacts/qa-v2/infographic/`:

- for max-txt2img: final English prompt, edit prompts, tool return and actual
  output details; do not invent a seed, model, source font size, or SVG source;
- for diagram-design: editable HTML/SVG, effective style/font choices,
  self-check result, actual export method, and source/export hashes;
- for both: a copy map from visible factual strings to evidence claim IDs,
  creator, actual tool, output path, dimensions, SHA-256, intended width,
  requested/observed ratio, corrections, and inspection findings.

Register the existing media version 2 fields with `origin: generated`,
`kind: image`, `role: concept` (or `comparison` when appropriate), claim IDs,
provenance, rights, dimensions, hash, alt text, caption, and local path. Keep
creator-specific data in the generation record, not new media schema fields.
Use `{{media:id}}` at the planned position. Captions must identify explanations
as such and not imply an unobserved product screen or completed experiment.

Inspect the untouched raster at full resolution and its actual displayed
width on a 360 CSS-pixel article page, including narrower skin gutters. Read
every Korean label, essential number, code character, and caveat. Simplify or
restructure an unreadable figure; do not crop meaningful content or use the
UI-screenshot scrolling escape hatch for a normal infographic. Essential
content and a user-fixed ratio remain constraints. Record unresolved failures.

Source or substantive caption changes return to source review and invalidate
downstream evidence. A new raster needs fresh visual and final-page evidence.
Do not rewrite approved facts to accommodate a diagram.

## Independent validation and return

Hand the exact raster, prompt or editable source, copy map, production record,
evidence, placement, and intended width to the independent validator. Its
full-raster, actual-size, enlarged-region, glyph, connector, contrast, spacing,
and copy checks apply to both creators. Inspect painted bounds in generated
art and source geometry in deterministic diagrams where available; do not
invent unavailable measurements or approve from a good prompt alone.

Return defects to the selected creator, respecting that route's actual retry
constraints. Only an independent `pass` allows the media item to become
validated. Record the result in `audit.md` and focused evidence in this v2
artifact directory, then resume local preflight, native Tistory binding, and
the final light/dark page gate.
