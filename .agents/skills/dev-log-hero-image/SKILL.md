---
name: dev-log-hero-image
description: Create or revise the required hero image for a dev.log Tistory post. Use when a post needs a representative image, hero concept, image-generation prompt, subject-recognition cue, versioned raster asset, alt text, or placement record. Aim for an iconic topic-specific image with large-enterprise campaign quality, then hand the candidate to dev-log-hero-validation; do not create supporting infographics or approve the final image.
---

# dev.log hero image creation

Create one visually led hero candidate. The independent hero validator decides
whether it is publishable.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory.
2. Read `standards/image-guide.md` and
   `standards/image-art-direction.md` completely.
3. Read the target `brief.md`, `evidence.md`, `article.md`, and `audit.md`.
4. Inspect existing hero versions and any user references before planning.
5. Use the built-in image-generation workflow for the raster.

## Build the concept

1. Wait until the article angle and retained message are stable.
2. Form two or three directions internally and select the least generic one.
3. Reduce the concept to one memorable visual idea, not a feature inventory.
4. For a named product, tool, person, place, or event, define one visible
   recognition cue grounded in its core action, native input/output,
   environment, object, or brand-safe motif.
5. Apply the subject-swap preflight: if an unrelated subject could replace the
   named subject without weakening the idea, strengthen the cue.
6. Choose the medium deliberately: editorial photography, crafted still life,
   architectural/material study, contemporary illustration, or justified 3D.
7. Specify visible production choices rather than adjectives alone:
   composition, crop-safe negative space, plausible key and fill light,
   restrained palette, believable materials, texture, contact, and depth.

The target is an iconic editorial image that could appear in a major enterprise
technology campaign: immediate hierarchy, confident restraint, distinctive
subject identity, and no generic AI visual language.

## Generate the candidate

- Default to a wide 16:9 or similar landscape hero.
- Keep it visually led. Do not add explanatory panels or turn it into an
  infographic.
- Avoid fake UI, pseudo-code, arbitrary logos, watermarks, unsupported outcomes,
  neon technology clichés, glassmorphism, floating dashboards, plastic icons,
  and generic laptop scenes.
- Generate exact embedded text only when essential and explicitly justified.
- Save a new inspected raster under the post's `assets/` directory. Never
  overwrite a prior candidate; increment `-v2`, `-v3`, and so on.

Record in `audit.md`:

- candidate path and dimensions;
- recommended placement and concise Korean alt text;
- final prompt and generation method;
- intended recognition cue and why it belongs to this subject;
- relevant reference roles and constraints.

## Handoff

Return the candidate path, prompt, intended cue, and known risks to
`dev-log-hero-validation`. Do not declare the candidate final, modify
infographic standards, set the post to `ready`, commit, or push.
