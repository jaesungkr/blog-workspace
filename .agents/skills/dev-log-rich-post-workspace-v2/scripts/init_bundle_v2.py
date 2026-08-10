#!/usr/bin/env python3
"""Create a new dev.log post bundle configured for rich-post v2."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

from rich_post_v2_common import REPO_ROOT, SKILL_DIR, atomic_write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a rich-post v2 bundle.")
    parser.add_argument("slug")
    parser.add_argument("--title", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--subcategory", required=True)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument(
        "--profile",
        choices=("standard-rich", "evidence-rich"),
        default="standard-rich",
    )
    args = parser.parse_args()

    command = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "blog.py"),
        "new",
        args.slug,
        "--title",
        args.title,
        "--category",
        args.category,
        "--subcategory",
        args.subcategory,
        "--date",
        args.date,
    ]
    completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
    if completed.returncode:
        return completed.returncode

    post_dir = REPO_ROOT / "posts" / f"{args.date}-{args.slug}"
    article_path = post_dir / "article.md"
    try:
        article = article_path.read_text(encoding="utf-8")
        article, count = re.subn(
            r"(?m)^(status:\s*planning\s*)$",
            r"\1\nformat: rich-post-v2",
            article,
            count=1,
        )
        if count != 1:
            raise ValueError("cannot add v2 format after planning status")
        article_path.write_text(article, encoding="utf-8")

        workflow = json.loads(
            (SKILL_DIR / "assets" / "workflow-template-v2.json").read_text(
                encoding="utf-8"
            )
        )
        workflow["profile"] = args.profile
        if args.profile == "evidence-rich":
            workflow["direct_capture"] = True
        atomic_write_json(post_dir / "workflow-v2.json", workflow)

        media = json.loads(
            (SKILL_DIR / "assets" / "media-template-v2.json").read_text(
                encoding="utf-8"
            )
        )
        atomic_write_json(post_dir / "media.json", media)
        if args.profile == "evidence-rich":
            capture_plan = (
                SKILL_DIR / "assets" / "capture-plan-template-v2.md"
            ).read_text(encoding="utf-8")
            (post_dir / "capture-plan.md").write_text(
                capture_plan,
                encoding="utf-8",
            )
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: bundle created but v2 setup failed: {exc}", file=sys.stderr)
        return 1

    print(f"rich-post v2: {post_dir.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
