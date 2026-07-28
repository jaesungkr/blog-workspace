#!/usr/bin/env python3
"""Inventory template-like signals in a Korean Markdown article.

The output is diagnostic only. No signal is an automatic quality failure.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


GENERIC_HEADING_PATTERNS = (
    re.compile(r"(정체|관계|구조|이유|결과|경계|기준|순서|진단|방어|용도|경우|것)$"),
    re.compile(r"(한눈에|총정리|완벽 가이드|바로 적용할|알아보기|이해하기|정리하기)"),
)

STOCK_PHRASE_PATTERNS = (
    ("이번 글에서는", re.compile(r"이번 글에서는")),
    ("차례로 살펴보겠습니다", re.compile(r"차례로 살펴보겠습니다")),
    ("살펴보겠습니다", re.compile(r"살펴보겠습니다")),
    ("알아보겠습니다", re.compile(r"알아보겠습니다")),
    ("정리해 보겠습니다", re.compile(r"정리해 보겠습니다")),
    ("핵심은", re.compile(r"핵심은")),
    ("중요한 점은", re.compile(r"중요한 점은")),
    ("결론적으로", re.compile(r"(?:^|[.!?]\s+)결론적으로")),
    ("요약하면", re.compile(r"(?:^|[.!?]\s+)요약하면")),
    ("정리하면", re.compile(r"(?:^|[.!?]\s+)정리하면")),
    ("이를 통해", re.compile(r"이를 통해")),
    ("단순히 A를 넘어 B", re.compile(r"단순히[^.!?\n]{0,50}넘어")),
)

ABSTRACT_NOUNS = (
    "구조",
    "범위",
    "경계",
    "기준",
    "결과",
    "구성",
    "경우",
    "지점",
    "의미",
    "관계",
    "차이",
    "설명",
    "과정",
    "방식",
)

CORRECTIVE_FRAMES = (
    "아니라",
    "아닙니다",
    "하지만",
    "다만",
    "그러나",
    "반면",
    "반대로",
    "그래도",
    "그렇다고",
    "다른 이야기",
)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return "", text
    return text[4:closing], text[closing + 5 :]


def advance_fence(
    stripped_line: str, state: tuple[str, int] | None
) -> tuple[tuple[str, int] | None, bool]:
    match = re.match(r"^(`{3,}|~{3,})(.*)$", stripped_line)
    if state is None:
        if not match:
            return None, False
        marker = match.group(1)
        return (marker[0], len(marker)), True

    if not match:
        return state, False
    marker = match.group(1)
    trailing = match.group(2).strip()
    if marker[0] == state[0] and len(marker) >= state[1] and not trailing:
        return None, True
    return state, False


def strip_markdown_for_prose(body: str) -> str:
    lines: list[str] = []
    fence_state: tuple[str, int] | None = None
    for line in body.splitlines():
        stripped = line.strip()
        fence_state, is_fence_line = advance_fence(stripped, fence_state)
        if is_fence_line:
            continue
        if fence_state is not None:
            continue
        if (
            not stripped
            or stripped.startswith("#")
            or stripped.startswith("|")
            or stripped.startswith(">")
            or re.match(r"^[-*+]\s+", stripped)
        ):
            lines.append("")
            continue
        cleaned = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", stripped)
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        cleaned = cleaned.replace("**", "").replace("__", "")
        lines.append(cleaned)
    return "\n".join(lines)


def sentence_list(prose: str) -> list[str]:
    compact = re.sub(r"[ \t]+", " ", prose)
    compact = re.sub(r"\n+", "\n", compact)
    sentences = re.split(r"(?<=[.!?])(?:\s+|\n+)", compact)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def ending_key(sentence: str) -> str:
    if re.search(r'\?["”’)\]}]*\s*$', sentence):
        return "question"
    clean = re.sub(r'["”’)\]}]+$', "", sentence.rstrip())
    clean = re.sub(r"[.!?]+$", "", clean)
    match = re.search(
        r"(했습니다|였습니다|있습니다|없습니다|됩니다|입니다|합니다|봅니다|보입니다|바랍니다)$",
        clean,
    )
    if match:
        return match.group(1)
    for suffix in ("습니다", "니다", "세요", "까요", "네요", "군요", "어요", "아요"):
        if clean.endswith(suffix):
            return f"-{suffix}"
    return "other"


def prose_paragraph_records(
    body: str, body_start_line: int
) -> list[dict[str, object]]:
    paragraphs: list[dict[str, object]] = []
    current_lines: list[tuple[int, str]] = []
    fence_state: tuple[str, int] | None = None

    def flush() -> None:
        if not current_lines:
            return
        text_parts: list[str] = []
        offsets: list[tuple[int, int]] = []
        cursor = 0
        for file_line, cleaned in current_lines:
            if text_parts:
                cursor += 1
            offsets.append((cursor, file_line))
            text_parts.append(cleaned)
            cursor += len(cleaned)
        paragraphs.append(
            {
                "line": current_lines[0][0],
                "text": " ".join(text_parts),
                "offsets": offsets,
            }
        )
        current_lines.clear()

    for body_line_number, line in enumerate(body.splitlines(), start=0):
        stripped = line.strip()
        fence_state, is_fence_line = advance_fence(stripped, fence_state)
        if is_fence_line:
            flush()
            continue
        if (
            fence_state is not None
            or not stripped
            or stripped.startswith("#")
            or stripped.startswith("|")
            or stripped.startswith(">")
            or re.match(r"^[-*+]\s+", stripped)
        ):
            flush()
            continue

        cleaned = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", stripped)
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        cleaned = cleaned.replace("**", "").replace("__", "")
        current_lines.append((body_start_line + body_line_number, cleaned))

    flush()
    return paragraphs


def sentence_records(
    paragraphs: list[dict[str, object]],
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for paragraph in paragraphs:
        paragraph_text = str(paragraph["text"])
        cursor = 0
        for sentence in sentence_list(paragraph_text):
            start = paragraph_text.find(sentence, cursor)
            if start == -1:
                start = cursor
            cursor = start + len(sentence)
            source_line = int(paragraph["line"])
            for offset, file_line in paragraph["offsets"]:
                if offset > start:
                    break
                source_line = file_line
            records.append(
                {
                    "line": source_line,
                    "chars_no_spaces": len(re.sub(r"\s+", "", sentence)),
                    "ending": ending_key(sentence),
                    "excerpt": sentence,
                }
            )
    return records


def line_signal_matches(body: str, body_start_line: int) -> list[dict[str, object]]:
    matches: list[dict[str, object]] = []
    fence_state: tuple[str, int] | None = None
    for body_line_number, line in enumerate(body.splitlines(), start=0):
        stripped = line.strip()
        fence_state, is_fence_line = advance_fence(stripped, fence_state)
        if is_fence_line:
            continue
        if (
            fence_state is not None
            or not stripped
            or stripped.startswith("#")
            or stripped.startswith("|")
            or stripped.startswith(">")
            or re.match(r"^[-*+]\s+", stripped)
        ):
            continue

        cleaned = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", stripped)
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        cleaned = cleaned.replace("**", "").replace("__", "")
        file_line = body_start_line + body_line_number

        for label, pattern in STOCK_PHRASE_PATTERNS:
            if pattern.search(cleaned):
                matches.append(
                    {
                        "line": file_line,
                        "kind": "stock_phrase",
                        "signal": label,
                        "excerpt": cleaned,
                    }
                )
        for frame in CORRECTIVE_FRAMES:
            if frame in cleaned:
                matches.append(
                    {
                        "line": file_line,
                        "kind": "corrective_frame",
                        "signal": frame,
                        "excerpt": cleaned,
                    }
                )
        for noun in ABSTRACT_NOUNS:
            if noun in cleaned:
                matches.append(
                    {
                        "line": file_line,
                        "kind": "abstract_noun",
                        "signal": noun,
                        "excerpt": cleaned,
                    }
                )
    return matches


def analyze(text: str) -> dict[str, object]:
    frontmatter, body = split_frontmatter(text)
    body_start_line = text[: text.find(body)].count("\n") + 1
    title_match = re.search(r'(?m)^title:\s*["\']?(.*?)["\']?\s*$', frontmatter)
    title = title_match.group(1).strip("\"'") if title_match else ""

    headings = []
    fence_state: tuple[str, int] | None = None
    for line_number, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        fence_state, is_fence_line = advance_fence(stripped, fence_state)
        if is_fence_line:
            continue
        if fence_state is not None:
            continue
        match = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        heading = match.group(2)
        signals = [
            pattern.pattern
            for pattern in GENERIC_HEADING_PATTERNS
            if pattern.search(heading)
        ]
        headings.append(
            {
                "line": body_start_line + line_number - 1,
                "level": len(match.group(1)),
                "text": heading,
                "generic_signals": signals,
            }
        )

    prose = strip_markdown_for_prose(body)
    paragraphs = prose_paragraph_records(body, body_start_line)
    sentence_details = sentence_records(paragraphs)
    sentences = [str(record["excerpt"]) for record in sentence_details]
    lengths = [int(record["chars_no_spaces"]) for record in sentence_details]
    hangul_count = len(re.findall(r"[가-힣]", prose))
    units = hangul_count / 1000 if hangul_count else 0

    phrase_counts = {
        label: len(pattern.findall(prose))
        for label, pattern in STOCK_PHRASE_PATTERNS
        if pattern.search(prose)
    }
    abstract_counts = {
        word: prose.count(word) for word in ABSTRACT_NOUNS if word in prose
    }
    corrective_counts = {
        word: prose.count(word) for word in CORRECTIVE_FRAMES if word in prose
    }
    endings = Counter(str(record["ending"]) for record in sentence_details)
    opener_details: list[dict[str, object]] = []
    opener_counts: Counter[str] = Counter()
    for paragraph in paragraphs:
        words = str(paragraph["text"]).strip().split()
        if not words:
            continue
        opener = " ".join(words[:2])
        if opener == "안녕하세요. dev.log입니다.":
            continue
        opener_counts[opener] += 1
        opener_details.append(
            {
                "line": paragraph["line"],
                "opener": opener,
                "excerpt": paragraph["text"],
            }
        )
    repeated_openers = {
        opener: count for opener, count in opener_counts.items() if count > 1
    }
    repeated_opener_matches = [
        item for item in opener_details if item["opener"] in repeated_openers
    ]
    ending_samples: dict[str, list[dict[str, object]]] = {}
    for record in sentence_details:
        ending = str(record["ending"])
        ending_samples.setdefault(ending, [])
        if len(ending_samples[ending]) < 2:
            ending_samples[ending].append(record)

    return {
        "title": title,
        "headings": headings,
        "summary": {
            "heading_count": len(headings),
            "headings_with_generic_signal": sum(
                bool(item["generic_signals"]) for item in headings
            ),
            "sentence_count": len(sentences),
            "average_sentence_chars_no_spaces": (
                round(sum(lengths) / len(lengths), 1) if lengths else 0
            ),
            "sentences_over_50_chars": sum(length > 50 for length in lengths),
            "sentences_over_70_chars": sum(length > 70 for length in lengths),
            "hangul_chars": hangul_count,
            "abstract_nouns_per_1000_hangul": (
                round(sum(abstract_counts.values()) / units, 1) if units else 0
            ),
            "corrective_frames_per_1000_hangul": (
                round(sum(corrective_counts.values()) / units, 1) if units else 0
            ),
        },
        "stock_phrases": phrase_counts,
        "abstract_nouns": abstract_counts,
        "corrective_frames": corrective_counts,
        "matched_lines": line_signal_matches(body, body_start_line),
        "long_sentences": [
            record for record in sentence_details if record["chars_no_spaces"] > 50
        ],
        "sentence_endings": dict(endings.most_common()),
        "sentence_ending_samples": ending_samples,
        "repeated_paragraph_openers": repeated_openers,
        "repeated_paragraph_opener_matches": repeated_opener_matches,
        "note": "Signals are review prompts, not pass/fail rules.",
    }


def render_text(report: dict[str, object]) -> str:
    summary = report["summary"]
    lines = [
        f"Title: {report['title']}",
        (
            "Summary: "
            f"{summary['heading_count']} headings, "
            f"{summary['headings_with_generic_signal']} generic-heading signals, "
            f"{summary['sentence_count']} prose sentences, "
            f"average {summary['average_sentence_chars_no_spaces']} chars"
        ),
        (
            "Density: "
            f"{summary['abstract_nouns_per_1000_hangul']} abstract nouns / 1,000 Hangul, "
            f"{summary['corrective_frames_per_1000_hangul']} corrective frames / 1,000 Hangul"
        ),
        (
            "Long sentences: "
            f"{summary['sentences_over_50_chars']} over 50 chars, "
            f"{summary['sentences_over_70_chars']} over 70 chars"
        ),
        "",
        "Headings:",
    ]
    for heading in report["headings"]:
        suffix = " [review]" if heading["generic_signals"] else ""
        lines.append(
            f"- L{heading['line']} H{heading['level']}: {heading['text']}{suffix}"
        )

    for label, key in (
        ("Stock phrases", "stock_phrases"),
        ("Abstract nouns", "abstract_nouns"),
        ("Corrective frames", "corrective_frames"),
        ("Sentence endings", "sentence_endings"),
        ("Repeated paragraph openers", "repeated_paragraph_openers"),
    ):
        values = report[key]
        lines.extend(("", f"{label}:"))
        if values:
            lines.extend(f"- {name}: {count}" for name, count in values.items())
        else:
            lines.append("- none")

    lines.extend(("", "Matched lines:"))
    if report["matched_lines"]:
        for match in report["matched_lines"]:
            lines.append(
                f"- L{match['line']} {match['kind']}:{match['signal']}: "
                f"{match['excerpt']}"
            )
    else:
        lines.append("- none")

    lines.extend(("", "Long sentences:"))
    if report["long_sentences"]:
        for sentence in report["long_sentences"]:
            lines.append(
                f"- L{sentence['line']} ({sentence['chars_no_spaces']} chars): "
                f"{sentence['excerpt']}"
            )
    else:
        lines.append("- none")

    lines.extend(("", "Sentence-ending samples:"))
    for ending, samples in report["sentence_ending_samples"].items():
        excerpts = " | ".join(
            f"L{sample['line']} {sample['excerpt']}" for sample in samples
        )
        lines.append(f"- {ending}: {excerpts}")

    lines.extend(("", "Repeated opener matches:"))
    if report["repeated_paragraph_opener_matches"]:
        for match in report["repeated_paragraph_opener_matches"]:
            lines.append(
                f"- L{match['line']} {match['opener']}: {match['excerpt']}"
            )
    else:
        lines.append("- none")

    lines.extend(("", str(report["note"])))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article", type=Path)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    report = analyze(args.article.read_text(encoding="utf-8"))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
