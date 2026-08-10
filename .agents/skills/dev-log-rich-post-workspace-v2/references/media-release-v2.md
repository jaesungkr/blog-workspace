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

## Local preflight

Before upload, run the v2 checker and render local light and dark previews.
Inspect 1280 and 360 CSS pixels. Add 390 or 768 only when
`workflow-v2.json` routes that profile. Fix layout and media defects here; if
the text must change, return to the source gate.

## Map final URLs

After the source pass:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  plan posts/YYYY-MM-DD-slug
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/tistory_media_map_v2.py \
  set-url posts/YYYY-MM-DD-slug <media-id> <https-tistory-cdn-url>
```

The user may supply URLs. Upload to an unpublished Tistory draft only with
explicit authority and an unambiguous destination. Never publish.

Record one baseline GET:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/remote_media_v2.py \
  record posts/YYYY-MM-DD-slug --by "<actual creator>"
```

Run `verify` only when `second_remote_fetch` is true. This is mandatory for GIF
and high-risk remote media, optional for ordinary static Tistory images.
