---
name: dev-log-infographic
description: Decide whether a dev.log post needs a supporting infographic and create or revise the candidate when it does. Use for process, mechanism, decision, comparison, experiment, or troubleshooting visuals; deterministic Korean labels; balanced typography, painted-bound spacing, and canvas composition; HTML, SVG, or template layout sources; raster assets; alt text; and placement records. Hand every candidate to dev-log-infographic-validation and keep the hero workflow separate.
---

# dev.log supporting infographic creation

Create an explanatory visual only when it materially reduces reader effort.
The independent infographic validator owns final approval.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory.
2. Read `standards/image-guide.md`,
   `standards/image-art-direction.md`, and
   `standards/supporting-infographic-guide.md` completely.
3. Read the target `brief.md`, `evidence.md`, `article.md`, and `audit.md`.
4. Inspect every existing infographic raster and editable source.

## Apply the gate

Add an infographic only when a process, mechanism, decision, comparison,
experiment, or troubleshooting path becomes materially easier to understand at
a glance. Skip decoration, table duplication, and poster-sized article
summaries. Default to none for Reflections unless explicitly requested or
indispensable.

Before choosing a visual, write its retained message as one plain sentence.
If a short paragraph, two-value callout, bullets, or an existing table conveys
that message just as quickly, record `not_applicable`. Do not manufacture extra
sections to justify an image. An exception is a required lead visual that
encodes the relationship through scale, sequence, or transformation instead of
repeating the sentence as a poster; record that separate media role explicitly.

Record in `brief.md`:

- the reader question;
- the relationship to show;
- why prose, bullets, or a table are insufficient;
- the type;
- the exact placement;
- why any additional image answers a distinct question.

Record `not_applicable` in `audit.md` when the gate fails.

## Design the candidate

1. Use the smallest complete structure. Default to one headline, two to five
   primary blocks, and only the labels required to preserve meaning. A simple
   contrast may use two blocks; do not add a third block for symmetry.
2. Set a copy budget before layout. Prefer one headline, one short label per
   primary block, and at most one decision-changing caveat. Omit kickers,
   subheads, rhetorical questions, instructional footers, and conclusion bars
   unless removing one makes the relationship ambiguous. Delete labels such as
   `무엇으로 판단할까요?` when the diagram or surrounding prose already
   supplies that instruction.
3. Map every factual label, number, comparison, and conclusion to the article
   or `evidence.md`. Preserve a limit when omitting it changes the decision.
4. Use a meaningful process, scene, transformation, comparison, or data
   relationship. Reject interchangeable card grids and generic slide layouts.
5. Choose the canvas ratio from the retained relationship. Default to portrait
   3:4 or 4:5 for multi-step material, but use a shorter portrait or square
   canvas when sparse content would otherwise create decorative filler.
6. Render exact Korean copy, numbers, units, arrows, and labels with a
   deterministic code-native or template layout and a Korean-capable font.
7. Use image generation only for an optional text-free illustration layer that
   materially improves explanation.
8. Keep connectors simple and reserve clear space around text. For SVG markers,
   prefer explicit `markerUnits="userSpaceOnUse"` and explicit dimensions.
9. Set type from the source canvas and the intended editorial hierarchy. Start
   smaller than feels necessary, compare it with the illustration at the final
   publication size, and enlarge only the roles that are genuinely hard to
   read. Do not use a minimum CSS-pixel band to force every label upward.
10. Measure painted glyph bounds rather than baseline coordinates. Keep visible
   vertical air between adjacent lines; use roughly `0.6-1.0×` the smaller
   line's painted height as a starting gap and more between semantic groups.
   Add a render-time assertion when deterministic layout repeatedly crowds the
   same roles. Do not let labels, badges, or company lists fill a region merely
   because their bounding boxes technically fit.
   Measure illustration and connector envelopes as well. Never let a painted
   object touch a section rule. Repeated boundaries need optically consistent
   clearance on both sides; when a rule carries no meaning, remove it and use
   aligned anchors plus negative space. Add envelope assertions for recurring
   scene bands.
11. Keep the headline area compact, usually about 18% or less of canvas height.
   The relationship or diagram must remain the dominant visual, not a large
   title sitting above a small framed panel.
12. Do not use one large rounded outer card as the default container. Prefer an
   open field, meaningful regions, or a boundary that carries information.
   When a frame is necessary, leave generous internal breathing room and make
   the diagram feel native to the canvas rather than squeezed into an inset.
13. Reserve visible quiet space inside every primary region. If labels and copy
    consume most of a block, shorten the copy, simplify the structure, or
    increase useful diagram area. Solve cramped composition by adjusting font
    size, leading, grouping, copy length, and useful visual area together.
14. Preview the untouched full-resolution candidate and the actual intended
    publication width early. Reject it when the first impression is `headline
    + boxed text` instead of the intended relationship. Treat direct user
    feedback that type dominates or spacing feels cramped as a required
    revision even when no collision is present.
    Do not resize, re-encode, save, or commit a separate QA derivative; inspect
    the publication raster itself.

Save:

- a versioned final-candidate raster under `assets/`; never overwrite an older
  candidate;
- practical editable source and render code under `artifacts/`;
- placement, alt text, type, copy source, production method, and candidate hash
  in `audit.md`;
- the source font sizes, painted-bound gaps, headline-height share, intended
  publication width, and any deliberate hierarchy exception in `audit.md`.

Do not add a local filesystem image link to `article.md`.

## Handoff

Return the candidate raster, editable source, copy map, intended placement, and
known risks to `dev-log-infographic-validation`. Do not approve the image,
change hero generation, set the post to `ready`, commit, or push.
