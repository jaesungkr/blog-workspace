# dev.log editorial standard

## Identity and format

- Write for the Korean Tistory blog dev.log, whose identity is
  `추측 대신 검증(Tested, not guessed)`.
- Optimize monetized posts for useful search traffic without sacrificing
  accuracy.
- Treat source synthesis as a foundation, not the post's differentiator. A
  monetized post should add at least one verifiable first-party contribution
  such as an original test, exact environment, dataset, log, screenshot,
  observation, or evidence-based decision framework.
- Use consistent 존대어 in all body prose, including introductions,
  explanations, tables, captions, and closings. Prefer natural
  `~습니다/~입니다/~해 보겠습니다` forms and do not mix them with 한다체.
- Deliver finished posts as rendered Markdown, not inside an outer code fence.
  Article code blocks may use normal fences.
- Use `###` for section headings. Number major sections when it improves
  navigation.
- Do not use an em dash (`—`); use a hyphen (`-`).
- Include at least one generated, publishable image with every complete post.
  Follow `image-guide.md` and record its recommended placement and alt text
  outside the article body.

## Titles and headings

- Put the likely search keyword near the front, then add a differentiating hook.
- Connect unfamiliar subjects to something the reader already knows.
- Avoid bland concept lists.
- End titles and headings with a noun, phrase, contrast, or reason form. Do not
  end them with `~다`.
- Make headings short and informative enough that scanning them reveals the
  argument.

## Opening and structure

- Start every post with the short greeting `안녕하세요. dev.log입니다.` unless
  the user supplies a different greeting.
- Follow the greeting with a conversational setup of roughly 2-4 sentences:
  raise a familiar scene, question, or point of confusion and explain why the
  topic matters before presenting the main result.
- Keep the setup warm but purposeful. Do not add a long self-introduction,
  generic small talk, or unrelated throat-clearing.
- Place the memorable conclusion or question within the opening 5-6 sentences.
- A natural one-sentence scope cue such as `이번 글에서는 직접 비교해 봤습니다`
  is allowed. Avoid a mechanical roadmap that lists every section in order.
- Never place an unfamiliar method, model, metric, acronym, or product name in a
  result table before explaining what it is and why it was included.
- For comparisons and tests, use this reader order when the subject is
  unfamiliar: conversational opening -> comparison map -> test design and
  judging rule -> compact results summary -> detailed results -> practical
  choice.
- A comparison map briefly divides the methods into understandable families,
  defines every label later used in tables, and explains the practical
  difference between them.
- For a technical comparison, show each method's complete calculation path
  before results: what goes in, whether it is normalized or vectorized, what the
  representation contains, how it is compared, and what the final score means.
  A compact arrow flow, conceptual numeric example, or 3-4 column table is
  usually enough.
- Separate stages readers commonly confuse, such as preprocessing,
  vectorization, model inference, similarity calculation, ranking, and final
  judgment. Explicitly say when two methods share a later calculation but
  create different representations, and when another method does not use that
  calculation at all.
- A test-design section states what was tested, what counts as a good result,
  how scores should be read, and any sample-size or environment limitation
  before showing winners.
- Place the compact final-results summary after that orientation, not
  necessarily immediately after the greeting. Show the best choice by use case,
  the observed result, and the important limitation.
- Label the scope of every result table in its heading or lead-in. Distinguish a
  result from one scenario or small test from an overall recommendation so a
  reader cannot mistake `three search questions` for a universal model ranking.
- When the reader's main intent is `결국 무엇을 쓰면 되는가`, give a direct
  default choice when the evidence supports one, then state the important
  purpose-specific exceptions. Do not make the reader infer the recommendation
  from several score tables.
- If presenting an overall rank, define what is being ranked and the criteria
  used, such as breadth, observed performance, speed, failure risk, or
  implementation cost. Include measured evidence and a limitation for each
  rank, and state whether it is a benchmark rank or a practical adoption
  priority.
- Keep paragraphs to roughly 3-4 sentences and change paragraphs with the
  subject.
- Define a technical term in plain Korean at first use.
- Use one everyday analogy per difficult concept at most.
- Turn three or more comparable items into bullets or a table.
- Use Markdown tables for comparisons, tradeoffs, levels, or decision criteria.
  Keep 3-4 columns, short cells, and a one-line introduction above each table.
- For explanations, prefer definition -> structure -> mechanism -> example.
- For tutorials and reviews, consider scene/problem -> pain -> solution ->
  Before/After -> real use -> limitation -> close.

## Voice

- Put one message in each sentence, but join clauses when forced short sentences
  sound mechanical.
- Prefer direct verbs and spoken-natural Korean.
- Assume some readers are not developers. Explain each technical term in plain
  Korean at first use and describe what it changes for the reader before
  discussing implementation details.
- Do not treat a plain-language synonym as a full explanation. For each central
  method, cover what goes in, what it measures, why it differs from the
  alternatives, and where it tends to fail.
- Explain the mechanism with a small familiar example before introducing
  production code. Label invented numeric vectors or simplified calculations as
  structural examples rather than measured results.
- When comparing several models that use the same technique, first explain the
  shared technique, then explain how the models differ in training purpose,
  language focus, size or speed, and expected use.
- Before interpreting a score table, tell the reader what a higher or lower
  value means and what pattern would count as success.
