# Supporting infographic guide

Read this file only when the user explicitly requests an infographic or the
supporting-infographic gate in `standards/image-guide.md` passes. The hero image
remains a separate required deliverable and keeps its existing editorial role.

## Purpose

A supporting infographic should let a reader grasp one important relationship
faster than prose alone. It is part of the explanation, not decoration, a
second hero, or a poster-sized summary of the whole article.

Good candidates include:

- three or more linked steps whose order or transformation matters;
- a mechanism with interacting parts;
- a decision path with meaningful branches or exceptions;
- a comparison whose shared and different stages matter;
- an experiment from input and conditions to observed result;
- a troubleshooting path from symptom to check and next action.

Skip the infographic when:

- it only repeats a short paragraph, list, or table;
- the reader needs exact values better served by HTML text or a table;
- the concept requires so many labels that it will fail at mobile width;
- visual simplification would overstate certainty or remove a critical caveat;
- it is proposed only to make the post look more complete.

Write the retained message as one plain sentence before planning the image. If
a short paragraph, a two-value callout, bullets, or an existing table carries
that sentence just as quickly, do not create an infographic. Never expand a
small idea into extra labels or sections merely to fill a canvas. A required
lead visual may be an exception only when scale, sequence, or transformation
does explanatory work that the repeated sentence would not.

Default to no supporting infographic for Reflections. Use one there only when
the user explicitly requests it or when a visual relationship is indispensable
to understanding the reflection.

## Quantity and placement

Default to one image after the core explanation it clarifies. Do not place it
automatically beneath the title or at the end.

Use more than one only when all conditions hold:

1. each image answers a different reader question;
2. combining them would create an illegible or misleading image;
3. each image can be understood at its intended placement;
4. the extra image earns its space instead of repeating context.

Prefer one overview infographic over a multi-card series. Use a series only
when the article itself teaches a staged journey and each stage needs separate
attention.

## Plan before rendering

Record in `brief.md`:

- the relationship the reader should understand at a glance;
- why prose, bullets, or a table are not sufficient;
- the type: process, mechanism, decision, comparison, experiment, or
  troubleshooting;
- the exact section after which the image should appear;
- for multiple images, the distinct reader question answered by each.

Build the content from the article and `evidence.md`. Use the smallest complete
structure: normally one headline, two to five primary blocks, one short label
per block, and at most one decision-changing caveat. Do not add a block for
symmetry. Remove kickers, subheads, rhetorical questions, instructional
footers, and conclusion bars unless their absence creates a real ambiguity.
Keep necessary caveats near the claim they limit.

## Rendering method

Produce a final raster image under the post's `assets/` directory with a
descriptive ASCII filename such as `<slug>-infographic.png`. Do not overwrite an
existing final; add `-v2` when needed.

Use deterministic layout for all publication copy:

- render exact Korean text, numbers, units, arrows, and labels with a
  code-native or template-based layout;
- use a Korean-capable font and verify glyph rendering;
- use image generation only for an optional illustration, texture, or visual
  motif that does not carry factual text;
- never accept pseudo-writing or ask an image model to reproduce exact copy;
- keep editable copy or layout source in `artifacts/` when practical.

Do not confuse deterministic typography with a finished visual concept. A
layout made only from headings, rounded cards, generic icons, and arrows is a
slide, not automatically a publishable infographic. Each primary block should
carry meaning through a specific scene, diagram, comparison, transformation, or
real data relationship before the labels are read.

When a supplied reference succeeds through narrative illustration, character
expression, or a visible mechanism, transfer those principles rather than only
its palette and spacing. Use image generation for a text-free illustration
layer when it materially improves the explanation, then add exact Korean copy
deterministically. Do not copy the reference's characters, exact layout, or
distinctive centerpiece.

Use a portrait 3:4 or 4:5 canvas by default for in-article mobile reading.
Use a shorter portrait or square canvas when sparse content would otherwise
invite decorative filler or excessive empty height.
Prefer a calm editorial layout, strong reading order, restrained colors, and
simple connectors over dense dashboard styling.

Mobile legibility is a floor, not a reason to enlarge every text role. Keep one
publication raster at its source dimensions; do not create a reduced-size
mobile derivative. Convert source typography to its 360px CSS-display
equivalent with
`source font px × 360 ÷ source canvas width`. Use these starting bands:

- headline: `20-24px`;
- primary labels: `15-18px`;
- supporting copy: `12-14px`;
- caveat: `11-12px`.

