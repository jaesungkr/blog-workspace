# Rich-post v2 workflow

## State model

Keep the repository lifecycle unchanged:

`planning -> researching -> drafting -> reviewing -> ready -> published`

Use `artifacts/qa-v2/source-pass.json` as the internal `source_frozen` gate while
the public lifecycle remains `reviewing`. After that record exists, do not edit
the title, opening, headings, tables, links, usage steps, or substantive
captions without rerunning the source review.

## Route once

Record the route in `workflow-v2.json`.

- `standard-rich`: source-based explanation with static official, generated,
  or user-supplied media;
- `evidence-rich`: direct UI work, reproducible experiment, GIF, or another
  capture-led promise.

Turn on only the risks that actually exist:

- `direct_capture`: create `capture-plan.md` and preserve raw evidence;
- `gif`: require the poster and second remote fetch;
- `generated_lead`: use the separate hero creator and validator;
- `infographic`: use the infographic stages only when the visual reduces
  reading effort;
- `complex_layout`: inspect the affected component and set `include_390` or
  `include_768` only when the transition needs it;
- `high_risk_remote_media`: set `second_remote_fetch` to true.

For a procedural software guide, also use `decision_note` to record the
reader-friction screenshot map before drafting:

- entry point: can a first-time reader find the menu or screen from prose?
- choice: can the reader identify the correct field, option, or value?
- verification: can the reader recognize success, waiting, or error state?

Choose screenshots only where prose alone leaves one of these questions hard
to answer. A normal guide often needs two to five, but this is not a quota.
Require a different reader question for every selected image and record why an
obvious candidate was excluded when it would be redundant or increase the
user's Tistory upload burden without improving the explanation.

For a recommendation or benefit explainer aimed at non-specialists, record a
reader-benefit contract in `brief.md` and summarize it in `decision_note`:

- the concrete situation or discomfort the reader already recognizes;
- what the reader does not yet know about the subject;
- one intended reader and one plain recommendation;
- the useful consequence in ordinary language before any nutrient, metric,
  feature, or mechanism;
- the practical choice or use the article will support;
- evidence detail and adjacent topics the article will deliberately exclude.

Do not treat a folk association or search habit as prior knowledge. A title
such as `붓기에 팥물을 찾는다면` fails for readers who do not yet know why
red beans are associated with swelling. Name the recognizable problem and the
recommendation instead. Keep the audience fixed when research reveals more
possible benefits; move unrelated benefits to another article.

The v2 checker rejects GIF or high-risk remote media when the second fetch is
not enabled.

## Main sequence

1. Initialize the bundle and fill `workflow-v2.json`.
2. Research, capture raw evidence when routed, draft, run the v2 editorial
   voice-and-density gate, and polish.
3. Run an independent cold-read source review and write `source-pass.json`.
4. Finish publication media and local light/dark preflight.
5. Bind final Tistory URLs and record the first remote observation.
6. Prepare one remote-media light/dark candidate.
7. Let one independent reviewer capture and inspect both themes.
8. Record `final-page.json`, set `ready`, render, deliver Git, and hand off the
   byte-identical paste file.

## Invalidation

| Change | Repeat |
|---|---|
| Title, article body, table, link, usage step | Source pass and final page |
| Brief or evidence | Source pass and final page |
| CSS, display size, media file, caption | Final page |
| Tistory URL | Remote record and final page |
| Audit-only note | No page rerun |
| Tool change with byte-identical final HTML | Keep the reviewed artifact; record the unchanged hash |

Never start remote staging before the source pass. This ordering prevents a
late editorial revision from invalidating expensive browser evidence.