- Prefer a conversational question, familiar example, or short `쉽게 말하면`
  explanation when a paragraph becomes abstract. Use these deliberately rather
  than in every paragraph.
- Keep code and implementation detail available for readers who need it, but
  make the conclusion understandable without reading the code blocks.
- Minimize first person in monetized posts. Express tests as `직접 써본 결과` or
  `테스트에서는` when true.
- Remove hype, sarcasm, emotional intensifiers, generic reassurance, and filler.
- Avoid habitual summary constructions such as `~인 셈이다`, `~하게 된다`, and
  `~해진 셈이다`.
- Use about one inline bold sentence or phrase per section, not per paragraph.
- Keep humor to one place when it fits.

## Evidence hygiene

- Attach a source and measurement basis to statistics and benchmarks.
- Mark facts, estimates, and examples distinctly.
- Give every strong claim at least one verifiable support line.
- Never present folklore, unattributed quotations, or anecdotes as fact.
- Never attribute Codex-run research or tests to the user. State the actual
  actor and method, or use neutral phrasing when authorship is not material.
- For original tests, retain the inputs, environment, judging rule, raw or
  representative output, and at least one failure or limitation.
- State limits, costs, uncertainty, and counterarguments honestly.
- Weave attribution into the sentence. Omit detached footnotes, a references
  appendix, `※` disclaimers, and sponsorship boilerplate unless the user
  requests them or the publishing context legally requires them.

## Human signal and anti-template check

- Do not mistake sentence variation for originality. A polished rewrite of
  information already available elsewhere remains generic.
- Show why this author chose the question, what was inspected or run, what
  changed the initial view, and what the reader should do differently.
- Avoid repeating the same greeting-plus-summary-table-plus-conclusion skeleton
  when the subject calls for a narrative test, troubleshooting sequence,
  annotated example, or failure analysis.
- Explain material AI assistance when readers would reasonably ask how the work
  was produced. Keep responsibility for facts, tests, and judgment explicit.
- Apply the substitution check: if another blog name can replace `dev.log`
  without weakening the post, add stronger first-party evidence or a clearer
  connection to an existing series.

## Korean sentence hygiene

Rewrite these patterns rather than merely deleting keywords:

| Problem | Typical symptom | Preferred repair |
|---|---|---|
| Translationese | `~에 의해`, `~를 가지다`, excessive `~에 대한` | Active, direct Korean |
| Double passive | `보여진다`, `쓰여지다`, `되어지다` | `보입니다`, `쓰입니다`, `됩니다` |
| Abstract nominalization | `검토를 진행합니다`, `실시합니다` | `검토합니다`, direct verb |
| Zombie noun | `개선이 이루어집니다` | `개선합니다` |

Remove hedges such as `~라고 할 수 있다`, `~인 것으로 생각된다`, and
`~하는 부분이 있다` unless uncertainty is real and material.

## Closing

- Close with a concrete next action when natural.
- A Log analysis may instead end with one or two plain personal observations.
- A Trends post ends with relevance to Korean readers and one or two restrained
  personal observations. Only here may `~것 같다` be used sparingly.
- Do not end with a list of rhetorical questions, a heavy political or social
  editorial, a metaphor, generic thanks, or reassurance.

## Independent final audit

Re-read from the start as if someone else wrote it. Revise until all applicable
checks pass:

- Body uses consistent 존대어 from greeting through closing and contains no
  accidental 한다체 paragraphs.
- Title starts from search intent and title/headings do not end in `~다`.
- The post starts with the standard greeting, then a short conversational setup
  that explains why the topic matters.
- The opening 5-6 sentences contain the memorable conclusion or question
  without a mechanical roadmap.
- Every method, model, metric, and acronym used in a result table has already
  been explained in plain Korean.
- Every central method has a readable input-to-result chain, and shared steps
  such as vectorization or cosine similarity are distinguished from
  method-specific steps.
- Comparison and test posts establish the comparison map, test design, scoring
  rule, and limitations before the final-results summary table.
- The results summary includes a use-case choice, observed result, and
  limitation without relying on unexplained IDs or labels.
- Scenario-specific result tables are clearly labeled and cannot be mistaken for
  an overall ranking.
- A reader seeking a choice receives a direct default recommendation plus
  purpose-specific exceptions; any overall rank states its criteria, evidence,
  and limits.
- A non-developer can understand the main conclusion without reading code or
  already knowing the technical terms.
- Headings are short, phrase-like, and scannable.
- Bold emphasis averages about one per section.
- Sentences flow naturally rather than forming a staccato list.
- Terms are defined and comparisons use concise tables where useful.
- First person, hype, filler, translationese, double passive, nominalization,
  and zombie nouns are removed.
- Every number and strong claim has a source, basis, and appropriate limitation.
- The post contains a verifiable first-party contribution and does not rely on
  source summary alone.
- Test authorship is accurate; no Codex-run work is presented as the user's
  personal experience.
- The post passes the substitution check and has a clear reason to exist on
  dev.log.
- No invented anecdote, detached disclaimer, or references appendix remains.
- Limitations and counterarguments are visible.
- Closing follows the category rule.
- Output is rendered Markdown without an outer code fence.
- At least one final blog image is generated, inspected, saved under the post's
  `assets/` directory, previewed for the user, and accompanied by alt text and
  placement guidance.
