#!/usr/bin/env python3
"""Render the China AI three-signal infographic as a deterministic PNG."""

from pathlib import Path
from math import atan2, cos, pi, sin

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "china-ai-three-signals-v4.png"
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

W, H = 1080, 1080
BG = "#F5F0E7"
INK = "#213039"
MUTED = "#5E6C70"
RED = "#B94233"
RED_LIGHT = "#E6B2A7"
AMBER = "#946020"
AMBER_LIGHT = "#E9D1A6"
TEAL = "#39766F"
TEAL_LIGHT = "#AFCEC6"
SILVER = "#98A1A5"
WHITE = "#FFFDF8"
HAIRLINE = "#D4CDC0"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size=size, index=7 if bold else 0)


def text(draw, xy, value, size, fill=INK, bold=False, anchor="la"):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def arrow(draw, points, fill, width=10):
    draw.line(points, fill=fill, width=width, joint="curve")
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    angle = atan2(y2 - y1, x2 - x1)
    head = 24
    wing = pi / 7
    draw.polygon(
        [
            (x2, y2),
            (x2 - head * cos(angle - wing), y2 - head * sin(angle - wing)),
            (x2 - head * cos(angle + wing), y2 - head * sin(angle + wing)),
        ],
        fill=fill,
    )


def seal(draw, x, y, w, h, fill=RED):
    draw.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=fill)
    draw.line((x + 14, y + 13, x + w - 15, y + 13), fill=RED_LIGHT, width=4)
    draw.line((x + w - 17, y + 20, x + w - 17, y + h - 19), fill="#8F2F26", width=4)


def draw_performance(draw, cx, cy):
    # 53, 53, 58, and 60 compared with the 62-point reference bar.
    for i, height in enumerate((118, 118, 129, 134)):
        seal(draw, cx + i * 42, cy - height, 30, height)
    draw.rounded_rectangle((cx + 178, cy - 138, cx + 212, cy), radius=12, fill=SILVER)
    draw.line((cx - 6, cy + 12, cx + 220, cy + 12), fill=HAIRLINE, width=4)


def draw_cost(draw, cx, cy):
    # GPT-5.6 Sol medium is the 100% reference. The three China-model bars
    # represent 20%, 14.7%, and 13.2% of its output-token price.
    widths = (180, 36, 26, 24)
    colors = (SILVER, AMBER, RED, RED)
    ys = (cy - 82, cy - 40, cy + 2, cy + 44)
    for width, color, y in zip(widths, colors, ys):
        draw.rounded_rectangle((cx, y, cx + width, y + 26), radius=12, fill=color)
        draw.ellipse((cx + 8, y + 8, cx + 18, y + 18), fill=WHITE)


def draw_ecosystem(draw, cx, cy):
    trunk = (cx, cy)
    branches = [
        (cx + 58, cy - 58),
        (cx + 78, cy),
        (cx + 58, cy + 58),
    ]
    leaves = [
        (cx + 138, cy - 94),
        (cx + 150, cy - 40),
        (cx + 164, cy + 6),
        (cx + 142, cy + 66),
        (cx + 116, cy + 102),
    ]
    for point in branches:
        draw.line((*trunk, *point), fill=TEAL, width=8)
    for i, point in enumerate(leaves):
        branch = branches[min(i // 2, 2)]
        draw.line((*branch, *point), fill=TEAL, width=6)
    for x, y in [trunk, *branches, *leaves]:
        r = 15 if (x, y) == trunk else 11
        draw.ellipse((x - r, y - r, x + r, y + r), fill=TEAL, outline=WHITE, width=3)


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Header: 190px / 1080px = 17.6% of canvas height.
text(draw, (64, 58), "중국 AI를 다시 볼 세 가지 신호", 60, bold=True)
draw.line((64, 158, 1016, 158), fill=HAIRLINE, width=3)

lanes = [
    (282, RED, "성능 근접", ("4개 모델 · Fable 5 점수", "85.5~96.8%")),
    (520, AMBER, "낮은 출력 단가", ("3개 모델 · GPT-5.6 Sol", "13.2~20%")),
    (758, TEAL, "개발자 확산", ("2025년 9월 신규 파생 모델", "63%")),
]

# Open-field lanes: icons and text remain outside a decorative outer card.
for y, color, label, support_lines in lanes:
    draw.line((64, y + 110, 720, y + 110), fill=HAIRLINE, width=3)
    text(draw, (332, y - 58), label, 46, fill=color, bold=True)
    text(draw, (332, y + 8), support_lines[0], 36, fill=MUTED)
    text(draw, (332, y + 50), support_lines[1], 36, fill=MUTED)

draw_performance(draw, 72, 322)
draw_cost(draw, 120, 540)
draw_ecosystem(draw, 96, 758)

# Three distinct signals converge on one reader decision.
arrow(draw, [(722, 392), (786, 392), (832, 460)], RED, width=10)
arrow(draw, [(722, 630), (800, 630), (832, 590)], AMBER, width=10)
arrow(draw, [(722, 868), (786, 868), (832, 700)], TEAL, width=10)

draw.ellipse((808, 458, 1034, 684), fill=INK)
text(draw, (921, 525), "같은 조건", 46, fill=WHITE, bold=True, anchor="mm")
text(draw, (921, 582), "다시 비교", 46, fill=WHITE, bold=True, anchor="mm")
draw.ellipse((904, 620, 938, 654), fill=RED)

# One decision-changing caveat, kept separate from the relationship.
draw.line((64, 960, 1016, 960), fill=HAIRLINE, width=3)
text(
    draw,
    (540, 1010),
    "전면 역전 근거는 아님 · 모델 설정과 지표 시점이 다름",
    34,
    fill=MUTED,
    anchor="mm",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, format="PNG", optimize=True)
print(OUT)
