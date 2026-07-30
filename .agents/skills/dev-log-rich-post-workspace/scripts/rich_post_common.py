#!/usr/bin/env python3
"""Shared validation helpers for dev.log rich-post bundles."""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
import tempfile
import zlib
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
REPO_SCRIPTS = REPO_ROOT / "scripts"
if str(REPO_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REPO_SCRIPTS))

from md2tistory import split_frontmatter  # noqa: E402


DIRECTIVE_RE = re.compile(
    r"(?m)^\s*\{\{media:([a-z0-9]+(?:-[a-z0-9]+)*)\}\}\s*$"
)
ANY_DIRECTIVE_RE = re.compile(r"\{\{media:([^}]+)\}\}")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FENCE_OPEN_RE = re.compile(r"^\s*(`{3,}|~{3,})")
IMG_SRC_RE = re.compile(r'(<img\b[^>]*\bsrc=")[^"]*(")', re.IGNORECASE)

KINDS = {"image", "screenshot", "gif"}
ORIGINS = {
    "first_party",
    "official",
    "user_supplied",
    "simulated",
    "generated",
}
ROLES = {
    "lead",
    "concept",
    "action",
    "change",
    "result",
    "error",
    "comparison",
    "poster",
}
STATUSES = {"planned", "captured", "revision_required", "validated"}
STATIC_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
REQUIRED_VIEWPORTS = {
    1280: 900,
    390: 844,
    360: 800,
}
INDEPENDENT_BOOLEAN_CHECKS = {
    "captions_attached",
    "table_code_scroll",
    "content_order_preserved",
}
INDEPENDENT_GIF_CHECKS = {
    "reduced_motion_fallback",
    "gif_poster_matches_frame",
}
REMOTE_MAX_BYTES = 32 * 1024 * 1024
MAX_IMAGE_PIXELS = 50_000_000
MAX_DECODED_IMAGE_BYTES = 256 * 1024 * 1024
TISTORY_MEDIA_HOST_SUFFIXES = (
    "kakaocdn.net",
    "daumcdn.net",
    "tistory.com",
)
REMOTE_FINGERPRINT_FIELDS = (
    "id",
    "requested_url",
    "final_url",
    "content_type",
    "content_encoding",
    "byte_length",
    "sha256",
    "format",
    "width",
    "height",
    "frame_count",
    "duration_seconds",
)


def iter_fence_lines(lines: list[str]):
    """Yield each line with whether it is outside a fenced code block."""
    fence_char = ""
    fence_length = 0
    for line in lines:
        if fence_char:
            yield line, False
            closing = re.match(
                rf"^\s*{re.escape(fence_char)}{{{fence_length},}}\s*$",
                line,
            )
            if closing:
                fence_char = ""
                fence_length = 0
            continue

        opening = FENCE_OPEN_RE.match(line)
        if opening:
            marker = opening.group(1)
            fence_char = marker[0]
            fence_length = len(marker)
            yield line, False
        else:
            yield line, True


def outside_fenced_text(text: str) -> str:
    return "\n".join(
        line if outside else ""
        for line, outside in iter_fence_lines(text.splitlines())
    )


def is_https_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
        return parsed.scheme == "https" and bool(parsed.netloc)
    except ValueError:
        return False


def is_tistory_media_url(value: str) -> bool:
    if not is_https_url(value):
        return False
    try:
        parsed = urlparse(value)
        port = parsed.port
    except ValueError:
        return False
    if parsed.username or parsed.password or port not in {None, 443}:
        return False
    hostname = (parsed.hostname or "").rstrip(".").lower()
    return any(
        hostname == suffix or hostname.endswith(f".{suffix}")
        for suffix in TISTORY_MEDIA_HOST_SUFFIXES
    )


def is_iso_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return "T" in value and parsed.tzinfo is not None


def resolve_inside(base: Path, relative: str) -> Path | None:
    try:
        candidate = Path(relative)
        if candidate.is_absolute():
            return None
        resolved = (base / candidate).resolve()
        resolved.relative_to(base.resolve())
    except (OSError, ValueError):
        return None
    return resolved


def resolve_under(base: Path, relative: str, required_root: str) -> Path | None:
    resolved = resolve_inside(base, relative)
    if resolved is None:
        return None
    root = (base / required_root).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None
    return resolved


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write JSON through a unique same-directory file, then replace atomically."""
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except (OSError, TypeError, ValueError):
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
        raise


def remote_toolchain_files() -> dict[str, str]:
    """Return hashes for every source file that decides remote-media validity."""
    scripts_dir = SKILL_DIR / "scripts"
    return {
        "remote_media.py": sha256_file(scripts_dir / "remote_media.py"),
        "rich_post_common.py": sha256_file(scripts_dir / "rich_post_common.py"),
    }


def remote_toolchain_sha256(files: dict[str, str] | None = None) -> str:
    if files is None:
        files = remote_toolchain_files()
    digest = hashlib.sha256()
    for name, file_hash in sorted(files.items()):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_hash.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def article_content_sha256(path: Path) -> str:
    """Hash publication content while ignoring lifecycle-only frontmatter."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    filtered_lines = lines
    if lines and lines[0].strip() == "---":
        closing_index = next(
            (
                index
                for index, line in enumerate(lines[1:], start=1)
                if line.strip() == "---"
            ),
            None,
        )
        if closing_index is not None:
            filtered_lines = [
                line
                for index, line in enumerate(lines)
                if not (
                    0 < index < closing_index
                    and re.match(r"^(status|published_url)\s*:", line)
                )
            ]
    filtered = "".join(filtered_lines)
    return hashlib.sha256(filtered.encode("utf-8")).hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def preview_structure_sha256(text: str) -> str:
    normalized = IMG_SRC_RE.sub(r"\1__LOCAL_MEDIA__\2", text)
    return text_sha256(normalized)


def image_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return (
            int.from_bytes(data[16:20], "big"),
            int.from_bytes(data[20:24], "big"),
        )
    if data[:6] in {b"GIF87a", b"GIF89a"} and len(data) >= 10:
        return (
            int.from_bytes(data[6:8], "little"),
            int.from_bytes(data[8:10], "little"),
        )
    if data.startswith(b"\xff\xd8"):
        offset = 2
        start_of_frame = {
            0xC0,
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        }
        while offset + 9 < len(data):
            if data[offset] != 0xFF:
                offset += 1
                continue
            marker = data[offset + 1]
            offset += 2
            if marker in {0xD8, 0xD9}:
                continue
            if offset + 2 > len(data):
                break
            length = int.from_bytes(data[offset : offset + 2], "big")
            if length < 2 or offset + length > len(data):
                break
            if marker in start_of_frame and length >= 7:
                height = int.from_bytes(data[offset + 3 : offset + 5], "big")
                width = int.from_bytes(data[offset + 5 : offset + 7], "big")
                return width, height
            offset += length
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8X" and len(data) >= 30:
            width = 1 + int.from_bytes(data[24:27], "little")
            height = 1 + int.from_bytes(data[27:30], "little")
            return width, height
        if chunk == b"VP8L" and len(data) >= 25 and data[20] == 0x2F:
            b1, b2, b3, b4 = data[21:25]
            width = 1 + b1 + ((b2 & 0x3F) << 8)
            height = 1 + ((b2 & 0xC0) >> 6) + (b3 << 2) + ((b4 & 0x0F) << 10)
            return width, height
        signature = data.find(b"\x9d\x01\x2a")
        if signature >= 0 and signature + 7 <= len(data):
            width = int.from_bytes(data[signature + 3 : signature + 5], "little")
            height = int.from_bytes(data[signature + 5 : signature + 7], "little")
            return width & 0x3FFF, height & 0x3FFF
    return None


def detected_kind(path: Path) -> str | None:
    header = path.read_bytes()[:16]
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if header.startswith(b"\xff\xd8"):
        return "jpeg"
    if header[:6] in {b"GIF87a", b"GIF89a"}:
        return "gif"
    if header.startswith(b"RIFF") and header[8:12] == b"WEBP":
        return "webp"
    return None


def _png_scan_layout(
    width: int,
    height: int,
    bits_per_pixel: int,
    interlace: int,
) -> tuple[int, list[tuple[int, int]]] | None:
    if width <= 0 or height <= 0 or width * height > MAX_IMAGE_PIXELS:
        return None
    if interlace == 0:
        row_bytes = (width * bits_per_pixel + 7) // 8
        total = (row_bytes + 1) * height
        return total, [(row_bytes, height)]

    passes = (
        (0, 0, 8, 8),
        (4, 0, 8, 8),
        (0, 4, 4, 8),
        (2, 0, 4, 4),
        (0, 2, 2, 4),
        (1, 0, 2, 2),
        (0, 1, 1, 2),
    )
    layout: list[tuple[int, int]] = []
    total = 0
    for x_start, y_start, x_step, y_step in passes:
        pass_width = (
            0
            if width <= x_start
            else (width - x_start + x_step - 1) // x_step
        )
        pass_height = (
            0
            if height <= y_start
            else (height - y_start + y_step - 1) // y_step
        )
        if pass_width == 0 or pass_height == 0:
            continue
        row_bytes = (pass_width * bits_per_pixel + 7) // 8
        total += (row_bytes + 1) * pass_height
        layout.append((row_bytes, pass_height))
    return total, layout


def _validate_png_scanlines(
    compressed_parts: list[bytes],
    expected_length: int,
    layout: list[tuple[int, int]],
) -> str | None:
    layout_index = 0
    rows_left = layout[0][1] if layout else 0
    row_bytes_left = 0
    total = 0

    def consume(decoded: bytes) -> str | None:
        nonlocal layout_index, rows_left, row_bytes_left, total
        total += len(decoded)
        if total > expected_length:
            return "PNG decoded data exceeds the declared dimensions"
        position = 0
        while position < len(decoded):
            if layout_index >= len(layout):
                return "PNG decoded data exceeds the scanline layout"
            if row_bytes_left == 0:
                if decoded[position] > 4:
                    return "PNG scanline uses an invalid filter"
                position += 1
                row_bytes_left = layout[layout_index][0]
                if row_bytes_left == 0:
                    rows_left -= 1
            take = min(row_bytes_left, len(decoded) - position)
            position += take
            row_bytes_left -= take
            if row_bytes_left == 0:
                rows_left -= 1
                if rows_left == 0:
                    layout_index += 1
                    if layout_index < len(layout):
                        rows_left = layout[layout_index][1]
        return None

    decompressor = zlib.decompressobj()
    try:
        for compressed in compressed_parts:
            pending = compressed
            while pending:
                decoded = decompressor.decompress(pending, 1024 * 1024)
                error = consume(decoded)
                if error:
                    return error
                pending = decompressor.unconsumed_tail
                if not decoded and pending:
                    return "PNG IDAT stream made no decompression progress"
        decoded = decompressor.flush(1024 * 1024)
        error = consume(decoded)
        if error:
            return error
    except zlib.error:
        return "PNG IDAT stream cannot be decompressed"
    if not decompressor.eof or decompressor.unused_data:
        return "PNG IDAT stream is incomplete or has trailing data"
    if (
        total != expected_length
        or layout_index != len(layout)
        or row_bytes_left != 0
    ):
        return "PNG decoded data does not match the declared dimensions"
    return None


