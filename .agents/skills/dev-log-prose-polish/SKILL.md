---
name: dev-log-prose-polish
description: Polish Korean dev.log article prose without changing its facts, evidence, authorship, or technical meaning. Use after a draft or material text revision when titles and headings feel templated, paragraph transitions feel difficult or mechanical, sentence rhythm feels AI-like, or the user asks for natural Korean, human editorial texture, voice, readability, or a final prose pass. Keep the article at reviewing and hand the result to independent article validation.
---

# dev.log prose polish

Polish the editorial surface after the evidence and explanation structure are
stable. Restore a post-specific line of thought; do not imitate a person,
optimize for an AI detector, or manufacture human signals.

## Load context

1. Resolve `repo_root` as the directory three levels above this skill
   directory. If the request names a `target_bundle`, staging copy, or review
   copy, resolve that exact directory separately and treat it as the only write
   target. Otherwise resolve `target_bundle` inside `repo_root`. Never silently
   redirect an explicit copy back to the canonical bundle.
2. Read `standards/editorial-standard.md` and
   `standards/category-guides.md` from `repo_root` completely. Read this skill's
   reference and analyzer from `repo_root`; read and edit bundle files only
   under `target_bundle`.
3. Read `brief.md`, `evidence.md`, `article.md`, and `audit.md` in the target
   bundle. Read any raw note or artifact needed to distinguish a sourced
   observation from invented voice.
4. Read `references/human-prose-benchmarks.md` completely.
5. Inspect the titles and headings of three to five recent, finished canonical
   posts. `Same category` means the same non-empty `subcategory`; if it is
   absent, use the top-level `category`. Exclude the target slug and posts that
   are not `ready` or `published`. If fewer than three remain, use every
   available same-category post, then fill the set with recent finished posts
   that share the article shape first and reader intent second. Stop after five
   total posts. Record the slugs, lifecycle states, and fallback reason in
   `audit.md`. Do not count `target_bundle` twice when it is a copy. Avoid
   repeating the repository's recent title skeleton merely because it passes
   the formal rules.

## Lock the content

Before rewriting, list the content invariants from the bundle:

- numbers, dates, code, commands, URLs, quotations, and table values;
- test actor, environment, method, result, failure, and limitation;
- user-supplied experience, opinion, and wording, unless the current request
  explicitly authorizes revising that wording;
- search intent, category requirements, lifecycle state, and image meaning.

Never add an anecdote, emotion, dialogue, failure, team reaction, personal
opinion, or first-person action that the source material does not support.
Never make a claim stronger to improve rhythm. Set `status: reviewing` before a
material prose edit; only the article validator may restore `ready`. If the
bundle is already `published`, do not silently demote or edit it. Confirm that
the request explicitly includes revising the published source, preserve
`published_url`, record that the live page may now differ, and route the edited
bundle through the orchestrator's validation and delivery gates.

## Find the post's own shape

Write one private spine sentence:

`[situation] met [specific constraint], so [actor] chose [action] and observed [result or changed judgment].`

Choose the structure that follows the material:

- case or retrospective: trigger -> constraint -> first choice -> collision or
  failure -> revision -> observed result -> remaining risk;
- explanation or argument: common belief -> counterexample -> principle ->
  concrete case -> applicable range and limit;
- tutorial: destination and prerequisite -> shortest path -> checkpoints and
  likely failures -> alternatives;
- reflection: scene -> change in thought -> grounded episode -> present
  judgment.

Do not force every post into `background -> problem -> solution -> result`.
Preserve a valid category-specific structure when it serves the reader. This
step diagnoses the existing structure; it does not authorize rebuilding it. If
the spine cannot describe the current section order, a claim needs new
evidence, or whole sections must move, stop and return the bundle to
`dev-log-writing`. Resume prose polish after the writing stage stabilizes the
argument.

## Diagnose before rewriting

Run the bundled analyzer as an inventory:

```bash
python3 "$repo_root/.agents/skills/dev-log-prose-polish/scripts/analyze_prose.py" \
  "$target_bundle/article.md"
```

Treat every signal as a review prompt, never as a score or automatic failure.
Use the reported line and sentence excerpts to inspect each match in context.
The sentence-ending distribution is a cadence overview, not a defect list; read
its samples and then the whole passage. Do not rewrite from a count alone.
Then perform four human checks:

1. Read only the public title and headings. Confirm they reveal this post's
   event, decision, observation, or useful navigation.
