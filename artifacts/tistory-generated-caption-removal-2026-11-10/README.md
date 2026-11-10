# Tistory generated-image caption cleanup, 2026-11-10

The requested label-only edit was completed on 28 existing public posts at https://dop3n.tistory.com. Thirty labels were removed, including the original request at https://dop3n.tistory.com/117. The scope was extended to matching captions across the published blog. Images, meaningful caption descriptions, article prose, titles, canonical URLs, and original publication dates were retained.

## Scope and verification

- Initial public discovery: 146 published post URLs from the sitemap, cross-checked against 17 category-list pages. Nonpublic admin entries were not edited.
- 13 posts contained 15 standalone `devlog-rich__credit` spans. The exact span was removed.
- 15 older posts contained 15 native image-caption labels. Only the AI/generated-image suffix was removed, preserving any descriptive prefix. Caption-only labels became empty captions.
- All edits used the existing Tistory editor and original publication settings. The pre-edit editor fragment and exact submitted fragment are saved for each post.
- Independent public checks passed for all 28: expected label-only normalized visible-text change; 37 image elements with identical source paths, alt text, and count; unchanged title, canonical URL, and original publication date.
- A fresh full-site scan fetched all 146 published posts without error and found zero remaining matching visible labels.
- Tistory normalizes some HTML attributes and whitespace when saving. Raw public markup equality and complete visual/image-load validation are not claimed. The submitted editor HTML differs only in the recorded intended replacements.

## Files

- `manifest.json`: initial inventory and exact caption candidates.
- `category-manifest.json`: independent public inventory cross-check.
- `baseline-metadata.json`: original title, URL, and publication metadata.
- `editor-delta-verification.json`: all 28 exact replacement/hash checks.
- `all-28-verification.json`: aggregate public preservation checks.
- `final-site-scan.json`: final 146-post scan.
- `posts/<post-id>/editor-before.html`: original editor HTML.
- `posts/<post-id>/submitted-fragment.txt`: exact submitted HTML.
- `posts/<post-id>/receipt.json`: original settings, saved outcome, and hashes.
- `posts/<post-id>/public-article-before.html` and `public-article-after.html`: public article-body snapshots.
- `posts/<post-id>/public-verification.json`: post-specific independent checks.

This evidence package records the live-site correction. It does not claim that older local source articles have been fully reconciled with live content. Current source caption definitions and the renderer already omit these targeted labels; meaningful explanatory captions must remain intact. Historical archives are not rewritten.