def _png_container_error(data: bytes) -> str | None:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "PNG signature is missing"

    position = 8
    chunks: list[tuple[bytes, bytes]] = []
    while position + 12 <= len(data):
        length = int.from_bytes(data[position : position + 4], "big")
        chunk_end = position + 12 + length
        if chunk_end > len(data):
            return "truncated PNG chunk"
        kind = data[position + 4 : position + 8]
        chunk_data = data[position + 8 : position + 8 + length]
        expected_crc = int.from_bytes(
            data[position + 8 + length : chunk_end],
            "big",
        )
        if zlib.crc32(kind + chunk_data) & 0xFFFFFFFF != expected_crc:
            return "PNG chunk CRC mismatch"
        chunks.append((kind, chunk_data))
        position = chunk_end
        if kind == b"IEND":
            break

    if not chunks or chunks[0][0] != b"IHDR":
        return "PNG must begin with IHDR"
    if chunks[-1][0] != b"IEND" or position != len(data):
        return "PNG is missing a terminal IEND chunk"
    if chunks[-1][1]:
        return "PNG IEND chunk must be empty"
    if sum(kind == b"IHDR" for kind, _ in chunks) != 1:
        return "PNG must contain exactly one IHDR"
    if len(chunks[0][1]) != 13:
        return "PNG IHDR length must be 13"

    ihdr = chunks[0][1]
    width = int.from_bytes(ihdr[0:4], "big")
    height = int.from_bytes(ihdr[4:8], "big")
    bit_depth = ihdr[8]
    color_type = ihdr[9]
    compression, filter_method, interlace = ihdr[10:13]
    valid_depths = {
        0: {1, 2, 4, 8, 16},
        2: {8, 16},
        3: {1, 2, 4, 8},
        4: {8, 16},
        6: {8, 16},
    }
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
    if color_type not in valid_depths or bit_depth not in valid_depths[color_type]:
        return "PNG color type and bit depth are incompatible"
    if compression != 0 or filter_method != 0 or interlace not in {0, 1}:
        return "PNG uses unsupported IHDR methods"
    if color_type == 3 and not any(kind == b"PLTE" for kind, _ in chunks):
        return "indexed PNG is missing PLTE"

    known_critical = {b"IHDR", b"PLTE", b"IDAT", b"IEND"}
    for kind, _ in chunks:
        if len(kind) != 4 or not all(
            ord("A") <= value <= ord("Z") or ord("a") <= value <= ord("z")
            for value in kind
        ):
            return "PNG chunk type is invalid"
        if kind[0] & 0x20 == 0 and kind not in known_critical:
            return "PNG contains an unknown critical chunk"

    idat_indexes = [
        index for index, (kind, _) in enumerate(chunks) if kind == b"IDAT"
    ]
    if not idat_indexes:
        return "PNG is missing IDAT image data"
    if idat_indexes != list(range(idat_indexes[0], idat_indexes[-1] + 1)):
        return "PNG IDAT chunks must be consecutive"
    plte_indexes = [
        index for index, (kind, _) in enumerate(chunks) if kind == b"PLTE"
    ]
    if len(plte_indexes) > 1:
        return "PNG must contain at most one PLTE"
    if plte_indexes:
        palette = chunks[plte_indexes[0]][1]
        if plte_indexes[0] > idat_indexes[0]:
            return "PNG PLTE must appear before IDAT"
        if len(palette) == 0 or len(palette) % 3 or len(palette) > 768:
            return "PNG PLTE length is invalid"
        if color_type == 3 and len(palette) // 3 > 2**bit_depth:
            return "PNG PLTE has too many indexed entries"
    layout_result = _png_scan_layout(
        width,
        height,
        channels[color_type] * bit_depth,
        interlace,
    )
    if layout_result is None:
        return "PNG dimensions are invalid or exceed the pixel limit"
    expected_length, layout = layout_result
    if expected_length > MAX_DECODED_IMAGE_BYTES:
        return "PNG decoded image exceeds the safety limit"

    return _validate_png_scanlines(
        [chunks[index][1] for index in idat_indexes],
        expected_length,
        layout,
    )


