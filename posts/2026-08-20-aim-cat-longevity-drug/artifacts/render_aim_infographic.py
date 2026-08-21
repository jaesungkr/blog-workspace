#!/usr/bin/env python3
"""Render the AIM kidney mechanism infographic as a deterministic PNG."""

from pathlib import Path
from math import cos, pi, sin

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "aim-kidney-mechanism-v1.png"
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

W, H = 1080, 1350
BG = "#F4F0E9"
INK = "#16343A"
MUTED = "#5A6F70"
TEAL = "#2C7774"
TEAL_LIGHT = "#DCEAE6"
AMBER = "#E49A3B"
AMBER_LIGHT = "#F7E4C7"
ROSE = "#C97268"
ROSE_LIGHT = "#F1D9D4"
WHITE = "#FFFDF9"
LINE = "#B8C9C4"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    # Apple SD Gothic Neo TTC exposes the regular and bold faces by index.
    return ImageFont.truetype(FONT, size=size, index=7 if bold else 0)


def text(draw, xy, value, size, fill=INK, bold=False, anchor="la"):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def arrow(draw, start, end, fill=TEAL, width=8, dashed=False):
    x1, y1 = start
    x2, y2 = end
    if dashed:
        steps = 9
        for i in range(steps):
            if i % 2 == 0:
                a = i / steps
                b = min((i + 1) / steps, 1)
                draw.line(
                    (x1 + (x2 - x1) * a, y1 + (y2 - y1) * a,
                     x1 + (x2 - x1) * b, y1 + (y2 - y1) * b),
                    fill=fill,
                    width=width,
                )
    else:
        draw.line((x1, y1, x2, y2), fill=fill, width=width)
    angle = __import__("math").atan2(y2 - y1, x2 - x1)
    head = 20
    pts = [
        (x2, y2),
        (x2 - head * cos(angle - pi / 6), y2 - head * sin(angle - pi / 6)),
        (x2 - head * cos(angle + pi / 6), y2 - head * sin(angle + pi / 6)),
    ]
    draw.polygon(pts, fill=fill)


def draw_igm(draw, center, scale=1.0, blocked=False, attach_markers=True):
    cx, cy = center
    radius = 64 * scale
    arm = 38 * scale
    for i in range(5):
        angle = -pi / 2 + i * 2 * pi / 5
        px = cx + radius * cos(angle)
        py = cy + radius * sin(angle)
        draw.line((cx, cy, px, py), fill=TEAL, width=max(5, int(8 * scale)))
        for delta in (-0.18, 0.18):
            ex = px + arm * cos(angle + delta)
            ey = py + arm * sin(angle + delta)
            draw.line((px, py, ex, ey), fill=TEAL, width=max(5, int(8 * scale)))
    draw.ellipse(
        (cx - 26 * scale, cy - 26 * scale, cx + 26 * scale, cy + 26 * scale),
        fill=TEAL_LIGHT,
        outline=TEAL,
        width=max(4, int(6 * scale)),
    )
    # AIM remains visibly tethered to the IgM complex.
    if attach_markers:
        for i in range(3):
            angle = 0.2 + i * 2.15
            ax = cx + (radius + arm + 17) * cos(angle) * scale
            ay = cy + (radius + arm + 17) * sin(angle) * scale
            draw.ellipse((ax - 14, ay - 14, ax + 14, ay + 14), fill=AMBER, outline=WHITE, width=3)
    text(draw, (cx, cy + 3), "IgM", 30, fill=INK, bold=True, anchor="mm")
    if blocked:
        draw.ellipse((cx - 104, cy - 104, cx + 104, cy + 104), outline=ROSE, width=7)


def draw_tubule(draw, box, debris=False, cleared=False):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=52, fill=WHITE, outline=LINE, width=6)
    inner = (x1 + 32, y1 + 38, x2 - 32, y2 - 38)
    draw.rounded_rectangle(inner, radius=28, fill="#EAF3F0")
    if debris:
        pieces = [
            (x1 + 80, y1 + 68, 34, ROSE),
            (x1 + 135, y1 + 100, 28, AMBER),
            (x1 + 190, y1 + 72, 42, ROSE),
            (x1 + 240, y1 + 112, 32, AMBER),
            (x1 + 290, y1 + 78, 36, ROSE),
        ]
        for px, py, r, color in pieces:
            draw.ellipse((px - r, py - r, px + r, py + r), fill=color)
    if cleared:
        for px, py in [(x1 + 110, y1 + 75), (x1 + 190, y1 + 108), (x1 + 270, y1 + 73)]:
            draw.ellipse((px - 13, py - 13, px + 13, py + 13), fill=AMBER, outline=WHITE, width=3)
        arrow(draw, (x1 + 115, y2 - 28), (x2 - 80, y2 - 28), fill=TEAL, width=7)


