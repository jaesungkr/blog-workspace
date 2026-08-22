# Editorial voice and density v2

Use this gate for every new or materially revised rich-post v2 source. It
supplements the shared prose-polishing skill with the failures that remained
visible after the first v2 production post.

## Calibration, not imitation

This contract was calibrated on 2026-08-14 from:

- the repository source at
  `posts/2026-08-13-grok-bot-guide/article.md`;
- the author's edited live Grok Bot post at
  <https://dop3n.tistory.com/entry/Grok-Bot-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%9D%BC%EB%A1%A0-%EB%A8%B8%EC%8A%A4%ED%81%AC%EC%9D%98-%EC%95%A0%EC%B0%A9-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8>;
- the six-pattern note at
  <https://curious-500.com/v2/community/post/1100>;
- the reminder to break formulaic transitions, over-explanation, and overly
  balanced rhythm at
  <https://www.threads.com/@human__bro/post/DWyjm8SEpEJ>.

The live Grok post is diagnostic evidence, not a voice template. The author
removed the source's defensive title disclaimer, shortened the evidence
boundary, and opened with the product's plain identity. Those edits reveal
what had been over-explained. The unchanged headings and some replacement
phrases still felt mechanical to the author, so do not copy either version as
a house style.

The public reference posts are also prompts for editorial judgment, not proof
of human authorship and not authorities on factual content. Translate their
useful observations into the checks below. Do not chase an AI-detector score.

## Preserve before cutting

Lock the article's facts, evidence, links, authorship, direct-test boundary,
prerequisites, exceptions, and material cautions. Compression may move or merge
them, but it may not weaken or delete them merely because they sound formal.

Natural prose does not mean deliberate mistakes, slang, emojis, chatty
fillers, invented anecdotes, fake uncertainty, or unsupported `~죠`,
`~거든요`, and `~했어요` endings. Keep the established Korean honorific
style. Uneven rhythm must come from the thought, not manufactured imperfection.

## Pass 0: lock the reader-benefit contract

Use this pass for recommendation and benefit explainers aimed at
non-specialists. Record the following in `brief.md` and the revision result in
`audit.md`:

- the situation, discomfort, or decision the reader already recognizes;
- what the reader does not yet know about the subject;
- one intended reader;
- one plain recommendation and its useful consequence;
- the practical choice or use the article supports;
- evidence detail and adjacent benefits deliberately excluded from the article.

Reject a title or opening that assumes the reader already knows a folk
association, search habit, nutrient, metric, feature, or mechanism. `붓기에
팥물을 찾는다면` assumes a connection that a first-time reader may not know;
name the recognizable problem and why the subject is worth recommending
instead. Do not broaden the reader to everyone who might benefit after research
reveals additional facts.

Within the first three publishable sentences, a recommendation or benefit
explainer should make the intended reader, recommendation, and useful
consequence understandable in ordinary language. This is a comprehension gate,
not a fixed sentence template. Explain the practical effect before asking the
reader to interpret `칼륨`, `식이섬유`, a benchmark, a feature name, or an
internal mechanism.

For a simple lifestyle explainer, begin with three stage-level jobs: why the
recommendation fits, how to choose or use it, and who needs a material caution.
This is a default, not a quota. Add a section only when it changes a separate
reader decision; merge background, mechanism, or evidence detail that merely
supports an existing job.

### Lock the topic boundary

For a disease, cause, prevention, or another broad explainer, write the small
set of questions that the public title and opening naturally create. Give each
question one owner section and list adjacent topics that will stay out. Do not
copy a source taxonomy, clinical guideline, product feature list, or category
template into the outline merely because the material is accurate.

Apply the topic-link test to every heading and practical paragraph:

- What exact question from the title or opening does this answer?
- What subject-specific cause, evidence, tradeoff, warning, or next decision
  connects the advice to this article?
- Could the paragraph be pasted unchanged into a generic article for the same
  demographic or category?