def _jpeg_container_error(data: bytes) -> str | None:
    if not data.startswith(b"\xff\xd8"):
        return "JPEG start marker is missing"

    position = 2
    saw_frame = False
    saw_scan = False
    saw_entropy = False
    frame_marker: int | None = None
    saw_quantization_table = False
    saw_huffman_table = False
    saw_arithmetic_table = False
    quantization_tables: set[int] = set()
    huffman_tables: set[tuple[int, int]] = set()
    referenced_quantization_tables: set[int] = set()
    frame_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    while position < len(data):
        if data[position] != 0xFF:
            return "JPEG marker stream is malformed"
        marker_start = position
        while position < len(data) and data[position] == 0xFF:
            position += 1
        if position >= len(data):
            return "JPEG marker is truncated"
        marker = data[position]
        position += 1
        if marker == 0x00:
            return "JPEG contains stuffed data outside a scan"
        if marker == 0xD9:
            if position != len(data):
                return "JPEG has trailing bytes after its end marker"
            if not saw_frame or not saw_scan or not saw_entropy:
                return "JPEG is missing a frame or encoded scan"
            lossless_frames = {0xC3, 0xC7, 0xCB, 0xCF}
            arithmetic_frames = {0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
            if frame_marker not in lossless_frames and not saw_quantization_table:
                return "JPEG DCT frame is missing a quantization table"
            if frame_marker in arithmetic_frames:
                if not saw_arithmetic_table:
                    return "JPEG arithmetic frame is missing a conditioning table"
            elif not saw_huffman_table:
                return "JPEG Huffman frame is missing a coding table"
            return None
        if marker in {0x01, *range(0xD0, 0xD9)}:
            if marker in range(0xD0, 0xD8):
                return "JPEG restart marker appears outside a scan"
            continue
        if position + 2 > len(data):
            return "JPEG segment length is truncated"
        segment_length = int.from_bytes(data[position : position + 2], "big")
        if segment_length < 2 or position + segment_length > len(data):
            return "JPEG segment is truncated"
        segment_end = position + segment_length
        if marker in frame_markers:
            if segment_length < 8:
                return "JPEG frame header is too short"
            height = int.from_bytes(data[position + 3 : position + 5], "big")
            width = int.from_bytes(data[position + 5 : position + 7], "big")
            components = data[position + 7]
            if components <= 0 or segment_length != 8 + 3 * components:
                return "JPEG frame component table is malformed"
            if width <= 0 or height <= 0 or width * height > MAX_IMAGE_PIXELS:
                return "JPEG dimensions are invalid or exceed the pixel limit"
            component_start = position + 8
            for index in range(components):
                table_id = data[component_start + index * 3 + 2]
                if table_id > 3:
                    return "JPEG frame references an invalid quantization table"
                referenced_quantization_tables.add(table_id)
            saw_frame = True
            frame_marker = marker
        elif marker == 0xDB:
            table_position = position + 2
            parsed_table = False
            while table_position < segment_end:
                specification = data[table_position]
                precision = specification >> 4
                table_id = specification & 0x0F
                if precision not in {0, 1} or table_id > 3:
                    return "JPEG quantization table header is invalid"
                table_position += 1 + (64 if precision == 0 else 128)
                if table_position > segment_end:
                    return "JPEG quantization table is truncated"
                quantization_tables.add(table_id)
                parsed_table = True
            if table_position != segment_end or not parsed_table:
                return "JPEG quantization table segment is empty"
            saw_quantization_table = True
        elif marker == 0xC4:
            table_position = position + 2
            parsed_table = False
            while table_position < segment_end:
                if table_position + 17 > segment_end:
                    return "JPEG Huffman table is truncated"
                specification = data[table_position]
                table_class = specification >> 4
                table_id = specification & 0x0F
                if table_class not in {0, 1} or table_id > 3:
                    return "JPEG Huffman table header is invalid"
                symbol_count = sum(data[table_position + 1 : table_position + 17])
                if symbol_count <= 0 or symbol_count > 256:
                    return "JPEG Huffman table symbol count is invalid"
                table_position += 17 + symbol_count
                if table_position > segment_end:
                    return "JPEG Huffman table symbols are truncated"
                huffman_tables.add((table_class, table_id))
                parsed_table = True
            if table_position != segment_end or not parsed_table:
                return "JPEG Huffman table segment is empty"
            saw_huffman_table = True
        elif marker == 0xCC:
            payload_length = segment_length - 2
            if payload_length <= 0 or payload_length % 2:
                return "JPEG arithmetic conditioning table is malformed"
            saw_arithmetic_table = True
        if marker != 0xDA:
            position = segment_end
            continue

        if segment_length < 6:
            return "JPEG scan header is too short"
        scan_components = data[position + 2]
        if scan_components <= 0 or segment_length != 6 + 2 * scan_components:
            return "JPEG scan component table is malformed"
        if not referenced_quantization_tables.issubset(quantization_tables):
            return "JPEG scan references a missing quantization table"
        if frame_marker not in {0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            selector_start = position + 3
            for index in range(scan_components):
                selector = data[selector_start + index * 2 + 1]
                dc_table = selector >> 4
                ac_table = selector & 0x0F
                if dc_table > 3 or ac_table > 3:
                    return "JPEG scan references an invalid Huffman table"
                if (0, dc_table) not in huffman_tables:
                    return "JPEG scan references a missing DC Huffman table"
                if frame_marker not in {0xC3, 0xC7} and (
                    1,
                    ac_table,
                ) not in huffman_tables:
                    return "JPEG scan references a missing AC Huffman table"
        saw_scan = True
        position = segment_end
        entropy_bytes = 0
        while position < len(data):
            if data[position] != 0xFF:
                entropy_bytes += 1
                position += 1
                continue
            marker_start = position
            while position < len(data) and data[position] == 0xFF:
                position += 1
            if position >= len(data):
                return "JPEG scan marker is truncated"
            scan_marker = data[position]
            if scan_marker == 0x00:
                entropy_bytes += 1
                position += 1
                continue
            if 0xD0 <= scan_marker <= 0xD7:
                position += 1
                continue
            position = marker_start
            break
        if entropy_bytes == 0:
            return "JPEG scan contains no encoded image data"
        saw_entropy = True
    return "JPEG is missing its end marker"


def _webp_container_error(data: bytes) -> str | None:
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return "WebP RIFF signature is missing"
    if int.from_bytes(data[4:8], "little") + 8 != len(data):
        return "WebP RIFF length does not match its body"

    position = 12
    bitstreams = 0
    extended_dimensions: tuple[int, int] | None = None
    bitstream_dimensions: tuple[int, int] | None = None
    while position < len(data):
        if position + 8 > len(data):
            return "WebP chunk header is truncated"
        kind = data[position : position + 4]
        length = int.from_bytes(data[position + 4 : position + 8], "little")
        data_start = position + 8
        data_end = data_start + length
        padded_end = data_end + (length % 2)
        if padded_end > len(data):
            return "WebP chunk is truncated"
        payload = data[data_start:data_end]
        if kind in {b"ANIM", b"ANMF"}:
            return "animated WebP is unsupported; use GIF with a poster"
        if kind == b"VP8 ":
            bitstreams += 1
            if len(payload) < 10 or payload[3:6] != b"\x9d\x01\x2a":
                return "WebP VP8 bitstream header is invalid"
            frame_tag = int.from_bytes(payload[0:3], "little")
            if frame_tag & 1:
                return "WebP VP8 bitstream must begin with a key frame"
            if (frame_tag >> 1) & 0x07 > 3 or not (frame_tag & 0x10):
                return "WebP VP8 frame tag is invalid"
            first_partition_length = frame_tag >> 5
            if (
                first_partition_length <= 0
                or 10 + first_partition_length > len(payload)
            ):
                return "WebP VP8 first partition is truncated"
            width = int.from_bytes(payload[6:8], "little") & 0x3FFF
            height = int.from_bytes(payload[8:10], "little") & 0x3FFF
            if width <= 0 or height <= 0 or width * height > MAX_IMAGE_PIXELS:
                return "WebP dimensions are invalid or exceed the pixel limit"
            bitstream_dimensions = (width, height)
        elif kind == b"VP8L":
            bitstreams += 1
            if len(payload) <= 5 or payload[0] != 0x2F:
                return "WebP VP8L bitstream header is invalid"
            b1, b2, b3, b4 = payload[1:5]
            if b4 & 0xE0:
                return "WebP VP8L version bits are unsupported"
            width = 1 + b1 + ((b2 & 0x3F) << 8)
            height = 1 + ((b2 & 0xC0) >> 6) + (b3 << 2) + (
                (b4 & 0x0F) << 10
            )
            if width * height > MAX_IMAGE_PIXELS:
                return "WebP dimensions exceed the pixel limit"
            bitstream_dimensions = (width, height)
        elif kind == b"VP8X":
            if len(payload) != 10:
                return "WebP VP8X header length must be 10"
            flags = payload[0]
            if flags & 0xC3 or payload[1:4] != b"\x00\x00\x00":
                return "WebP VP8X reserved fields or animation flag are invalid"
            width = 1 + int.from_bytes(payload[4:7], "little")
            height = 1 + int.from_bytes(payload[7:10], "little")
            if width * height > MAX_IMAGE_PIXELS:
                return "WebP VP8X canvas exceeds the pixel limit"
            extended_dimensions = (width, height)
        position = padded_end
    if position != len(data):
        return "WebP chunk padding is malformed"
    if bitstreams != 1:
        return "WebP must contain exactly one VP8 or VP8L image bitstream"
    if (
        extended_dimensions is not None
        and bitstream_dimensions is not None
        and extended_dimensions != bitstream_dimensions
    ):
        return "WebP VP8X canvas and image bitstream dimensions differ"
    return None


def image_container_error_bytes(data: bytes, media_format: str) -> str | None:
    if media_format == "png":
        return _png_container_error(data)
    if media_format == "gif":
        if data[:6] not in {b"GIF87a", b"GIF89a"} or len(data) < 10:
            return "GIF header is truncated"
        width = int.from_bytes(data[6:8], "little")
        height = int.from_bytes(data[8:10], "little")
        if width <= 0 or height <= 0 or width * height > MAX_IMAGE_PIXELS:
            return "GIF dimensions are invalid or exceed the pixel limit"
        if not data.endswith(b"\x3b"):
            return "GIF is missing its trailer"
        return None
    if media_format == "jpeg":
        return _jpeg_container_error(data)
    if media_format == "webp":
        return _webp_container_error(data)
    return "unsupported image format"


def image_container_error(path: Path, media_format: str) -> str | None:
    return image_container_error_bytes(path.read_bytes(), media_format)


def bind_screenshot_evidence(
    post_dir: Path,
    value: object,
    screenshot_root: str = "artifacts/qa",
) -> object:
    if not isinstance(value, list):
        return value

    bound: list[object] = []
    for viewport in value:
        if not isinstance(viewport, dict):
            bound.append(viewport)
            continue
        item = dict(viewport)
        for field in (
            "screenshot_sha256",
            "screenshot_pixel_width",
            "screenshot_pixel_height",
        ):
            item.pop(field, None)
        screenshot = item.get("screenshot")
        if isinstance(screenshot, str):
            screenshot_path = resolve_under(
                post_dir,
                screenshot,
                screenshot_root,
            )
            if screenshot_path is not None and screenshot_path.is_file():
                dimensions = image_dimensions(screenshot_path)
                if dimensions is not None:
                    item["screenshot_pixel_width"] = dimensions[0]
                    item["screenshot_pixel_height"] = dimensions[1]
                item["screenshot_sha256"] = sha256_file(screenshot_path)
        bound.append(item)
    return bound


def _skip_gif_sub_blocks(data: bytes, position: int) -> int | None:
    while position < len(data):
        size = data[position]
        position += 1
        if size == 0:
            return position
        if position + size > len(data):
            return None
        position += size
    return None


def gif_animation_info(path: Path) -> tuple[int, float] | None:
    """Return GIF frame count and total declared frame delay."""
    data = path.read_bytes()
    if data[:6] not in {b"GIF87a", b"GIF89a"} or len(data) < 13:
        return None

    position = 13
    packed = data[10]
    if packed & 0x80:
        position += 3 * (2 ** ((packed & 0x07) + 1))
    frames = 0
    total_delay_cs = 0
    pending_delay_cs = 0

    while position < len(data):
        marker = data[position]
        if marker == 0x3B:
            return frames, total_delay_cs / 100
        if marker == 0x21:
            if position + 2 >= len(data):
                return None
            label = data[position + 1]
            if label == 0xF9:
                if (
                    position + 8 > len(data)
                    or data[position + 2] != 4
                    or data[position + 7] != 0
                ):
                    return None
                pending_delay_cs = int.from_bytes(
                    data[position + 4 : position + 6], "little"
                )
                position += 8
            else:
                skipped = _skip_gif_sub_blocks(data, position + 2)
                if skipped is None:
                    return None
                position = skipped
            continue
        if marker == 0x2C:
            if position + 10 > len(data):
                return None
            descriptor_packed = data[position + 9]
            position += 10
            if descriptor_packed & 0x80:
                position += 3 * (2 ** ((descriptor_packed & 0x07) + 1))
            if position >= len(data):
                return None
            if not 2 <= data[position] <= 8:
                return None
            position += 1
            skipped = _skip_gif_sub_blocks(data, position)
            if skipped is None:
                return None
            position = skipped
            frames += 1
            total_delay_cs += pending_delay_cs
            pending_delay_cs = 0
            continue
        return None
    return None


def _required_string(
    item: dict[str, Any], field: str, item_id: str, errors: list[str]
) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{item_id}: `{field}` must be a non-empty string")
        return ""
    return value.strip()


def _load_json_object(
    path: Path,
    label: str,
    errors: list[str],
) -> dict[str, Any]:
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as exc:
        errors.append(f"cannot read {label}: {exc}")
        return {}
    if not isinstance(loaded, dict):
        errors.append(f"{label} root must be an object")
        return {}
    return loaded


CAPTURE_MODE_PATHS = {
    "creator": {
        "receipt": "artifacts/qa/browser-capture.json",
        "screenshot_root": "artifacts/qa",
    },
    "independent": {
        "receipt": "artifacts/qa/independent/browser-capture.json",
        "screenshot_root": "artifacts/qa/independent",
    },
}
CAPTURE_VIEWPORT_FIELDS = (
    "width",
    "height",
    "client_width",
    "scroll_width",
    "h1_count",
    "toc_targets_unique",
    "images_loaded",
    "screenshot",
    "screenshot_sha256",
    "screenshot_pixel_width",
    "screenshot_pixel_height",
)
CAPTURE_SCREENSHOT_NAMES = {
    1280: "desktop-1280.png",
    390: "mobile-390.png",
    360: "mobile-360.png",
}


def validate_browser_capture_receipt(
    post_dir: Path,
    preview_path: Path,
    mode: str,
    errors: list[str],
) -> tuple[Path, dict[str, Any]]:
    config = CAPTURE_MODE_PATHS[mode]
    receipt_path = post_dir / config["receipt"]
    if not receipt_path.is_file():
        errors.append(f"missing {config['receipt']}")
        return receipt_path, {}
    try:
        receipt_path.resolve().relative_to(post_dir.resolve())
    except (OSError, ValueError):
        errors.append(f"{config['receipt']} must resolve inside the post bundle")
        return receipt_path, {}

    receipt = _load_json_object(receipt_path, config["receipt"], errors)
    if not receipt:
        return receipt_path, receipt
    label = f"{mode} browser capture"
    if receipt.get("version") != 1:
        errors.append(f"{label} version must be 1")
    if receipt.get("status") != "pass":
        errors.append(f"{label} status must be `pass`")
    if receipt.get("mode") != mode:
        errors.append(f"{label} mode must be `{mode}`")
    if not is_iso_timestamp(receipt.get("checked_at")):
        errors.append(f"{label} checked_at must be an ISO-8601 timestamp")
    if not isinstance(receipt.get("checked_by"), str) or not receipt[
        "checked_by"
    ].strip():
        errors.append(f"{label} checked_by must name the actual reviewer")
    capture_tool = SKILL_DIR / "scripts" / "capture_rich_qa.py"
    if receipt.get("tool_sha256") != sha256_file(capture_tool):
        errors.append(f"{label} tool_sha256 does not match capture_rich_qa.py")
    try:
        expected_preview_relative = preview_path.relative_to(post_dir).as_posix()
    except ValueError:
        expected_preview_relative = ""
    if receipt.get("preview_path") != expected_preview_relative:
        errors.append(f"{label} preview_path is not the reviewed preview")
    if (
        not preview_path.is_file()
        or receipt.get("preview_sha256") != sha256_file(preview_path)
    ):
        errors.append(f"{label} preview_sha256 does not match the preview")
    if receipt.get("screenshot_root") != config["screenshot_root"]:
        errors.append(f"{label} screenshot_root is not canonical")
    if receipt.get("receipt_path") != config["receipt"]:
        errors.append(f"{label} receipt_path is not canonical")
    for field in ("browser_version", "protocol_version", "session"):
        if not isinstance(receipt.get(field), str) or not receipt[field].strip():
            errors.append(f"{label} {field} must be non-empty")

    try:
        preview_markup = preview_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot read {label} preview: {exc}")
        preview_sources: list[str] = []
    else:
        preview_sources = [
            html.unescape(source)
            for source in re.findall(
                r'<img\b[^>]*\bsrc="([^"]+)"',
                preview_markup,
                re.IGNORECASE,
            )
        ]

    viewports = receipt.get("viewports")
    if not isinstance(viewports, list):
        errors.append(f"{label} viewports must be an array")
        viewports = []
    seen_widths: set[int] = set()
    seen_hashes: set[str] = set()
    for index, viewport in enumerate(viewports):
        viewport_label = f"{label} viewports[{index}]"
        if not isinstance(viewport, dict):
            errors.append(f"{viewport_label} must be an object")
            continue
        width = viewport.get("width")
        height = viewport.get("height")
        if (
            type(width) is not int
            or width not in REQUIRED_VIEWPORTS
            or height != REQUIRED_VIEWPORTS.get(width)
        ):
            errors.append(f"{viewport_label} is not a required exact profile")
            continue
        if width in seen_widths:
            errors.append(f"{viewport_label} duplicates width {width}")
        seen_widths.add(width)
        expected_values = {
            "inner_width": width,
            "inner_height": height,
            "client_width": width,
            "h1_count": 1,
            "toc_targets_unique": True,
            "images_loaded": True,
            "status": "pass",
        }
        for field, expected in expected_values.items():
            if viewport.get(field) != expected:
                errors.append(
                    f"{viewport_label} {field} must equal {expected!r}"
                )
        if viewport.get("scroll_width") != width:
            errors.append(f"{viewport_label} page overflow must be zero")
        if viewport.get("ready_state") != "complete":
            errors.append(f"{viewport_label} document must be complete")
        if viewport.get("location") != preview_path.as_uri():
            errors.append(f"{viewport_label} location is not the canonical preview")
        if (
            type(viewport.get("toc_anchor_count")) is not int
            or viewport["toc_anchor_count"] <= 0
        ):
            errors.append(f"{viewport_label} must contain TOC anchors")

        images = viewport.get("images")
        observed_sources: list[str] = []
        if not isinstance(images, list) or not images:
            errors.append(f"{viewport_label} images must be a non-empty array")
        else:
            for image_index, image in enumerate(images):
                if not isinstance(image, dict):
                    errors.append(
                        f"{viewport_label} images[{image_index}] must be an object"
                    )
                    continue
                source = image.get("src")
                if not isinstance(source, str) or not is_tistory_media_url(source):
                    errors.append(
                        f"{viewport_label} images[{image_index}] has invalid src"
                    )
                else:
                    observed_sources.append(source)
                if image.get("complete") is not True:
                    errors.append(
                        f"{viewport_label} images[{image_index}] is incomplete"
                    )
                for dimension_field in ("natural_width", "natural_height"):
                    value = image.get(dimension_field)
                    if type(value) is not int or value <= 0:
                        errors.append(
                            f"{viewport_label} images[{image_index}] "
                            f"{dimension_field} must be positive"
                        )
        if sorted(observed_sources) != sorted(preview_sources):
            errors.append(
                f"{viewport_label} decoded images differ from preview img sources"
            )

        expected_screenshot = (
            f"{config['screenshot_root']}/"
            f"{CAPTURE_SCREENSHOT_NAMES[width]}"
        )
        if viewport.get("screenshot") != expected_screenshot:
            errors.append(f"{viewport_label} screenshot path is not canonical")
            continue
        screenshot_path = resolve_under(
            post_dir,
            expected_screenshot,
            config["screenshot_root"],
        )
        if screenshot_path is None or not screenshot_path.is_file():
            errors.append(f"{viewport_label} screenshot file does not exist")
            continue
        screenshot_kind = detected_kind(screenshot_path)
        if screenshot_kind != "png":
            errors.append(f"{viewport_label} screenshot must be PNG")
            continue
        container_error = image_container_error(screenshot_path, screenshot_kind)
        if container_error:
            errors.append(
                f"{viewport_label} screenshot is malformed: {container_error}"
            )
        dimensions = image_dimensions(screenshot_path)
        if dimensions != (width, height):
            errors.append(
                f"{viewport_label} screenshot pixels must equal {width}x{height}"
            )
        screenshot_hash = sha256_file(screenshot_path)
        if viewport.get("screenshot_sha256") != screenshot_hash:
            errors.append(f"{viewport_label} screenshot_sha256 does not match")
        if viewport.get("screenshot_pixel_width") != width or viewport.get(
            "screenshot_pixel_height"
        ) != height:
            errors.append(f"{viewport_label} screenshot dimensions do not match")
        if screenshot_hash in seen_hashes:
            errors.append(f"{viewport_label} screenshot content must be unique")
        seen_hashes.add(screenshot_hash)
    if seen_widths != set(REQUIRED_VIEWPORTS):
        errors.append(f"{label} must contain exactly the three required viewports")
    return receipt_path, receipt


def merge_browser_capture_viewports(
    receipt: dict[str, Any],
    human_viewports: object,
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(human_viewports, list):
        errors.append("browser measurements `viewports` must be an array")
        return []
    human_by_width: dict[int, dict[str, Any]] = {}
    for index, viewport in enumerate(human_viewports):
        if not isinstance(viewport, dict):
            errors.append(f"browser measurements viewports[{index}] must be an object")
            continue
        width = viewport.get("width")
        if type(width) is not int or width in human_by_width:
            errors.append(
                f"browser measurements viewports[{index}] has invalid width"
            )
            continue
        human_by_width[width] = viewport
    if set(human_by_width) != set(REQUIRED_VIEWPORTS):
        errors.append("browser measurements must cover exactly the required widths")

    captured = receipt.get("viewports")
    if not isinstance(captured, list):
        return []
    merged: list[dict[str, Any]] = []
    for viewport in captured:
        if not isinstance(viewport, dict):
            continue
        width = viewport.get("width")
        human = human_by_width.get(width, {})
        item = {
            field: viewport.get(field) for field in CAPTURE_VIEWPORT_FIELDS
        }
        item["readable_media"] = human.get("readable_media")
        item["status"] = human.get("status")
        merged.append(item)
    return merged


def validate_remote_media_records(
    post_dir: Path,
    manifest_path: Path,
    manifest: dict[str, Any],
    errors: list[str],
    require_verification: bool = False,
) -> tuple[Path, dict[str, Any], Path, dict[str, Any]]:
    qa_dir = post_dir / "artifacts" / "qa"
    baseline_path = qa_dir / "remote-media.json"
    verification_path = qa_dir / "remote-media-verification.json"
    if not baseline_path.is_file():
        errors.append("missing artifacts/qa/remote-media.json")
        return baseline_path, {}, verification_path, {}

    baseline = _load_json_object(
        baseline_path,
        "artifacts/qa/remote-media.json",
        errors,
    )
    if not baseline:
        return baseline_path, baseline, verification_path, {}

    expected_media_hash = sha256_file(manifest_path)
    expected_fetcher_files = remote_toolchain_files()
    expected_fetcher_hash = remote_toolchain_sha256(expected_fetcher_files)
    if baseline.get("version") != 1:
        errors.append("remote-media `version` must be 1")
    if baseline.get("status") != "pass":
        errors.append("remote-media `status` must be `pass`")
    if not isinstance(baseline.get("record_id"), str) or not baseline[
        "record_id"
    ].strip():
        errors.append("remote-media `record_id` must be non-empty")
    if not is_iso_timestamp(baseline.get("recorded_at")):
        errors.append("remote-media `recorded_at` must be an ISO-8601 timestamp")
    if not isinstance(baseline.get("recorded_by"), str) or not baseline[
        "recorded_by"
    ].strip():
        errors.append("remote-media `recorded_by` must be non-empty")
    if baseline.get("media_sha256") != expected_media_hash:
        errors.append("remote-media media_sha256 does not match media.json")
    if baseline.get("fetcher_sha256") != expected_fetcher_hash:
        errors.append("remote-media fetcher_sha256 does not match the toolchain")
    if baseline.get("fetcher_files") != expected_fetcher_files:
        errors.append("remote-media fetcher_files do not match the toolchain")
    policy = baseline.get("policy")
    expected_policy = {
        "max_bytes": REMOTE_MAX_BYTES,
        "timeout_seconds": 20,
        "deadline_scope": "dns_redirect_headers_body",
        "max_redirects": 5,
        "accept_encoding": "identity",
    }
    if not isinstance(policy, dict) or any(
        policy.get(field) != expected
        for field, expected in expected_policy.items()
    ):
        errors.append("remote-media policy does not match the checker")

    baseline_items = baseline.get("items")
    if not isinstance(baseline_items, list):
        errors.append("remote-media `items` must be an array")
        baseline_items = []
    observed_by_id: dict[str, dict[str, Any]] = {}
    for index, observed in enumerate(baseline_items):
        if not isinstance(observed, dict):
            errors.append(f"remote-media items[{index}] must be an object")
            continue
        item_id = observed.get("id")
        if not isinstance(item_id, str) or item_id in observed_by_id:
            errors.append(f"remote-media items[{index}] has invalid or duplicate id")
            continue
        observed_by_id[item_id] = observed

    manifest_item_values = manifest.get("items")
    if not isinstance(manifest_item_values, list):
        manifest_item_values = []
    manifest_items = {
        item.get("id"): item
        for item in manifest_item_values
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    if set(observed_by_id) != set(manifest_items):
        errors.append("remote-media item IDs must exactly match media.json")

    for item_id, item in manifest_items.items():
        observed = observed_by_id.get(item_id)
        if observed is None:
            continue
        requested_url = item.get("tistory_url")
        if observed.get("requested_url") != requested_url:
            errors.append(f"{item_id}: remote requested_url differs from media.json")
        if not is_tistory_media_url(str(observed.get("final_url", ""))):
            errors.append(f"{item_id}: remote final_url is not an allowed Tistory URL")
        if observed.get("http_status") != 200:
            errors.append(f"{item_id}: remote HTTP status must be 200")
        if not is_iso_timestamp(observed.get("observed_at")):
            errors.append(f"{item_id}: remote observed_at must be ISO-8601")
        content_type = observed.get("content_type")
        allowed_content_types = {
            "image/png",
            "image/jpeg",
            "image/jpg",
            "image/webp",
            "image/gif",
            "application/octet-stream",
        }
        if (
            not isinstance(content_type, str)
            or content_type not in allowed_content_types
        ):
            errors.append(f"{item_id}: remote content_type is not an image")
            content_type = ""
        content_encoding = observed.get("content_encoding")
        if not isinstance(content_encoding, str) or content_encoding not in {
            "",
            "identity",
        }:
            errors.append(f"{item_id}: remote content_encoding must be identity")
        byte_length = observed.get("byte_length")
        if (
            type(byte_length) is not int
            or byte_length <= 0
            or byte_length > REMOTE_MAX_BYTES
        ):
            errors.append(f"{item_id}: remote byte_length is outside policy")
        header_length = observed.get("header_content_length")
        if header_length is not None and header_length != byte_length:
            errors.append(
                f"{item_id}: remote Content-Length differs from byte_length"
            )
        digest = observed.get("sha256")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            errors.append(f"{item_id}: remote sha256 is invalid")

        remote_format = observed.get("format")
        if not isinstance(remote_format, str):
            errors.append(f"{item_id}: remote format must be a string")
            remote_format = ""
        declared_formats = {
            "image/png": "png",
            "image/jpeg": "jpeg",
            "image/jpg": "jpeg",
            "image/webp": "webp",
            "image/gif": "gif",
        }
        if (
            content_type in declared_formats
            and declared_formats[content_type] != remote_format
        ):
            errors.append(
                f"{item_id}: remote content_type and format disagree"
            )
        if item.get("kind") == "gif":
            allowed_formats = {"gif"}
        else:
            allowed_formats = {"png", "jpeg", "webp"}
        if remote_format not in allowed_formats:
            errors.append(
                f"{item_id}: remote format `{remote_format}` is incompatible"
            )
        remote_width = observed.get("width")
        remote_height = observed.get("height")
        if (
            type(remote_width) is not int
            or remote_width <= 0
            or type(remote_height) is not int
            or remote_height <= 0
        ):
            errors.append(f"{item_id}: remote dimensions must be positive integers")
        else:
            local_width = item.get("width")
            local_height = item.get("height")
            if (
                type(local_width) is int
                and local_width > 0
                and type(local_height) is int
                and local_height > 0
            ):
                local_ratio = local_width / local_height
                remote_ratio = remote_width / remote_height
                if abs(remote_ratio - local_ratio) / local_ratio > 0.005:
                    errors.append(
                        f"{item_id}: remote aspect ratio differs by more than 0.5%"
                    )
            local_width = item.get("width")
            display_width = item.get(
                "display_width",
                min(local_width, 916)
                if type(local_width) is int and local_width > 0
                else 916,
            )
            if type(display_width) is int and remote_width < display_width:
                errors.append(
                    f"{item_id}: remote pixel width is below display_width"
                )

        frame_count = observed.get("frame_count")
        duration = observed.get("duration_seconds")
        if item.get("kind") == "gif":
            if type(frame_count) is not int or frame_count < 2:
                errors.append(f"{item_id}: remote GIF must have at least two frames")
            if (
                isinstance(duration, bool)
                or not isinstance(duration, (int, float))
                or duration <= 0
                or duration > 5
            ):
                errors.append(f"{item_id}: remote GIF duration must be 0-5 seconds")
        elif frame_count != 1 or duration != 0:
            errors.append(f"{item_id}: remote static image animation data is invalid")

    verification: dict[str, Any] = {}
    if require_verification:
        if not verification_path.is_file():
            errors.append(
                "missing artifacts/qa/remote-media-verification.json"
            )
        else:
            verification = _load_json_object(
                verification_path,
                "artifacts/qa/remote-media-verification.json",
                errors,
            )
        if verification:
            if verification.get("version") != 1:
                errors.append("remote verification `version` must be 1")
            if verification.get("status") != "pass":
                errors.append("remote verification `status` must be `pass`")
            if not is_iso_timestamp(verification.get("verified_at")):
                errors.append(
                    "remote verification `verified_at` must be ISO-8601"
                )
            verified_by = verification.get("verified_by")
            if not isinstance(verified_by, str) or not verified_by.strip():
                errors.append("remote verification `verified_by` must be non-empty")
            elif verified_by.strip() == str(baseline.get("recorded_by", "")).strip():
                errors.append(
                    "remote verification reviewer must differ from recorder"
                )
            if verification.get("remote_media_sha256") != sha256_file(
                baseline_path
            ):
                errors.append(
                    "remote verification does not match remote-media.json"
                )
            if verification.get("media_sha256") != expected_media_hash:
                errors.append(
                    "remote verification media_sha256 does not match media.json"
                )
            if verification.get("fetcher_sha256") != expected_fetcher_hash:
                errors.append(
                    "remote verification fetcher_sha256 does not match "
                    "the toolchain"
                )
            if verification.get("fetcher_files") != expected_fetcher_files:
                errors.append(
                    "remote verification fetcher_files do not match the toolchain"
                )
            verification_items = verification.get("items")
            if not isinstance(verification_items, list):
                errors.append("remote verification `items` must be an array")
                verification_items = []
            verified_by_id = {
                item.get("id"): item
                for item in verification_items
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            }
            if set(verified_by_id) != set(observed_by_id):
                errors.append(
                    "remote verification item IDs must match the baseline"
                )
            for item_id, observed in observed_by_id.items():
                verified = verified_by_id.get(item_id)
                if verified is None:
                    continue
                for field in REMOTE_FINGERPRINT_FIELDS:
                    if verified.get(field) != observed.get(field):
                        errors.append(
                            f"{item_id}: remote verification `{field}` differs "
                            "from baseline"
                        )

    return baseline_path, baseline, verification_path, verification


def validate_qa_data(
    post_dir: Path,
    article_path: Path,
    manifest_path: Path,
    loaded: dict[str, Any],
    errors: list[str],
    reviewed_root: str = "artifacts/qa/rendered",
    screenshot_root: str = "artifacts/qa",
    capture_mode: str = "creator",
) -> None:
    if type(loaded.get("version")) is not int or loaded.get("version") != 1:
        errors.append("rich-post QA `version` must be 1")
    checked_at = loaded.get("checked_at")
    if not isinstance(checked_at, str) or not DATE_RE.fullmatch(checked_at):
        errors.append("rich-post QA `checked_at` must use YYYY-MM-DD")
    checked_by = loaded.get("checked_by")
    if not isinstance(checked_by, str) or not checked_by.strip():
        errors.append("rich-post QA `checked_by` must name the actual reviewer")
    browser = loaded.get("browser")
    if not isinstance(browser, str) or not browser.strip():
        errors.append("rich-post QA `browser` must name the browser used")
    session = loaded.get("session")
    if not isinstance(session, str) or not session.strip():
        errors.append("rich-post QA `session` must identify the browser run")

    expected_hashes = {
        "article_content_sha256": article_content_sha256(article_path),
        "media_sha256": sha256_file(manifest_path),
        "renderer_sha256": sha256_file(
            SKILL_DIR / "scripts" / "render_rich_post.py"
        ),
        "css_sha256": sha256_file(SKILL_DIR / "assets" / "rich-post.css"),
        "markdown_renderer_sha256": sha256_file(
            REPO_ROOT / "scripts" / "md2tistory.py"
        ),
    }
    remote_media_path = post_dir / "artifacts" / "qa" / "remote-media.json"
    if remote_media_path.is_file():
        expected_hashes["remote_media_sha256"] = sha256_file(remote_media_path)
    else:
        errors.append("rich-post QA requires artifacts/qa/remote-media.json")
    for field, expected in expected_hashes.items():
        if loaded.get(field) != expected:
            errors.append(f"rich-post QA `{field}` does not match the current bundle")

    reviewed_markup: dict[str, str] = {}
    reviewed_paths: dict[str, Path] = {}
    for label, path_field, hash_field in (
        ("preview", "preview_path", "preview_sha256"),
        ("fragment", "fragment_path", "fragment_sha256"),
    ):
        relative_path = loaded.get(path_field)
        if not isinstance(relative_path, str) or not relative_path:
            errors.append(f"rich-post QA `{path_field}` must be a path")
            continue
        artifact_path = resolve_under(
            post_dir,
            relative_path,
            reviewed_root,
        )
        if artifact_path is None:
            errors.append(
                f"rich-post QA `{path_field}` must resolve under "
                f"{reviewed_root}/"
            )
        elif not artifact_path.is_file():
            errors.append(f"rich-post QA reviewed {label} file does not exist")
        else:
            if loaded.get(hash_field) != sha256_file(artifact_path):
                errors.append(f"rich-post QA `{hash_field}` does not match its file")
            try:
                reviewed_markup[label] = artifact_path.read_text(
                    encoding="utf-8"
                )
                reviewed_paths[label] = artifact_path
            except (OSError, UnicodeError) as exc:
                errors.append(
                    f"cannot read rich-post QA reviewed {label} file: {exc}"
                )

    preview_markup = reviewed_markup.get("preview")
    capture_receipt: dict[str, Any] = {}
    preview_path_for_capture = reviewed_paths.get("preview")
    if preview_path_for_capture is not None:
        capture_receipt_path, capture_receipt = (
            validate_browser_capture_receipt(
                post_dir,
                preview_path_for_capture,
                capture_mode,
                errors,
            )
        )
        if capture_receipt:
            expected_capture_fields = {
                "capture_receipt_path": capture_receipt_path.relative_to(
                    post_dir
                ).as_posix(),
                "capture_receipt_sha256": sha256_file(capture_receipt_path),
                "capture_tool_sha256": sha256_file(
                    SKILL_DIR / "scripts" / "capture_rich_qa.py"
                ),
                "checked_by": capture_receipt.get("checked_by"),
                "browser": capture_receipt.get("browser_version"),
                "session": capture_receipt.get("session"),
            }
            checked_at = capture_receipt.get("checked_at")
            if isinstance(checked_at, str):
                expected_capture_fields["checked_at"] = checked_at[:10]
            for field, expected in expected_capture_fields.items():
                if loaded.get(field) != expected:
                    errors.append(
                        f"rich-post QA `{field}` differs from browser capture"
                    )

    if preview_markup is not None:
        preview_media_source = loaded.get("preview_media_source")
        if preview_media_source != "remote":
            errors.append(
                "rich-post QA preview_media_source must be `remote`"
            )
        if loaded.get("preview_structure_sha256") != preview_structure_sha256(
            preview_markup
        ):
            errors.append(
                "rich-post QA `preview_structure_sha256` does not match "
                "the reviewed preview"
            )
        if len(re.findall(r"<h1\b", preview_markup, re.IGNORECASE)) != 1:
            errors.append("reviewed rich-post preview must contain exactly one H1")
        preview_path = reviewed_paths["preview"]
        preview_sources = re.findall(
            r'<img\b[^>]*\bsrc="([^"]+)"',
            preview_markup,
            re.IGNORECASE,
        )
        if not preview_sources:
            errors.append("reviewed rich-post preview must contain media")
        for source in preview_sources:
            decoded_source = html.unescape(source)
            if preview_media_source == "remote":
                if not is_tistory_media_url(decoded_source):
                    errors.append(
                        "reviewed rich-post preview image sources must use "
                        "allowed Tistory CDN URLs"
                    )
                continue
            parsed_source = urlparse(decoded_source)
            if parsed_source.scheme or parsed_source.netloc or parsed_source.path.startswith(
                "/"
            ):
                errors.append(
                    "reviewed rich-post preview image sources must be "
                    "bundle-relative paths"
                )
                continue
            preview_asset = (preview_path.parent / parsed_source.path).resolve()
            try:
                preview_relative = preview_asset.relative_to(post_dir.resolve())
            except ValueError:
                errors.append(
                    "reviewed rich-post preview image source escapes the bundle"
                )
                continue
            if not preview_relative.parts or preview_relative.parts[0] != "assets":
                errors.append(
                    "reviewed rich-post preview image source must resolve "
                    "under assets/"
                )
            elif not preview_asset.is_file():
                errors.append(
                    "reviewed rich-post preview image source does not exist"
                )

    fragment_markup = reviewed_markup.get("fragment")
    if fragment_markup is not None:
        if re.search(r"<h1\b", fragment_markup, re.IGNORECASE):
            errors.append("reviewed Tistory fragment must not contain an H1")
        if "__TISTORY_MEDIA_" in fragment_markup or "{{media:" in fragment_markup:
            errors.append("reviewed Tistory fragment contains a media placeholder")
        if re.search(
            r"(?:file://|/Users/|[A-Za-z]:\\\\)",
            fragment_markup,
        ):
            errors.append("reviewed Tistory fragment contains a local path")
        fragment_sources = re.findall(
            r'<img\b[^>]*\bsrc="([^"]+)"',
            fragment_markup,
            re.IGNORECASE,
        )
        if not fragment_sources or not all(
            is_tistory_media_url(source) for source in fragment_sources
        ):
            errors.append(
                "reviewed Tistory fragment image sources must use allowed "
                "Tistory CDN URLs"
            )

    viewports = loaded.get("viewports")
    if not isinstance(viewports, list):
        errors.append("rich-post QA `viewports` must be an array")
        viewports = []
    seen_widths: set[int] = set()
    seen_screenshot_paths: set[Path] = set()
    seen_screenshot_hashes: set[str] = set()
    captured_viewports = capture_receipt.get("viewports")
    if not isinstance(captured_viewports, list):
        captured_viewports = []
    captured_by_width = {
        viewport.get("width"): viewport
        for viewport in captured_viewports
        if isinstance(viewport, dict) and type(viewport.get("width")) is int
    }
    for index, viewport in enumerate(viewports):
        label = f"rich-post QA viewports[{index}]"
        if not isinstance(viewport, dict):
            errors.append(f"{label} must be an object")
            continue
        width = viewport.get("width")
        if type(width) is not int or width <= 0:
            errors.append(f"{label} `width` must be a positive integer")
            continue
        height = viewport.get("height")
        if type(height) is not int or height <= 0:
            errors.append(f"{label} `height` must be a positive integer")
        elif width in REQUIRED_VIEWPORTS and height != REQUIRED_VIEWPORTS[width]:
            errors.append(
                f"{label} height must equal {REQUIRED_VIEWPORTS[width]} "
                f"for required width {width}"
            )
        if width in seen_widths:
            errors.append(f"{label} duplicates width {width}")
        seen_widths.add(width)
        client_width = viewport.get("client_width")
        scroll_width = viewport.get("scroll_width")
        if client_width != width:
            errors.append(f"{label} client_width must equal {width}")
        if type(scroll_width) is not int or scroll_width != client_width:
            errors.append(f"{label} page overflow must be zero")
        if viewport.get("h1_count") != 1:
            errors.append(f"{label} preview must contain exactly one H1")
        if viewport.get("toc_targets_unique") is not True:
            errors.append(f"{label} TOC targets must be unique")
        if viewport.get("images_loaded") is not True:
            errors.append(f"{label} every remote image must decode in the browser")
        if viewport.get("readable_media") is not True:
            errors.append(f"{label} media must pass no-zoom reading review")
        if viewport.get("status") != "pass":
            errors.append(f"{label} status must be `pass`")
        captured_viewport = captured_by_width.get(width)
        if captured_viewport is None:
            errors.append(f"{label} has no matching browser capture")
        else:
            for field in CAPTURE_VIEWPORT_FIELDS:
                if viewport.get(field) != captured_viewport.get(field):
                    errors.append(
                        f"{label} `{field}` differs from browser capture"
                    )

        screenshot = viewport.get("screenshot")
        if not isinstance(screenshot, str) or not screenshot:
            errors.append(f"{label} must include a screenshot path")
            continue
        screenshot_path = resolve_under(post_dir, screenshot, screenshot_root)
        if screenshot_path is None:
            errors.append(
                f"{label} screenshot must resolve under {screenshot_root}/"
            )
        elif not screenshot_path.is_file():
            errors.append(f"{label} screenshot file does not exist")
        elif detected_kind(screenshot_path) not in {"png", "jpeg", "webp"}:
            errors.append(f"{label} screenshot must be a raster image")
        else:
            screenshot_kind = detected_kind(screenshot_path)
            container_error = image_container_error(
                screenshot_path,
                str(screenshot_kind),
            )
            if container_error:
                errors.append(f"{label} screenshot is malformed: {container_error}")
            if screenshot_path in seen_screenshot_paths:
                errors.append(
                    f"{label} screenshot path must be unique per viewport"
                )
            seen_screenshot_paths.add(screenshot_path)
            dimensions = image_dimensions(screenshot_path)
            if dimensions is None:
                errors.append(f"{label} screenshot dimensions cannot be read")
                continue
            if (
                viewport.get("screenshot_pixel_width") != dimensions[0]
                or viewport.get("screenshot_pixel_height") != dimensions[1]
            ):
                errors.append(
                    f"{label} recorded screenshot dimensions do not match its file"
                )
            screenshot_hash = sha256_file(screenshot_path)
            if viewport.get("screenshot_sha256") != screenshot_hash:
                errors.append(f"{label} screenshot_sha256 does not match its file")
            if screenshot_hash in seen_screenshot_hashes:
                errors.append(
                    f"{label} screenshot content must be unique per viewport"
                )
            seen_screenshot_hashes.add(screenshot_hash)
            if dimensions[0] < width or (
                type(height) is int and height > 0 and dimensions[1] < height
            ):
                errors.append(
                    f"{label} screenshot pixels must cover its CSS viewport"
                )

    missing_widths = set(REQUIRED_VIEWPORTS) - seen_widths
    if missing_widths:
        errors.append(
            "rich-post QA is missing required viewport widths: "
            + ", ".join(str(width) for width in sorted(missing_widths))
        )

    fragment = loaded.get("fragment")
    if not isinstance(fragment, dict):
        errors.append("rich-post QA `fragment` must be an object")
    else:
        expected_fragment = {
            "h1_count": 0,
            "unresolved_placeholders": 0,
            "local_paths": 0,
            "status": "pass",
        }
        for field, expected in expected_fragment.items():
            if fragment.get(field) != expected:
                errors.append(
                    f"rich-post QA fragment `{field}` must equal {expected!r}"
                )


def validate_qa_record(
    post_dir: Path,
    article_path: Path,
    manifest_path: Path,
    errors: list[str],
) -> tuple[Path, dict[str, Any]]:
    qa_path = post_dir / "artifacts" / "qa" / "rich-post.json"
    if not qa_path.is_file():
        errors.append("missing artifacts/qa/rich-post.json for paste-ready output")
        return qa_path, {}

    try:
        loaded = json.loads(qa_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as exc:
        errors.append(f"cannot read artifacts/qa/rich-post.json: {exc}")
        return qa_path, {}
    if not isinstance(loaded, dict):
        errors.append("artifacts/qa/rich-post.json root must be an object")
        return qa_path, {}

    validate_qa_data(
        post_dir,
        article_path,
        manifest_path,
        loaded,
        errors,
    )
    return qa_path, loaded


def validate_independent_data(
    post_dir: Path,
    article_path: Path,
    manifest_path: Path,
    manifest: dict[str, Any],
    creator_qa: dict[str, Any],
    loaded: dict[str, Any],
    errors: list[str],
) -> None:
    validate_qa_data(
        post_dir,
        article_path,
        manifest_path,
        loaded,
        errors,
        reviewed_root="artifacts/qa/independent-rendered",
        screenshot_root="artifacts/qa/independent",
        capture_mode="independent",
    )
    if loaded.get("result") != "pass":
        errors.append("independent final-page review result must be `pass`")
    remote_verification_path = (
        post_dir / "artifacts" / "qa" / "remote-media-verification.json"
    )
    if (
        not remote_verification_path.is_file()
        or loaded.get("remote_verification_sha256")
        != sha256_file(remote_verification_path)
    ):
        errors.append(
            "independent final-page remote_verification_sha256 does not "
            "match remote-media-verification.json"
        )
    elif remote_verification_path.is_file():
        remote_verification = _load_json_object(
            remote_verification_path,
            "artifacts/qa/remote-media-verification.json",
            errors,
        )
        if remote_verification:
            remote_reviewer = remote_verification.get("verified_by")
            page_reviewer = loaded.get("checked_by")
            if (
                isinstance(remote_reviewer, str)
                and isinstance(page_reviewer, str)
                and remote_reviewer.strip() != page_reviewer.strip()
            ):
                errors.append(
                    "independent final-page reviewer must match the "
                    "remote verifier"
                )

    creator_path = post_dir / "artifacts" / "qa" / "rich-post.json"
    if (
        not creator_path.is_file()
        or loaded.get("creator_qa_sha256") != sha256_file(creator_path)
    ):
        errors.append(
            "independent final-page creator_qa_sha256 does not match "
            "rich-post.json"
        )
    creator_reviewer = creator_qa.get("checked_by")
    independent_reviewer = loaded.get("checked_by")
    if (
        isinstance(creator_reviewer, str)
        and isinstance(independent_reviewer, str)
        and creator_reviewer.strip() == independent_reviewer.strip()
    ):
        errors.append(
            "independent final-page reviewer must differ from creator QA reviewer"
        )
    creator_session = creator_qa.get("session")
    independent_session = loaded.get("session")
    if (
        isinstance(creator_session, str)
        and isinstance(independent_session, str)
        and creator_session.strip() == independent_session.strip()
    ):
        errors.append(
            "independent final-page browser session must differ from creator QA"
        )

    checks = loaded.get("checks")
    if not isinstance(checks, dict):
        errors.append("independent final-page `checks` must be an object")
    else:
        for field in sorted(INDEPENDENT_BOOLEAN_CHECKS):
            if checks.get(field) is not True:
                errors.append(
                    f"independent final-page check `{field}` must be true"
                )
        manifest_items = manifest.get("items")
        if not isinstance(manifest_items, list):
            manifest_items = []
        has_gif = any(
            isinstance(item, dict) and item.get("kind") == "gif"
            for item in manifest_items
        )
        expected_gif_result = "pass" if has_gif else "not_applicable"
        for field in sorted(INDEPENDENT_GIF_CHECKS):
            if checks.get(field) != expected_gif_result:
                errors.append(
                    f"independent final-page check `{field}` must equal "
                    f"`{expected_gif_result}`"
                )

    creator_screenshots: set[Path] = set()
    creator_viewports = creator_qa.get("viewports")
    if not isinstance(creator_viewports, list):
        creator_viewports = []
    for viewport in creator_viewports:
        if not isinstance(viewport, dict):
            continue
        screenshot = viewport.get("screenshot")
        if isinstance(screenshot, str):
            path = resolve_under(post_dir, screenshot, "artifacts/qa")
            if path is not None:
                creator_screenshots.add(path)
    independent_viewports = loaded.get("viewports")
    if not isinstance(independent_viewports, list):
        independent_viewports = []
    for viewport in independent_viewports:
        if not isinstance(viewport, dict):
            continue
        screenshot = viewport.get("screenshot")
        if not isinstance(screenshot, str):
            continue
        path = resolve_under(post_dir, screenshot, "artifacts/qa/independent")
        if path is not None and path in creator_screenshots:
            errors.append(
                "independent final-page screenshots must use separate files"
            )


def validate_independent_review(
    post_dir: Path,
    article_path: Path,
    manifest_path: Path,
    manifest: dict[str, Any],
    creator_qa: dict[str, Any],
    errors: list[str],
) -> tuple[Path, dict[str, Any]]:
    review_path = (
        post_dir / "artifacts" / "qa" / "independent-final-page.json"
    )
    if not review_path.is_file():
        errors.append(
            "missing artifacts/qa/independent-final-page.json for ready output"
        )
        return review_path, {}

    try:
        loaded = json.loads(review_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as exc:
        errors.append(f"cannot read independent final-page review: {exc}")
        return review_path, {}
    if not isinstance(loaded, dict):
        errors.append("independent final-page review root must be an object")
        return review_path, {}

    validate_independent_data(
        post_dir,
        article_path,
        manifest_path,
        manifest,
        creator_qa,
        loaded,
        errors,
    )
    return review_path, loaded


def validate_bundle(
    post_dir: Path,
    require_publish_urls: bool = False,
    qa_record_override: dict[str, Any] | None = None,
    require_independent_pass: bool = False,
    require_remote_verification: bool = False,
) -> dict[str, Any]:
    post_dir = post_dir.resolve()
    article_path = post_dir / "article.md"
    manifest_path = post_dir / "media.json"
    evidence_path = post_dir / "evidence.md"
    capture_plan_path = post_dir / "capture-plan.md"
    errors: list[str] = []
    warnings: list[str] = []
    if require_independent_pass:
        require_publish_urls = True
        require_remote_verification = True
    if require_remote_verification:
        require_publish_urls = True

    if not article_path.is_file():
        errors.append("missing article.md")
        raw_article = ""
        meta: dict[str, Any] = {}
        body = ""
    else:
        try:
            raw_article = article_path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw_article)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"cannot read article.md: {exc}")
            raw_article = ""
            meta = {}
            body = ""

    publication_body = outside_fenced_text(body)
    if meta.get("format") != "rich-post":
        errors.append("article.md frontmatter must contain `format: rich-post`")
    slug = meta.get("slug")
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        errors.append("article.md frontmatter must contain a valid kebab-case `slug`")
    if meta.get("status") in {"ready", "published"}:
        require_publish_urls = True
        require_independent_pass = True
        require_remote_verification = True
    if re.search(r"(?m)^#\s+", publication_body):
        errors.append("article.md body must not contain a page-level H1")
    if re.search(
        r"!\[[^\]]*\]\((?:/|file:|[A-Za-z]:\\\\)",
        publication_body,
    ):
        errors.append("article.md contains a local filesystem image link")
    markdown_images = re.findall(
        r"!\[[^\]]*\]\([^)]+\)",
        publication_body,
    )
    if markdown_images:
        errors.append("rich posts must use `{{media:id}}` instead of Markdown images")

    all_tokens = ANY_DIRECTIVE_RE.findall(publication_body)
    directives = DIRECTIVE_RE.findall(publication_body)
    if len(all_tokens) != len(directives):
        errors.append("every media directive must be standalone and use a valid kebab-case ID")
    directive_counts = Counter(directives)
    for item_id, count in directive_counts.items():
        if count > 1:
            errors.append(f"{item_id}: media directive appears {count} times")

    if not manifest_path.is_file():
        errors.append("missing media.json")
        manifest: dict[str, Any] = {}
    else:
        try:
            loaded_manifest = json.loads(
                manifest_path.read_text(encoding="utf-8")
            )
            if not isinstance(loaded_manifest, dict):
                errors.append("media.json root must be an object")
                manifest = {}
            else:
                manifest = loaded_manifest
        except (json.JSONDecodeError, OSError, UnicodeError) as exc:
            errors.append(f"cannot read media.json: {exc}")
            manifest = {}

    if type(manifest.get("version")) is not int or manifest.get("version") != 1:
        errors.append("media.json `version` must be 1")
    items = manifest.get("items")
    if not isinstance(items, list) or not items:
        errors.append("media.json `items` must be a non-empty array")
        items = []

    items_by_id: dict[str, dict[str, Any]] = {}
    poster_ids: set[str] = set()
    all_claim_ids: set[str] = set()
    gif_info_by_id: dict[str, tuple[int, float]] = {}
    seen_tistory_urls: set[str] = set()
    for index, raw_item in enumerate(items):
        if not isinstance(raw_item, dict):
            errors.append(f"items[{index}] must be an object")
            continue
        item_id = raw_item.get("id")
        if not isinstance(item_id, str) or not ID_RE.fullmatch(item_id):
            errors.append(f"items[{index}]: invalid `id`")
            item_id = f"items[{index}]"
        elif item_id in items_by_id:
            errors.append(f"{item_id}: duplicate media ID")
        else:
            items_by_id[item_id] = raw_item

        kind = _required_string(raw_item, "kind", item_id, errors)
        origin = _required_string(raw_item, "origin", item_id, errors)
        role = _required_string(raw_item, "role", item_id, errors)
        status = _required_string(raw_item, "status", item_id, errors)
        if kind and kind not in KINDS:
            errors.append(f"{item_id}: unsupported kind `{kind}`")
        if origin and origin not in ORIGINS:
            errors.append(f"{item_id}: unsupported origin `{origin}`")
        if role and role not in ROLES:
            errors.append(f"{item_id}: unsupported role `{role}`")
        if status and status not in STATUSES:
            errors.append(f"{item_id}: unsupported status `{status}`")
        if status != "validated":
            message = f"{item_id}: status is `{status or 'missing'}`, not `validated`"
            (errors if require_publish_urls else warnings).append(message)
        if origin == "generated":
            if kind != "image":
                errors.append(f"{item_id}: generated media must use kind `image`")
            if role not in {"lead", "concept", "comparison"}:
                errors.append(
                    f"{item_id}: generated media cannot prove product action or state"
                )

        claim_ids = raw_item.get("claim_ids")
        if not isinstance(claim_ids, list) or not claim_ids or not all(
            isinstance(value, str) and value.strip() for value in claim_ids
        ):
            errors.append(f"{item_id}: `claim_ids` must be a non-empty string array")
        else:
            all_claim_ids.update(value.strip() for value in claim_ids)

        for field in (
            "alt",
            "caption",
            "placement",
            "rights",
            "publish_path",
            "sha256",
        ):
            _required_string(raw_item, field, item_id, errors)
        if (
            isinstance(raw_item.get("alt"), str)
            and isinstance(raw_item.get("caption"), str)
            and raw_item["alt"].strip() == raw_item["caption"].strip()
        ):
            errors.append(f"{item_id}: alt and caption must serve different purposes")
        for field in ("processing", "redactions"):
            if not isinstance(raw_item.get(field), list):
                errors.append(f"{item_id}: `{field}` must be an array")

        width, height = raw_item.get("width"), raw_item.get("height")
        if type(width) is not int or width <= 0:
            errors.append(f"{item_id}: `width` must be a positive integer")
        if type(height) is not int or height <= 0:
            errors.append(f"{item_id}: `height` must be a positive integer")
        display_width = raw_item.get("display_width")
        if display_width is not None and (
            type(display_width) is not int or not 240 <= display_width <= 916
        ):
            errors.append(f"{item_id}: `display_width` must be between 240 and 916")
        elif (
            type(display_width) is int
            and type(width) is int
            and width < display_width
        ):
            errors.append(
                f"{item_id}: source pixel width must cover display_width"
            )

        publish_path = raw_item.get("publish_path")
        publish_file: Path | None = None
        if isinstance(publish_path, str) and publish_path:
            publish_file = resolve_under(post_dir, publish_path, "assets")
            if publish_file is None:
                errors.append(f"{item_id}: publish_path must resolve under assets/")
            elif not publish_file.is_file():
                errors.append(f"{item_id}: publish file does not exist: {publish_path}")
            else:
                extension = publish_file.suffix.lower()
                if kind == "gif" and extension != ".gif":
                    errors.append(f"{item_id}: GIF media must use a .gif publish file")
                if kind in {"image", "screenshot"} and extension not in STATIC_EXTENSIONS:
                    errors.append(f"{item_id}: static media must be PNG, JPEG, or WebP")
                actual_kind = detected_kind(publish_file)
                if actual_kind is None:
                    errors.append(f"{item_id}: unrecognized image signature")
                elif extension == ".gif" and actual_kind != "gif":
                    errors.append(f"{item_id}: extension and GIF signature differ")
                elif extension == ".png" and actual_kind != "png":
                    errors.append(f"{item_id}: extension and PNG signature differ")
                elif extension in {".jpg", ".jpeg"} and actual_kind != "jpeg":
                    errors.append(f"{item_id}: extension and JPEG signature differ")
                elif extension == ".webp" and actual_kind != "webp":
                    errors.append(f"{item_id}: extension and WebP signature differ")
                if actual_kind is not None:
                    container_error = image_container_error(
                        publish_file,
                        actual_kind,
                    )
                    if container_error:
                        errors.append(
                            f"{item_id}: malformed publish image: "
                            f"{container_error}"
                        )
                digest = raw_item.get("sha256")
                if isinstance(digest, str) and SHA256_RE.fullmatch(digest):
                    if sha256_file(publish_file) != digest:
                        errors.append(f"{item_id}: sha256 does not match publish file")
                elif isinstance(digest, str) and digest:
                    errors.append(f"{item_id}: sha256 must be 64 lowercase hex characters")
                dimensions = image_dimensions(publish_file)
                if dimensions is None:
                    errors.append(f"{item_id}: cannot read image dimensions")
                elif type(width) is int and type(height) is int:
                    if dimensions != (width, height):
                        errors.append(
                            f"{item_id}: declared {width}x{height} differs from "
                            f"file {dimensions[0]}x{dimensions[1]}"
                        )
                if kind == "gif":
                    animation_info = gif_animation_info(publish_file)
                    if animation_info is None:
                        errors.append(f"{item_id}: cannot parse GIF animation")
                    else:
                        gif_info_by_id[item_id] = animation_info
                        if animation_info[0] < 2:
                            errors.append(
                                f"{item_id}: GIF must contain at least two frames"
                            )

        if origin in {"first_party", "simulated"}:
            captured_at = _required_string(raw_item, "captured_at", item_id, errors)
            _required_string(raw_item, "actor", item_id, errors)
            _required_string(raw_item, "environment", item_id, errors)
            raw_path = _required_string(raw_item, "raw_path", item_id, errors)
            if captured_at and not DATE_RE.fullmatch(captured_at):
                errors.append(f"{item_id}: captured_at must use YYYY-MM-DD")
            if raw_path:
                raw_file = resolve_under(post_dir, raw_path, "artifacts")
                if raw_file is None:
                    errors.append(
                        f"{item_id}: raw_path must resolve under artifacts/"
                    )
                elif kind == "gif" and resolve_under(
                    post_dir,
                    raw_path,
                    "artifacts/recordings",
                ) is None:
                    errors.append(
                        f"{item_id}: first-party GIF raw_path must be under "
                        "artifacts/recordings/"
                    )
                elif kind in {"image", "screenshot"} and resolve_under(
                    post_dir,
                    raw_path,
                    "artifacts/captures",
                ) is None:
                    errors.append(
                        f"{item_id}: first-party still raw_path must be under "
                        "artifacts/captures/"
                    )
                elif not raw_file.is_file():
                    errors.append(f"{item_id}: raw file does not exist: {raw_path}")
        source_url = raw_item.get("source_url", "")
        if source_url and (
            not isinstance(source_url, str) or not is_https_url(source_url)
        ):
            errors.append(f"{item_id}: source_url must be an HTTPS URL")
        if origin == "official" and not source_url:
            errors.append(f"{item_id}: official media requires source_url")

        tistory_url = raw_item.get("tistory_url", "")
        if tistory_url and (
            not isinstance(tistory_url, str)
            or not is_tistory_media_url(tistory_url)
        ):
            errors.append(
                f"{item_id}: tistory_url must be an allowed Tistory CDN URL"
            )
        elif isinstance(tistory_url, str) and tistory_url:
            if tistory_url in seen_tistory_urls:
                errors.append(f"{item_id}: tistory_url must be unique")
            seen_tistory_urls.add(tistory_url)
        if require_publish_urls and not tistory_url:
            errors.append(f"{item_id}: missing tistory_url for paste-ready output")

        if kind == "gif":
            poster_id = _required_string(raw_item, "poster_id", item_id, errors)
            if poster_id:
                poster_ids.add(poster_id)
            duration = raw_item.get("duration_seconds")
            if (
                isinstance(duration, bool)
                or not isinstance(duration, (int, float))
                or duration <= 0
            ):
                errors.append(f"{item_id}: GIF duration_seconds must be positive")
            elif duration > 5:
                errors.append(
                    f"{item_id}: GIF exceeds five seconds; shorten it or use "
                    "a static sequence"
                )
            animation_info = gif_info_by_id.get(item_id)
            if (
                animation_info is not None
                and isinstance(duration, (int, float))
                and not isinstance(duration, bool)
                and abs(animation_info[1] - duration) > 0.051
            ):
                errors.append(
                    f"{item_id}: declared GIF duration {duration:g}s differs "
                    f"from file duration {animation_info[1]:g}s"
                )

    lead_id = manifest.get("lead_id")
    if not isinstance(lead_id, str) or lead_id not in items_by_id:
        errors.append("media.json `lead_id` must reference a registered item")
    else:
        lead = items_by_id[lead_id]
        if lead.get("kind") == "gif":
            errors.append("lead media cannot be a GIF")
        if lead.get("role") != "lead":
            errors.append("lead media item must use role `lead`")
        if lead_id not in directive_counts:
            errors.append("lead media must appear in article.md")
        hero_image = meta.get("hero_image")
        if hero_image != lead.get("publish_path"):
            message = "article.md hero_image must match media.json lead publish_path"
            (errors if require_publish_urls else warnings).append(message)

    lead_role_ids = [
        item_id
        for item_id, item in items_by_id.items()
        if item.get("role") == "lead"
    ]
    if len(lead_role_ids) != 1 or lead_role_ids[0] != lead_id:
        errors.append("exactly one media item must use role `lead` and match lead_id")

    for poster_id in poster_ids:
        poster = items_by_id.get(poster_id)
        if poster is None:
            errors.append(f"{poster_id}: GIF poster is not registered")
        elif poster.get("kind") == "gif":
            errors.append(f"{poster_id}: GIF poster must be static")
        else:
            if poster.get("role") != "poster":
                errors.append(f"{poster_id}: GIF poster must use role `poster`")
            if poster_id in directive_counts:
                errors.append(f"{poster_id}: GIF poster must not have an article directive")
            for item in items_by_id.values():
                if item.get("poster_id") != poster_id:
                    continue
                if poster.get("derived_from") != item.get("id"):
                    errors.append(
                        f"{poster_id}: GIF poster derived_from must reference "
                        f"{item.get('id')}"
                    )
                if poster.get("origin") != item.get("origin"):
                    errors.append(
                        f"{poster_id}: GIF poster origin must match its GIF"
                    )
                if poster.get("source_url", "") != item.get("source_url", ""):
                    errors.append(
                        f"{poster_id}: GIF poster source_url must match its GIF"
                    )
                if poster.get("rights") != item.get("rights"):
                    errors.append(
                        f"{poster_id}: GIF poster rights must match its GIF"
                    )
                poster_processing = poster.get("processing")
                if (
                    not isinstance(poster_processing, list)
                    or "frame_extract" not in poster_processing
                ):
                    errors.append(
                        f"{poster_id}: GIF poster processing must record "
                        "`frame_extract`"
                    )
                gif_width, gif_height = item.get("width"), item.get("height")
                poster_width, poster_height = (
                    poster.get("width"),
                    poster.get("height"),
                )
                if all(
                    type(value) is int
                    for value in (
                        gif_width,
                        gif_height,
                        poster_width,
                        poster_height,
                    )
                ) and (gif_width, gif_height) != (
                    poster_width,
                    poster_height,
                ):
                    errors.append(
                        f"{poster_id}: poster and GIF must use identical dimensions"
                    )
                if poster.get("display_width") != item.get("display_width"):
                    errors.append(
                        f"{poster_id}: poster and GIF display_width must match"
                    )

    for item_id in directives:
        if item_id not in items_by_id:
            errors.append(f"{item_id}: article directive is not registered")
    used_ids = set(directives) | poster_ids
    for item_id in items_by_id:
        if item_id not in used_ids:
            errors.append(f"{item_id}: registered media is unused")

    if not capture_plan_path.is_file():
        errors.append("missing capture-plan.md")
    if not evidence_path.is_file():
        errors.append("missing evidence.md")
    else:
        try:
            evidence_text = evidence_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read evidence.md: {exc}")
            evidence_text = ""
        registered_claims = {
            match
            for match in re.findall(
                r"(?m)^\|\s*([A-Za-z][A-Za-z0-9-]*)\s*\|",
                evidence_text,
            )
            if match != "ID"
        }
        for claim_id in sorted(all_claim_ids - registered_claims):
            errors.append(f"{claim_id}: media claim is not registered in evidence.md")

    remote_media_path = post_dir / "artifacts" / "qa" / "remote-media.json"
    remote_media: dict[str, Any] = {}
    remote_verification_path = (
        post_dir / "artifacts" / "qa" / "remote-media-verification.json"
    )
    remote_verification: dict[str, Any] = {}
    if require_publish_urls and manifest_path.is_file():
        (
            remote_media_path,
            remote_media,
            remote_verification_path,
            remote_verification,
        ) = validate_remote_media_records(
            post_dir,
            manifest_path,
            manifest,
            errors,
            require_verification=require_remote_verification,
        )

    qa_path = post_dir / "artifacts" / "qa" / "rich-post.json"
    qa_record: dict[str, Any] = {}
    if require_publish_urls and article_path.is_file() and manifest_path.is_file():
        if qa_record_override is None:
            qa_path, qa_record = validate_qa_record(
                post_dir,
                article_path,
                manifest_path,
                errors,
            )
        else:
            if not isinstance(qa_record_override, dict):
                errors.append("rich-post QA override root must be an object")
            else:
                qa_record = qa_record_override
                validate_qa_data(
                    post_dir,
                    article_path,
                    manifest_path,
                    qa_record,
                    errors,
                )

    independent_review_path = (
        post_dir / "artifacts" / "qa" / "independent-final-page.json"
    )
    independent_review: dict[str, Any] = {}
    if (
        require_independent_pass
        and article_path.is_file()
        and manifest_path.is_file()
        and qa_record
    ):
        independent_review_path, independent_review = (
            validate_independent_review(
                post_dir,
                article_path,
                manifest_path,
                manifest,
                qa_record,
                errors,
            )
        )

    return {
        "post_dir": post_dir,
        "article_path": article_path,
        "manifest_path": manifest_path,
        "evidence_path": evidence_path,
        "capture_plan_path": capture_plan_path,
        "qa_path": qa_path,
        "qa_record": qa_record,
        "remote_media_path": remote_media_path,
        "remote_media": remote_media,
        "remote_verification_path": remote_verification_path,
        "remote_verification": remote_verification,
        "independent_review_path": independent_review_path,
        "independent_review": independent_review,
        "meta": meta,
        "body": body,
        "manifest": manifest,
        "items_by_id": items_by_id,
        "directives": directives,
        "errors": errors,
        "warnings": warnings,
        "require_publish_urls": require_publish_urls,
        "require_independent_pass": require_independent_pass,
        "require_remote_verification": require_remote_verification,
    }
