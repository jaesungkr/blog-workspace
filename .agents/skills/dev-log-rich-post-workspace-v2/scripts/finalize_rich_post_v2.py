#!/usr/bin/env python3
"""Promote a passed rich-post v2 candidate and write final deliverables."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
from pathlib import Path

from render_rich_post_v2 import render_outputs
from rich_post_v2_common import validate_bundle


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def with_status(text: str, status: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("article.md is missing YAML frontmatter")
    closing = next(
        (index for index, line in enumerate(lines[1:], 1) if line.strip() == "---"),
        None,
    )
    if closing is None:
        raise ValueError("article.md frontmatter is not closed")
    for index in range(1, closing):
        if re.match(r"^status\s*:", lines[index]):
            ending = "\n" if lines[index].endswith("\n") else ""
            lines[index] = f"status: {status}{ending}"
            return "".join(lines)
    raise ValueError("article.md frontmatter has no status field")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Require the v2 source, remote-media, and one final-page pass; "
            "then set ready and write the exact paste fragment."
        )
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--output-dir",
        default="dist",
        help="Final HTML directory, relative to the repository by default.",
    )
    parser.add_argument(
        "--paste-file",
        required=True,
        help="User-facing .txt path that receives only the exact HTML fragment.",
    )
    parser.add_argument(
        "--require-second-fetch",
        action="store_true",
        help="Require the optional second CDN byte verification for high-risk media.",
    )
    args = parser.parse_args()

    post_dir = Path(args.post_dir).expanduser().resolve()
    article_path = post_dir / "article.md"
    if not article_path.is_file():
        print(f"ERROR: missing article.md: {article_path}", file=sys.stderr)
        return 1
    try:
        original_article = article_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read article.md: {exc}", file=sys.stderr)
        return 1

    before = validate_bundle(
        post_dir,
        require_publish_urls=True,
        require_final_pass=True,
        require_remote_verification=args.require_second_fetch,
    )
    if before["meta"].get("status") != "reviewing":
        before["errors"].append("finalize only a `reviewing` candidate")
    if before["errors"]:
        for error in before["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    try:
        ready_article = with_status(original_article, "ready")
        atomic_write_text(article_path, ready_article)
        ready = validate_bundle(
            post_dir,
            require_publish_urls=True,
            require_final_pass=True,
            require_remote_verification=args.require_second_fetch,
        )
        if ready["errors"]:
            raise ValueError("; ".join(ready["errors"]))
        output_dir = Path(args.output_dir).expanduser().resolve()
        preview, fragment = render_outputs(
            ready,
            output_dir,
            preview_media_source="remote",
        )
        slug = str(ready["meta"]["slug"])
        preview_path = output_dir / f"{slug}-rich-preview.html"
        fragment_path = output_dir / f"{slug}-tistory-fragment.html"
        paste_path = Path(args.paste_file).expanduser().resolve()
        atomic_write_text(preview_path, preview)
        atomic_write_text(fragment_path, fragment)
        atomic_write_text(paste_path, fragment)
        if digest(fragment) != hashlib.sha256(paste_path.read_bytes()).hexdigest():
            raise ValueError("paste file differs from the final fragment")
    except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
        try:
            atomic_write_text(article_path, original_article)
        except OSError as restore_exc:
            print(
                f"ERROR: finalization failed and article restore failed: {restore_exc}",
                file=sys.stderr,
            )
            return 1
        print(f"ERROR: finalization failed; status restored: {exc}", file=sys.stderr)
        return 1

    print(f"preview: {preview_path}")
    print(f"fragment: {fragment_path}")
    print(f"paste file: {paste_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