If the last answer is yes and the first two have no concrete answer, remove the
paragraph or rewrite it around the missing connection. For example, a dementia
article should not become a checklist for healthy ageing; exercise, blood
pressure, hearing, or diet belongs only when the prose explains how it changes
the reader's dementia-risk judgment. This is a scope test, not a ban on
foundational health advice.

## Pass 1: rewrite the heading strip

Read only the title and headings. For each heading, write its one reader job in
private: identify, choose, act, compare, verify, recover, or decide. A heading
passes only when its wording names that job naturally and the section fulfills
it.

Reject or rewrite a heading when:

- it uses `A가 아니라 B` to create importance instead of naming the useful
  distinction directly;
- it compresses a whole explanatory sentence into a headline;
- it stacks several abstract nouns or middle-dot items where one plain object
  and verb would be clearer;
- it joins two separable decisions with `와/과`, `및`, `~하고`, or a balanced
  pair merely to make the outline look complete;
- it says `정체`, `구조`, `기준`, `활용`, `살펴보기`, or another reusable label
  without the subject and practical consequence;
- it promises a broader scope than the section actually covers.

Do not solve this by turning every heading into a question or an imperative.
Use the form the section needs: a concise noun phrase, a direct action, a real
reader question, a finding, or a bounded decision. Keep a conventional heading
when it is the clearest navigation.

The Grok draft illustrates the diagnosis, not mandatory replacements:

| Mechanical surface | Why it failed | Better direction |
|---|---|---|
| `Grok Bot은 답변이 아니라 앱 안의 결과를 만드는 도구` | contrast frame plus sentence-shaped explanation | name the concrete difference: `Grok과 Grok Bot은 무엇이 다른가` |
| `처음 맡길 일은 수집·정리·초안 만들기` | compressed noun list | give the first decision: `처음에는 초안까지만 맡겨 보세요` |
| `7일 체험 제공 여부 확인과 데스크톱 앱 설치` | two jobs and bureaucratic nouns | choose the real section scope or split the jobs |
| `첫 지시는 목표·자료·완료 조건·금지 행동까지` | four-item label with an omitted verb | state what the reader should put in the request |
| `전송·결제·변경은 승인 뒤로 남기기` | unnatural nominal ending | name who approves the consequential action |

After rewriting, read the strip aloud. It should sound like one article moving
through changing reader needs, not seven slogans built from the same mold.

## Pass 2: break AI-template sentence frames

Search in context for the following patterns. They are review prompts, not a
keyword ban:

- repeated `단순히 A가 아니라 B`, `A를 넘어 B`, `A에 그치지 않고 B`;
- repeated `~하는 순간, ~이 됩니다` or `~하면, ~이 됩니다`;
- generic `우리` that turns a bounded observation into a universal claim;
- comma chains that hide the actor and action;
- unsupported grand adjectives such as `혁신적인`, `효율적인`,
  `지속가능한`, `명확한`, `강력한`, or `획기적인`;
- roadmap and presenter phrases such as `이번 글에서는`, `오늘은`,
  `차근차근 살펴보겠습니다`, `알아보겠습니다`, and `함께 보겠습니다`;
- empty emphasis such as `핵심은`, `중요한 점은`, `가장 큰 차이는`,
  `주목할 점은`, or `여기서 한 단계 더 나아갑니다` when the following
  sentence can state the fact directly;
- repeated soft judgments such as `~하는 편이 좋습니다`, `~할 수
  있습니다`, and `~할 필요가 있습니다` where a direct observation,
  recommendation, or limitation is available;
- an explanation followed by `즉`, a bold takeaway, a list, and a closing
  recap that all restate the same point.

Replace the frame, not only the trigger word. Name an actor and direct verb,
show the condition that changes the recommendation, or delete the sentence
when the neighboring evidence already carries the meaning. Preserve a
contrast when the distinction itself is the claim.

