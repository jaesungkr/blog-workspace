---
name: dev-log-infographic-validation
description: Independently validate dev.log supporting infographics with special emphasis on balanced typography-to-canvas scale, Korean text visibility, and collision-free mobile reading. Use for full-raster, 360 CSS-pixel browser display, enlarged-crop and type-scale QA; framed-poster detection; glyph accuracy; overlap; connector meaning; factual copy checks; version approval; or revision decisions. Keep this gate separate from hero campaign quality and Git delivery.
---

# dev.log infographic validation

Treat text visibility and collision-free reading as release-blocking. Do not
approve from a whole-image preview alone.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory.
2. Read `standards/supporting-infographic-guide.md` completely.
3. Read the target article, brief, evidence, audit, copy map, editable source,
   and render code.
4. Inspect the exact candidate raster, not only its HTML or SVG source.

## Content and diagram gate

- The image answers the reader question recorded in `brief.md`.
- Every factual label, number, comparison, conclusion, and caveat maps to the
  article or `evidence.md`.
- Reading order and connectors are unambiguous.
- Three to five primary blocks carry one relationship without becoming a
  generic card grid.
- With labels mentally hidden, the problem, transformation, branches, or result
  remain distinguishable.
- The visual adds understanding after the surrounding prose instead of merely
  repeating it.

## Mandatory visual QA

Generate all views from the exact final candidate:

1. Full-resolution raster.
2. The same untouched raster displayed in a browser at `width:360px` without
   zoom. Do not create, save, re-encode, or commit a smaller raster derivative.
3. Enlarged crops around every headline, primary block, icon-label pair,
   connector, arrowhead, footnote, result, and caveat.

Before checking individual glyphs, audit the whole 360px browser display:

- calculate each text role's 360px equivalent with
  `source font px × 360 ÷ source canvas width`;
- use `20-24px` for the headline, `15-18px` for primary labels, `12-14px`
  for supporting copy, and `11-12px` for caveats as the default bands;
- require an explicit semantic reason in `audit.md` for a value outside a band;
- reject a headline area that occupies much more than 22% of the canvas height
  or makes the explanatory visual feel secondary;
- reject a large decorative outer card when it makes the diagram look like a
  small framed insert;
- reject blocks whose words, badges, and labels visually fill the available
  region. Require quiet space and a diagram-led shape before reading the text;
- do not fix an oversized headline or crowded block by shrinking supporting
  copy below its mobile floor. Reduce copy, change hierarchy, open the layout,
  or increase useful diagram area.

Run `scripts/check_mobile_type_scale.py` with the actual canvas, header, and
source font sizes. Use repeated role flags when needed. A nonzero result is
`revision_required` unless the exception is semantically necessary and recorded
with a same-size visual comparison. The script checks scale only; it never
replaces raster inspection or the framed-poster test.

Run a first-impression test while the original raster is displayed at
`width:360px`: look away, then look back for one second. The relationship or
mechanism must register with the headline. If the image reads first as a poster,
slide, or boxed text sheet, return `revision_required` even when every word is
legible.

For every text block:

- verify exact Korean glyphs, numbers, units, punctuation, and line breaks;
- trace a clear zone around the glyphs;
- reject any line, stroke, arrowhead, marker, icon, shadow, texture, highlight,
  or crop edge that enters the glyph area or weakens contrast;
- inspect the complete painted bounds of SVG strokes and markers, not only path
  endpoints; prefer explicit `markerUnits="userSpaceOnUse"` and dimensions;
- verify no clipping, orphaned label, pseudo-writing, low-resolution layer, or
  ambiguous connector remains.

Read labels once in normal order and once by scanning only text blocks. Then
scan only the diagram to confirm the relationship remains visible.

## Decision loop

Return:

- `not_applicable` when the creation gate correctly produced no infographic;
- `pass` only when the full raster, untouched 360px CSS display, and every crop
  pass;
- `revision_required` for any content, collision, legibility, connector, or
  mobile defect.

For a failure, send exact coordinates or named regions and the observed problem
back to `dev-log-infographic`. Require a new versioned raster, regenerate all
affected views from that raster, and rerun the complete visual QA. Do not accept
an automated check as a substitute for actual raster inspection.

Record in `audit.md`:

- candidate path, dimensions, hash, type, question, placement, and alt text;
- 360px CSS-display-equivalent sizes for headline, primary labels, supporting
  copy, and caveat, plus the headline-height share;
- full raster, untouched 360px CSS display, and crop observations;
- whether the composition passed the one-second relationship test and the
  framed-poster rejection;
- every `problem -> revision -> re-verification`;
- final stage result.

## Handoff

Return the stage result and visual evidence to `dev-log-workspace`. Do not
change hero-image standards, set the article ready by yourself, commit, or push.
