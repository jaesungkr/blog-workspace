#!/usr/bin/env python3
"""Render an editorial-tech China AI signal field as a deterministic PNG."""

from pathlib import Path
from math import atan2, cos, pi, sin

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "china-ai-signal-field-v7.png"
KOREAN_FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
MONO_FONT = "/System/Library/Fonts/Menlo.ttc"

W, H = 1080, 1200
BG_TOP = (16, 20, 23)
BG_BOTTOM = (23, 28, 32)
INK = "#F3F0E8"
MUTED = "#A9B1B4"
QUIET = "#687378"
GRID = "#30383C"
GRID_SOFT = "#252C30"
ACCENT = "#E55240"
ACCENT_LIGHT = "#F28A79"
SILVER = "#78858B"
WHITE = "#FFFFFF"


def korean(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(KOREAN_FONT, size=size, index=7 if bold else 0)


def mono(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(MONO_FONT, size=size, index=1 if bold else 0)


def label(draw, xy, value, size, fill=INK, bold=False, anchor="la"):
    draw.text(xy, value, font=korean(size, bold), fill=fill, anchor=anchor)


def utility(draw, xy, value, size=34, fill=MUTED, bold=False, anchor="la"):
    draw.text(xy, value, font=mono(size, bold), fill=fill, anchor=anchor)


def arrowhead(draw, start, end, fill=ACCENT, size=20):
    angle = atan2(end[1] - start[1], end[0] - start[0])
    wing = pi / 7
    draw.polygon(
        [
            end,
            (
                end[0] - size * cos(angle - wing),
                end[1] - size * sin(angle - wing),
            ),
            (
                end[0] - size * cos(angle + wing),
                end[1] - size * sin(angle + wing),
            ),
        ],
        fill=fill,
    )


def signal_node(draw, x, y):
    draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=ACCENT)
    draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=WHITE)


# A quiet vertical gradient keeps the dark field dimensional without a neon glow.
img = Image.new("RGB", (W, H))
pixels = img.load()
for y in range(H):
    t = y / (H - 1)
    row = tuple(round(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM))
    for x in range(W):
        pixels[x, y] = row

draw = ImageDraw.Draw(img)

# Sparse engineered grid, kept behind the information hierarchy.
for x in (70, 330, 600, 820, 1010):
    draw.line((x, 42, x, 1134), fill=GRID_SOFT, width=2)
for y in (188, 488, 760, 1018, 1134):
    draw.line((70, y, 1010, y), fill=GRID, width=2)
for y in range(220, 1000, 34):
    draw.line((1002, y, 1010, y), fill=QUIET, width=2)

# Header: 188 / 1200 = 15.7% of the canvas.
utility(draw, (70, 48), "SIGNAL FIELD / 2026.08.21", 34, fill=ACCENT_LIGHT, bold=True)
label(draw, (70, 102), "중국 AI 경쟁을 바꾸는 세 신호", 60, bold=True)
utility(draw, (1010, 115), "03 AXES", 34, fill=MUTED, anchor="ra")

# Decision spine joins all three signals without enclosing them in cards.
SPINE_X = 820
draw.line((SPINE_X, 230, SPINE_X, 1004), fill=QUIET, width=4)

# 01 Performance — exact 53, 53, 58, 60 against a 62-point reference.
utility(draw, (70, 232), "01 / PERFORMANCE", 34, fill=MUTED, bold=True)
label(draw, (70, 278), "성능 근접", 46, fill=INK, bold=True)
label(draw, (70, 354), "85.5~96.8", 86, fill=INK, bold=True)
label(draw, (513, 372), "%", 46, fill=ACCENT, bold=True)
label(draw, (70, 430), "4개 모델 · Fable 5 점수 대비", 36, fill=MUTED)

