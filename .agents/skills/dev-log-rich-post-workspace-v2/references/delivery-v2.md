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

## Publication boundary

Codex never uploads Tistory media or creates or edits a Tistory draft. The user
first uploads the handed-off local media privately and returns the CDN URLs;
Codex then binds and validates those URLs and creates the final `.txt` HTML.
The user pastes the `.txt`, checks the Tistory preview and hELLO theme toggle,
and publishes. Keep `status: ready` until the user supplies the live URL.
Validate the live desktop and mobile page before changing to `published`.
