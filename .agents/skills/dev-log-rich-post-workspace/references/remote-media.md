# Final Tistory media verification

Treat a syntactically valid CDN URL as unresolved until the bytes at that URL
have been fetched and checked. The final responsive previews use these remote
URLs, not the local publication files.

## Two independent records

Use:

- `artifacts/qa/remote-media.json` as the creator's baseline observation;
- `artifacts/qa/remote-media-verification.json` as the independent validator's
  second observation.

Both records bind the current `media.json` and the complete remote-validation
toolchain: `remote_media.py` plus the shared URL, parser, dimension, animation,
and fingerprint logic in `rich_post_common.py`. Each component hash and their
combined hash are stored. The second record also binds the exact first record.
A changed URL, manifest, toolchain file, CDN response, MIME type, format,
dimensions, animation, or response hash invalidates the ready gate.

## Commands

After uploading every asset and filling every `tistory_url`, run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py \
  record posts/YYYY-MM-DD-slug --by "actual creator identity"
```

During the independent final-page stage, a different reviewer runs:

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py \
  verify posts/YYYY-MM-DD-slug --by "actual independent reviewer"
```

Immediately before paste or after publication, check the live bytes without
changing either readiness record:

```bash
python3 .agents/skills/dev-log-rich-post-workspace/scripts/remote_media.py \
  check-live posts/YYYY-MM-DD-slug
```

Do not simulate these commands or write their JSON by hand. A network failure
is `inconclusive`, not a pass. Keep the article at `reviewing` until a real
fetch succeeds. Starting `record` atomically replaces any prior baseline with
`in_progress`; starting `verify` does the same to the prior verification. A
failed or interrupted rerun therefore cannot leave stale readiness evidence
active. `check-live` is intentionally read-only.

## Fetch policy

The fetcher:

- permits only HTTPS hosts under the repository's Tistory media allowlist;
- rejects credentials, nonstandard ports, private, loopback, link-local,
  reserved, multicast, and unspecified addresses;
- rechecks every redirect and stops after five redirects;
- performs GET with a fixed image `Accept`, `Accept-Encoding: identity`, and a
  20-second total response deadline in addition to socket timeouts;
- accepts only HTTP 200 and at most 32 MiB per item;
- accepts only the known PNG, JPEG, WebP, GIF MIME types or
  `application/octet-stream`, then verifies signature and structural image
  data instead of trusting the URL extension;
- records the final response hash, byte count, content type, format,
  dimensions, frame count, and duration.

PNG, JPEG, and static WebP are valid for static items. A GIF item must remain an
animated GIF with at least two frames and no more than five seconds per loop.
Animated WebP is intentionally unsupported in this profile.

Tistory may re-encode a static upload, so remote bytes do not have to match the
local file byte-for-byte. The remote aspect ratio may differ by at most 0.5%,
and its pixel width must cover the intended CSS display width. The independent
fetch must reproduce the creator's remote response fingerprint exactly. If the
CDN later changes that fingerprint, rebuild the baseline and repeat page QA.

## Static ready gate

Repository checks do not contact the network. They verify the two saved records
against the current manifest and toolchain. This avoids turning a temporary CDN
outage into a random regression failure while still requiring two successful
network observations before `ready`.

Structural parsing is deliberately not presented as a full JPEG or WebP pixel
decoder. `capture_rich_qa.py` therefore loads and decodes every remote image in
real Chrome at all three required profiles and records `images_loaded: true`.
Remote verification proves transport integrity, not semantic correctness. The
creator and independent reviewer must still open the remote-media preview and
confirm that every displayed screen is the intended screen.
