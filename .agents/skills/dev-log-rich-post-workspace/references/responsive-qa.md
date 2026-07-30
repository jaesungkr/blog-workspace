# Responsive QA record

Inspect the full preview and Tistory fragment in a real browser. Use this exact
order:

1. Render with `--preview-media-source remote --output-dir
   posts/<bundle>/artifacts/qa/rendered`.
2. Run `scripts/capture_rich_qa.py <bundle> --mode creator --by <reviewer>`.
   It opens that canonical file in one real Chrome session, scrolls the page to
   load lazy media, measures the DOM, and writes the three actual screenshots
   plus `artifacts/qa/browser-capture.json`.
3. Copy `assets/qa-template.json` to
   `posts/<bundle>/artifacts/qa/measurements.json`.
4. Scroll the same exact preview and inspect each screenshot. Replace only the
   pending human decisions: `readable_media`, viewport `status`, and fragment
   results.
5. Run `scripts/record_rich_qa.py` to bind both inputs and create
   `artifacts/qa/rich-post.json`.

Do not infer a pass from CSS or HTML source. The recorder rejects candidates
from any other directory.

## Focused evidence for changed components

The three canonical screenshots can show only the first viewport after the
capture helper scrolls the page. They do not prove that a changed table, code
block, long link, or below-fold control is readable.

When a changed component is outside those screenshots, or when its
`scrollWidth` exceeds its mobile wrapper:

1. Reopen the exact canonical preview under the same creator or independent
   review role. If the canonical capture process has exited, use a fresh real
   browser session and record its identifier with the supplemental evidence.
2. At both 390 and 360 CSS pixels, record the document client and scroll
   widths, component wrapper client and scroll widths, `overflow-x`, text size,
   line height, headers, and a representative first row or state.
3. Inspect the component at `scrollLeft = 0` and at its maximum horizontal
   scroll. Save focused screenshots for both ends when different columns or
   controls become visible.
4. Confirm the document itself does not move horizontally, labels do not
   collide, and every column or control can be reached without zoom.
5. Save supplemental measurements and images under
   `artifacts/qa/component-details/` for creator review or
   `artifacts/qa/independent/component-details/` for independent review.
   Include the exact preview hash, browser session, browser version, viewport,
   and screenshot paths.
6. Record the direct observation in `audit.md` and, when accepted by the
   measurement schema, the human-review measurement file.

Focused evidence supplements the canonical browser receipt; it never replaces
the required three screenshots or the hash-bound creator and independent
records. A table passes only after its left and right mobile states are read in
the browser. Do not award a pass merely because the stylesheet contains
`overflow-x: auto`.

## Required record

```json
{
  "version": 1,
  "checked_at": "2026-07-30",
  "checked_by": "Codex browser run",
  "browser": "Google Chrome/<version derived from CDP>",
  "session": "UUID derived from the capture run",
  "capture_receipt_path": "artifacts/qa/browser-capture.json",
  "capture_receipt_sha256": "exact browser receipt SHA-256",
  "capture_tool_sha256": "current capture_rich_qa.py SHA-256",
  "article_content_sha256": "lifecycle-normalized article.md SHA-256",
  "media_sha256": "current media.json SHA-256",
  "renderer_sha256": "current render_rich_post.py SHA-256",
  "css_sha256": "current rich-post.css SHA-256",
  "markdown_renderer_sha256": "current md2tistory.py SHA-256",
  "remote_media_sha256": "current remote-media.json SHA-256",
  "preview_media_source": "remote",
  "preview_path": "artifacts/qa/rendered/slug-rich-preview.html",
  "preview_sha256": "exact reviewed preview SHA-256",
  "preview_structure_sha256": "reviewed preview with local img src normalized",
  "fragment_path": "artifacts/qa/rendered/slug-tistory-fragment.html",
  "fragment_sha256": "exact reviewed Tistory fragment SHA-256",
  "viewports": [
    {
      "width": 1280,
      "height": 900,
      "client_width": 1280,
      "scroll_width": 1280,
      "h1_count": 1,
      "toc_targets_unique": true,
      "images_loaded": true,
      "readable_media": true,
      "screenshot": "artifacts/qa/desktop-1280.png",
      "screenshot_sha256": "derived by record_rich_qa.py",
      "screenshot_pixel_width": 1280,
      "screenshot_pixel_height": 900,
      "status": "pass"
    },
    {
      "width": 390,
      "height": 844,
      "client_width": 390,
      "scroll_width": 390,
      "h1_count": 1,
      "toc_targets_unique": true,
      "images_loaded": true,
      "readable_media": true,
      "screenshot": "artifacts/qa/mobile-390.png",
      "screenshot_sha256": "derived by record_rich_qa.py",
      "screenshot_pixel_width": 390,
      "screenshot_pixel_height": 844,
      "status": "pass"
    },
    {
      "width": 360,
      "height": 800,
      "client_width": 360,
      "scroll_width": 360,
      "h1_count": 1,
      "toc_targets_unique": true,
      "images_loaded": true,
      "readable_media": true,
      "screenshot": "artifacts/qa/mobile-360.png",
      "screenshot_sha256": "derived by record_rich_qa.py",
      "screenshot_pixel_width": 360,
      "screenshot_pixel_height": 800,
      "status": "pass"
    }
  ],
  "fragment": {
    "h1_count": 0,
    "unresolved_placeholders": 0,
    "local_paths": 0,
    "status": "pass"
  }
}
```

