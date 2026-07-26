---
name: dev-log-infographic-validation
description: Independently validate dev.log supporting infographics with special emphasis on Korean text visibility and collision-free mobile reading. Use for full-raster, native 360px, and enlarged-crop QA; glyph accuracy; line, marker, icon, shadow, and crop overlap; connector meaning; factual copy checks; version approval; or revision decisions. Keep this gate separate from hero campaign quality and Git delivery.
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
2. Native 360 CSS-pixel raster viewed without zoom.
3. Enlarged crops around every headline, primary block, icon-label pair,
   connector, arrowhead, footnote, result, and caveat.

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
- `pass` only when full, 360px, and every crop pass;
- `revision_required` for any content, collision, legibility, connector, or
  mobile defect.

For a failure, send exact coordinates or named regions and the observed problem
back to `dev-log-infographic`. Require a new versioned raster, regenerate all
affected views from that raster, and rerun the complete visual QA. Do not accept
an automated check as a substitute for actual raster inspection.

Record in `audit.md`:

- candidate path, dimensions, hash, type, question, placement, and alt text;
- full, 360px, and crop observations;
- every `problem -> revision -> re-verification`;
- final stage result.

## Handoff

Return the stage result and visual evidence to `dev-log-workspace`. Do not
change hero-image standards, set the article ready by yourself, commit, or push.
