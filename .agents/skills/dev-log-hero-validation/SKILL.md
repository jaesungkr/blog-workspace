---
name: dev-log-hero-validation
description: Independently validate dev.log hero-image candidates for iconic topic recognition and large-enterprise campaign quality. Use for full-size and thumbnail visual QA, subject-swap tests, art-direction review, composition, materials, lighting, originality, reference comparison, image defects, final candidate selection, or decisions to edit versus regenerate. Keep this gate separate from infographic legibility and Git delivery.
---

# dev.log hero validation

Judge whether the candidate is memorable, unmistakably connected to the post,
and finished to a major enterprise campaign standard. A technically valid or
pretty image is not enough.

## Load context

1. Resolve the canonical repository as the directory three levels above this
   skill directory.
2. Read `standards/image-guide.md` and
   `standards/image-art-direction.md` completely.
3. Read the target article, brief, evidence, audit, final prompt, and intended
   recognition cue.
4. Open the candidate at full resolution and required thumbnail size.
5. Compare user or official references side by side when they exist.

## Validation gates

### Article and subject fit

- The image embodies the retained message rather than the broad category.
- A named subject is recognizable at thumbnail size through a specific,
  brand-safe cue grounded in what it does, consumes, produces, or inhabits.
- The subject-swap test fails: replacing the actual subject with an unrelated
  one would weaken the image.
- The image does not depend only on alt text, a logo, or an embedded title.

### Iconic campaign quality

- One memorable visual idea and focal hierarchy read within one second.
- Composition uses confident scale, controlled asymmetry or justified balance,
  crop-safe negative space, and intentional depth.
- Palette is restrained and purposeful; lighting has a plausible physical
  cause and controlled shadows.
- Materials have believable surface response, thickness, contact, optics, and
  microtexture.
- The finish feels commissioned, current, and editorial rather than generic,
  stiff, cheap, dated, plasticky, cluttered, or obviously AI-generated.
- Technology clichés such as dark neon, glass panels, floating dashboards,
  plastic icons, fake terminals, circuit wallpaper, robots, and arbitrary
  shields are absent unless the article specifically requires them.

### Integrity and craft

- Perspective, anatomy, edges, scale, interaction, reflections, and shadows are
  coherent.
- No pseudo-writing, malformed details, halos, excessive bloom, watermark,
  fabricated UI, fake proof, or unsupported success symbolism remains.
- Any necessary embedded text is exact and legible.

## Decision loop

Return:

- `pass` only after both full-size and thumbnail inspection pass;
- `targeted_edit` for a local defect when the concept, medium, composition, and
  finish are already strong;
- `regenerate` when the metaphor, subject recognition, hierarchy, medium,
  lighting, palette, originality, or overall taste is weak.

Send edits or regeneration back to `dev-log-hero-image`, then inspect the new
version from the beginning. Never polish a generic direction through repeated
local edits.

Record in `audit.md`:

- observed full-size and thumbnail findings;
- subject-recognition and subject-swap results;
- reference comparison;
- `problem -> revision -> re-verification`;
- selected version, dimensions, hash, placement, and alt text.

## Handoff

Return the stage result and evidence to `dev-log-workspace`. Do not approve or
modify supporting infographics, set the article ready by yourself, commit, or
push.