2. Apply the subject-substitution test. If another technology or topic can
   replace the subject without weakening a heading, make it more specific or
   justify keeping the conventional label for navigation.
3. Read each paragraph's last sentence beside the next paragraph's first
   sentence. Label the seam as cause, consequence, contrast, time, example,
   question, or deliberate reset.
4. Find smooth but empty lines that preview, summarize, or balance both sides
   without adding information.

## Rewrite titles and headings

- Keep the search term findable, but do not default to the recent
  `keyword - explanatory hook` pattern.
- When the user makes search traffic the title's top priority, inspect the
  current search results for the primary query and close variants before
  drafting. Put the broadest accurate intent near the front and the article's
  differentiator after it. Record whether the judgment is qualitative or based
  on actual query-volume data; never promise maximum traffic from a title
  alone.
- Draft candidates from different angles: concrete incident or number,
  decision or tradeoff, reader problem, observed result, or a precise question.
- Select the title whose promise the body actually pays.
- Build headings from the spine's real turns. Prefer a specific object, action,
  failed expectation, observation, or decision over labels such as `정체`,
  `이유`, `결과`, `방어`, or `정리`.
- Apply a scan-only clarity test to every heading. Without reading its section,
  a reader should be able to name the subject and what the section explains,
  compares, measures, or changes. Spell out what a fraction counts. When a
  heading mentions a discarded attempt, identify what invalidated it and
  whether it was rerun.
- Do not ban conventional headings such as `결과`, `장애 탐지`, `들어가며`, or
  `마치며` in isolation. Keep one when it genuinely improves navigation.
- Do not make every heading witty, interrogative, numbered, or sentence-shaped.
  Variety must come from the article's changing job, not a new template.
- Prefer concise headings, but do not remove the subject, measured object, or
  causal detail merely to make a heading shorter.
- Follow the repository's title and heading syntax, category convention, and
  ending rules.

## Repair paragraph flow

- Start the next paragraph from a concrete noun, action, result, or unanswered
  question left by the previous one.
- State the relationship itself instead of decorating a gap with `또한`,
  `한편`, `따라서`, or `이를 통해`.
- Replace chains of abstract nouns with an actor and a direct verb. Explain what
  changed for the reader before naming an implementation detail.
- Keep necessary caveats, but combine repeated `A가 아니라 B`, `다만`, and
  `그렇다고` defenses when one precise boundary can do the work.
- Remove mechanical roadmaps and repeated takeaways. A section does not need a
  bold maxim merely because neighboring sections have one.
- Vary sentence length only when the thought calls for it. Join choppy clauses;
  split a long sentence when its actor, action, and consequence become hard to
  follow.
- Read difficult paragraphs aloud. Prefer Korean that is easy to say while
  preserving the established 존대어 and the author's actual tone.

## Preserve honest author signal

Recover only signals already present in the material: the reason the question
was chosen, an inspected artifact, a rejected attempt, a changed expectation,
an exact constraint, or a bounded recommendation. Specificity and accountable
judgment matter more than slang, humor, emojis, or forced intimacy.

Do not copy a benchmark author's catchphrase or persona. Do not change
`Codex가 실행했습니다` into a user experience. When the evidence lacks a
needed detail, record an evidence gap rather than smoothing over it.

## Verify and hand off

1. Rerun the analyzer and compare signals without chasing zero findings.
2. Re-read the title and headings alone, every paragraph seam, and the full
   article aloud in spirit.
3. Compare all locked content against the source. Confirm numbers, links, code,
   tables, test authorship, and limitations remain intact.
4. When the public title changes, synchronize the selected title in
   `brief.md`, the heading in `evidence.md` and `audit.md`, and any image
   placement record that names a changed section.
5. Record representative
   `problem -> revision -> re-verification` entries in `audit.md`, including
   title or heading changes, repaired seams, removed empty phrasing, protected
   claims, and remaining concerns.
6. If a previously `ready` or explicitly authorized `published` bundle returns
   to `reviewing`, preserve its old validation history and prior lifecycle
   state as historical evidence. Add a new row that marks the current edit as
   awaiting revalidation. For a formerly published bundle, retain
   `published_url` and record that the live page still contains the older
   revision until the user republishes it. Do not leave an old final `ready` or
   `published` statement describing the current source state.
7. Leave the article at `reviewing` and hand it to
   `dev-log-article-validation`.

Report changed files, the protected content invariants, representative
before/after edits, and any remaining style or evidence concern. Do not create
images, set `ready`, commit, or push.
