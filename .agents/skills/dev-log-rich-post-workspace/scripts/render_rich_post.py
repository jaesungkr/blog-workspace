#!/usr/bin/env python3
"""Render a rich-post bundle into a local preview and Tistory HTML fragment."""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from rich_post_common import (
    REPO_ROOT,
    SKILL_DIR,
    iter_fence_lines,
    text_sha256,
    validate_bundle,
)

if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

from md2tistory import convert, inline  # noqa: E402


MAJOR_HEADING_RE = re.compile(r"^###\s+(.+?)\s*$")
MEDIA_LINE_RE = re.compile(
    r"^\s*\{\{media:([a-z0-9]+(?:-[a-z0-9]+)*)\}\}\s*$"
)
TABLE_RE = re.compile(r"(<table\b.*?</table>)", re.DOTALL)
STYLE_STRIP_RE = re.compile(
    r'<(p|h3|h4|ul|ol|li|blockquote|table|th|td)\s+style="[^"]*"'
)


def plain_text(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def heading_id(title: str, used: set[str], index: int) -> str:
    normalized = unicodedata.normalize("NFKC", plain_text(title)).lower()
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"[^\w가-힣-]", "", normalized).replace("_", "-")
    normalized = re.sub(r"-+", "-", normalized).strip("-")
    base = normalized or f"section-{index}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def split_sections(body: str) -> tuple[list[str], list[dict[str, Any]]]:
    intro: list[str] = []
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line, outside in iter_fence_lines(body.splitlines()):
        match = MAJOR_HEADING_RE.match(line) if outside else None
        if match:
            current = {"title": match.group(1), "lines": []}
            sections.append(current)
        elif current is None:
            intro.append(line)
        else:
            current["lines"].append(line)
    return intro, sections


def clean_converted(markup: str) -> str:
    markup = STYLE_STRIP_RE.sub(r"<\1", markup)
    return TABLE_RE.sub(r'<div class="rich-table-wrap">\1</div>', markup)


def media_src(
    item: dict[str, Any],
    mode: str,
    post_dir: Path,
    output_dir: Path,
) -> str:
    if mode in {"fragment", "remote-preview"}:
        placeholder = item["id"].upper().replace("-", "_")
        return item.get("tistory_url") or f"__TISTORY_MEDIA_{placeholder}__"
    asset = (post_dir / item["publish_path"]).resolve()
    return Path(os.path.relpath(asset, output_dir.resolve())).as_posix()


def origin_label(item: dict[str, Any]) -> str:
    labels = {
        "first_party": "직접 캡처",
        "official": "공식 자료",
        "user_supplied": "사용자 제공",
        "simulated": "에뮬레이터 확인",
        "generated": "생성 이미지",
    }
    origin = item.get("origin")
    label = labels.get(origin, "출처 기록")
    if origin == "first_party":
        label = f"{item['actor']} 캡처"
        if item.get("captured_at"):
            label += f" · {item['captured_at']}"
    elif origin == "simulated":
        label = f"{item['actor']} 시뮬레이션 캡처"
        if item.get("captured_at"):
            label += f" · {item['captured_at']}"
    return label


