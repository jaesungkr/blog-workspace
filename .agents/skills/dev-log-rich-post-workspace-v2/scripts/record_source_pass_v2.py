#!/usr/bin/env python3
"""Persist the independent editorial freeze before rich-post v2 release work."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from rich_post_v2_common import (
    ANY_DIRECTIVE_RE,
    DIRECTIVE_RE,
    article_content_sha256,
    atomic_write_json,
    sha256_file,
    split_frontmatter,
)


UNRESOLVED_RE = re.compile(r"(?i)\b(?:TODO|TBD|FIXME)\b")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Record the independent source-level pass that freezes a "
            "rich-post v2 article before the user's media upload and browser QA."
        )
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--by",
        required=True,
        dest="reviewer",
        help="Actual independent source reviewer.",
    )
    parser.add_argument(
        "--note",
        default="",
        help="Optional concise boundary or remaining-risk note.",
    )
    args = parser.parse_args()

    post_dir = Path(args.post_dir).expanduser().resolve()
    reviewer = args.reviewer.strip()
    if not reviewer:
        print("ERROR: --by must name the actual source reviewer", file=sys.stderr)
        return 1

    errors: list[str] = []
    article_path = post_dir / "article.md"
    brief_path = post_dir / "brief.md"
    evidence_path = post_dir / "evidence.md"
    for path in (article_path, brief_path, evidence_path):
        if not path.is_file():
            errors.append(f"missing {path.name}")
    metadata: dict[str, object] = {}
    article_body = ""
    if article_path.is_file():
        try:
            metadata, article_body = split_frontmatter(
                article_path.read_text(encoding="utf-8")
            )
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"cannot parse article.md: {exc}")
    if metadata.get("status") != "reviewing":
        errors.append("record the source pass while article status is `reviewing`")
    if metadata.get("format") != "rich-post-v2":
        errors.append("article.md must contain `format: rich-post-v2`")
    if re.search(r"(?m)^#\s+", article_body):
        errors.append("article body must not contain a page-level H1")
    if len(ANY_DIRECTIVE_RE.findall(article_body)) != len(
        DIRECTIVE_RE.findall(article_body)
    ):
        errors.append("every media directive must be standalone and kebab-case")

    for path in (article_path, evidence_path):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {path.name}: {exc}")
            continue
        if UNRESOLVED_RE.search(text):
            errors.append(f"{path.name} contains an unresolved marker")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    record = {
        "version": 2,
        "result": "pass",
        "checked_at": utc_now(),
        "checked_by": reviewer,
        "article_content_sha256": article_content_sha256(article_path),
        "brief_sha256": sha256_file(brief_path),
        "evidence_sha256": sha256_file(evidence_path),
        "note": args.note.strip(),
    }
    target = post_dir / "artifacts" / "qa-v2" / "source-pass.json"
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_json(target, record)
    except (OSError, TypeError, ValueError) as exc:
        print(f"ERROR: cannot save source pass: {exc}", file=sys.stderr)
        return 1
    print(f"source pass: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
