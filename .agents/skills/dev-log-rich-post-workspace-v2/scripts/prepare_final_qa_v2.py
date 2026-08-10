#!/usr/bin/env python3
"""Render the canonical remote light/dark candidates for one final v2 review."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from render_rich_post_v2 import render_outputs
from rich_post_v2_common import (
    SKILL_DIR,
    atomic_write_json,
    is_tistory_media_url,
    validate_bundle,
    validate_remote_media_records,
    validate_source_pass,
)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: prepare_final_qa_v2.py posts/YYYY-MM-DD-slug", file=sys.stderr)
        return 2
    post_dir = Path(sys.argv[1]).expanduser().resolve()
    result = validate_bundle(post_dir)
    errors = list(result["errors"])
    if result["meta"].get("status") != "reviewing":
        errors.append("prepare final QA while status is `reviewing`")
    if result["article_path"].is_file():
        validate_source_pass(post_dir, result["article_path"], errors)
    items = result["manifest"].get("items", [])
    for item in items if isinstance(items, list) else []:
        if isinstance(item, dict) and not is_tistory_media_url(
            str(item.get("tistory_url", ""))
        ):
            errors.append(f"{item.get('id', 'unknown')}: missing Tistory CDN URL")
    if result["manifest_path"].is_file():
        validate_remote_media_records(
            post_dir,
            result["manifest_path"],
            result["manifest"],
            errors,
            require_verification=False,
        )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    slug = str(result["meta"]["slug"])
    qa_dir = post_dir / "artifacts" / "qa-v2"
    light_dir = qa_dir / "final-rendered"
    dark_dir = qa_dir / "final-dark-rendered"
    try:
        light_preview, fragment = render_outputs(
            result,
            light_dir,
            preview_media_source="remote",
        )
        dark_preview, dark_fragment = render_outputs(
            result,
            dark_dir,
            preview_media_source="remote",
            preview_theme="dark",
        )
        if fragment != dark_fragment:
            raise ValueError("light and dark renders produced different fragments")
        write_text(light_dir / f"{slug}-rich-preview.html", light_preview)
        write_text(light_dir / f"{slug}-tistory-fragment.html", fragment)
        write_text(dark_dir / f"{slug}-rich-preview.html", dark_preview)
        write_text(dark_dir / f"{slug}-tistory-fragment.html", dark_fragment)
        measurements_path = qa_dir / "final-measurements.json"
        if not measurements_path.exists():
            template = json.loads(
                (SKILL_DIR / "assets" / "final-qa-template-v2.json").read_text(
                    encoding="utf-8"
                )
            )
            optional_profiles = []
            if result["workflow"].get("include_390") is True:
                optional_profiles.append((390, 844))
            if result["workflow"].get("include_768") is True:
                optional_profiles.append((768, 900))
            for width, _ in optional_profiles:
                decision = {
                    "width": width,
                    "readable_media": None,
                    "status": "pending",
                }
                template["viewports"].append(dict(decision))
                template["dark_viewports"].append(dict(decision))
            atomic_write_json(measurements_path, template)
    except (OSError, UnicodeError, ValueError, TypeError, KeyError) as exc:
        print(f"ERROR: cannot prepare final QA: {exc}", file=sys.stderr)
        return 1
    print(f"light preview: {light_dir / f'{slug}-rich-preview.html'}")
    print(f"dark preview: {dark_dir / f'{slug}-rich-preview.html'}")
    print(f"measurements: {measurements_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
