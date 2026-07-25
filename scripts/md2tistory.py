#!/usr/bin/env python3
"""
마크다운 초안을 티스토리 HTML 에디터에 붙여넣을 HTML로 변환한다.

사용법:
    python3 scripts/md2tistory.py posts/2026-07-25-foo/article.md
    python3 scripts/md2tistory.py posts/2026-07-25-foo/article.md -o dist/foo.html
    python3 scripts/md2tistory.py posts/2026-07-25-foo/article.md --stdout

티스토리는 스킨마다 CSS가 달라서 클래스를 쓸 수 없다. 모든 스타일을 인라인으로 넣는다.
외부 의존성 없이 표준 라이브러리만 사용한다.
"""

import argparse
import html
import os
import re
import sys

# --- 인라인 스타일 정의 ---------------------------------------------------
# 티스토리 기본 스킨에서 튀지 않으면서 가독성이 확보되는 값으로 맞췄다.

S = {
    "h2": (
        "font-size:1.35em;font-weight:700;margin:2.4em 0 0.8em;"
        "padding-bottom:0.35em;border-bottom:1px solid #e5e5e5;word-break:keep-all;"
    ),
    "h3": "font-size:1.15em;font-weight:700;margin:1.9em 0 0.6em;word-break:keep-all;",
    "h4": "font-size:1.02em;font-weight:700;margin:1.5em 0 0.5em;word-break:keep-all;",
    "p": "margin:0 0 1.15em;line-height:1.9;word-break:keep-all;",
    "table": (
        "border-collapse:collapse;width:100%;margin:1.6em 0;"
        "font-size:0.95em;line-height:1.7;"
    ),
    "th": (
        "border:1px solid #ddd;padding:10px 12px;background:#f7f7f7;"
        "font-weight:700;word-break:keep-all;"
    ),
    "td": "border:1px solid #ddd;padding:10px 12px;word-break:keep-all;",
    "blockquote": (
        "margin:1.6em 0;padding:0.9em 1.2em;border-left:3px solid #ccc;"
        "background:#fafafa;color:#444;line-height:1.85;word-break:keep-all;"
    ),
    "pre": (
        "background:#f6f6f6;border:1px solid #e5e5e5;border-radius:4px;"
        "padding:14px 16px;overflow-x:auto;font-size:0.9em;line-height:1.6;"
        "margin:1.4em 0;"
    ),
    "pre_code": "font-family:Menlo,Consolas,monospace;white-space:pre;",
    "code": (
        "background:#f0f0f0;border-radius:3px;padding:2px 5px;"
        "font-family:Menlo,Consolas,monospace;font-size:0.92em;"
    ),
    "list": "margin:0 0 1.25em;padding-left:1.6em;line-height:1.9;",
    "li": "margin-bottom:0.4em;word-break:keep-all;",
    "hr": "border:0;border-top:1px solid #e5e5e5;margin:2.6em 0;",
    "a": "color:#1a73e8;text-decoration:none;",
    "img": "max-width:100%;height:auto;",
}


# --- 프론트매터 ------------------------------------------------------------

def split_frontmatter(text):
    """YAML 프론트매터와 본문을 분리한다. 필요한 키만 얕게 파싱한다."""
    if not text.startswith("---"):
        return {}, text

    end = re.search(r"^---\s*$", text[3:], re.MULTILINE)
    if not end:
        return {}, text

    raw = text[3:3 + end.start()]
    body = text[3 + end.end():].lstrip("\n")

    meta = {}
    current_list = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        # 블록 형태 리스트 항목 ("    - 값")
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and current_list is not None:
            meta[current_list].append(item.group(1).strip().strip("'\""))
            continue

        kv = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not kv:
            continue

        key, value = kv.group(1), kv.group(2).strip()
        if value == "":
            # 뒤따르는 들여쓴 항목들이 이 키의 리스트다
            meta[key] = []
            current_list = key
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            meta[key] = [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
            current_list = None
        else:
            meta[key] = value.strip("'\"")
            current_list = None

    return meta, body


# --- 인라인 변환 -----------------------------------------------------------

def inline(text):
    """한 줄 안의 마크다운 인라인 문법을 HTML로 바꾼다."""
    text = html.escape(text, quote=False)

    # 인라인 코드는 다른 규칙이 건드리지 못하게 먼저 빼둔다
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return "\x00%d\x00" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)

    # 이미지가 링크보다 먼저 (문법이 겹친다)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)",
        lambda m: '<img src="%s" alt="%s" style="%s">' % (m.group(2), m.group(1), S["img"]),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)",
        lambda m: '<a href="%s" style="%s" target="_blank">%s</a>' % (m.group(2), S["a"], m.group(1)),
        text,
    )

    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"~~(.+?)~~", r"<s>\1</s>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w_])_([^_\n]+?)_(?![\w_])", r"<em>\1</em>", text)

    # 빼뒀던 인라인 코드를 되돌린다
    text = re.sub(
        r"\x00(\d+)\x00",
        lambda m: '<code style="%s">%s</code>' % (S["code"], spans[int(m.group(1))]),
        text,
    )
    return text


