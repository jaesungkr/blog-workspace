---
name: dev-log-infographic-validation
description: Independently validate dev.log supporting infographics with special emphasis on typography-to-canvas balance, painted-bound spacing, Korean text visibility, and collision-free reading. Use for full-raster and intended-publication-size inspection, enlarged-crop QA, framed-poster detection, glyph accuracy, overlap, connector meaning, factual copy checks, version approval, or revision decisions. Keep this gate separate from hero campaign quality and Git delivery.
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
- The candidate uses the smallest complete structure, normally two to five
  primary blocks, without adding blocks only for visual symmetry.
- Every kicker, subhead, rhetorical question, footer, and conclusion line earns
  its place by preventing a real ambiguity. Reject text that merely repeats the
  article, narrates an obvious connector, or tells the reader how to interpret
  a relationship that is already visually clear.
- With labels mentally hidden, the problem, transformation, branches, or result
  remain distinguishable.
- The visual adds understanding after the surrounding prose instead of merely
  repeating it.

## Mandatory visual QA

Generate all views from the exact final candidate:

1. Full-resolution raster.
2. The same untouched raster displayed at its intended publication width.
3. Enlarged crops around every headline, primary block, icon-label pair,
   connector, arrowhead, footnote, result, and caveat.

Do not create, save, re-encode, or commit a separate reduced QA raster. Inspect
the exact publication candidate in every view.

Before checking individual glyphs, audit the whole intended-size display:

- compare each text role with the canvas, illustration, and nearby text rather
  than a fixed CSS-pixel band;
- reject a headline area that occupies much more than 18% of the canvas height
  or makes the explanatory visual feel secondary;
- reject a large decorative outer card when it makes the diagram look like a
  small framed insert;
- reject blocks whose words, badges, and labels visually fill the available
  region. Require quiet space and a diagram-led shape before reading the text;
- reject sparse relationships padded with generic helper copy, bottom
  takeaways, or decorative sections. Require copy reduction or a smaller canvas;
- treat user feedback that text is too large relative to the image as
  release-blocking. Require a versioned revision, a fresh intended-size display,
  and refreshed crops;
- measure the painted bounds of adjacent text blocks. Reject cramped leading
  even when baselines do not overlap. As a starting judgment, expect visible
  vertical air of roughly `0.6-1.0×` the smaller line's painted height within a
  group and more between semantic groups;
- measure complete painted envelopes for illustrations, connectors, and rules.
  Reject any object that touches a section rule and repeated boundaries whose
  surrounding clearances vary without semantic reason. Prefer removing a
  non-semantic divider to preserving a table-like rhythm;
- reduce type, increase leading, regroup copy, or enlarge useful diagram area
  together. Do not preserve an oversized hierarchy merely because it was once
  described as readable.

Run a first-impression test while the original raster is displayed at its
intended publication width: look away, then look back for one second. The relationship or
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
- `pass` only when the full raster, intended-size display, and every crop
  pass;
- `revision_required` for any content, collision, legibility, connector, or
  spacing defect.

For a failure, send exact coordinates or named regions and the observed problem
back to `dev-log-infographic`. Require a new versioned raster, regenerate all
affected views from that raster, and rerun the complete visual QA. Do not accept
an automated check as a substitute for actual raster inspection.

Record in `audit.md`:

- candidate path, dimensions, hash, type, question, placement, and alt text;
- source sizes for headline, primary labels, supporting copy, and caveat;
- measured text gaps, scene-envelope or rule clearances, headline-height share,
  and intended display width;
- full raster, intended-size display, and crop observations;
- whether the composition passed the one-second relationship test and the
  framed-poster rejection;
- every `problem -> revision -> re-verification`;
- final stage result.

## Handoff

Return the stage result and visual evidence to `dev-log-workspace`. Do not
change hero-image standards, set the article ready by yourself, commit, or push.
