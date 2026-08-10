# Source freeze v2

## Review boundary

Finish substantive writing before release QA. Independently verify:

- claims, numbers, dates, links, quotations, and authorship;
- the primary reader, plain identity, easiest start, and evidence boundary;
- comparison targets, units, score direction, source character, and limits;
- prerequisites, exact entry point, identifiers, representative first task,
  likely failure, and official documentation;
- Korean honorific style, title-heading scan, paragraph seams, and preserved
  technical meaning.

Return evidence or structure defects to writing. Return title, opening,
heading, or rhythm defects to prose polish. Repeat until the source passes.

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