# --- 블록 판별 -------------------------------------------------------------

def is_table_separator(line):
    """|---|:---:|---| 형태의 표 구분선인지 판별한다."""
    s = line.strip()
    if "|" not in s or "-" not in s:
        return False
    return re.fullmatch(r"[\s|:-]+", s) is not None


def split_row(line):
    """표 한 줄을 셀 목록으로 나눈다. 양끝 파이프는 버린다."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


UL_RE = re.compile(r"^(\s*)[-*+]\s+(.*)$")
OL_RE = re.compile(r"^(\s*)\d+[.)]\s+(.*)$")


# --- 블록 파서 -------------------------------------------------------------

def render_list(items):
    """(들여쓰기, 순서여부, 내용) 항목들을 중첩 <ul>/<ol>로 만든다."""
    out = []

    def build(pos, indent):
        ordered = items[pos][1]
        tag = "ol" if ordered else "ul"
        buf = ['<%s style="%s">' % (tag, S["list"])]
        i = pos
        while i < len(items):
            item_indent, item_ordered, content = items[i]
            if item_indent < indent:
                break
            if item_indent > indent:
                # 더 깊은 항목은 직전 <li> 안에 붙인다
                nested, i = build(i, item_indent)
                if buf and buf[-1].endswith("</li>"):
                    buf[-1] = buf[-1][: -len("</li>")] + nested + "</li>"
                else:
                    buf.append(nested)
                continue
            if item_ordered != ordered:
                break
            buf.append('<li style="%s">%s</li>' % (S["li"], inline(content)))
            i += 1
        buf.append("</%s>" % tag)
        return "".join(buf), i

    i = 0
    while i < len(items):
        chunk, i = build(i, items[i][0])
        out.append(chunk)
    return "\n".join(out)


def convert(body):
    """본문 마크다운을 블록 단위로 훑어 HTML 조각 목록을 만든다."""
    lines = body.split("\n")
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # 빈 줄
        if not line.strip():
            i += 1
            continue

        # 코드 펜스
        fence = re.match(r"^\s*(```+|~~~+)\s*([\w+-]*)\s*$", line)
        if fence:
            marker = fence.group(1)[0] * 3
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith(marker):
                buf.append(lines[i])
                i += 1
            i += 1  # 닫는 펜스 소비
            code = html.escape("\n".join(buf), quote=False)
            out.append(
                '<pre style="%s"><code style="%s">%s</code></pre>'
                % (S["pre"], S["pre_code"], code)
            )
            continue

        # 수평선 (프론트매터 구분선과 헷갈리지 않게 --- 3개 이상만)
        if re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", line):
            out.append('<hr style="%s">' % S["hr"])
            i += 1
            continue

        # 제목
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            # H1은 티스토리 제목과 중복되므로 H2로 낮춘다.
            # 현행 원고는 섹션에 H3(###)를 사용하므로 그대로 H3가 된다.
            tag = "h%d" % min(max(level, 2), 4)
            out.append('<%s style="%s">%s</%s>' % (tag, S[tag], inline(heading.group(2)), tag))
            i += 1
            continue

        # 표 (헤더 줄 + 구분선)
        if "|" in line and i + 1 < n and is_table_separator(lines[i + 1]):
            header = split_row(line)
            aligns = []
            for cell in split_row(lines[i + 1]):
                left, right = cell.startswith(":"), cell.endswith(":")
                aligns.append("center" if left and right else "right" if right else "left")
            i += 2

            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1

            buf = ['<table style="%s">' % S["table"], "<thead><tr>"]
            for idx, cell in enumerate(header):
                align = aligns[idx] if idx < len(aligns) else "left"
                buf.append('<th style="%stext-align:%s;">%s</th>' % (S["th"], align, inline(cell)))
            buf.append("</tr></thead><tbody>")
            for row in rows:
                buf.append("<tr>")
                for idx in range(len(header)):
                    cell = row[idx] if idx < len(row) else ""
                    align = aligns[idx] if idx < len(aligns) else "left"
                    buf.append('<td style="%stext-align:%s;">%s</td>' % (S["td"], align, inline(cell)))
                buf.append("</tr>")
            buf.append("</tbody></table>")
            out.append("".join(buf))
            continue

        # 인용
        if re.match(r"^\s*>", line):
            buf = []
            while i < n and re.match(r"^\s*>", lines[i]):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = "<br>".join(inline(b) if b.strip() else "" for b in buf)
            out.append('<blockquote style="%s">%s</blockquote>' % (S["blockquote"], inner))
            continue

        # 목록
        if UL_RE.match(line) or OL_RE.match(line):
            items = []
            while i < n:
                m_ul, m_ol = UL_RE.match(lines[i]), OL_RE.match(lines[i])
                if m_ul:
                    items.append((len(m_ul.group(1)), False, m_ul.group(2)))
                    i += 1
                elif m_ol:
                    items.append((len(m_ol.group(1)), True, m_ol.group(2)))
                    i += 1
                elif lines[i].strip() and indent_of(lines[i]) >= 2 and items:
                    # 항목의 이어지는 줄
                    ind, ordered, content = items[-1]
                    items[-1] = (ind, ordered, content + " " + lines[i].strip())
                    i += 1
                else:
                    break
            out.append(render_list(items))
            continue

        # 문단 — 빈 줄이나 다른 블록이 나올 때까지 모은다
        buf = []
        while i < n and lines[i].strip():
            if re.match(r"^(#{1,6})\s|^\s*>|^\s*(```|~~~)", lines[i]):
                break
            if UL_RE.match(lines[i]) or OL_RE.match(lines[i]):
                break
            if re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", lines[i]):
                break
            if "|" in lines[i] and i + 1 < n and is_table_separator(lines[i + 1]):
                break
            buf.append(lines[i].strip())
            i += 1
        if buf:
            out.append('<p style="%s">%s</p>' % (S["p"], "<br>".join(inline(b) for b in buf)))

    return "\n".join(out)


# --- 유틸 ------------------------------------------------------------------

def text_length(markup):
    """공백 포함 글자 수. 태그를 걷어내고 센다."""
    plain = re.sub(r"<[^>]+>", "", markup)
    return len(html.unescape(plain).replace("\n", ""))


def main():
    parser = argparse.ArgumentParser(description="마크다운 → 티스토리 HTML 변환")
    parser.add_argument("source", help="변환할 .md 파일")
    parser.add_argument("-o", "--output", help="출력 경로 (기본: dist/<파일명>.html)")
    parser.add_argument("--stdout", action="store_true", help="파일 대신 표준출력으로")
    args = parser.parse_args()

    if not os.path.isfile(args.source):
        print("파일을 찾을 수 없습니다: %s" % args.source, file=sys.stderr)
        return 1

    with open(args.source, encoding="utf-8") as f:
        raw = f.read()

    meta, body = split_frontmatter(raw)

    # HTML 주석(TODO 표시 등)은 발행물에 나가면 안 되므로 제거하고 개수를 알린다
    comments = re.findall(r"<!--.*?-->", body, re.DOTALL)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)

    markup = convert(body)

    if args.stdout:
        print(markup)
    else:
        base = os.path.splitext(os.path.basename(args.source))[0]
        out_path = args.output or os.path.join("dist", base + ".html")
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markup + "\n")
        print("생성: %s" % out_path)

    # 발행에 필요한 메타 정보를 표준에러로 안내한다 (파이프 사용 시 방해되지 않게)
    tags = meta.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    print("", file=sys.stderr)
    print("제목      : %s" % meta.get("title", "(없음)"), file=sys.stderr)
    print("카테고리  : %s / %s" % (meta.get("category", "?"), meta.get("subcategory", "?")), file=sys.stderr)
    print("태그(%d개) : %s" % (len(tags), ", ".join(tags) if tags else "(없음)"), file=sys.stderr)
    print("글자 수   : {:,}자".format(text_length(markup)), file=sys.stderr)
    if comments:
        print("주석 %d개를 제거했습니다. TODO가 남아 있는지 원본을 확인하세요." % len(comments), file=sys.stderr)
    if not tags:
        print("경고: 태그가 없습니다.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
