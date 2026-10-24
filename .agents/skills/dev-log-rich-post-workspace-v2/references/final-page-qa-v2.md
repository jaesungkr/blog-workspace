# Final page QA v2

## Prepare one candidate

Run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/prepare_final_qa_v2.py \
  posts/YYYY-MM-DD-slug
```

This writes canonical remote-media light and dark previews plus one pending
human-measurement file under `artifacts/qa-v2/`.

## Capture both themes

One reviewer uses two fresh browser sessions, one per theme:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/capture_rich_qa_v2.py \
  posts/YYYY-MM-DD-slug --mode final-light --by "<reviewer>"
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/capture_rich_qa_v2.py \
  posts/YYYY-MM-DD-slug --mode final-dark --by "<same reviewer>"
```

Add `--include-390` or `--include-768` to both commands only when routed in
`workflow-v2.json`.

Inspect the entire page, not only the first viewport. Confirm remote image
meaning and readability, one preview H1, unique TOC targets, no page overflow,
caption attachment, list markers and spacing, table and code scrolling,
fragment H1 count zero, and no local path or placeholder. In dark mode confirm
contrast, preserved inline styles, and neutral image surrounds without
recoloring image pixels.

For troubleshooting and procedural posts, confirm at 1280 and 360 that the
first safe action remains visible before the lead visual and TOC, the TOC reads
as one compact action or decision path rather than an exhaustive checklist,
and wrapped numbered headings are not clipped or visually crowded. Return text
defects to the source stage; do not approve a visually neat page whose
navigation still hides the next action or overwhelms it with same-stage detail.

Use focused screenshots only after an automated failure, for a new component,
or when a risky table state is not visible in the canonical evidence. Do not
capture every repeated table or list.

Loaded dimensions alone do not prove that image pixels were painted. If a
full-page capture has a blank media region despite valid `naturalWidth`, bring
that image into the viewport and take a focused screenshot, including the
needed horizontal-scroll position. Preserve both observations. A normal focused
view can distinguish a capture paint omission; if that view is also blank,
leave the defect unresolved rather than retrying until a pass appears.

Fill only the human decisions in `final-measurements.json`, then run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/record_final_page_v2.py \
  posts/YYYY-MM-DD-slug \
  --preview posts/YYYY-MM-DD-slug/artifacts/qa-v2/final-rendered/<slug>-rich-preview.html \
  --dark-preview posts/YYYY-MM-DD-slug/artifacts/qa-v2/final-dark-rendered/<slug>-rich-preview.html \
  --fragment posts/YYYY-MM-DD-slug/artifacts/qa-v2/final-rendered/<slug>-tistory-fragment.html \
  --measurements posts/YYYY-MM-DD-slug/artifacts/qa-v2/final-measurements.json
```

This is the only manual page approval. Do not repeat the source editorial gate
here. If a real text defect appears, return to writing and invalidate this
candidate.

## Exact Tistory attachment preview and live verification

The standalone preview uses observed CDN URLs; the publication fragment uses
native attachment blocks. After finalization, inspect that exact fragment in
the actual Tistory editor preview before publication. Check image recognition,
alt text, captions, order, and 1280/360 widths in real hELLO light/dark themes.
This verifies the platform transformation; it does not reopen source review
or add a second independent local-page approval. Return a real defect to its
owning stage and refresh affected evidence before publication.

Native Tistory blocks expand into `figure.imageblock`. Keep the outer media
wrapper a `div` to avoid nested figures. Reset native centering transforms
inside the scoped wrapper; the 2026-10-24 repair exposed a conflict between
`margin: 0 auto` and Tistory's `translateX(-50%)` at mobile widths. The v2 CSS
handles this only inside `.devlog-rich__native-image`.

After publication, verify the public page itself, including successful image
loads (`naturalWidth > 0`), captions, native imageblock markup, navigation,
table/code scrolling, and both desktop/mobile layouts. Record the live URL,
actual measurements, and screenshots in `artifacts/qa-v2/publication.json`.
Do not equate a local preview pass or an editor save click with live success.

Test a fresh load at each required public viewport, not only a page resized
from desktop to mobile. If resizing exposes overflow, locate its owner and
record that observation separately from the fresh-load result. An ad iframe
that retains its desktop width is still a resize defect; a passing mobile
reload does not erase it or prove that all responsive behavior passed. Keep
article scroll regions distinct from document overflow and do not hide the
problem with page-wide overflow suppression.

Include the live title/metadata contrast over the actual skin cover, following
the publication preflight. A cover-only CSS correction requires current
candidate hashes, affected capture records, and an actual cover recheck. When
the article body is byte-identical, reuse its substantive review and inspect
the changed component instead of reopening editorial review or rereading every
unchanged section. Never reuse a stale final-page pass.
