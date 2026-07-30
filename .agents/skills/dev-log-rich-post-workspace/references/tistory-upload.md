# Tistory media staging and URL mapping

Uploading files or saving an editor draft changes the user's Tistory account.
Do it only when the user has authorized that remote write and the intended blog
and draft are unambiguous. Final publication is a separate action and always
requires explicit authorization.

## Prepare the exact queue

Keep the article at `reviewing`, finish the local media validation, then run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/tistory_media_map.py \
  plan posts/YYYY-MM-DD-slug
```

The output order, media ID, local path, dimensions, and SHA-256 form the upload
map. Upload each file once in that order. Do not use a resized screenshot,
editor-generated thumbnail, or a file that differs from the listed hash.

## Two allowed paths

1. **User-supplied URLs.** The user uploads the listed files and returns the
   final CDN URLs mapped to media IDs. This path makes no account changes.
2. **Authorized editor staging.** In the signed-in Tistory editor, confirm the
   destination blog and target draft, insert each listed file as an attachment,
   and keep the draft unpublished. Switch to HTML mode and collect the final
   `src` URL for each inserted file. Match it to the media ID using the upload
   order, original filename, and dimensions. Saving or creating that draft is
   allowed only when the user authorized it.

The editor may rename a file. Never guess a mapping from the CDN filename
alone, and never reuse one URL for two media IDs. If the signed-in session,
destination draft, upload permission, or mapping is uncertain, stop at
`reviewing` and return the upload queue to the user.

Do not extract, print, or persist browser cookies or session tokens.

## Bind each final URL

For every mapped asset, run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/tistory_media_map.py \
  set-url posts/YYYY-MM-DD-slug <media-id> <https-tistory-cdn-url>
```

The command accepts only the configured HTTPS Tistory CDN hosts, rejects a URL
already assigned to another item, and updates `media.json` atomically. URL
changes invalidate prior remote and browser evidence; do not hand-edit old QA
records to make them pass.

After all URLs are present, run the creator `remote_media.py record` command.
That GET is the first proof that every mapping resolves to an image with the
expected format, aspect ratio, size, and animation behavior. The independent
reviewer performs the second GET later.

Uploading assets is not permission to paste the article, save unrelated editor
changes, or click Tistory's final publish control.
