---
name: dev-log-infographic
description: Decide whether a dev.log post needs a supporting infographic and create or revise the candidate when it does. Use for process, mechanism, decision, comparison, experiment, or troubleshooting visuals; deterministic Korean labels; balanced mobile typography and canvas composition; HTML, SVG, or template layout sources; raster assets; alt text; and placement records. Hand every candidate to dev-log-infographic-validation and keep the hero workflow separate.
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

Record in `brief.md`:

- the reader question;
- the relationship to show;
- why prose, bullets, or a table are insufficient;
- the type;
- the exact placement;
- why any additional image answers a distinct question.

Record `not_applicable` in `audit.md` when the gate fails.

## Design the candidate

1. Reduce the content to one headline, three to five primary blocks, and only
   the labels required to preserve meaning.
2. Map every factual label, number, comparison, and conclusion to the article
   or `evidence.md`. Preserve a limit when omitting it changes the decision.
3. Use a meaningful process, scene, transformation, comparison, or data
   relationship. Reject interchangeable card grids and generic slide layouts.
4. Default to a portrait 3:4 or 4:5 canvas for in-article mobile reading.
5. Render exact Korean copy, numbers, units, arrows, and labels with a
   deterministic code-native or template layout and a Korean-capable font.
6. Use image generation only for an optional text-free illustration layer that
   materially improves explanation.
7. Keep connectors simple and reserve clear space around text. For SVG markers,
   prefer explicit `markerUnits="userSpaceOnUse"` and explicit dimensions.
8. Treat mobile legibility as both a minimum and a maximum. Before finalizing,
   convert source font sizes to their 360px CSS-display equivalents:
   `source font px × 360 ÷ source canvas width`. Start with these bands:
   headline `20-24px`, primary labels `15-18px`, supporting copy `12-14px`,
   and caveats `11-12px`. Deviate only when the visual role clearly
   requires it and record why.
9. Keep the headline area at about 22% or less of canvas height. The relationship
   or diagram must remain the dominant visual, not a large title sitting above
   a small framed panel.
10. Do not use one large rounded outer card as the default container. Prefer an
    open field, meaningful regions, or a boundary that carries information.
    When a frame is necessary, leave generous internal breathing room and make
    the diagram feel native to the canvas rather than squeezed into an inset.
11. Reserve visible quiet space inside every primary region. If labels and copy
    consume most of a block, shorten the copy, simplify the structure, or
    increase useful diagram area. Do not solve crowding by shrinking supporting
    copy below the mobile floor.
12. Preview the untouched full-resolution candidate in a browser at
   `width:360px` early. Do not resize, re-encode, save, or commit a smaller
   raster derivative for mobile QA. Reject the browser display when the first
   impression is `headline + boxed text` instead of the intended relationship,
   even if every word is technically readable.

Before handoff, run the validator's deterministic type-scale checker with the
actual source values:

```bash
python3 ../dev-log-infographic-validation/scripts/check_mobile_type_scale.py \
  --canvas-width 1080 --canvas-height 1350 --header-height 260 \
  --headline 64 --primary 52 --support 40 --caveat 36
```

Use repeated flags when a role has multiple sizes. Treat a failure as a layout
revision, not as permission to shrink all copy.

Save:

- a versioned final-candidate raster under `assets/`; never overwrite an older
  candidate;
- practical editable source and render code under `artifacts/`;
- placement, alt text, type, copy source, production method, and candidate hash
  in `audit.md`;
- the 360px CSS-display-equivalent type scale, headline-height share, and any
  justified deviation from the default bands in `audit.md`. Do not save a
  reduced-size QA raster under the post bundle.

Do not add a local filesystem image link to `article.md`.

## Handoff

Return the candidate raster, editable source, copy map, intended placement, and
known risks to `dev-log-infographic-validation`. Do not approve the image,
change hero generation, set the post to `ready`, commit, or push.
