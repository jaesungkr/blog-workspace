# Blog image guide

Read `standards/image-art-direction.md` with this file. The present guide
defines delivery, placement, and factual constraints; the art-direction guide
defines the concept and visual quality required for publication.

## Required hero deliverable

- This required-hero contract applies to standard posts. For
  `format: rich-post`, a validated first-party screenshot or
  provenance-checked official, user-supplied, or simulated raster may serve as
  the lead visual; an original generated hero is optional. If the selected
  rich-post lead is generated, apply this entire guide and the normal hero
  validation gate.
- Generate at least one original raster image for every complete standard post.
  Do not satisfy this requirement with a stock-image link, web-search result,
  SVG placeholder, or prompt alone.
- Treat this required image as the hero image. Preserve its visual, editorial
  role; do not add explanatory panels or turn it into an infographic merely
  because the post also benefits from a supporting visual.
- Use the built-in image-generation workflow.
- Generate after the article's angle and central message are stable so the image
  matches the published argument.
- Inspect the result at thumbnail size and full resolution before delivery.
  Apply the complete quality gate in `image-art-direction.md`.
- For a post about a named subject, verify that at least one visible cue
  identifies that subject rather than only the broad category. The cue should
  come from the subject's core action, native input/output, environment,
  object, or a brand-safe motif. Do not use a logo or title as a shortcut when
  the image can communicate the connection visually.
- Use a targeted correction only when the concept, medium, composition, and
  finish are already strong and the defect is local. Regenerate from a new
  direction when the result is generic, stiff, cheap, dated, plasticky,
  cluttered, overly dark, or visibly AI-generated.
- Save the selected final image in the post's `assets/` directory with a
  descriptive ASCII filename. Do not overwrite an existing file; add `-v2`
  when needed.
- Preview the image for the user and record its path, recommended article
  position, concise Korean alt text, and final generation prompt in `audit.md`.

## Default hero visual

Unless the user specifies otherwise:

- Create one landscape hero image suitable for the top of a Tistory post.
- Use a 16:9 or similarly wide composition with a clear central subject and safe
  margins for responsive cropping.
- Prefer a natural editorial photograph for health, culture, sports, or
  everyday topics.
- Prefer one strong editorial metaphor for abstract technology and LLM topics.
  Choose photography, a crafted still life, contemporary illustration, an
  architectural/material study, or justified 3D deliberately. Do not default
  to a generic workspace scene.
- Prefer a restrained contemplative photograph or illustration for Reflections;
  avoid literal depictions of God or an identifiable real preacher unless the
  user supplies a reference and requests it.
- For `Reflections/말씀 묵상`, use the category-specific visual system in
  `standards/reflections-guide.md`: a bright, pale, pattern-led abstract image
  is the default and takes precedence over the general Reflections photograph
  option.
- Use no embedded title, labels, logos, UI trademarks, watermark, or decorative
  Korean text unless exact in-image text is essential and explicitly requested.
- Avoid clickbait expressions, medical fear imagery, fake product branding,
  fabricated interfaces, misleading before/after claims, and visuals that imply
  evidence the article does not establish.
- Technology alone is not a reason to use a dark background. Avoid default
  neon, glassmorphism, glowing circuits, symmetrical pods, floating dashboards,
  and plastic 3D icons.

## Match image to article role

Choose one useful role:

| Article need | Image role | Default approach |
|---|---|---|
| Search-entry overview | Hero image | One memorable scene or metaphor embodying the main conclusion |
| Product or tool comparison | Comparison concept | Neutral side-by-side objects without fake logos or labels |
| Mechanism explanation | Educational visual | Simple accurate composition; minimize text |
| Tutorial | Result scene | Show the practical outcome rather than a generic laptop |
| Reflections | Contemplative scene | Symbolic but restrained scene connected to the passage |

Do not generate a dense infographic when accuracy depends on many labels. Use a
table in the article and a simpler supporting image instead.

## Optional supporting infographic

The hero and a supporting infographic have separate jobs. The hero earns
attention and establishes the topic; the infographic reduces the effort needed
to understand one important relationship.

Consider a supporting infographic only after the article's explanation is
stable. Add one when a process, mechanism, decision, comparison, experiment, or
troubleshooting path becomes materially easier to scan than in prose alone.
Skip it when it would only decorate, repeat a short list, or reproduce a table.

- Default to none for Reflections. Use one only when explicitly requested or
  indispensable to a relationship in the reflection.
- Default to one for other categories when the gate passes.
- Add more only when each image answers a distinct reader question and remains
  legible on its own.
- Place each image immediately after the core explanation it clarifies.
- Read `standards/supporting-infographic-guide.md` before creating one.
- Keep exact Korean copy, numbers, arrows, and factual labels deterministic.
  Do not ask an image model to typeset publication copy.

## Prompt scaffold

Form two or three short concept directions internally, choose the least generic
one that communicates the article's retained message, then shape the request
using only relevant lines:

```text
Use case: <photorealistic-natural | stylized-concept | scientific-educational>
Asset type: Korean Tistory blog hero image
Primary request: <one concrete visual expression of the article's core message>
Creative intent: <one idea or feeling>
Visual idea: <one metaphor or scene, not an object inventory>
Subject-recognition cue: <the visible detail that identifies the named subject at thumbnail size>
Art direction: <photography, crafted set, editorial illustration, material study, or justified 3D>
Scene/backdrop: <specific environment>
Subject: <main subject>
Style/medium: <specific medium and visible finish>
Composition/framing: wide landscape, immediate focal hierarchy, controlled depth, crop-safe negative space
Lighting/mood: <plausible key light, fill, shadow character, emotional register>
Color palette: <neutrals and intentional accents>
Materials/textures: <specific believable surfaces>
Constraints: factually neutral, publication-ready, no logos, no watermark, no unnecessary embedded text
Avoid: topic-specific cliches, generic AI artifacts, clutter, sensationalism, unsupported claims
```

## Placement and accessibility

- Recommend `대표 이미지 - 제목 바로 아래` for the hero by default.
- If the visual explains a mechanism or comparison, recommend the relevant
  section instead.
- Write alt text that describes what is visible and why it matters in one
  concise Korean sentence. Do not stuff SEO keywords.
- Do not insert a local filesystem Markdown image link into the Tistory article
  body. The user uploads the saved image manually; provide placement guidance
  separately.
