# Approved public article synchronization · 2026-10-30

Archive-only synchronization of already-published, author-approved edits for
https://dop3n.tistory.com/141, /144, /143, /127 and /62. No Tistory publication
or settings changes were performed in this repository task.

Input: `blog-approved-public-patches-20261030.zip`, 9009 bytes,
SHA256 `4ddc9b68486c32446cffd99febe6a262a1a50fb939d394bad8d2c450af9f5410`.
Size and hash verified before applying. Base master:
`4d5b63732d2c26b9c3024aab925521c2a49ce916`.

The five `post-*.patch` files record the actual minimal changes to canonical
Markdown; they are partial public diffs, not full article or editor backups.
`SOURCES.md` retains the supplied public source basis. Source claims were
synchronized from the approved patch, not newly researched or benchmarked.

| Public post | Canonical bundle | Change |
| --- | --- | --- |
| 141 | `posts/2026-09-29-opus-5-5-vs-gpt-6-astra` | One contextual Effort link |
| 144 | `posts/2026-09-30-gpt-6-1-sol-vs-opus-5-5` | Effort and Opus–Astra links |
| 143 | `posts/2026-09-29-sonnet-5-5-vs-gpt-6-sol` | Sonnet cache read $0.10/1M correction; successor and Effort links |
| 127 | `posts/2026-09-06-gpt-6-astra-vs-fable-5-1` | Historical date clarification and successor comparison link |
| 62 | `posts/2026-07-25-orca-agent-ide-guide` | Approved title, introduction and four-step quick start |

## Context reconciliation

- Exact titles and matching body passages identify each canonical file. Existing
  `published_url` fields are empty; their metadata is preserved, with public URL
  mapping recorded here rather than guessing or rewriting publication state.
- Post 144's older science paragraph in the input is absent from current master.
  Current master has a fuller Terminal-Bench Science paragraph and retains the
  official source elsewhere in that section. Only the approved new comparison
  link paragraph was inserted after that existing science paragraph. All current
  benchmark text, values and citations are unchanged.
- Post 62's repository introduction differs from the live before-fragment. Only
  text between the greeting and section 1 was replaced with the approved opening
  and quick start. The technical body from section 1 through the end is
  byte-identical to the base. Title is the only frontmatter change.
- HTML emphasis, paragraphs and ordered list were converted to Markdown. The
  four list separators use hyphens, as required by the repository checker.
- The standard Orca renderer emits headings without IDs. Quick-start links
  therefore use `https://dop3n.tistory.com/62#` plus the three approved existing
  live heading IDs. They work as public-page links in both Markdown and generated
  HTML rather than unresolved local preview fragments. The parent task reported
  live anchor verification; this task did not perform a new browser check.

## Validation and limits

- `python3 scripts/blog.py check <bundle>`: all five passed, zero errors/warnings.
- `python3 scripts/blog.py render <Orca bundle>`: passed; HTML generated in
  ignored `dist/`. Static inspection confirms one four-item quick-start list and
  six links targeting the three approved public anchors.
- Dedicated `check_rich_post_v2.py` and `render_rich_post_v2.py` were attempted for
  all four AI bundles. All are blocked by existing media/QA inconsistencies:
  141/127 have media and remote-fetch record mismatches; 144 has remote-fetch
  toolchain mismatch; all three have old renderer/CSS/capture records. Post 143
  has a native attachment alt mismatch. The same failures were reproduced on
  base articles before the edits. The current edits also invalidate article
  content hashes for 141/144/127, as expected. Historical QA records were not
  rewritten or presented as fresh passes.
- No new browser/responsive/media verification was performed. These source
  archives are not newly certified publication bundles. Existing lifecycle
  values are preserved; rendering blockers need a separate publication QA task.
- Diff review and automated invariants confirm original dates, slugs, other
  metadata, image references, AI tables and Orca sections 1–11 are unchanged.
- Public additions and patches were reviewed for secrets, signed media URLs and
  private data. No analytics, advertising settings, private HTML, credentials,
  unrelated posts, image assets or renderer files are included.