track_x, track_w = 580, 190
scores = (53, 53, 58, 60)
for i, score in enumerate(scores):
    y = 275 + i * 43
    draw.line((track_x, y, track_x + track_w, y), fill=GRID, width=8)
    value_w = round(track_w * score / 62)
    draw.line((track_x, y, track_x + value_w, y), fill=ACCENT, width=8)
    draw.ellipse((track_x + value_w - 6, y - 6, track_x + value_w + 6, y + 6), fill=ACCENT_LIGHT)
draw.line((track_x + track_w, 250, track_x + track_w, 424), fill=SILVER, width=3)
draw.line((770, 354, SPINE_X, 354), fill=ACCENT, width=4)
signal_node(draw, SPINE_X, 354)

# 02 Cost — one 100% reference and three China-model ratios.
utility(draw, (360, 522), "02 / OUTPUT COST", 34, fill=MUTED, bold=True)
label(draw, (360, 568), "낮은 출력 단가", 46, fill=INK, bold=True)
label(draw, (360, 632), "13.2~20", 86, fill=INK, bold=True)
label(draw, (725, 650), "%", 46, fill=ACCENT, bold=True)
label(draw, (360, 712), "3개 모델 · GPT-5.6 Sol 대비", 36, fill=MUTED)

cost_x, cost_w = 70, 220
costs = (100, 20, 14.7, 13.2)
for i, ratio in enumerate(costs):
    y = 548 + i * 43
    width = round(cost_w * ratio / 100)
    draw.line((cost_x, y, cost_x + cost_w, y), fill=GRID, width=8)
    draw.line((cost_x, y, cost_x + width, y), fill=SILVER if i == 0 else ACCENT, width=8)
    draw.ellipse((cost_x + width - 6, y - 6, cost_x + width + 6, y + 6), fill=WHITE if i == 0 else ACCENT_LIGHT)
draw.line((760, 618, SPINE_X, 618), fill=ACCENT, width=4)
signal_node(draw, SPINE_X, 618)

# 03 Ecosystem — a branching derivative-model field, not a generic icon card.
utility(draw, (70, 782), "03 / DERIVATIVE ECOSYSTEM", 34, fill=MUTED, bold=True)
label(draw, (70, 828), "개발자 확산", 46, fill=INK, bold=True)
label(draw, (70, 892), "63", 86, fill=INK, bold=True)
label(draw, (213, 910), "%", 46, fill=ACCENT, bold=True)
label(draw, (70, 972), "2025년 9월 신규 파생 모델", 36, fill=MUTED)

root = (520, 882)
level_one = ((595, 820), (605, 882), (595, 944))
level_two = ((695, 790), (720, 838), (740, 882), (720, 926), (695, 974))
for point in level_one:
    draw.line((*root, *point), fill=SILVER, width=5)
for index, point in enumerate(level_two):
    parent = level_one[min(index // 2, 2)]
    draw.line((*parent, *point), fill=ACCENT if index in (1, 2, 3) else SILVER, width=4)
for point in (root, *level_one, *level_two):
    radius = 12 if point == root else 8
    draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), fill=ACCENT if point == root else INK)
draw.line((755, 882, SPINE_X, 882), fill=ACCENT, width=4)
signal_node(draw, SPINE_X, 882)

# The spine resolves into one practical decision, with no poster-like result card.
draw.line((SPINE_X, 1004, 866, 1004), fill=ACCENT, width=8)
arrowhead(draw, (846, 1004), (866, 1004), fill=ACCENT, size=22)
utility(draw, (920, 960), "COMPARE", 34, fill=ACCENT_LIGHT, bold=True, anchor="ma")
label(draw, (1010, 1040), "같은 조건으로 다시 비교", 46, fill=INK, bold=True, anchor="ra")

# One decision-changing limit, aligned to the technical grid.
utility(draw, (70, 1164), "LIMIT", 34, fill=ACCENT_LIGHT, bold=True, anchor="lm")
label(
    draw,
    (1010, 1164),
    "전면 역전 근거는 아님 · 모델 설정과 지표 시점이 다름",
    34,
    fill=MUTED,
    anchor="rm",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, format="PNG", optimize=True)
print(OUT)