Do not mechanically vary connectors or endings. A paragraph may start without
a connector when the heading or previous sentence already establishes the
relationship. Let sentence length change with the amount of thought. Split a
comma chain when its actor, action, or result becomes hard to say aloud.

## Pass 3: run the new-information test

Make a private reverse outline in `audit.md`. Give each paragraph one primary
job and one new unit it contributes:

- fact or observation;
- evidence or example;
- action or prerequisite;
- comparison or decision rule;
- limitation or exception.

Delete or merge a paragraph when removing it loses none of those units. A
sentence that only announces the next section, says the topic is important,
repeats the heading, paraphrases a table, or summarizes the previous paragraph
does not count as new information.

For a recommendation or benefit explainer, each retained paragraph must also
help the reader answer at least one of these questions: `나에게 왜 필요한가`,
`무엇을 선택하거나 해야 하는가`, `어느 정도 기대할 수 있는가`, or `언제
조심해야 하는가`. Research effort does not earn publication space by itself.
Keep the smallest representative number or comparison that changes the answer;
move supporting detail to a table or `evidence.md`. Do not repeat the same
number in a table, explanatory paragraph, summary box, and later recap.

For a broad explainer, `generally useful` is not new reader value by itself.
Each practical paragraph must also pay one title-created question and make its
subject-specific link explicit. When adjacent recommendations add no new cause,
tradeoff, warning, or decision, compress them behind the strongest
representative action or leave them in `evidence.md`.

For every central claim and action, name one owner section in the audit. A
later section may depend on it or refer back briefly, but must not explain the
same cause, procedure, evidence, and caution again. This ownership check is
semantic; the prose analyzer cannot perform it.

Pay special attention to safety boundaries. Keep a consequential warning close
to the action it limits. Do not repeat the full `draft first, approve later`
argument in the opening, use-case section, prompt section, approval section,
and closing. Choose the main section, then keep only the short reminder needed
to make another step safe.

Preserve the shortest complete explanation for troubleshooting: cause,
condition, next action, and material exception when each applies. Compression
is not permission to remove the branch that a reader needs to succeed.

## Pass 4: compress the edges and read aloud

The opening must earn the first screen. Give the reader the plain identity,
useful consequence, or first safe action without a presenter roadmap. A
greeting is allowed, but it cannot substitute for the answer. Move a caveat
beside the claim it qualifies unless the caveat changes whether the reader
should continue at all.

Do not create a standalone `효능의 한계`, `주의할 점`, or `오해와 진실`
section merely to display defensive completeness. Put one precise evidence
boundary beside the claim it narrows. Keep a separate caution section only when
the reader must make a distinct safety decision, and preserve every material
medical, legal, financial, security, or operational warning even when the
article is being compressed.

The closing must change or settle the reader's decision. Do not repeat the
article outline, copy the comparison table into prose, or restate every safety
rule. A bounded recommendation, unresolved risk, or next check is enough.

Read the complete article aloud in spirit. Mark passages that sound like a
press release, lecture script, generated checklist, or perfectly balanced
three-part cadence. Revise only where the wording hides the article's actual
judgment. Do not add spontaneity for its own sake.

## Required audit and independent gate

Record:

- the reader-benefit contract, including the reader's knowledge baseline and
  deliberately excluded detail when this pass applies;
- for broad explainers, the title-created question map, excluded adjacent
  topics, and topic-link test decisions;
- the original and selected heading strip, with the job of each section;
- representative template frames removed or justified;
- paragraphs deleted or merged by the new-information test;
- representative numbers or evidence detail moved out of repeated prose;
- caveats kept beside their claims and any separate safety section justified by
  a distinct reader decision;
- the owner section for every repeated central claim or action;
- facts, caveats, and branches protected during compression;
- any remaining passage the source reviewer must challenge.

The independent reviewer must cold-read `article.md` before reading these
notes. A polished article still fails when the reviewer can point to an
awkward heading, generic roadmap, empty paragraph, repeated takeaway, or
over-balanced rhythm that the audit declared acceptable without evidence.
