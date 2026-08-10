#!/usr/bin/env python3
"""Bind the one independent light/dark final-page review to a v2 candidate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rich_post_v2_common import (
    REPO_ROOT,
    SKILL_DIR,
    SLUG_RE,
    article_content_sha256,
    atomic_write_json,
    bind_screenshot_evidence,
    merge_browser_capture_viewports,
    preview_structure_sha256,
    sha256_file,
    text_sha256,
    validate_browser_capture_receipt,
    validate_bundle,
)
from render_rich_post_v2 import render_outputs


def load_object(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create the single hash-bound rich-post v2 final-page record."
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument("--preview", required=True, help="Reviewed full preview HTML")
    parser.add_argument(
        "--dark-preview",
        required=True,
        help="Reviewed dark-theme full preview HTML",
    )
    parser.add_argument("--fragment", required=True, help="Reviewed Tistory fragment")
    parser.add_argument(
        "--measurements",
        required=True,
        help="JSON containing checked_at, checked_by, viewports, and fragment checks",
    )
    args = parser.parse_args()

    post_dir = Path(args.post_dir).resolve()
    preview_source = Path(args.preview).resolve()
    dark_preview_source = Path(args.dark_preview).resolve()
    fragment_source = Path(args.fragment).resolve()
    measurements_path = Path(args.measurements).resolve()
    for path, label in (
        (preview_source, "preview"),
        (dark_preview_source, "dark preview"),
        (fragment_source, "fragment"),
        (measurements_path, "measurements"),
    ):
        if not path.is_file():
            print(f"ERROR: missing {label}: {path}", file=sys.stderr)
            return 1

    try:
        measurements = load_object(measurements_path, "measurements")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    qa_dir = post_dir / "artifacts" / "qa-v2"
    reviewed_dir = qa_dir / "final-rendered"
    dark_reviewed_dir = qa_dir / "final-dark-rendered"
    slug = post_dir.name
    article_path = post_dir / "article.md"
    manifest_path = post_dir / "media.json"
    source_pass_path = qa_dir / "source-pass.json"
    for path, label in (
        (article_path, "article.md"),
        (manifest_path, "media.json"),
        (source_pass_path, "source pass"),
    ):
        if not path.is_file():
            print(f"ERROR: missing {label}: {path}", file=sys.stderr)
            return 1

    try:
        from md2tistory import split_frontmatter

        meta, _ = split_frontmatter(article_path.read_text(encoding="utf-8"))
        slug = meta.get("slug") or slug
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read article.md: {exc}", file=sys.stderr)
        return 1
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        print("ERROR: article.md must contain a valid kebab-case slug", file=sys.stderr)
        return 1
    if meta.get("status") != "reviewing":
        print(
            "ERROR: record rich-post QA while article status is `reviewing`",
            file=sys.stderr,
        )
        return 1

    preview_target = reviewed_dir / f"{slug}-rich-preview.html"
    fragment_target = reviewed_dir / f"{slug}-tistory-fragment.html"
    dark_preview_target = dark_reviewed_dir / f"{slug}-rich-preview.html"
    if preview_source != preview_target.resolve():
        print(
            "ERROR: render and review the preview at its canonical path: "
            f"{preview_target}",
            file=sys.stderr,
        )
        return 1
    if fragment_source != fragment_target.resolve():
        print(
            "ERROR: render and review the fragment at its canonical path: "
            f"{fragment_target}",
            file=sys.stderr,
        )
        return 1
    if dark_preview_source != dark_preview_target.resolve():
        print(
            "ERROR: render and review the dark preview at its canonical path: "
            f"{dark_preview_target}",
            file=sys.stderr,
        )
        return 1
    try:
        preview_markup = preview_target.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read reviewed HTML: {exc}", file=sys.stderr)
        return 1

    capture_errors: list[str] = []
    capture_receipt_path, capture_receipt = (
        validate_browser_capture_receipt(
            post_dir,
            preview_target,
            "final-light",
            capture_errors,
        )
    )
    dark_capture_receipt_path, dark_capture_receipt = (
        validate_browser_capture_receipt(
            post_dir,
            dark_preview_target,
            "final-dark",
            capture_errors,
        )
    )
    captured_viewports = merge_browser_capture_viewports(
        capture_receipt,
        measurements.get("viewports"),
        capture_errors,
    )
    dark_captured_viewports = merge_browser_capture_viewports(
        dark_capture_receipt,
        measurements.get("dark_viewports"),
        capture_errors,
    )
    if capture_errors:
        for error in capture_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if capture_receipt.get("checked_by") != dark_capture_receipt.get("checked_by"):
        print("ERROR: one reviewer must inspect both final themes", file=sys.stderr)
        return 1

    try:
        capture_checked_at = str(capture_receipt["checked_at"])[:10]
        record = {
            "version": 2,
            "checked_at": capture_checked_at,
            "checked_by": capture_receipt["checked_by"],
            "browser": capture_receipt["browser_version"],
            "session": capture_receipt["session"],
            "capture_receipt_path": capture_receipt_path.relative_to(
                post_dir
            ).as_posix(),
            "capture_receipt_sha256": sha256_file(capture_receipt_path),
            "capture_tool_sha256": capture_receipt["tool_sha256"],
            "dark_capture_receipt_path": dark_capture_receipt_path.relative_to(
                post_dir
            ).as_posix(),
            "dark_capture_receipt_sha256": sha256_file(
                dark_capture_receipt_path
            ),
            "source_pass_sha256": sha256_file(source_pass_path),
            "article_content_sha256": article_content_sha256(article_path),
            "media_sha256": sha256_file(manifest_path),
            "renderer_sha256": sha256_file(
                SKILL_DIR / "scripts" / "render_rich_post_v2.py"
            ),
            "css_sha256": sha256_file(SKILL_DIR / "assets" / "rich-post-v2.css"),
            "markdown_renderer_sha256": sha256_file(
                REPO_ROOT / "scripts" / "md2tistory.py"
            ),
            "remote_media_sha256": sha256_file(
                qa_dir / "remote-media.json"
            ),
            "preview_media_source": "remote",
            "preview_path": preview_target.relative_to(post_dir).as_posix(),
            "preview_sha256": sha256_file(preview_target),
            "preview_structure_sha256": preview_structure_sha256(preview_markup),
            "dark_preview_path": dark_preview_target.relative_to(
                post_dir
            ).as_posix(),
            "dark_preview_sha256": sha256_file(dark_preview_target),
            "fragment_path": fragment_target.relative_to(post_dir).as_posix(),
            "fragment_sha256": sha256_file(fragment_target),
            "viewports": bind_screenshot_evidence(
                post_dir,
                captured_viewports,
                "artifacts/qa-v2/final/light",
            ),
            "dark_viewports": bind_screenshot_evidence(
                post_dir,
                dark_captured_viewports,
                "artifacts/qa-v2/final/dark",
            ),
            "fragment": measurements.get("fragment"),
            "dark_theme": measurements.get("dark_theme"),
        }
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot bind QA evidence: {exc}", file=sys.stderr)
        return 1

    result = validate_bundle(
        post_dir,
        require_publish_urls=True,
        qa_record_override=record,
    )
    if not result["errors"]:
        try:
            current_preview, current_fragment = render_outputs(
                result,
                reviewed_dir,
                preview_media_source="remote",
            )
            current_dark_preview, _ = render_outputs(
                result,
                dark_reviewed_dir,
                preview_media_source="remote",
                preview_theme="dark",
            )
        except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
            result["errors"].append(f"cannot reproduce reviewed HTML: {exc}")
        else:
            if text_sha256(current_preview) != record["preview_sha256"]:
                result["errors"].append(
                    "reviewed preview differs from the current renderer output"
                )
            if text_sha256(current_fragment) != record["fragment_sha256"]:
                result["errors"].append(
                    "reviewed fragment differs from the current renderer output"
                )
            if text_sha256(current_dark_preview) != record["dark_preview_sha256"]:
                result["errors"].append(
                    "reviewed dark preview differs from the current renderer output"
                )
    if result["errors"]:
        for error in result["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    qa_path = qa_dir / "final-page.json"
    try:
        atomic_write_json(qa_path, record)
    except (OSError, TypeError, ValueError) as exc:
        print(f"ERROR: cannot save rich-post v2 final-page record: {exc}", file=sys.stderr)
        return 1
    print(f"final page: {qa_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
