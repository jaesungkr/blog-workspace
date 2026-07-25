# Blog image art direction

This file is the Git-tracked source of truth for the visual quality of
public-facing dev.log images. Read it with `image-guide.md` for every complete
post or image task.

The built-in image-generation skill is an execution tool. When its generic
defaults conflict with this file, this file wins for dev.log work.

## Quality bar

Treat every final image as commissioned editorial or campaign work, not a
technically correct illustration. A valid prompt result is not automatically a
publishable image.

Prefer:

- one memorable visual idea over an inventory of features;
- restrained hierarchy over evenly weighted objects;
- tactile, believable surfaces over generic glossy plastic;
- controlled asymmetry and depth over rigid centered symmetry;
- intentional negative space over filling the canvas;
- tonal nuance and a limited palette over neon contrast;
- editorial confidence over explanatory clutter.

Reject a result that is merely accurate but still looks generic, stiff, cheap,
dated, plasticky, cluttered, or obviously AI-generated.

## Concept before style

Before generating, form two or three short directions internally and choose the
least generic direction that communicates the article's retained message. Each
direction should identify:

1. the single idea the viewer should understand or feel;
2. the visual metaphor or scene carrying that idea;
3. the medium that makes the metaphor convincing;
4. the composition and emotional register;
5. the most likely cliche or factual failure.

Do not expose internal ideation unless the user asks to compare directions.

A concept is not a list of objects. `Two terminals, branch lines, database,
diff window, and magnifying glass` is an inventory. `Two precise paths split
from one source and reunite only at a deliberate inspection surface` is a
visual idea.

For a named subject, a strong metaphor still needs subject identity. Choose one
visible recognition cue grounded in what the subject uniquely does, consumes,
produces, inhabits, or is commonly associated with. Apply a subject-swap test:
if an unrelated tool, person, place, or event could replace the named subject
without weakening the image, the concept is too generic. Strengthen the cue
without turning the composition into a logo card, title slide, or feature
inventory.

## Translate taste into visible choices

Do not use `premium`, `polished`, `modern`, `cinematic`, or `elegant` as the
entire art direction.

| Weak direction | Visible decisions |
|---|---|
| premium | restrained palette, controlled highlights, generous negative space, precise materials |
| modern | contemporary editorial composition, clean hierarchy, current but non-trendy materials |
| cinematic | motivated key light, shaped shadows, intentional depth, coherent atmosphere |
| elegant | few elements, refined proportions, quiet contrast, graceful spacing |
| corporate | confident, clear, credible, calm; no anonymous boardroom stock imagery |
| futuristic | plausible materials and interactions; no sci-fi filler |

Specify physical causes. Use `large diffused window light with a narrow warm
edge light` instead of `beautiful lighting`, or `uncoated paper, brushed
aluminum, and softly frosted acrylic` instead of `premium materials`.

## Choose the medium deliberately

Choose the medium from the message rather than defaulting to 3D:

- Editorial photography: credibility, human scale, tactile realism, products,
  work, culture, and everyday technology.
- Crafted still life or practical miniature set: abstract systems that need a
  premium physical metaphor.
- Editorial illustration: ideas that benefit from simplification, wit, or
  controlled abstraction.
- Architectural or material study: structure, flow, separation, coordination,
  reliability, and scale.
- 3D rendering: only when volume, impossible geometry, or a product-like object
  is essential. Require plausible materials, gravity, optics, and contact.
- Diagram or infographic: when accuracy and labels matter more than mood. Do
  not disguise a diagram as campaign art.

For a hero image, ask whether a real creative team would photograph, build,
illustrate, or render the idea. Choose that medium explicitly.

## Technology images without AI cliches

Technology alone is not a reason to make an image dark.

Do not default to:

- dark navy backgrounds with cyan, violet, or orange neon;
- glassmorphism boxes, glowing tubes, floating panels, or holographic UI;
- centered laptops or dashboards surrounded by feature icons;
- circuit-board backgrounds, network-node wallpaper, or binary code rain;
- robot heads, glowing brains, chrome humanoids, or generic cloud symbols;
- perfectly mirrored left and right pods;
- plastic rounded cubes with tiny pseudo-code;
- excessive bloom, volumetric fog, lens flares, or cyberpunk atmosphere;
- locks and shields used as vague symbols of safety;
- arrows pointing upward as a generic success claim.

For technology and software topics, prefer:

- luminous neutral or daylight-led scenes unless darkness serves the story;
- sophisticated physical metaphors made from paper, glass, metal, fabric,
  architecture, or carefully staged objects;
- subtle traces of process rather than fake interfaces;
- neutrals plus one intentional accent color;
- human-scale evidence such as annotations, inspection marks, or crafted
  organization without fake product screens;