def figure_markup(
    item: dict[str, Any],
    items_by_id: dict[str, dict[str, Any]],
    lead_id: str,
    mode: str,
    post_dir: Path,
    output_dir: Path,
) -> str:
    item_id = html.escape(item["id"], quote=True)
    alt = html.escape(item["alt"], quote=True)
    caption = html.escape(item["caption"])
    width = int(item["width"])
    height = int(item["height"])
    display_width = int(item.get("display_width", min(width, 916)))
    loading = "eager" if item["id"] == lead_id else "lazy"
    src = html.escape(
        media_src(item, mode, post_dir, output_dir), quote=True
    )
    classes = "devlog-rich__image"
    if item.get("kind") == "gif":
        classes += " devlog-rich__motion"
    image = (
        f'<img class="{classes}" src="{src}" alt="{alt}" '
        f'width="{width}" height="{height}" loading="{loading}" '
        'decoding="async">'
    )
    if item.get("kind") == "gif":
        poster = items_by_id[item["poster_id"]]
        poster_src = html.escape(
            media_src(poster, mode, post_dir, output_dir), quote=True
        )
        poster_alt = html.escape(poster["alt"], quote=True)
        image += (
            f'<img class="devlog-rich__image devlog-rich__poster" '
            f'src="{poster_src}" alt="{poster_alt}" '
            f'width="{int(poster["width"])}" height="{int(poster["height"])}" '
            'loading="lazy" decoding="async">'
        )

    credit = html.escape(origin_label(item))
    source_url = item.get("source_url")
    if source_url:
        safe_url = html.escape(source_url, quote=True)
        credit_markup = (
            f'<a href="{safe_url}" target="_blank" rel="noopener noreferrer">'
            f"{credit}</a>"
        )
    else:
        credit_markup = credit

    return (
        f'<figure class="devlog-rich__figure" data-media-id="{item_id}" '
        f'style="--rich-media-width:{display_width}px">'
        f"{image}"
        f'<figcaption class="devlog-rich__caption">{caption} '
        f'<span class="devlog-rich__credit">· {credit_markup}</span>'
        "</figcaption></figure>"
    )


def render_lines(
    lines: list[str],
    items_by_id: dict[str, dict[str, Any]],
    lead_id: str,
    mode: str,
    post_dir: Path,
    output_dir: Path,
) -> str:
    chunks: list[str] = []
    text_buffer: list[str] = []

    def flush() -> None:
        if text_buffer:
            markup = convert("\n".join(text_buffer))
            if markup.strip():
                chunks.append(clean_converted(markup))
            text_buffer.clear()

    for line, outside in iter_fence_lines(lines):
        match = MEDIA_LINE_RE.match(line) if outside else None
        if match:
            flush()
            chunks.append(
                figure_markup(
                    items_by_id[match.group(1)],
                    items_by_id,
                    lead_id,
                    mode,
                    post_dir,
                    output_dir,
                )
            )
        else:
            text_buffer.append(line)
    flush()
    return "\n".join(chunks)


def build_article(
    result: dict[str, Any],
    mode: str,
    output_dir: Path,
    css: str,
) -> str:
    body = result["body"]
    use_alternate_sections = (
        result["meta"].get("section_backgrounds", "alternate")
        != "plain"
    )
    intro_lines, sections = split_sections(body)
    items_by_id = result["items_by_id"]
    lead_id = result["manifest"]["lead_id"]
    used_ids: set[str] = set()
    for index, section in enumerate(sections, start=1):
        section["id"] = heading_id(section["title"], used_ids, index)

    parts = [f"<style>\n{css}\n</style>", '<article class="devlog-rich">']
    parts.append('<section class="devlog-rich__section is-intro">')
    parts.append(
        render_lines(
            intro_lines,
            items_by_id,
            lead_id,
            mode,
            result["post_dir"],
            output_dir,
        )
    )
    parts.append("</section>")

    if len(sections) >= 2:
        parts.append('<section class="devlog-rich__section is-toc">')
        parts.append(
            '<nav class="devlog-rich__toc" aria-label="글 목차">'
            '<p class="devlog-rich__toc-title">목차</p><ol>'
        )
        for section in sections:
            title = html.escape(plain_text(section["title"]))
            parts.append(f'<li><a href="#{section["id"]}">{title}</a></li>')
        parts.append("</ol></nav></section>")

    for index, section in enumerate(sections):
        alt_class = (
            " is-alt" if use_alternate_sections and index % 2 else ""
        )
        parts.append(
            f'<section class="devlog-rich__section{alt_class}" '
            f'aria-labelledby="{section["id"]}">'
        )
        parts.append(
            f'<h2 id="{section["id"]}">{inline(section["title"])}</h2>'
        )
        parts.append(
            render_lines(
                section["lines"],
                items_by_id,
                lead_id,
                mode,
                result["post_dir"],
                output_dir,
            )
        )
        parts.append("</section>")
    parts.append("</article>")
    return "\n".join(parts)


