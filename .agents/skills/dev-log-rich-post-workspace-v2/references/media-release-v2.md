# Media release v2

## Local media

Use `media.json` version 2. Keep one validated non-GIF lead and one standalone
`{{media:id}}` directive for each published item except a GIF poster.

Each item records its stable ID, kind, origin, role, claim IDs, actor when
applicable, source, raw and publish paths, rights, alt, caption, processing,
redactions, dimensions, display width when needed, SHA-256, status, and final
Tistory URL.

Require `capture-plan.md` only for direct, simulated, or GIF media. Generated
media never proves an actual UI state. Recapture secrets instead of preserving
and blurring them later.

## Generated infographic

When `workflow-v2.json` enables `infographic`, read
[infographic-v2.md](infographic-v2.md). Use `max-txt2img` for creation and
`dev-log-infographic-validation` for independent approval before marking the
media item validated. Preserve the final English prompt with the candidate.

## Instructional screenshot gate

For a procedural software guide, carry the reader-friction map from
`workflow-v2.json` and `brief.md` into `media.json`. A screenshot is justified
when it helps the reader find an entry point, choose the correct field or
value, or recognize a success/error state. Each screenshot must answer a
different concrete question and map to the claim it illustrates.

Put the screenshot directly after the relevant step. In the surrounding prose,
explain all three parts: where the reader is, what to inspect or enter, and what
to do next. Do not rely on a caption as the only instruction. Exclude screens
that merely repeat an obvious list or button, and record that exclusion so the
browser's Tistory upload queue stays purposeful. Two to five screenshots
is a common range, not a quota.

## Local preflight

Before opening the publication editor, run the v2 checker and render local light and
dark previews. Inspect 1280 and 360 CSS pixels. Add 390 or 768 only when
`workflow-v2.json` routes that profile. Fix layout and media defects here; if
the text must change, return to the source gate.

At 360 CSS pixels, verify the actual UI labels needed by the article rather
than accepting a successfully loaded but unreadable image. Use a mobile crop,
an additional focused image, or the scroll treatment below when labels are too
small.

When a wide UI screenshot is readable on desktop but its labels become too
small at 360 CSS pixels, set `mobile_scroll_width` to an integer from 480 to
916 in that screenshot's media item. The renderer keeps the caption fixed and
places only the screenshot in a keyboard- and touch-scrollable region on
mobile. State the horizontal-scroll action in the caption. Use this escape
hatch only for screenshots whose labels must remain legible, not for lead art,
photos, or decoration.

## Browser-owned attachment release

After the source pass and local preflight, obtain the author's approval of
this specific article and instruction to publish. Follow
[tistory-publication-v2.md](tistory-publication-v2.md) in the Codex in-app
browser. Codex uploads the validated local files, inserts the approved article,
previews it, and publishes under that approval. Login or two-factor prompts
may require the author's participation; resume in the same draft afterwards.

Print the deterministic queue for Codex, matching each upload by media ID,
local publication path, dimensions, and SHA-256:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  plan posts/YYYY-MM-DD-slug
```

Capture the complete native `[##_Image|..._##]` block from the editor's HTML
mode. Keep it in a bundle artifact such as
`artifacts/qa-v2/attachments/<media-id>.txt`. Observe the matching image URL in
the actual Tistory preview; use that URL only for remote byte observation and
standalone previews. Bind both:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  set-embed posts/YYYY-MM-DD-slug <media-id> \
  --embed-file <captured-native-block-file> --url <observed-preview-cdn-url>
```

The manifest's `tistory_embed` is the publication source. Its `tistory_url` is
an observation that can expire; never replace a native block with that URL in
the final fragment. Never construct a `kage@` reference by stripping the query
from a CDN address. If Tistory generates a native block containing a signed
query, preserve it as generated and verify its actual editor attachment
recognition. The validator also matches the captured block to the observed
asset identity, including thumbnail-wrapped URLs.

Record one baseline GET with `remote_media_v2.py record --by <actual creator>`.
Run `verify` when `second_remote_fetch` is true, including GIF and high-risk
remote media. For a GIF, capture both its own attachment and its validated
poster, and confirm animation and reduced-motion fallback in the real preview.
A currently successful URL fetch does not establish indefinite availability.

Keep these raw editor blocks separate from the assembled final fragment.
They allow re-rendering from stable native references instead of copying a
month-specific display URL back into publication HTML.
