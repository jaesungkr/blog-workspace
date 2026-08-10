#!/usr/bin/env python3
"""Validate a staged dev.log rich-post v2 bundle."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rich_post_v2_common import validate_bundle


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate article.md, media.json, and rich-post v2 gates."
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--require-publish-urls",
        action="store_true",
        help="Require every media item to have a final HTTPS Tistory URL.",
    )
    parser.add_argument(
        "--require-final-pass",
        action="store_true",
        help="Require the one current independent final-page validation record.",
    )
    parser.add_argument(
        "--require-remote-verification",
        action="store_true",
        help="Require the independent remote-media fetch record.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print a machine-readable result.",
    )
    args = parser.parse_args()

    result = validate_bundle(
        Path(args.post_dir),
        require_publish_urls=args.require_publish_urls,
        require_final_pass=args.require_final_pass,
        require_remote_verification=args.require_remote_verification,
    )
    payload = {
        "post_dir": str(result["post_dir"]),
        "media_count": len(result["items_by_id"]),
        "directive_count": len(result["directives"]),
        "require_publish_urls": result["require_publish_urls"],
        "require_final_pass": result["require_final_pass"],
        "require_remote_verification": result["require_remote_verification"],
        "errors": result["errors"],
        "warnings": result["warnings"],
        "status": "pass" if not result["errors"] else "revision_required",
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"rich-post-v2: {payload['status']}")
        print(
            f"media {payload['media_count']} · directives "
            f"{payload['directive_count']}"
        )
        for warning in payload["warnings"]:
            print(f"WARNING: {warning}")
        for error in payload["errors"]:
            print(f"ERROR: {error}")

    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    sys.exit(main())