def preview_document(fragment: str, meta: dict[str, Any]) -> str:
    title = html.escape(meta.get("title", "dev.log rich post"))
    category = html.escape(meta.get("category", "dev.log"))
    summary = html.escape(meta.get("summary", ""))
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{summary}">
  <style>
    html {{ scrollbar-width:none; }}
    html::-webkit-scrollbar {{ display:none; }}
    body {{ margin:0; background:#ffffff; color:#1d1d1f; }}
    .rich-preview-header {{ width:min(calc(100% - 40px), 1040px); margin:0 auto;
      padding:56px 0 44px; font-family:"Noto Sans KR","Apple SD Gothic Neo",
      system-ui,sans-serif; }}
    .rich-preview-header p {{ margin:0 0 10px; color:#0066cc; font-size:15px;
      font-weight:700; }}
    .rich-preview-header h1 {{ margin:0; font-size:42px; line-height:1.2;
      letter-spacing:-0.025em; word-break:keep-all; }}
    @media (max-width:735px) {{
      .rich-preview-header {{ padding:36px 0 30px; }}
      .rich-preview-header h1 {{ font-size:32px; }}
    }}
  </style>
</head>
<body>
  <header class="rich-preview-header">
    <p>{category}</p>
    <h1>{title}</h1>
  </header>
  {fragment}
</body>
</html>
"""


def render_outputs(
    result: dict[str, Any],
    output_dir: Path,
    preview_media_source: str = "local",
) -> tuple[str, str]:
    css = (SKILL_DIR / "assets" / "rich-post.css").read_text(encoding="utf-8")
    preview_mode = (
        "remote-preview" if preview_media_source == "remote" else "preview"
    )
    preview_fragment = build_article(result, preview_mode, output_dir, css)
    tistory_fragment = build_article(result, "fragment", output_dir, css)
    return (
        preview_document(preview_fragment, result["meta"]),
        tistory_fragment + "\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a dev.log rich-post preview and Tistory fragment."
    )
    parser.add_argument("post_dir", help="Path to posts/YYYY-MM-DD-slug")
    parser.add_argument(
        "--output-dir",
        default=str(REPO_ROOT / "dist"),
        help="Output directory; defaults to repository dist/.",
    )
    parser.add_argument(
        "--require-publish-urls",
        action="store_true",
        help="Fail unless every media item has a final HTTPS Tistory URL.",
    )
    parser.add_argument(
        "--preview-media-source",
        choices=("local", "remote"),
        default="local",
        help="Use local bundle assets or final CDN URLs in the full preview.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    if args.require_publish_urls and args.preview_media_source != "remote":
        print(
            "ERROR: strict rendering requires --preview-media-source remote",
            file=sys.stderr,
        )
        return 1
    result = validate_bundle(
        Path(args.post_dir), require_publish_urls=args.require_publish_urls
    )
    for warning in result["warnings"]:
        print(f"WARNING: {warning}", file=sys.stderr)
    if result["errors"]:
        for error in result["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    slug = result["meta"].get("slug") or result["post_dir"].name
    preview_path = output_dir / f"{slug}-rich-preview.html"
    fragment_path = output_dir / f"{slug}-tistory-fragment.html"
    preview_markup, fragment_markup = render_outputs(
        result,
        output_dir,
        preview_media_source=args.preview_media_source,
    )
    if result["require_publish_urls"]:
        qa_record = result["qa_record"]
        if qa_record.get("preview_sha256") != text_sha256(preview_markup):
            print(
                "ERROR: rendered preview differs from the exact reviewed preview",
                file=sys.stderr,
            )
            return 1
        if qa_record.get("fragment_sha256") != text_sha256(fragment_markup):
            print(
                "ERROR: rendered Tistory fragment differs from the "
                "independently reviewed fragment",
                file=sys.stderr,
            )
            return 1

    preview_path.write_text(preview_markup, encoding="utf-8")
    fragment_path.write_text(fragment_markup, encoding="utf-8")
    print(f"preview: {preview_path}")
    print(f"fragment: {fragment_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
