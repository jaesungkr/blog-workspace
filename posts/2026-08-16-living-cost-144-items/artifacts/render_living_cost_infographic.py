#!/usr/bin/env python3
"""Render the deterministic supporting infographic for the 144-item analysis."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "assets" / "living-cost-144-overview-v3.png"
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

W, H = 1080, 1350
SCALE = 2

BG = "#F5F1E9"
INK = "#202B2D"
MUTED = "#657174"
GRID = "#D9D2C6"
UP = "#E45C3A"
UP_DARK = "#A93B28"
DOWN = "#297A86"
FLAT = "#A8A49B"
CREAM = "#FFFDF8"


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size * SCALE, index=index)


def xy(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value * SCALE for value in values)


def text(draw: ImageDraw.ImageDraw, pos: tuple[int, int], value: str, size: int, fill: str = INK, anchor: str = "la") -> None:
    draw.text(xy(pos), value, font=font(size), fill=fill, anchor=anchor)


def rounded_line(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: str, width: int) -> None:
    scaled = [xy(point) for point in points]
    draw.line(scaled, fill=fill, width=width * SCALE, joint="curve")
    radius = width * SCALE // 2
    for px, py in (scaled[0], scaled[-1]):
        draw.ellipse((px - radius, py - radius, px + radius, py + radius), fill=fill)


def main() -> None:
    image = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    draw = ImageDraw.Draw(image)

    # Header: 205px high (15.2% of canvas).
    text(draw, (72, 74), "144개 중 98개 상승", 62)
    text(draw, (72, 150), "높이 뛴 품목과 넓게 오른 지출은 체감이 다릅니다", 38, MUTED)
    draw.line(xy((72, 205, 1008, 205)), fill=GRID, width=2 * SCALE)

    # One 12×12 field: every dot represents one of the 144 detailed items.
    dot_left, dot_top = 84, 270
    pitch, radius = 43, 13
    for idx in range(144):
        row, col = divmod(idx, 12)
        cx = dot_left + col * pitch
        cy = dot_top + row * pitch
        color = UP if idx < 98 else DOWN if idx < 136 else FLAT
        draw.ellipse(xy((cx - radius, cy - radius, cx + radius, cy + radius)), fill=color)

    # Open legend beside the distribution; no enclosing card.
    legend_x = 670
    legend = [
        (UP, "오른 품목", "98개 · 68.1%"),
        (DOWN, "내린 품목", "38개 · 26.4%"),
        (FLAT, "변동 없음", "8개 · 5.6%"),
    ]
    for i, (color, label, value) in enumerate(legend):
        cy = 326 + i * 132
        draw.ellipse(xy((legend_x, cy - 15, legend_x + 30, cy + 15)), fill=color)
        text(draw, (legend_x + 52, cy - 20), label, 46)
        text(draw, (legend_x + 52, cy + 36), value, 38, MUTED)

    text(draw, (670, 708), "5% 이상 상승", 38, MUTED)
    text(draw, (670, 758), "16개", 46, UP_DARK)

    draw.line(xy((72, 820, 1008, 820)), fill=GRID, width=2 * SCALE)

    # Left: magnitude is carried by three measured bars.
    text(draw, (72, 882), "높이 뛴 품목", 46)
    base_y = 1192
    bar_data = [("경유", 21.5), ("파", 18.3), ("보험서비스료", 13.4)]
    bar_x = [112, 266, 420]
    for x, (label, value) in zip(bar_x, bar_data):
        height = int(value / 22.0 * 205)
        rounded_line(draw, [(x, base_y), (x, base_y - height)], UP, 22)
        text(draw, (x, base_y - height - 32), f"+{value:.1f}%", 38, UP_DARK, "ms")
        text(draw, (x, base_y + 42), label, 38, INK, "ma")

    # Right: breadth is carried by twenty identical marks, all active.
    text(draw, (618, 882), "넓게 오른 외식", 46)
    for idx in range(20):
        row, col = divmod(idx, 4)
        cx = 630 + col * 52
        cy = 956 + row * 52
        draw.ellipse(xy((cx - 14, cy - 14, cx + 14, cy + 14)), fill=UP)
    text(draw, (998, 1000), "20 / 20", 46, UP_DARK, "ra")
    text(draw, (998, 1058), "전 품목 상승", 38, MUTED, "ra")
    text(draw, (998, 1134), "중앙값", 38, MUTED, "ra")
    text(draw, (998, 1192), "+3.1%", 46, INK, "ra")

    # The caveat changes how the visual may be interpreted, so it stays.
    draw.line(xy((72, 1272, 1008, 1272)), fill=GRID, width=2 * SCALE)
    text(draw, (72, 1312), "품목 수와 중앙값은 지출 가중치를 적용하지 않은 분포 비교입니다", 34, MUTED, "lm")

    image = image.resize((W, H), Image.Resampling.LANCZOS)
    image.save(OUTPUT, optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
