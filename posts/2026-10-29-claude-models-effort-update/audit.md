# Published-source archive audit

This archive preserves the approved and subsequently published post 18 revision. The original URL and 2026-06-18 11:53 KST publication date were preserved. The bundle date records the 2026-10-29 revision. `article.md` differs from the approved source only by lifecycle status `reviewing` -> `published`; the original hash is verified in `artifacts/archive-integrity.json`.

## Evidence and boundaries

The supplied independent native preview signoff covers PC1280/mobile360 and light/dark, exact prose/table/caption parity, 18 links and four alt texts. The review was independent inspection of evidence supplied by the browser owner, not a separately operated browser. Saved readback parity excluded four identified site-injected advertisement labels. No new live inspection was performed during archival.

Local Chromium was unavailable and local remote-media verification encountered DNS failure in the preceding workflow. Those failures are not native-browser passes. No strict finalizer/source-pass records were fabricated here. `media-source.json` intentionally omits signed native bindings. This is a sanitized historical archive, not a directly publishable release bundle. `workflow-v2.json` retains its historical draft-stage decisions; the publication receipt is authoritative for successful publication.

## Archive checks

- Sanitized input ZIP size and SHA-256 verified before extraction; all entries restricted to this article directory.
- Approved article hash recovered exactly by restoring only the reviewing lifecycle line.
- Four assets match manifest hashes and four source directives match media IDs.
- Text/JSON screened for signed URL parameters, Library identifiers, bearer headers and private-key markers; none found.
- No scripts, styles, other posts or live blog content changed.

The repository article checker reports existing approved-source conventions: absent `sources` frontmatter, a non-`###` subheading, a heading ending in `습니다`, an em dash and no final `### 참고 자료` section. The ready/published source-list rule also reports the absent key. These editorial differences are retained to preserve the actual approved publication, not silently rewritten after publication.

The rich-post strict checker fails because the sanitized archive intentionally does not include `media.json`, native publication URLs, current source-pass or final-page records. Its missing media/directive errors are consequences of that omission. These failures are recorded rather than bypassed. Prior source/local bundle checks in the supplied archive note describe the preceding workflow, not this sanitized archive's strict checker result.
