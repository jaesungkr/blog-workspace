#!/usr/bin/env python3
"""Record an independent, hash-bound final-page validation for a rich post."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from render_rich_post import render_outputs
from rich_post_common import (
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
    validate_independent_data,
)


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
        description="Record the independent rich-post final-page gate."
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--preview",
        required=True,
        help="Independently rendered and reviewed full preview HTML",
    )
    parser.add_argument(
        "--fragment",
        required=True,
        help="Independently rendered and reviewed Tistory fragment",
    )
    parser.add_argument(
        "--measurements",
        required=True,
        help="Independent browser measurements and visual checks JSON",
    )
    args = parser.parse_args()

    post_dir = Path(args.post_dir).resolve()
    preview_source = Path(args.preview).resolve()
    fragment_source = Path(args.fragment).resolve()
    measurements_path = Path(args.measurements).resolve()
    for path, label in (
        (preview_source, "preview"),
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

    result = validate_bundle(
        post_dir,
        require_publish_urls=True,
        require_remote_verification=True,
    )
    if result["errors"]:
        for error in result["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if result["meta"].get("status") != "reviewing":
        print(
            "ERROR: record independent validation while status is `reviewing`",
            file=sys.stderr,
        )
        return 1

    slug = result["meta"].get("slug") or post_dir.name
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        print("ERROR: article.md must contain a valid kebab-case slug", file=sys.stderr)
        return 1

    qa_dir = post_dir / "artifacts" / "qa"
    reviewed_dir = qa_dir / "independent-rendered"
    preview_target = reviewed_dir / f"{slug}-rich-preview.html"
    fragment_target = reviewed_dir / f"{slug}-tistory-fragment.html"
    if preview_source != preview_target.resolve():
        print(
            "ERROR: independently render and review the preview at: "
            f"{preview_target}",
            file=sys.stderr,
        )
        return 1
    if fragment_source != fragment_target.resolve():
        print(
            "ERROR: independently render and review the fragment at: "
            f"{fragment_target}",
            file=sys.stderr,
        )
        return 1

    capture_errors: list[str] = []
    capture_receipt_path, capture_receipt = (
        validate_browser_capture_receipt(
            post_dir,
            preview_target,
            "independent",
            capture_errors,
        )
    )
    captured_viewports = merge_browser_capture_viewports(
        capture_receipt,
        measurements.get("viewports"),
        capture_errors,
    )
    if capture_errors:
        for error in capture_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    article_path = result["article_path"]
    manifest_path = result["manifest_path"]
    creator_qa_path = result["qa_path"]
    try:
        preview_markup = preview_target.read_text(encoding="utf-8")
        record = {
            "version": 1,
            "result": measurements.get("result"),
            "checked_at": str(capture_receipt["checked_at"])[:10],
            "checked_by": capture_receipt["checked_by"],
            "browser": capture_receipt["browser_version"],
            "session": capture_receipt["session"],
            "capture_receipt_path": capture_receipt_path.relative_to(
                post_dir
            ).as_posix(),
            "capture_receipt_sha256": sha256_file(capture_receipt_path),
            "capture_tool_sha256": capture_receipt["tool_sha256"],
            "creator_qa_sha256": sha256_file(creator_qa_path),
            "article_content_sha256": article_content_sha256(article_path),
            "media_sha256": sha256_file(manifest_path),
            "renderer_sha256": sha256_file(
                SKILL_DIR / "scripts" / "render_rich_post.py"
            ),
            "css_sha256": sha256_file(SKILL_DIR / "assets" / "rich-post.css"),
            "markdown_renderer_sha256": sha256_file(
                REPO_ROOT / "scripts" / "md2tistory.py"
            ),
            "remote_media_sha256": sha256_file(
                qa_dir / "remote-media.json"
            ),
            "remote_verification_sha256": sha256_file(
                qa_dir / "remote-media-verification.json"
            ),
            "preview_media_source": "remote",
            "preview_path": preview_target.relative_to(post_dir).as_posix(),
            "preview_sha256": sha256_file(preview_target),
            "preview_structure_sha256": preview_structure_sha256(
                preview_markup
            ),
            "fragment_path": fragment_target.relative_to(post_dir).as_posix(),
            "fragment_sha256": sha256_file(fragment_target),
            "viewports": bind_screenshot_evidence(
                post_dir,
                captured_viewports,
                screenshot_root="artifacts/qa/independent",
            ),
            "fragment": measurements.get("fragment"),
            "checks": measurements.get("checks"),
        }
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot bind independent evidence: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    validate_independent_data(
        post_dir,
        article_path,
        manifest_path,
        result["manifest"],
        result["qa_record"],
        record,
        errors,
    )
    if not errors:
        try:
            current_preview, current_fragment = render_outputs(
                result,
                reviewed_dir,
                preview_media_source="remote",
            )
        except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
            errors.append(f"cannot reproduce independent HTML: {exc}")
        else:
            if text_sha256(current_preview) != record["preview_sha256"]:
                errors.append(
                    "independent preview differs from current renderer output"
                )
            if text_sha256(current_fragment) != record["fragment_sha256"]:
                errors.append(
                    "independent fragment differs from current renderer output"
                )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    review_path = qa_dir / "independent-final-page.json"
    try:
        atomic_write_json(review_path, record)
    except (OSError, TypeError, ValueError) as exc:
        print(
            f"ERROR: cannot save independent final-page review: {exc}",
            file=sys.stderr,
        )
        return 1

    print(f"independent review: {review_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
