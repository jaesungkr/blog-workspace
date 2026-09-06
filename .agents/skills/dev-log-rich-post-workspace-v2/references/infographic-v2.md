# Infographic creation and validation in v2

## Ownership and scope

For `format: rich-post-v2`, use
[max-txt2img](../../max-txt2img/SKILL.md) to create supporting infographics and
[dev-log-infographic-validation](../../dev-log-infographic-validation/SKILL.md)
for independent approval. The v2 orchestrator owns route selection, media
registration, source invalidation, final-page QA, and Git delivery.

This route implements the user's requested image-generation workflow. For
these candidates only, it supersedes the deterministic-copy and generated-
illustration-only production clauses in `standards/image-guide.md`,
`standards/image-art-direction.md`, and
`standards/supporting-infographic-guide.md`. Generate the complete infographic,
including its exact approved labels, with the image tool. Do not silently
replace it with an HTML/SVG layout or a text-free generated layer. Retain the
standards' factual accuracy, necessary caveats, clear relationships, spacing,
and publication-size readability requirements. Hero-specific campaign media
and physical-material preferences do not replace max-txt2img's flat infographic
style. Standard posts, v1 posts, and hero creation retain their existing routes.

## Decide before the source freeze

Set `infographic` in `workflow-v2.json` only when a diagram materially reduces
the effort needed to understand a process, mechanism, decision, comparison,
experiment, or troubleshooting path. An explicit infographic request also
qualifies. Record the reader question, one retained message, relationship,
reason prose or a table is insufficient, and exact placement in `brief.md`.
Do not add an infographic just to fill space. When omitted, record the reason
and `not_applicable` in `audit.md`.

Plan its role and source claims before the freeze; generate final media after
the source pass. Give max-txt2img the approved article section, relevant evidence
and claim IDs, the intended placement, and existing references or candidates.
Do not ask it to illustrate an entire article when one relationship is enough.

## Create with max-txt2img

Follow its complete pipeline: read source, extract structure, choose the diagram,
write and validate the English prompt, generate, inspect, and correct a clear
defect once. Preserve its prompt-only, same-prompt regeneration, and targeted
edit branches. A prompt-only result cannot count as validated publication media.

- Default to Korean labels for a Korean post and a 16:9 canvas unless the user
  specifies otherwise. Use minimal, professional, corporate-friendly flat
  illustration with restrained gradients and generous white space.
- Keep the exact number, order, direction, conditions, names, and values from
  the source. Use short labels and at most three keywords per component; this
  is a maximum, not a quota. List every permitted visible string in the prompt.
- Inspect the original generated raster at full resolution and at the actual
  article width, including the 360 CSS-pixel page. If a landscape diagram is
  unreadable there, simplify optional copy or adapt the layout when the aspect
  ratio was only a default. Do not crop meaningful content or enable screenshot
  scrolling for an infographic. A fixed user ratio and essential labels remain
  constraints; report an unresolved failure if they cannot both pass.
- Preserve Korean labels through correction. Do not silently translate to
  English, substitute numbers, or remove a decision-changing caveat to pass.
- Keep the same candidate's correction attempts within max-txt2img's one-retry
  budget, including defects found by the independent validator. A later explicit
  user revision can start a new attempt. If defects remain, preserve the
  candidate, prompt, and observed issue with `revision_required`; keep the post
  `reviewing`. Never switch to the old creator or claim an uninspected pass.

## Persist the candidate and provenance

Save a versioned publication raster under the post's `assets/`, for example
`<slug>-infographic-v1.png`. Never overwrite an earlier candidate. Preserve the
tool's actual format and dimensions rather than renaming its extension or
claiming the requested ratio was achieved without checking it.

Save each candidate's final English prompt and any edit prompt under
`artifacts/qa-v2/infographic/`. In that directory, also save a copy map from all
visible factual strings to article/evidence claim IDs and the actual generation
record: creator `max-txt2img`, tool used, references, output path, dimensions,
SHA-256, requested and observed ratio, correction count, and inspection result.
Record only returned settings; do not invent model, seed, source font sizes,
editable SVG, or rendering code. The prompt is the reusable production source.

Record the candidate, intended publication width, type, placement, alt text,
caption, production method, and known concerns in `audit.md`. Register it using
the existing media version 2 schema with `origin: generated`, `kind: image`,
and `role: concept` (or `comparison` for a comparison infographic), claim IDs,
provenance, rights, dimensions, hash, and local path. Do not invent a
`supporting` role or represent generated art as a real product state.
Do not add fields to `media.json` for the creator or
prompt; keep those details in the generation record. Use `{{media:id}}` at the
planned placement, never a local filesystem Markdown image link.

Source changes or substantive caption changes return to source review and
invalidate downstream evidence. Replacing the raster requires fresh visual and
final-page evidence. Do not rewrite frozen prose merely to fit an image.

## Independent validation and return

Hand the exact raster, final prompt, copy map, generation record, evidence,
placement, and intended width to the infographic validator. The creator's
self-check does not replace independent approval.

The validator keeps its full-raster, intended-size, enlarged-region, glyph,
connector, contrast, spacing, and content checks. Inspect the untouched
publication raster, including every label and caveat. For generated artwork,
use observable painted bounds; source font settings and code assertions are
unavailable, not failed requirements. Do not infer a good image from a good
prompt. Return defects to `max-txt2img` under the retry budget above.

Only an independent `pass` allows the orchestrator to mark the media validated.
Record the result in `audit.md` and any focused evidence under
`artifacts/qa-v2/infographic/`, never v1 QA paths. Then resume local preflight,
the user-owned Tistory upload queue, URL binding, and the single final light/dark
page gate. Neither this creator nor its validator uploads, publishes, commits,
pushes, or sets the post ready.
