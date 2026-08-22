#!/usr/bin/env python3
"""Render the deterministic commercialization map for the global robotics post."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "assets" / "robot-commercialization-map-v2.png"
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

W, H = 1080, 1350
SCALE = 2

BG = "#F4F0E8"
INK = "#202A2B"
MUTED = "#687275"
GRID = "#D8D1C5"
TEAL = "#1E6A70"
TEAL_LIGHT = "#8AB7B2"
ORANGE = "#D96B3B"
ORANGE_LIGHT = "#EAB18F"
CREAM = "#FFFCF5"


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size * SCALE, index=index)


def xy(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value * SCALE for value in values)


def text(
    draw: ImageDraw.ImageDraw,
    pos: tuple[int, int],
    value: str,
    size: int,
    fill: str = INK,
    anchor: str = "la",
) -> None:
    draw.text(xy(pos), value, font=font(size), fill=fill, anchor=anchor)


def line(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    fill: str,
    width: int,
) -> None:
    draw.line([xy(point) for point in points], fill=fill, width=width * SCALE, joint="curve")


def circle(draw: ImageDraw.ImageDraw, cx: int, cy: int, radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.ellipse(
        xy((cx - radius, cy - radius, cx + radius, cy + radius)),
        fill=fill,
        outline=outline,
        width=width * SCALE,
    )


def draw_structured_track(draw: ImageDraw.ImageDraw, top: int, bottom: int) -> None:
    """A rigid rail and repeated workpiece field for scaled operation."""
    for x in (118, 184, 250, 316):
        line(draw, [(x, top), (x, bottom)], TEAL_LIGHT, 4)
    for y in (top + 36, top + 96, top + 156):
        line(draw, [(104, y), (330, y)], GRID, 3)
    for x, y in ((151, top + 36), (217, top + 96), (283, top + 156)):
        draw.rounded_rectangle(xy((x - 19, y - 19, x + 19, y + 19)), radius=6 * SCALE, fill=ORANGE)
    # Articulated arm: grounded base, two links, visible gripper.
    draw.rounded_rectangle(xy((94, bottom - 45, 154, bottom - 25)), radius=7 * SCALE, fill=TEAL)
    line(draw, [(124, bottom - 45), (154, bottom - 91), (211, bottom - 70)], TEAL, 15)
    circle(draw, 154, bottom - 91, 12, CREAM, TEAL, 5)
    line(draw, [(211, bottom - 70), (235, bottom - 50)], TEAL, 11)
    line(draw, [(235, bottom - 50), (250, bottom - 62)], TEAL, 6)
    line(draw, [(235, bottom - 50), (252, bottom - 42)], TEAL, 6)


def draw_repeat_track(draw: ImageDraw.ImageDraw, top: int, bottom: int) -> None:
    """A controlled route with one precision loop and one field detour."""
    line(draw, [(126, top + 20), (126, bottom - 30)], TEAL_LIGHT, 4)
    line(draw, [(312, top + 20), (312, bottom - 30)], TEAL_LIGHT, 4)
    # Precision target and fine manipulator.
    circle(draw, 184, top + 92, 45, CREAM, TEAL, 5)
    circle(draw, 184, top + 92, 18, ORANGE)
    line(draw, [(245, top + 31), (220, top + 58), (198, top + 83)], TEAL, 10)
    circle(draw, 220, top + 58, 9, CREAM, TEAL, 4)
    # A mobile inspection route is bounded, but no longer perfectly straight.
    line(draw, [(145, bottom - 58), (188, bottom - 82), (239, bottom - 54), (292, bottom - 78)], ORANGE_LIGHT, 9)
    for x, y in ((145, bottom - 58), (188, bottom - 82), (239, bottom - 54), (292, bottom - 78)):
        circle(draw, x, y, 8, ORANGE)


def draw_customer_validation(draw: ImageDraw.ImageDraw, top: int, bottom: int) -> None:
    """A human-shaped worker following one proven branch while alternatives remain open."""
    root = (218, top + 20)
    line(draw, [root, (218, top + 76), (160, top + 134), (136, bottom - 30)], TEAL_LIGHT, 5)
    line(draw, [(218, top + 76), (276, top + 134), (304, bottom - 28)], ORANGE_LIGHT, 5)
    line(draw, [(218, top + 76), (218, bottom - 26)], GRID, 4)
    # Small neutral humanoid carrying a tote on the evidenced branch.
    circle(draw, 159, top + 108, 14, TEAL)
    line(draw, [(159, top + 123), (159, top + 169)], TEAL, 11)
    line(draw, [(159, top + 139), (129, top + 154)], TEAL, 8)
    line(draw, [(159, top + 139), (186, top + 153)], TEAL, 8)
    line(draw, [(159, top + 169), (140, top + 196)], TEAL, 8)
    line(draw, [(159, top + 169), (178, top + 196)], TEAL, 8)
    draw.rounded_rectangle(xy((111, top + 149, 142, top + 174)), radius=4 * SCALE, fill=ORANGE)


def draw_open_branches(draw: ImageDraw.ImageDraw, top: int, bottom: int) -> None:
    """Unconfirmed paths spread outward; the central robot is intentionally incomplete."""
    line(draw, [(218, top + 18), (218, top + 76)], GRID, 5)
    branches = [
        [(218, top + 76), (148, top + 124), (102, bottom - 25)],
        [(218, top + 76), (183, top + 146), (165, bottom - 24)],
        [(218, top + 76), (248, top + 150), (250, bottom - 22)],
        [(218, top + 76), (302, top + 124), (337, bottom - 28)],
    ]
    for points in branches:
        line(draw, points, ORANGE_LIGHT, 5)
        x, y = points[-1]
        circle(draw, x, y, 7, ORANGE)
    # Incomplete humanoid: open torso outline, no heroic pose.
    circle(draw, 218, top + 63, 14, TEAL)
    line(draw, [(218, top + 80), (218, top + 125)], TEAL, 9)
    line(draw, [(218, top + 92), (194, top + 112)], TEAL, 7)
    line(draw, [(218, top + 92), (242, top + 112)], TEAL, 7)
    line(draw, [(218, top + 125), (201, top + 151)], TEAL_LIGHT, 6)
    line(draw, [(218, top + 125), (235, top + 151)], TEAL_LIGHT, 6)


def main() -> None:
    image = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    draw = ImageDraw.Draw(image)

    # Header: 205px, 15.2% of the canvas.
    text(draw, (72, 70), "로봇은 어디까지 상용화됐나", 62)
    text(draw, (72, 145), "환경이 열릴수록 반복 운영의 근거는 아직 얕습니다", 38, MUTED)
    draw.line(xy((72, 205, 1008, 205)), fill=GRID, width=2 * SCALE)

    # Small reading anchors. The relationship is carried by the changing track itself.
    text(draw, (104, 244), "정돈된 환경", 34, TEAL)
    text(draw, (430, 244), "상용화 깊이", 34, MUTED)

    stages = [
        (264, 474, "대규모 운영", "산업용 · 물류 · 수술", "FANUC · ABB · Amazon · Intuitive", TEAL),
        (486, 696, "반복 상용", "서비스 · 농업 · 점검 · 좁은 유료 작업", "Pudu · John Deere · ANYbotics\nAgility", TEAL),
        (708, 918, "초기 상용·고객 검증", "생산 현장 · 소량 판매, 운영 지표 미공개", "Figure · UBTECH", ORANGE),
        (930, 1140, "개발·사전 주문", "배치 발표 · 파일럿 계획 · 하드웨어 판매", "Boston Dynamics · Tesla · Apptronik\nUnitree · 1X", ORANGE),
    ]

    for i, (top, bottom, title, scope, companies, color) in enumerate(stages):
        if i:
            draw.line(xy((72, top - 8, 1008, top - 8)), fill=GRID, width=2 * SCALE)
        circle(draw, 395, top + 36, 7, color)
        text(draw, (430, top + 13), title, 48)
        text(draw, (430, top + 76), scope, 38, MUTED)
        for j, company_line in enumerate(companies.split("\n")):
            text(draw, (430, top + 130 + j * 45), company_line, 36, color)

    draw_structured_track(draw, 272, 462)
    draw_repeat_track(draw, 494, 684)
    draw_customer_validation(draw, 716, 906)
    draw_open_branches(draw, 938, 1128)

    text(draw, (104, 1188), "열린 환경", 34, ORANGE)
    line(draw, [(218, 1162), (218, 1191)], GRID, 4)
    line(draw, [(218, 1191), (206, 1178)], GRID, 4)
    line(draw, [(218, 1191), (230, 1178)], GRID, 4)

    draw.line(xy((72, 1242, 1008, 1242)), fill=GRID, width=2 * SCALE)
    text(draw, (72, 1294), "2026년 8월 공개 자료 기준 · 실제 반복 운영과 발표된 계획을 구분", 34, MUTED, "lm")

    image = image.resize((W, H), Image.Resampling.LANCZOS)
    image.save(OUTPUT, optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
