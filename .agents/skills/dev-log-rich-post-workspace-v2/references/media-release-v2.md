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
user's private Tistory upload queue stays purposeful. Two to five screenshots
is a common range, not a quota.

## Local preflight

Before asking the user to upload, run the v2 checker and render local light and
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

## User-owned Tistory upload

Codex never accesses the Tistory editor, creates or edits a Tistory draft,
uploads any file to Tistory, or asks whether it may do so. Always treat Tistory
media upload as the user's action, even when a signed-in browser or another
upload mechanism appears available.

After the source pass and local preflight, print the queue and give the user
the listed local files. Include each stable ID, dimensions, and SHA-256 so the
returned CDN URL can be matched without relying on upload order. Stop the
release sequence at `reviewing` until the user privately uploads the files and
returns every required URL.

## Map final URLs

After the source pass:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  plan posts/YYYY-MM-DD-slug
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  set-url posts/YYYY-MM-DD-slug <media-id> <https-tistory-cdn-url>
```

Run `set-url` only with a URL the user returned for that media ID. Do not infer
that a URL belongs to a file from its order alone. Once all URLs are bound,
record the remote baseline and continue to the final page gate.

Record one baseline GET:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/remote_media_v2.py \
  record posts/YYYY-MM-DD-slug --by "<actual creator>"
```

Run `verify` only when `second_remote_fetch` is true. This is mandatory for GIF
and high-risk remote media, optional for ordinary static Tistory images.
