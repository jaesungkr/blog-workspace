# Reader-first editorial gate

Apply this gate to every rich post. Give it extra weight when the subject is a
new product, unfamiliar model, specialist tool, or technical comparison that a
general reader may encounter through search.

## Contents

- Establish the reader contract
- Open an unfamiliar subject
- Explain technical material in layers
- Keep headings useful and short
- Make comparisons self-explanatory
- Make usage instructions executable
- Recheck after material revision

## Establish the reader contract

Record these decisions before drafting:

- Choose one primary reader and state what that reader probably does not know.
- Choose a familiar anchor that explains the subject without distorting it.
- State the easiest useful first action for a non-specialist.
- Separate the no-code path from developer, API, and self-hosted paths.
- List the terms, prerequisites, paid entitlements, and identifiers that can
  block the first attempt.

When both developers and non-developers are expected, make the opening
accessible to the non-developer and layer technical detail later. Do not make
the broader audience decode architecture or benchmark names before learning
what the subject is.

## Open an unfamiliar subject

After the standard greeting, make the first two or three paragraphs answer
these questions in order:

1. What is it, using a familiar category or comparison?
2. What can an ordinary reader do with it, and where is the easiest place to
   start?
3. What did this article directly test, recalculate, or verify, and what did it
   not test?

Lead with specifications only when the reader's primary query is explicitly
about those specifications. Otherwise move architecture, parameter counts,
benchmarks, and deployment scale after the plain-language identity and first
use path.

Remove empty throat-clearing, launch hype, internal lifecycle wording, visible
`RICH POST` labels, and generated reading-time badges unless the user asks for
them. They do not help a reader understand the subject.

## Explain technical material in layers

At the first meaningful use of a technical term, use this sequence:

`exact term -> plain meaning -> why it matters to the reader`

After a large number, rank, file size, token limit, or infrastructure count,
state the practical consequence. Keep the exact term for accuracy, but never
leave the interpretation to the reader.

Give each paragraph one job. Prefer a concrete noun, action, example, or
consequence over abstract framing. When a paragraph must serve specialists,
precede it with the non-specialist meaning instead of opening with jargon.

## Keep headings useful and short

Treat a heading as a navigation label, not a compressed summary paragraph.

- Give one heading one job.
- Prefer a short noun phrase or familiar label when the section's first
  sentence immediately names the subject and scope.
- Keep conventional headings such as `평가 결과`, `사용법`, or `참고 자료`
  when they scan better than a longer claim.
- Do not concatenate the product name, source type, sample count, and result
  into one heading.
- Do not make a heading sentence-shaped merely to satisfy a subject or keyword
  test.
- Keep the search term early in the public title, but do not repeat it in every
  heading.

Reject a heading when a reader must reread it to parse the claim, or when it
contains three or more of these at once: subject, source, method, count,
ranking, conclusion. Move the detail into the opening sentence or table.

For example, prefer `코딩 평가 결과` plus an immediate scope sentence over
`제품명 공식 코딩 평가 9개 모두 3위 안`.

Run both checks:

1. **Scan test:** Do the title and headings reveal the article's route?
2. **Overload test:** Does any heading try to carry the whole paragraph?

## Make comparisons self-explanatory

Before a comparison table, state:

- who or what is being compared;
- how many comparison targets exist;
- whether the source is vendor-authored, independent, or directly rerun;
- whether higher or lower values are better;
- whether rows use different units and must not be added or averaged.

Choose columns that let the reader understand each row without reverse
engineering it. For a benchmark ranking, prefer:

`test or criterion | target value | target rank | row leader`

Do not publish only a rank-count summary such as `1위 2개·2위 6개` when the
reader cannot see the compared models, the row leader, or the scoring scope.
Keep the summary after the detailed table if it still helps.

Name vendor caveats, different harnesses, internal benchmarks, exclusions, and
the boundary between a rearranged vendor table and independent validation.

## Make usage instructions executable

For an unfamiliar product, include the easiest no-code start before developer
integration unless the article is explicitly expert-only.

For every recommended route, provide as applicable:

1. the exact website, app, menu, or command where the reader starts;
2. sign-in, membership, payment, operating-system, or API-key prerequisites;
3. the exact selection path, command, or model identifier;
4. one representative first task or prompt;
5. a nearby official documentation link;
6. the most likely failure and the correct recovery condition.

Distinguish a missing entitlement from a stale model list or UI cache. Do not
present logout, refresh, reinstall, or retry as a universal fix.

Do not invent a button, icon, menu, keyboard shortcut, or upload path from
memory. Support a UI step with direct observation or an official instruction.
When the evidence proves that upload exists but not which button performs it,
say only that the reader can upload the supported file.

Keep first-party usage, Codex-run checks, user reports, and source-based
instructions visibly separate.

## Recheck after material revision

Before source validation, perform this reader pass:

- Read the title and headings alone.
- Read the opening as someone who has never heard of the subject.
- Check that every technical term and large number has a practical meaning.
- Verify that each comparison names its targets, rule, leader, and source
  character.
- Follow each usage route from prerequisite to exact entry point and official
  link.
- Remove internal format labels and unsupported UI details.

Record the actual `problem -> revision -> re-verification` chain in `audit.md`.
When the title, opening, headings, tables, links, or usage steps change
materially, return the article to `reviewing` and invalidate the old source and
browser approvals. Label old passes as historical; never describe them as the
current candidate's result.
