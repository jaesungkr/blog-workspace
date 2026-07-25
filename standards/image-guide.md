# Blog image guide

## Required deliverable

- Generate at least one original raster image for every complete blog post. Do
  not satisfy this requirement with a stock-image link, web-search result, SVG
  placeholder, or prompt alone.
- Use the built-in image-generation workflow.
- Generate after the article's angle and central message are stable so the image
  matches the published argument.
- Inspect the result before delivery. Regenerate or make one targeted correction
  if the subject, composition, factual implication, or constraints are wrong.
- Save the selected final image in the post's `assets/` directory with a
  descriptive ASCII filename. Do not overwrite an existing file; add `-v2`
  when needed.
- Preview the image for the user and record its path, recommended article
  position, concise Korean alt text, and final generation prompt in `audit.md`.

## Default visual

Unless the user specifies otherwise:

- Create one landscape hero image suitable for the top of a Tistory post.
- Use a 16:9 or similarly wide composition with a clear central subject and safe
  margins for responsive cropping.
- Prefer a natural editorial photograph for health, culture, sports, or
  everyday topics.
- Prefer a polished editorial illustration or realistic workspace scene for
  abstract technology and LLM topics.
- Prefer a restrained contemplative photograph or illustration for Reflections;
  avoid literal depictions of God or an identifiable real preacher unless the
  user supplies a reference and requests it.
- Use no embedded title, labels, logos, UI trademarks, watermark, or decorative
  Korean text unless exact in-image text is essential and explicitly requested.
- Avoid clickbait expressions, medical fear imagery, fake product branding,
  fabricated interfaces, misleading before/after claims, and visuals that imply
  evidence the article does not establish.

## Match image to article role

Choose one useful role:

| Article need | Image role | Default approach |
|---|---|---|
| Search-entry overview | Hero image | One concrete scene embodying the main conclusion |
| Product or tool comparison | Comparison concept | Neutral side-by-side objects without fake logos or labels |
| Mechanism explanation | Educational visual | Simple accurate composition; minimize text |
| Tutorial | Result scene | Show the practical outcome rather than a generic laptop |
| Reflections | Contemplative scene | Symbolic but restrained scene connected to the passage |

Do not generate a dense infographic when accuracy depends on many labels. Use a
table in the article and a simpler supporting image instead.

## Prompt scaffold

Shape the request using only relevant lines:

```text
Use case: <photorealistic-natural | stylized-concept | scientific-educational>
Asset type: Korean Tistory blog hero image
Primary request: <one concrete visual expression of the article's core message>
Scene/backdrop: <specific environment>
Subject: <main subject>
Style/medium: <editorial photograph or polished illustration>
Composition/framing: wide landscape, clear focal point, safe margins for responsive crop
Lighting/mood: <topic-appropriate>
Constraints: factually neutral, suitable for publication, no logos, no watermark, no embedded text
Avoid: generic stock-photo look, clutter, sensationalism, unsupported claims
```

## Placement and accessibility

- Recommend `대표 이미지 - 제목 바로 아래` by default.
- If the visual explains a mechanism or comparison, recommend the relevant
  section instead.
- Write alt text that describes what is visible and why it matters in one
  concise Korean sentence. Do not stuff SEO keywords.
- Do not insert a local filesystem Markdown image link into the Tistory article
  body. The user uploads the saved image manually; provide placement guidance
  separately.