Use the exact required profiles `1280×900`, `390×844`, and `360×800`; add 768px
when a layout, table, or media transition needs a tablet check. `width` and
`height` are the actual CSS viewport dimensions. `client_width` and
`scroll_width` are document-element measurements, not table or code
measurements. A table or code block may scroll inside its own wrapper, but the
page must not. The capture helper records each screenshot's hash and exact
pixel dimensions in the same browser receipt; the recorder re-derives and
checks them. Each viewport requires a different canonical screenshot path and
different screenshot content.

`images_loaded` is not a self-entered judgment. The capture helper waits for
every preview `<img>` to report complete, positive natural dimensions in real
Chrome, and an allowed Tistory CDN source. It records those per-image
observations. A missing or undecodable remote image fails before the human
review.

`readable_media` is a visual decision. Set it to true only after opening each
figure at that viewport and confirming that the important control, label,
state, and caption are readable without zoom. Recapture or add a focused crop
when the answer is no.

The screenshots must show the actual reviewed page and live under
`artifacts/qa/`. The checker binds their canonical paths, browser receipt,
capture-tool hash, browser version, session, reviewer, and exact preview to the
current article content and exact `media.json`. It ignores only the
frontmatter fields `status` and `published_url`, because those lifecycle values
change after the independent pass without changing the rendered candidate.
Every other article or manifest edit invalidates the QA pass.

When a material edit invalidates the pass, reset the current QA decisions and
describe old receipts as historical evidence only. Do not leave checked audit
items or unqualified current-tense pass language that refers to the previous
article hash.

Keep the exact reviewed preview and fragment under `artifacts/qa/rendered/`.
The checker binds them to the current CSS, rich renderer, and Markdown renderer.
The preview must load the recorded Tistory CDN URLs, so the visual pass covers
the same remote files used by the paste fragment.
The strict remote renderer then reproduces both the fragment and the preview
byte-for-byte. Any renderer, CSS, source, remote URL, or fragment change
therefore requires a new capture, viewport inspection, and QA record.

Do not hand-edit browser-derived DOM values, image-load results, hashes,
screenshot dimensions, session data, or reviewed-artifact fields shown above.
`capture_rich_qa.py` produces them and `record_rich_qa.py` validates them
against the exact candidate, screenshots, and current toolchain.

The article validator must independently reopen the recorded candidate,
compare these measurements with the screenshots, and then create a second,
fresh candidate and evidence set. It must:

1. independently verify `remote-media.json`;
2. strict-render with `--preview-media-source remote` into
   `artifacts/qa/independent-rendered/`;
3. run `capture_rich_qa.py --mode independent --by <reviewer>` to open that
   fresh preview at `1280×900`, `390×844`, and `360×800`;
4. inspect the separate screenshots and receipt under
   `artifacts/qa/independent/`;
5. record its observations from `assets/independent-qa-template.json` with
   `record_rich_final_validation.py`.

The independent reviewer and browser-session identifier must differ from the
creator QA. Inspect reduced-motion GIF fallbacks and compare the poster with an
actual GIF frame. Return `revision_required` when any record and page differ.
A browser-less or network-less run cannot produce either pass.

`record_rich_final_validation.py` derives the creator-QA hash, remote baseline
and verification hashes, article and toolchain hashes, exact independent HTML
hashes, and screenshot hashes. The measurements input must set `result` to
`pass`, the three general checks to `true`, and both GIF checks to `pass` when a
GIF exists or `not_applicable` otherwise. It writes
`artifacts/qa/independent-final-page.json` atomically only after the fresh
renderer output and every independent observation agree.
