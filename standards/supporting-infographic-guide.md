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

Build the content from the article and `evidence.md`. Reduce it to one headline,
three to five primary blocks, and only the labels needed to preserve meaning.
Keep caveats near the claim they limit.

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

Use a portrait 3:4 or 4:5 canvas by default for in-article mobile reading.
Choose another ratio only when the information structure clearly requires it.
Prefer a calm editorial layout, strong reading order, restrained colors, and
simple connectors over dense dashboard styling.

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

Inspect the final raster at full resolution and at 360 CSS pixels wide.

- The headline and primary relationship are clear without zooming.
- Reading order is unambiguous.
- The image has three to five primary blocks unless a simpler structure works.
- Body copy is limited to one or two short lines per block where possible.
- Korean glyphs, numbers, units, arrows, and line breaks are exact.
- Contrast, spacing, and touch-sized visual separation work on mobile.
- Connectors point to the intended objects and do not cross confusingly.
- No clipped text, orphaned label, overlap, pseudo-writing, or low-resolution
  supporting artwork remains.
- The image still helps after surrounding prose is read and does not merely
  restate it.

Record the decision even when it is `없음`. When an infographic exists, record
its final path, type, reader question, placement, Korean alt text, copy/evidence
source, and full-size/mobile inspection in `audit.md`.

Do not insert a local filesystem Markdown image link into `article.md`. The user
uploads the raster to Tistory manually; record placement guidance separately.
