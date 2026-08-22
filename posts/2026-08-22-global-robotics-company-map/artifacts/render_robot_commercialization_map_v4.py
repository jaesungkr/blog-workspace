#!/usr/bin/env python3
"""Render an open, rule-free commercialization map with optical spacing (v4)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "assets" / "robot-commercialization-map-v4.png"
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

W, H = 1080, 1320
SCALE = 2

BG = "#F3EFE7"
PAPER = "#FBF8F1"
INK = "#202A2B"
MUTED = "#697376"
HAIRLINE = "#D7D0C4"
TEAL = "#176B70"
TEAL_MID = "#65A5A1"
TEAL_PALE = "#C7DEDA"
ORANGE = "#D9693A"
ORANGE_MID = "#E5A47E"
ORANGE_PALE = "#F0D7C7"


def xy(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value * SCALE for value in values)


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size * SCALE, index=index)


def text(
    draw: ImageDraw.ImageDraw,
    pos: tuple[int, int],
    value: str,
    size: int,
    fill: str = INK,
    anchor: str = "la",
) -> None:
    draw.text(xy(pos), value, font=font(size), fill=fill, anchor=anchor)


def source_text_box(
    draw: ImageDraw.ImageDraw,
    pos: tuple[int, int],
    value: str,
    size: int,
    anchor: str = "la",
) -> tuple[float, float, float, float]:
    box = draw.textbbox(xy(pos), value, font=font(size), anchor=anchor)
    return tuple(value / SCALE for value in box)


def assert_vertical_clearance(
    draw: ImageDraw.ImageDraw,
    upper: tuple[tuple[int, int], str, int],
    lower: tuple[tuple[int, int], str, int],
    minimum: int,
) -> float:
    upper_box = source_text_box(draw, upper[0], upper[1], upper[2])
    lower_box = source_text_box(draw, lower[0], lower[1], lower[2])
    gap = lower_box[1] - upper_box[3]
    assert gap >= minimum, (upper[1], lower[1], gap, minimum)
    return gap


def assert_region_clearance(name: str, upper_bound: int, lower_bound: int, minimum: int) -> int:
    """Guard optical space between complete painted scene envelopes."""
    gap = lower_bound - upper_bound
    assert gap >= minimum, (name, gap, minimum)
    return gap


def line(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: str, width: int) -> None:
    draw.line([xy(point) for point in points], fill=fill, width=width * SCALE, joint="curve")


def dot(draw: ImageDraw.ImageDraw, x: int, y: int, radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.ellipse(
        xy((x - radius, y - radius, x + radius, y + radius)),
        fill=fill,
        outline=outline,
        width=width * SCALE,
    )


def rounded_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(
        xy(box),
        radius=radius * SCALE,
        fill=fill,
        outline=outline,
        width=width * SCALE,
    )


def draw_factory_scene(draw: ImageDraw.ImageDraw) -> None:
    # Repeated rails occupy the scene; text lives only in the upper-right quiet area.
    for y in (236, 280, 324, 368):
        line(draw, [(116, y), (570, y)], TEAL_PALE, 5)
    for x in (142, 244, 346, 448, 550):
        line(draw, [(x, 218), (x, 386)], HAIRLINE, 3)
    for x, y in ((244, 236), (346, 280), (448, 324), (550, 368)):
        rounded_rect(draw, (x - 20, y - 20, x + 20, y + 20), 7, ORANGE)

    # Grounded industrial arm with a clear two-jaw gripper.
    rounded_rect(draw, (114, 344, 204, 375), 10, TEAL)
    line(draw, [(158, 344), (198, 286), (285, 313)], TEAL, 20)
    dot(draw, 198, 286, 15, PAPER, TEAL, 6)
    dot(draw, 285, 313, 12, PAPER, TEAL, 5)
    line(draw, [(285, 313), (322, 342)], TEAL, 14)
    line(draw, [(322, 342), (344, 328)], TEAL, 6)
    line(draw, [(322, 342), (346, 354)], TEAL, 6)

    # Low warehouse carrier reinforces the second mature specialization.
    rounded_rect(draw, (408, 334, 522, 375), 13, INK)
    rounded_rect(draw, (426, 306, 504, 340), 6, ORANGE_PALE, ORANGE_MID, 2)
    dot(draw, 433, 378, 8, TEAL)
    dot(draw, 497, 378, 8, TEAL)


def draw_repeat_scene(draw: ImageDraw.ImageDraw) -> None:
    # A bounded but less rigid route carries specialized service and inspection work.
    line(draw, [(520, 495), (612, 460), (714, 496), (818, 455), (956, 500)], TEAL_PALE, 22)
    line(draw, [(520, 495), (612, 460), (714, 496), (818, 455), (956, 500)], TEAL, 5)
    for x, y in ((520, 495), (612, 460), (714, 496), (818, 455), (956, 500)):
        dot(draw, x, y, 8, ORANGE)

    # Precision target and compact inspection quadruped.
    dot(draw, 792, 578, 62, PAPER, TEAL_MID, 6)
    dot(draw, 792, 578, 22, ORANGE)
    line(draw, [(870, 530), (835, 552), (810, 570)], TEAL, 13)
    dot(draw, 835, 552, 10, PAPER, TEAL, 4)
    rounded_rect(draw, (572, 570, 656, 608), 10, TEAL)
    line(draw, [(588, 605), (570, 634)], TEAL, 8)
    line(draw, [(610, 605), (600, 638)], TEAL, 8)
    line(draw, [(638, 605), (650, 638)], TEAL, 8)


def draw_validation_scene(draw: ImageDraw.ImageDraw) -> None:
    # One evidenced branch is solid; other possible tasks remain pale.
    line(draw, [(132, 764), (286, 764), (394, 718)], TEAL, 8)
    line(draw, [(286, 764), (405, 828)], ORANGE_MID, 7)
    line(draw, [(286, 764), (302, 874)], TEAL_PALE, 7)

    # Humanoid carrying one tote: a narrow proven task, not generic capability.
    dot(draw, 232, 731, 18, TEAL)
    line(draw, [(232, 750), (232, 811)], TEAL, 14)
    line(draw, [(232, 769), (190, 791)], TEAL, 10)
    line(draw, [(232, 770), (267, 792)], TEAL, 10)
    line(draw, [(232, 811), (202, 852)], TEAL, 10)
    line(draw, [(232, 811), (262, 852)], TEAL, 10)
    rounded_rect(draw, (151, 780, 196, 818), 6, ORANGE)


def dashed_line(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: str, width: int) -> None:
    # Simple deterministic dashed polyline for announced or planned routes.
    for start, end in zip(points, points[1:]):
        x1, y1 = start
        x2, y2 = end
        steps = 12
        for i in range(0, steps, 2):
            a = i / steps
            b = min((i + 1) / steps, 1)
            xa = round(x1 + (x2 - x1) * a)
            ya = round(y1 + (y2 - y1) * a)
            xb = round(x1 + (x2 - x1) * b)
            yb = round(y1 + (y2 - y1) * b)
            line(draw, [(xa, ya), (xb, yb)], fill, width)


def draw_planning_scene(draw: ImageDraw.ImageDraw) -> None:
    root = (790, 998)
    branches = [
        [root, (700, 1050), (618, 1118)],
        [root, (760, 1070), (738, 1140)],
        [root, (835, 1068), (842, 1144)],
        [root, (902, 1048), (970, 1110)],
    ]
    for points in branches:
        dashed_line(draw, points, ORANGE_MID, 7)
        x, y = points[-1]
        dot(draw, x, y, 9, PAPER, ORANGE, 4)

    # Incomplete outline expresses a product path without implying field operation.
    dot(draw, 790, 962, 19, PAPER, TEAL, 6)
    line(draw, [(790, 983), (790, 1038)], TEAL_MID, 10)
    line(draw, [(790, 1003), (756, 1024)], TEAL_MID, 8)
    line(draw, [(790, 1003), (824, 1024)], TEAL_MID, 8)
    line(draw, [(790, 1038), (766, 1075)], TEAL_PALE, 8)
    line(draw, [(790, 1038), (814, 1075)], TEAL_PALE, 8)


def main() -> None:
    image = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    draw = ImageDraw.Draw(image)

    # One compact headline; no subtitle block.
    text(draw, (72, 70), "로봇 상용화의 지형", 56)
    text(draw, (1008, 77), "반복 운영 깊음", 28, TEAL, "ra")
    # A single environmental axis and four quiet nodes replace horizontal rules.
    line(draw, [(72, 188), (72, 1180)], HAIRLINE, 4)
    line(draw, [(72, 1180), (59, 1162)], HAIRLINE, 4)
    line(draw, [(72, 1180), (85, 1162)], HAIRLINE, 4)
    for y, color in ((300, TEAL), (540, TEAL_MID), (790, ORANGE_MID), (1040, ORANGE)):
        dot(draw, 72, y, 7, color)
    text(draw, (96, 185), "정돈된 환경", 28, TEAL, "lm")
    text(draw, (96, 1185), "열린 환경", 28, ORANGE, "lm")

    # Alternating visual/label placement prevents a slide-like two-column grid.
    draw_factory_scene(draw)
    text(draw, (622, 226), "대규모 운영", 40)
    text(draw, (622, 306), "FANUC · Amazon · Intuitive", 30, TEAL)

    text(draw, (122, 480), "반복 상용", 40)
    text(draw, (122, 560), "Pudu · ANYbotics · Agility", 30, TEAL)
    draw_repeat_scene(draw)

    draw_validation_scene(draw)
    text(draw, (560, 760), "초기 상용·고객 검증", 40)
    text(draw, (560, 840), "Figure · UBTECH", 30, ORANGE)

    text(draw, (122, 970), "개발·사전 주문", 40)
    text(draw, (122, 1050), "Atlas · Tesla · Apptronik", 30, ORANGE)
    text(draw, (122, 1102), "Unitree · 1X", 30, ORANGE)
    draw_planning_scene(draw)

    text(draw, (72, 1272), "분야 순위가 아니라 공개된 반복 운영 근거의 깊이", 28, MUTED, "lm")

    # Release-blocking spacing assertions use painted glyph bounds, not baselines.
    gaps = [
        assert_vertical_clearance(draw, ((622, 226), "대규모 운영", 40), ((622, 306), "FANUC · Amazon · Intuitive", 30), 28),
        assert_vertical_clearance(draw, ((122, 480), "반복 상용", 40), ((122, 560), "Pudu · ANYbotics · Agility", 30), 28),
        assert_vertical_clearance(draw, ((560, 760), "초기 상용·고객 검증", 40), ((560, 840), "Figure · UBTECH", 30), 28),
        assert_vertical_clearance(draw, ((122, 970), "개발·사전 주문", 40), ((122, 1050), "Atlas · Tesla · Apptronik", 30), 28),
        assert_vertical_clearance(draw, ((122, 1050), "Atlas · Tesla · Apptronik", 30), ((122, 1102), "Unitree · 1X", 30), 18),
    ]
    region_gaps = [
        assert_region_clearance("factory-to-repeat", 386, 444, 48),
        assert_region_clearance("repeat-to-validation", 642, 713, 48),
        assert_region_clearance("validation-to-planning", 878, 943, 48),
        assert_region_clearance("planning-to-footer", 1153, 1255, 72),
    ]

    image = image.resize((W, H), Image.Resampling.LANCZOS)
    image.save(OUTPUT, optimize=True)
    print(OUTPUT)
    print("painted vertical gaps:", ", ".join(f"{gap:.1f}px" for gap in gaps))
    print("scene envelope gaps:", ", ".join(f"{gap}px" for gap in region_gaps))


if __name__ == "__main__":
    main()
