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

Use focused screenshots only after an automated failure, for a new component,
or when a risky table state is not visible in the canonical evidence. Do not
capture every repeated table or list.

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
