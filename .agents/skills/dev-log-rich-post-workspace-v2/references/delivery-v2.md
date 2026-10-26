# Delivery v2

## Finalize

After the source, remote-media, and final-page records pass, run:

```bash
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/finalize_rich_post_v2.py \
  posts/YYYY-MM-DD-slug \
  --output-dir dist \
  --paste-file <task-output-directory>/<slug>-tistory-fragment.txt
```

Add `--require-second-fetch` when routed. The finalizer:

- validates all current hashes and gates;
- changes `reviewing` to `ready` only after validation;
- restores `reviewing` if final rendering or paste-file creation fails;
- writes the final preview and fragment;
- writes a byte-identical raw-HTML `.txt` file.

Then inspect the exact diff, stage only task files, run affected repository
checks, commit, integrate without force, push to `origin/master`, and verify the
remote commit. Skill, script, template, CSS, or standard changes require the
full unit suite and `scripts/blog.py check --all`; an isolated new post does
not automatically require every repository regression test.

## Author-approved publication

Follow [tistory-publication-v2.md](tistory-publication-v2.md). The author reviews
and approves the specific article and asks to publish; Codex then carries out
the complete release in the Codex in-app browser without a second routine
permission request. A request to draft or proofread is not approval to publish.

Use the finalized TXT as the exact native-attachment fragment for the target
editor. Check its actual Tistory preview before clicking the final public
publish control. Confirm the successful result and article URL, record the
publication and submitted hash, then set `published` and commit/push the
lifecycle and evidence update. Leave subsequent visual checks and repairs to
the author unless explicitly requested; do not reopen the live page to inspect
images, responsive layout, themes, or title/cover contrast. If publication
succeeded but Git delivery failed, record that split state and resume from it;
do not publish a duplicate or claim the article is still unpublished.

Return the live article URL as the primary final link and the exact submitted
TXT as a backup. If a completion screenshot is needed, capture the already
observed success state without starting a new inspection pass. When the
author has not yet approved publication, provide the local review candidate
and wait at `reviewing`; do not route routine upload/paste work back to them.
