# Author-approved Tistory publication v2

## Approval belongs to the article

The author first reviews the complete article and publication images. An
instruction such as `이대로 올리자`, `확정했어. 게시해 줘`, or an equivalent
explicit instruction authorizes Codex to upload those images, assemble the
approved article in Tistory, preview, click the final publish control, and
verify the result. Do not ask for the same publication permission again.
Drafting, source-review approval by another agent, and silence do not authorize
publication. A material title, claim, recommendation, or media-content change
after author approval needs the author's approval of that changed candidate.
Routine attachment binding and layout corrections within the approved content
do not require another approval.

Record the real approval in `artifacts/qa-v2/author-publication-approval.json`:
the author's instruction, the approved source-pass hash, an ID-to-local-media
SHA-256 map, the target blog, and the approval time in Asia/Seoul. Never invent
an approval message or reuse another article's approval. The time comes from
the current client time context; the hashes come from the actual files.
Set `publication_mode: codex-browser` in `workflow-v2.json` for this release.

## Use the Codex in-app browser

Keep the editor and verification in Codex's in-app browser. Do not switch to
external Chrome for login, attachment upload, or publication. Use the available
browser/computer tool through its documented API, including the documented
file-chooser flow. Read UI state after actions. Do not replace editor actions
with copied cookies, hidden application APIs, injected editor setters, or
undocumented POST requests.

If login, two-factor authentication, CAPTCHA, or another genuinely required
human action blocks progress, keep the browser tab for resumption and explain
that exact action. Never request credentials in chat. Once the author finishes
login, resume the same publication rather than requesting approval again.

## Attach and assemble in one target editor

1. Open the intended existing post or a new editor for this approved article.
   Verify its title/blog before changes. For an existing post, back up the
   exact editor HTML and current publication metadata before editing.
2. Print `tistory_media_map_v2.py plan` and upload each validated local file in
   this editor. Match media IDs by file path, dimensions, and SHA-256. Reuse the
   working draft if interrupted; do not create duplicate posts or repeatedly
   upload files that are already attached.
3. In HTML mode, capture the complete native `[##_Image|..._##]` block that
   Tistory generated for each asset. Save one raw block per ID under
   `artifacts/qa-v2/attachments/`. Do not invent a native reference, strip a
   signature to make a supposedly permanent URL, or use the current display
   URL as the final `<img src>`.
4. Observe each matching CDN URL from Tistory's actual preview. Bind the code
   and observation with `tistory_media_map_v2.py set-embed` and run the native
   attachment preflight below. After any attachment corrections, finalize the
   binding, record remote media, and complete the independent local light/dark
   page gate. The generated final fragment contains native blocks; its
   standalone preview uses observed URLs. GIF and poster attachments both
   need mapping.
5. Use `finalize_rich_post_v2.py` and paste the exact resulting TXT into this
   editor. Preserve the attachment registrations by using the same editor
   instance. Verify the current editor text against the submitted artifact;
   protect the rest of the approved article when making an image-only repair.

If a file-chooser action fails, inspect the UI before retrying. The successful
2026-10-24 in-app repair used the documented file-chooser event with the native
AX click on the actual file input when a Playwright click failed. Use fresh
element indices from the current state. This is a fallback, not a fixed selector
or a reason to switch browsers.

## Native attachment preflight

Set each image's approved `media.json` alt in the editor or the native block's
valid metadata before binding it. Keep the untouched upload block separately
when adding metadata; retain its exact attachment reference and signed query.
Do not synthesize a new reference. `set-embed` and the bundle checker reject
missing, blank, or mismatched native alt in both CDM JSON and attribute blocks.
Manifest alt alone does not establish that the published image has alt text.
Use `set-embed` with the corrected captured block to repair an already bound
alt; this permits only the selected alt repair and retains other bundle/source
errors. Keep a published post's lifecycle history when staging such a repair.

Assemble a provisional fragment in the same editor and inspect its real
preview before freezing the final page candidate. Confirm actual image alt,
captions, dimensions, and the skin's representative-image behavior; then make
the final native binding, remote record, and canonical candidate. This catches
attachment corrections before they invalidate an expensive final-page pass.
After finalization, compare the exact TXT with the editor HTML and verify its
preview as usual. A byte-identical fragment needs no duplicate manual review.

Treat a body lead image and a skin cover as different uses. A readable table
crop can make a poor background behind a title. Check the actual title, date,
and category over the selected cover at desktop/mobile widths in both themes.
Prefer a suitable approved asset or a scoped `assets/post.css` contrast repair
when needed; do not impose a dark overlay or a new generated hero on every
post. If a new-post preview does not show the eventual automatic cover, record
that it was not represented and check it immediately on the first live page.
Repair that same post under the existing layout authorization, preserving its
URL/date, instead of publishing a duplicate. Refresh the affected final-page
evidence for CSS changes; reopen source review only for a material source edit.

## Preview, publish, verify

Inspect the exact native fragment in Tistory's own preview at desktop and
mobile widths, including real hELLO light/dark behavior. Confirm native image
recognition, nonzero loaded image dimensions, alt text, caption order, and
layout without clipping. Native blocks expand into their own figures; use the
renderer-provided scoped wrapper and centering reset rather than nesting them
inside another figure. Review publication title, category, public visibility,
URL, and date. For an existing post, retain its URL/date unless the requested
change includes those fields. New articles default to public publication now
unless the author specified another setting.

Under the recorded author approval, click the final publish/save control and
wait for an observable success state. If the result is ambiguous, inspect the
post list or live URL before retrying; do not create a second publication.
Read the live article URL from the successful browser result and verify the
public page, including desktop/mobile images, captions, TOC, and scrolling.
Record actual outcomes and screenshots in `artifacts/qa-v2/publication.json`,
including the post ID, URL, submitted fragment SHA-256, approval-record hash,
and publication/verification time. Distinguish editor preview, actual publish,
and public-page verification in the evidence.

Set `published` only after live verification. If publishing succeeded but
verification or Git delivery failed, record that split state and continue
from the existing post. Do not claim that no post exists or publish a duplicate.
Finish the focused commit/push and verify the remote commit. Return the live
URL first, the exact submitted TXT as a backup, and an embedded screenshot.

## Address lifetime

The persistent publication input is the native attachment reference, not a
month-specific display URL. Tistory may generate signed display URLs with
`expires` even for normal attachments. Preserve the native editor block and
let Tistory resolve it. A successful current fetch proves present availability;
do not promise infinite retention or claim an expiry-boundary test that was
not performed. If re-rendering later, refresh observation URLs through the
actual page/editor while retaining the native attachment reference.
