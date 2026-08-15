# Source freeze v2

## Review boundary

Finish substantive writing before release QA. The reviewer must first cold-read
`article.md` without the prior approvals or audit conclusions. Then read
`editorial-voice-v2.md`, the brief, evidence, and audit and independently
verify:

- claims, numbers, dates, links, quotations, and authorship;
- the primary reader, plain identity, easiest start, and evidence boundary;
- for a non-specialist recommendation or benefit explainer, a recorded
  reader-benefit contract with one recognizable situation, the reader's actual
  knowledge baseline, one intended reader, one plain recommendation, its useful
  consequence, supported practical use, and deliberately excluded detail;
- a zero-prior-knowledge title test: without opening the article, can the
  intended reader understand that the topic is relevant without already knowing
  a folk association, search habit, nutrient, metric, feature, or mechanism?;
- a first-three-sentences test for recommendation and benefit explainers: can a
  cold reader state who the article is for, what it recommends, and why it may
  be useful in ordinary language?;
- for troubleshooting and procedural intent, the first safe action or default
  choice before the lead visual and table of contents;
- a title-plus-headings-only pass that exposes the action or decision order,
  names every real branch, and does not require opening a section to learn what
  `추가 확인` or a similar aggregate label contains;
- a compact TOC whose entries are stage-level decisions rather than every
  click, checkpoint, or closely related error; same-stage detail must remain
  inside an honestly named section;
- progressive disclosure from default action through failure branch and
  supported exception to mechanism and technical limit;
- comparison targets, units, score direction, source character, and limits;
- prerequisites, exact entry point, identifiers, representative first task,
  likely failure, and official documentation;
- Korean honorific style, title-heading scan, paragraph seams, and preserved
  technical meaning.
- a heading strip without sentence-shaped contrast frames, bureaucratic noun
  stacks, or separate decisions joined only for symmetry;
- an opening that answers the reader without a generic presenter roadmap;
- a paragraph-level new-information pass in which every retained paragraph
  adds a fact, evidence, action, comparison, limitation, or necessary branch;
- recommendation prose in which one intended reader and benefit remain more
  prominent than supporting numbers, mechanisms, and defensive caveats;
- the useful consequence before an unexplained nutrient, metric, feature, or
  mechanism, with the technical term introduced only when it helps explain the
  recommendation;
- evidence density limited to the representative facts that change a reader's
  judgment, without the same number repeated across prose, table, summary, and
  recap;
- limitations placed beside the claims they narrow, with a separate caution
  section only for a distinct safety decision and no material warning removed;
- one owner section for each central claim and action, with no full takeaway
  repeated across the opening, body sections, and closing;
- natural cadence without forced slang, deliberate mistakes, invented
  anecdotes, or unsupported casual endings.

Return evidence or structure defects to writing. Return title, opening,
heading, density, repetition, or rhythm defects to prose polish. A clear full
article does not pass when its first screen or heading-only path still makes
the reader hunt for the next action, or when the prose analyzer reports zero
signals but the cold read exposes a mechanical surface. A recommendation or
benefit explainer also fails when the reviewer cannot complete `이 글은 ___한
사람에게 ___을 추천하고, 이유는 ___이다` from the title and opening without
specialized knowledge. Repeat until the source passes.

## Record the pass

Keep `status: reviewing`, then run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/record_source_pass_v2.py \
  posts/YYYY-MM-DD-slug --by "<actual independent source reviewer>"
```

The record binds the lifecycle-normalized article, `brief.md`, and
`evidence.md`. It intentionally does not bind `audit.md` or the final media
bytes. A material source edit makes the record stale automatically.

Do not treat the command as the editorial review itself. Run it only after the
reviewer has inspected the actual bundle and resolved every publishable issue.