def row_label(draw, y, number, title_value, subtitle):
    draw.ellipse((64, y + 36, 126, y + 98), fill=INK)
    text(draw, (95, y + 69), str(number), 32, fill=WHITE, bold=True, anchor="mm")
    text(draw, (154, y + 42), title_value, 48, bold=True)
    text(draw, (154, y + 100), subtitle, 39, fill=MUTED)


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Header
text(draw, (68, 44), "AIM · 고양이 만성 신장질환", 34, fill=TEAL, bold=True)
text(draw, (68, 88), "AIM이 신장 찌꺼기를", 68, bold=True)
text(draw, (68, 158), "치우는 흐름", 68, bold=True)
text(draw, (68, 238), "고양이에서 막힌 청소 경로를 재조합 AIM으로 보완하는 원리", 36, fill=MUTED)
draw.line((68, 284, 1012, 284), fill=LINE, width=3)

# Row 1
y = 306
row_label(draw, y, 1, "신장 손상 때", "AIM이 IgM에서 떨어져 찌꺼기로 이동합니다")
draw_igm(draw, (330, y + 220), scale=0.78, attach_markers=False)
text(draw, (330, y + 325), "IgM에서 분리", 36, fill=TEAL, bold=True, anchor="mm")
for px in (480, 520, 560):
    draw.ellipse((px - 13, y + 207, px + 13, y + 233), fill=AMBER, outline=WHITE, width=3)
arrow(draw, (470, y + 220), (590, y + 220), fill=TEAL)
draw_tubule(draw, (625, y + 144, 986, y + 290), debris=True, cleared=True)
text(draw, (806, y + 325), "찌꺼기에 표지를 붙여 제거", 36, fill=TEAL, bold=True, anchor="mm")
draw.line((68, 660, 1012, 660), fill=LINE, width=3)

# Row 2
y = 680
row_label(draw, y, 2, "고양이 신장 손상", "AIM이 IgM에서 잘 떨어지지 않습니다")
draw_igm(draw, (330, y + 245), scale=0.78, blocked=True)
arrow(draw, (470, y + 245), (590, y + 245), fill=ROSE, dashed=True)
draw.line((532, y + 209, 532, y + 281), fill=ROSE, width=12)
draw_tubule(draw, (625, y + 169, 986, y + 315), debris=True)
text(draw, (806, y + 337), "찌꺼기가 세뇨관에 축적", 36, fill=ROSE, bold=True, anchor="mm")
draw.line((68, 1034, 1012, 1034), fill=LINE, width=3)

# Row 3: compact decision row
y = 1050
draw.ellipse((37, y - 13, 99, y + 49), fill=INK)
text(draw, (68, y + 18), "3", 32, fill=WHITE, bold=True, anchor="mm")
text(draw, (126, y - 7), "재조합 AIM 연구", 48, bold=True)
text(draw, (126, y + 52), "외부 AIM이 찌꺼기 표지·제거를 보완합니다", 34, fill=MUTED)
for px in (550, 590, 630):
    draw.ellipse((px - 12, y + 3, px + 12, y + 27), fill=AMBER, outline=WHITE, width=3)
arrow(draw, (650, y + 15), (688, y + 15), fill=TEAL, width=7)
draw.rounded_rectangle((704, y - 14, 994, y + 48), radius=24, fill=WHITE, outline=LINE, width=5)
draw.rounded_rectangle((724, y + 1, 974, y + 33), radius=14, fill="#EAF3F0")
for px, color in ((772, ROSE), (838, INK), (904, ROSE)):
    draw.ellipse((px - 16, y + 1, px + 16, y + 33), fill=color)
for px in (760, 892):
    draw.ellipse((px - 8, y + 9, px + 8, y + 25), fill=AMBER, outline=WHITE, width=2)
arrow(draw, (788, y + 40), (948, y + 40), fill=TEAL, width=5)

# Evidence boundary footer
footer_y = 1190
draw.rounded_rectangle((68, footer_y, 1012, 1312), radius=30, fill=INK)
text(draw, (102, footer_y + 40), "확인된 범위", 34, fill="#A8D5CD", bold=True)
text(draw, (318, footer_y + 40), "악화 지연 가능성 · 신장 재생은 미확인", 34, fill=WHITE, bold=True)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, format="PNG", optimize=True)
print(OUT)
