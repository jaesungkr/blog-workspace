#!/usr/bin/env python3
"""Print the Tistory upload queue or bind one verified CDN URL to media.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rich_post_common import (
    atomic_write_json,
    is_tistory_media_url,
    validate_bundle,
)


def print_errors(result: dict) -> None:
    for warning in result["warnings"]:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in result["errors"]:
        print(f"ERROR: {error}", file=sys.stderr)


def upload_rows(result: dict) -> list[dict]:
    rows: list[dict] = []
    for item in result["manifest"].get("items", []):
        if not isinstance(item, dict):
            continue
        rows.append(
            {
                "id": item.get("id"),
                "publish_path": item.get("publish_path"),
                "sha256": item.get("sha256"),
                "width": item.get("width"),
                "height": item.get("height"),
                "kind": item.get("kind"),
                "tistory_url": item.get("tistory_url", ""),
            }
        )
    return rows


def run_plan(result: dict, as_json: bool) -> int:
    rows = upload_rows(result)
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0
    print("id\tpublish_path\tpixels\tsha256\ttistory_url")
    for row in rows:
        dimensions = f"{row['width']}x{row['height']}"
        print(
            f"{row['id']}\t{row['publish_path']}\t{dimensions}\t"
            f"{row['sha256']}\t{row['tistory_url']}"
        )
    return 0


def run_set_url(
    result: dict,
    post_dir: Path,
    media_id: str,
    url: str,
) -> int:
    if result["meta"].get("status") != "reviewing":
        print(
            "ERROR: bind Tistory URLs only while article status is `reviewing`",
            file=sys.stderr,
        )
        return 1
    if not is_tistory_media_url(url):
        print(
            "ERROR: URL must be HTTPS on an allowed Tistory CDN host",
            file=sys.stderr,
        )
        return 1

    manifest = result["manifest"]
    items = manifest.get("items")
    if not isinstance(items, list):
        print("ERROR: media.json items must be an array", file=sys.stderr)
        return 1
    selected: dict | None = None
    for item in items:
        if not isinstance(item, dict):
            continue
        if item.get("tistory_url") == url and item.get("id") != media_id:
            print(
                f"ERROR: URL is already bound to {item.get('id')}",
                file=sys.stderr,
            )
            return 1
        if item.get("id") == media_id:
            selected = item
    if selected is None:
        print(f"ERROR: unknown media id: {media_id}", file=sys.stderr)
        return 1

    selected["tistory_url"] = url
    manifest_path = post_dir / "media.json"
    try:
        atomic_write_json(manifest_path, manifest)
    except (OSError, TypeError, ValueError) as exc:
        print(f"ERROR: cannot update media.json: {exc}", file=sys.stderr)
        return 1
    print(f"bound {media_id}: {url}")
    print("NOTE: rerun remote-media recording and both browser QA gates.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare and bind the deterministic Tistory media upload map."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    plan = subparsers.add_parser("plan", help="Print upload order and identity data")
    plan.add_argument("post_dir")
    plan.add_argument("--json", action="store_true")
    bind = subparsers.add_parser("set-url", help="Bind one final Tistory CDN URL")
    bind.add_argument("post_dir")
    bind.add_argument("media_id")
    bind.add_argument("url")
    args = parser.parse_args()

    post_dir = Path(args.post_dir).resolve()
    result = validate_bundle(post_dir)
    print_errors(result)
    if result["errors"]:
        return 1
    if args.command == "plan":
        return run_plan(result, args.json)
    return run_set_url(result, post_dir, args.media_id, args.url)


if __name__ == "__main__":
    raise SystemExit(main())
