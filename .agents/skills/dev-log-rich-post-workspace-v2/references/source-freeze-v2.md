# Source freeze v2

## Review boundary

Finish substantive writing before release QA. Independently verify:

- claims, numbers, dates, links, quotations, and authorship;
- the primary reader, plain identity, easiest start, and evidence boundary;
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

Return evidence or structure defects to writing. Return title, opening,
heading, or rhythm defects to prose polish. A clear full article does not pass
when its first screen or heading-only path still makes the reader hunt for the
next action. Repeat until the source passes.

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
