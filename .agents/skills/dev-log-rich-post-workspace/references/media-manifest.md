# Media manifest

## Contents

1. [Top-level shape](#top-level-shape)
2. [Item fields](#item-fields)
3. [Provenance rules](#provenance-rules)
4. [GIF rules](#gif-rules)
5. [Article directives](#article-directives)
6. [Validation states](#validation-states)

Use `media.json` as the machine-verifiable bridge between evidence, local
preview assets, and final Tistory CDN URLs.

## Top-level shape

```json
{
  "version": 1,
  "lead_id": "orca-overview",
  "items": []
}
```

- Keep `version` at `1`.
- Select exactly one non-GIF `lead_id`.
- Keep item IDs unique and stable after captions or filenames change.

## Item fields

```json
{
  "id": "agent-select",
  "kind": "screenshot",
  "origin": "first_party",
  "role": "action",
  "claim_ids": ["C04"],
  "actor": "Codex browser run",
  "captured_at": "2026-07-30",
  "environment": "macOS 26.5, Orca 1.2.3",
  "source_url": "",
  "raw_path": "artifacts/captures/raw/agent-select.png",
  "publish_path": "assets/screenshots/agent-select.png",
  "tistory_url": "",
  "width": 1440,
  "height": 900,
  "display_width": 760,
  "placement": "after:agent-selection",
  "rights": "dev.log original capture",
  "alt": "Orca에서 기본 CLI 에이전트를 선택하는 화면",
  "caption": "기본 에이전트 선택 단계에서 설치된 CLI가 감지되는지 확인합니다.",
  "processing": ["crop"],
  "redactions": [],
  "sha256": "64 lowercase hexadecimal characters",
  "status": "validated"
}
```

Required values:

- `id`: lowercase letters, digits, and hyphens;
- `kind`: `image`, `screenshot`, or `gif`;
- `origin`: `first_party`, `official`, `user_supplied`, `simulated`, or
  `generated`;
- `role`: `lead`, `concept`, `action`, `change`, `result`, `error`,
  `comparison`, or `poster`;
- `claim_ids`: evidence IDs supported by this asset;
- `placement`: stable article location such as `after:opening` or
  `after:agent-selection`;
- `rights`: the publication-rights basis for this exact asset;
- `publish_path`: final file under `assets/`;
- `width`, `height`: actual pixel dimensions;
- `alt`, `caption`: distinct, non-empty publication copy;
- `processing`, `redactions`: arrays, including when empty;
- `sha256`: digest of the exact publishable file;
- `status`: `planned`, `captured`, `revision_required`, or `validated`.

Use `display_width` from `240` to `916` CSS pixels when a narrower presentation
improves legibility. Omit it to use the smaller of the asset's pixel width and
the `916px` media canvas; the renderer never intentionally upscales evidence.

## Provenance rules

- `first_party`: require `captured_at`, `environment`, and a raw asset under
  `artifacts/`; require `actor` and state that same actor in the evidence
  record. Keep still originals under `artifacts/captures/` and recording
  originals under `artifacts/recordings/`.
- `simulated`: require `captured_at`, `environment`, and a caption that does
  not imply a production device or account.
- `official`: require an HTTPS `source_url` and nearby source attribution.
- `user_supplied`: record the user's description and any permitted edits in
  the bundle evidence or capture plan.
- `generated`: never use as proof of an actual product state.
  Use only `kind: image` with `role: lead`, `concept`, or `comparison`.

Do not preserve a raw capture containing a password, token, QR pairing secret,
email, private repository name, personal notification, or identifying path.
Remove the sensitive state and recapture. Record ordinary privacy-safe crops or
redactions in `processing` and `redactions`.

## GIF rules

A GIF item adds:

```json
{
  "poster_id": "parallel-run-poster",
  "duration_seconds": 4.8
}
```

- Require a validated non-GIF poster item.
- Create the poster by extracting a frame from the exact GIF. Give it the same
  `origin`, `source_url`, `rights`, pixel dimensions, and `display_width`; set
  `derived_from` to the GIF ID and include `frame_extract` in `processing`.
  Never use a generated imitation of the product screen as the fallback.
- The checker verifies provenance metadata and dimensions. The independent
  article validator must also compare the rendered fallback with the actual
  GIF frame; metadata alone cannot prove that the pixels came from that frame.
- Show a meaningful start, action, and completed state.
- Keep the important crop readable at 360 CSS pixels.
- Prefer a focused clip and a short loop. A GIF must not exceed five seconds;
  shorten it or use a static sequence when the meaningful motion takes longer.
- Keep the original recording under `artifacts/recordings/`.
- Use an official GIF only with its source URL and never call it a direct
  recording.

## Article directives

Place each publication asset on its own source line:

```text
{{media:agent-select}}
```

- Do not place local paths in `article.md`.
- Use every registered item exactly once, except a poster referenced only by a
  GIF.
- Do not reuse one image to support unrelated claims.
- Move the directive with the paragraph it proves.

The preview renderer resolves `publish_path`. The Tistory fragment resolves
`tistory_url`; until it exists the renderer emits an obvious upload placeholder
and the post cannot become `ready`.

Final `tistory_url` values must use the approved Tistory media hosts under
`kakaocdn.net`, `daumcdn.net`, or `tistory.com`. Follow
`tistory-upload.md` and use `tistory_media_map.py` to preserve the exact
media-ID mapping. After filling them, follow `remote-media.md`; an HTTPS string
alone is not publication evidence.

## Validation states

- `planned`: the asset exists only in the capture plan.
- `captured`: raw and publishable candidates exist but have not passed review.
- `revision_required`: provenance, privacy, crop, legibility, or factual fit
  failed.
- `validated`: the exact hashed publication file passed independent visual
  review.

Do not set an article to `ready` unless every referenced item is `validated`,
every final URL is resolved, the rich-post checker passes, the hash-bound
responsive QA record matches the current bundle, and the independently
rechecked desktop and mobile pages pass visual inspection.