Unless the visual role clearly needs stronger type, start in the lower half of
those bands: headline `20-21px`, primary labels `15-16px`, supporting copy
`12-13px`, and caveats `11-11.5px`. Passing the broad band is necessary but not
sufficient. When words feel large relative to the mechanism or illustration,
reduce the affected hierarchy by about `4-8%` while staying above the mobile
floor, then reopen the quiet space around labels. Do not treat a previous
upper-band value as the default for a new canvas.

Keep the headline zone near 22% or less of canvas height. Reduce copy or
restructure the visual when a role falls outside its band; do not make the
headline larger while shrinking body copy. In the original raster's 360px CSS
display, the relationship must have at least equal visual presence to the
headline.

Avoid enclosing the whole explanation in one large rounded card by default.
Such a frame often makes the actual diagram feel like a small insert inside a
poster. Use open space, meaningful regions, or boundaries that encode the
relationship. Where a frame is necessary, preserve generous internal quiet
space and keep text, badges, and icons from filling each region.

## Content integrity

- Map every number, factual label, comparison, and conclusion to the article or
  `evidence.md`.
- Do not introduce stronger causality, certainty, ranking, or performance
  claims than the text supports.
- Preserve the key exception or limit when omitting it would change the
  decision.
- Avoid fabricated UI, logos, quotations, testimonials, and decorative charts
  without real data.
- If exact data is the main value, keep the table in the article even when an
  infographic provides an overview.

## Quality gate

Inspect the final raster at full resolution and display that same untouched
raster in a browser at `width:360px`. Do not resize, re-encode, save, or commit
a smaller QA raster.

- The headline and primary relationship are clear without zooming.
- Inspect the original raster at its 360px CSS display size, not a zoomed
  preview or exported small copy.
- Record the 360px-equivalent size of each text role and the headline-height
  share. Treat the default bands above as a release gate unless a semantic
  exception is documented.
- Look away and back for one second. Reject the image if it reads first as a
  large headline over a small framed card, slide, or boxed text sheet instead
  of the intended relationship.
- Reading order is unambiguous.
- The image uses the smallest complete structure, normally two to five primary
  blocks, and contains no block added only for balance or decoration.
- No kicker, subhead, rhetorical question, footer, or conclusion line repeats
  what the surrounding prose, headline, or visible relationship already says.
- With the labels mentally hidden, the scene or diagram still distinguishes the
  problem, transformation, and result. Reject interchangeable card grids.
- Body copy is limited to one or two short lines per block where possible.
- Every primary region retains visible quiet space. Readability alone does not
  excuse oversized labels, crowded blocks, or weak typography-to-canvas scale.
- Treat user feedback that the type dominates the image as release-blocking.
  Revise the hierarchy and rerun the full-size, 360px, crop, and type-scale
  checks before approval.
- Korean glyphs, numbers, units, arrows, and line breaks are exact.
- Contrast, spacing, and touch-sized visual separation work on mobile.
- Connectors point to the intended objects and do not cross confusingly.
- No clipped text, orphaned label, overlap, pseudo-writing, or low-resolution
  supporting artwork remains.
- The image still helps after surrounding prose is read and does not merely
  restate it.
- When a visual reference exists, compare it side by side with the final at a
  similar display size. Record the transferable qualities used and the largest
  remaining gap.

## Final overlap audit

Do not approve a supporting infographic from the whole-image preview alone.
Perform this audit on the exact final raster:

1. Open the full raster, then display that exact raster in a browser at
   `width:360px` without creating a derivative file.
2. Create enlarged crops around every headline, primary block, connector,
   arrowhead, icon-label pair, footnote, and caveat.
3. Trace a small clear zone around every text block. Reject any line,
   arrowhead, marker, icon, shadow, texture, or crop boundary that enters the
   glyph area or makes a word harder to read.
4. For SVG output, inspect the complete painted bounds of markers and strokes.
   Marker defaults may scale with stroke width, so source path endpoints alone
   are not evidence that an arrow clears nearby text. Prefer explicit
   `markerUnits="userSpaceOnUse"` and explicit marker dimensions when exact
   clearance matters.
5. Read the labels once in normal order and once by scanning only the text
   blocks. This second pass catches words hidden by visually dominant arrows or
   illustrations.
6. After any correction, write a versioned final raster, refresh its 360px CSS
   browser display and every affected full-raster crop, and repeat the audit.
   Record `problem -> revision -> re-verification` in `audit.md`.

Record the decision even when it is `없음`. When an infographic exists, record
its final path, type, reader question, placement, Korean alt text, copy/evidence
source, and full-size/360px CSS-display inspection in `audit.md`. Do not keep a
downscaled mobile raster in the post bundle.

Do not insert a local filesystem Markdown image link into `article.md`. The user
uploads the raster to Tistory manually; record placement guidance separately.
