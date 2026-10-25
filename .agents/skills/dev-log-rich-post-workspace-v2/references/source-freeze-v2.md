# Source freeze v2

## Review boundary

Finish substantive writing before release QA. The reviewer must first cold-read
`article.md` without the prior approvals or audit conclusions. Then read
`editorial-voice-v2.md`, the brief, evidence, and audit and independently
verify:

- claims, numbers, dates, links, quotations, and authorship;
- an independent comprehension account from the article alone: its question,
  purpose, supplied material or subject, relevant actor/tool actions, actual
  finding, and the reason for each secondary test or figure. For a software
  investigation, separate the app's behavior from the tool's analysis and any
  manual interpretation or execution check. Have the reviewer explain why the
  chosen material is suitable, what each test condition checks, and why any
  additional product/model names appear. Identify the introducing passage;
  an explanation supplied only by the brief or reviewer does not pass;
- natural Korean across paragraph boundaries: concrete actors and verbs,
  sufficient particles, understandable references, and a real reason for a
  change of subject. Reject an unexplained example even if each sentence is
  individually fluent; do not accept a generic assurance disclaimer in place
  of a specific, decision-relevant scope statement;
- direct statements throughout the title, headings, body, tables, captions,
  and closing, following `editorial-voice-v2.md#direct-statements-without-rhetorical-reversals`.
  Return even a single invented rebuttal such as `A가 아니라 B` or `A라고
  해서 B는 아닙니다`, and defensive judgments such as `단정할 근거는
  없습니다`. Preserve direct factual negatives, exact quotations, code, and
  material warnings; require the actual scope or condition where it matters;
- concrete predicates, following
  `editorial-voice-v2.md#concrete-predicates-instead-of-abstract-nominal-judgments`.
  Return an abstract label such as `도입 판단의 첫 조건입니다` when it hides
  the actual action or adds an unsupported priority. Accept natural
  definitions and genuine criteria; do not reject `~입니다` by itself or
  require tentative endings for established facts. Check that the closing
  answers the article's question rather than repeating an earlier check;
- the primary reader, plain identity, easiest start, and evidence boundary;
- for a broad explainer, a locked map of the questions created by the title and
  opening, one owner section for each question, and explicit adjacent-topic
  exclusions;
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
- an opening-movement test: does a truthful, subject-specific situation raise
  the article's real question, lead to one useful answer or action, and then
  establish the evidence boundary without an abstract search-result inventory,
  a canned `결론부터 말하면` pivot, or a repeated slogan? Treat these as
  reasoning beats rather than a fixed sentence count;
- for troubleshooting and procedural intent, the first safe action or default
  choice before the lead visual and table of contents;
- a title-plus-headings-only pass that exposes the action or decision order,
  names every real branch, and does not require opening a section to learn what
  `추가 확인` or a similar aggregate label contains;
- a topic-boundary pass in which a cold reader can name the promised subject
  after reading only the title and headings. Return an article whose outline is
  better described by an adjacent category such as `healthy ageing`, `general
  productivity`, or `overall device care` than by its public title;
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
- an opening that answers the reader without a generic presenter roadmap,
  interchangeable scene, abstract result summary, or repeated conclusion;
- a paragraph-level new-information pass in which every retained paragraph
  adds a fact, evidence, action, comparison, limitation, or necessary branch;
- a topic-link test for every practical recommendation. If the advice could be
  pasted unchanged into a generic guide for the same demographic, require an
  explicit subject-specific cause, evidence link, tradeoff, warning, or next
  decision; otherwise return it for deletion or rewrite;
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
  repeated across the opening, body sections, and closing. For an experiment
  or comparison, allow one compact synthesis of the separate results when it
  answers the title's question. Verify its verdicts against the detailed
  evidence, including partial success and scope, rather than rejecting all
  repeated outcomes. Follow `editorial-voice-v2.md#results-that-answer-the-title`;
- for comparisons, a closing judgment connected to the presented findings and
  the author's stated purpose and current use. Return a generic `직접 써 보고
  결정하세요` ending or unsolicited trial, additional subscription, or migration
  advice. A necessary personal test must name a concrete condition and the
  observation that would change the decision; preserve both products' evidence
  and do not treat the author's preference as a universal performance result;
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

For a broad explainer, also fail the source when it answers a guideline's full
list more completely than it answers the reader's actual questions. Accurate
adjacent advice is still scope drift when it displaces the promised cause,
personal relevance, realistic intervention, common misconception, or
escalation boundary.

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