- material microtexture and slight imperfection that prevent a sterile CG look.

Use dark art direction only when it is user-requested, brand-supported, or
conceptually necessary.

## Composition, light, color, and materials

### Composition

- Establish one focal hierarchy that reads at thumbnail size.
- Use asymmetry, cropping, foreground overlap, or depth when they add energy.
- Keep crop-safe margins without shrinking every object into the center.
- Avoid giving all objects the same scale, angle, and visual weight.
- Leave quiet areas. Premium work often communicates through omission.

### Light

- Name a plausible key light and supporting fill or edge light.
- Prefer broad soft sources, natural daylight, shaped studio light, or
  deliberate hard sun based on the concept.
- Do not light every edge. Controlled shadow is part of the composition.
- Check that transparent and reflective materials obey plausible optics.

### Color

- Start with neutrals and one intentional accent unless the brief provides a
  palette.
- Avoid pure black backgrounds and maximum saturation by default.
- Use contrast to guide attention, not to decorate every object.

### Materials

- Describe surface finish and construction: uncoated paper fibers, sandblasted
  glass, brushed aluminum, molded pulp, woven textile, matte ceramic, or
  painted wood.
- Avoid generic `glossy 3D` and weightless floating objects.
- Require contact shadows, believable thickness, and microtexture when realism
  matters.

## Reference use

Use supplied references for transferable principles such as composition
rhythm, tonal range, material treatment, lighting softness, negative space, and
finish.

Do not copy a protected logo, mascot, exact campaign layout, living artist's
signature style, or another image's distinctive centerpiece. Describe the
visual principles rather than naming a brand as the entire prompt.

Without a supplied reference, use broad disciplines such as `editorial still
life`, `architectural photography`, `museum-catalog object study`, `crafted
paper set`, or `contemporary magazine illustration`.

## Prompt scaffold

Use only the relevant lines:

```text
Use case: <photorealistic-natural | stylized-concept | scientific-educational>
Asset type: Korean Tistory blog hero image
Primary request: <concrete expression of the retained message>
Creative intent: <one idea or feeling>
Visual idea: <one metaphor or scene, not a feature inventory>
Art direction: <photography, crafted set, editorial illustration, material study, or justified 3D>
Scene/backdrop: <specific environment>
Subject: <main focal element>
Style/medium: <specific medium and visible finish>
Composition/framing: <hierarchy, viewpoint, depth, crop-safe negative space>
Lighting/mood: <plausible key light, fill, shadow character, emotional register>
Color palette: <neutrals and intentional accents>
Materials/textures: <specific believable surfaces>
Constraints: factually neutral, publication-ready, no logos, no watermark, no unnecessary text
Avoid: <topic-specific cliches, generic AI artifacts, unsupported implications>
```

For a premium technology hero, a useful direction is a crafted editorial still
life: luminous neutral studio, one physical metaphor, controlled asymmetry,
tactile paper or metal, shaped daylight, and one accent color. This is a
starting discipline, not a mandatory house style.

## Final quality gate

Inspect at thumbnail size and full resolution. A final image must pass all
applicable checks:

- Concept: one clear idea, not a feature inventory.
- Article fit: visibly connected to the retained message and image role.
- Topic recognition: a named subject remains identifiable at thumbnail size
  through at least one specific, brand-safe cue. It does not depend only on the
  prompt, alt text, embedded title, or logo.
- Originality: no obvious stock or generative-technology cliche.
- Hierarchy: focal point reads within one second at thumbnail size.
- Composition: intentional balance, crop safety, and useful negative space.
- Craft: coherent perspective, anatomy, edges, scale, and object interaction.
- Materials: believable surface response, thickness, contact, and texture.
- Lighting: motivated, controlled, and consistent.
- Color: restrained, deliberate, and not muddy or over-saturated.
- Evidence integrity: no fake UI, fake proof, misleading symbol, or unsupported
  outcome.
- Text: exact, legible, and necessary; otherwise absent.
- Finish: no malformed details, pseudo-writing, halos, plastic CG sheen, or
  accidental clutter.

Record the actual visual inspection in `audit.md`; do not mark the image checks
complete from the prompt alone.

## Edit or regenerate

Use a targeted edit only when the concept, medium, composition, and overall
finish are already strong and the defect is local.

Regenerate from a new concept or substantially revised art direction when the
visual metaphor, medium, composition, lighting strategy, palette, or overall
taste is weak.

Do not spend several local edits polishing a direction that feels generic,
stiff, cluttered, plasticky, dated, or overly dark. A technically successful
edit cannot rescue a poor concept.
