#!/usr/bin/env python3
"""Render a deterministic, brand-led hero from official logo assets."""

from pathlib import Path
from collections import deque

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
LOGO_DIR = ROOT / "artifacts" / "captures" / "official-logos"
OUT = ROOT / "assets" / "china-ai-logo-roster-hero-v7.png"
RAW = ROOT / "artifacts" / "captures" / "china-ai-logo-roster-source-v1.png"

W, H = 1672, 941
BG = "#E7E4DC"
INK = "#16191C"
MUTED = "#6B7075"
ACCENT = "#E04C3E"
WHITE = "#F8F7F2"
VIOLET_MIST = "#F1EFFF"
BLUE_MIST = "#EEF3FF"
GRAPHITE = "#1B1F22"

KOREAN_FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
MONO_FONT = "/System/Library/Fonts/Menlo.ttc"


def korean(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(KOREAN_FONT, size=size, index=7 if bold else 0)


def mono(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(MONO_FONT, size=size, index=1 if bold else 0)


def fit(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
    scale = min(max_width / image.width, max_height / image.height)
    size = (round(image.width * scale), round(image.height * scale))
    return image.resize(size, Image.Resampling.LANCZOS)


def white_to_alpha(image: Image.Image) -> Image.Image:
    """Remove a flat white asset background while retaining antialiased logo edges."""
    rgba = image.convert("RGBA")
    converted = []
    for r, g, b, _ in rgba.getdata():
        distance = max(255 - r, 255 - g, 255 - b)
        alpha = max(0, min(255, distance * 6))
        converted.append((r, g, b, alpha))
    rgba.putdata(converted)
    return rgba


def remove_connected_light_background(image: Image.Image) -> Image.Image:
    """Clear only the light field connected to the border, preserving white logo details."""
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    seen = bytearray(rgba.width * rgba.height)
    queue: deque[tuple[int, int]] = deque()

    def enqueue(x: int, y: int) -> None:
        offset = y * rgba.width + x
        if seen[offset]:
            return
        r, g, b, _ = pixels[x, y]
        if min(r, g, b) < 205:
            return
        seen[offset] = 1
        queue.append((x, y))

    for x in range(rgba.width):
        enqueue(x, 0)
        enqueue(x, rgba.height - 1)
    for y in range(rgba.height):
        enqueue(0, y)
        enqueue(rgba.width - 1, y)

    while queue:
        x, y = queue.popleft()
        pixels[x, y] = (*pixels[x, y][:3], 0)
        if x:
            enqueue(x - 1, y)
        if x + 1 < rgba.width:
            enqueue(x + 1, y)
        if y:
            enqueue(x, y - 1)
        if y + 1 < rgba.height:
            enqueue(x, y + 1)

    bbox = rgba.getchannel("A").getbbox()
    return rgba.crop(bbox) if bbox else rgba


def paste_center(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    x = x0 + (x1 - x0 - image.width) // 2
    y = y0 + (y1 - y0 - image.height) // 2
    canvas.alpha_composite(image, (x, y))


def panel_label(draw: ImageDraw.ImageDraw, x: int, y: int, index: str, owner: str) -> None:
    draw.text((x, y), index, font=mono(24, True), fill=ACCENT)
    draw.text((x + 54, y), owner, font=mono(24, True), fill=MUTED)


canvas = Image.new("RGBA", (W, H), BG)
draw = ImageDraw.Draw(canvas)

# Open editorial masthead: one claim, four recognizable names below it.
draw.rectangle((56, 48, 68, 156), fill=ACCENT)
draw.text((94, 43), "딥시크만이 아니다", font=korean(72, True), fill=INK)
draw.text((1616, 62), "CHINA AI / FOUR LABS", font=mono(26, True), fill=MUTED, anchor="ra")
draw.text((1616, 111), "ONE COMPETITIVE FIELD", font=mono(26), fill=INK, anchor="ra")

# A continuous, offset matrix avoids the stock-card look while keeping every mark intact.
top_y, split_y, bottom_y = 194, 528, 886
top_split, bottom_split = 966, 732
gap = 8

draw.rectangle((56, top_y, top_split - gap // 2, split_y - gap // 2), fill=WHITE)
draw.rectangle((top_split + gap // 2, top_y, 1616, split_y - gap // 2), fill=VIOLET_MIST)
draw.rectangle((56, split_y + gap // 2, bottom_split - gap // 2, bottom_y), fill=BLUE_MIST)
draw.rectangle((bottom_split + gap // 2, split_y + gap // 2, 1616, bottom_y), fill=GRAPHITE)

# Small indexing is secondary; the unmodified official marks carry the image.
panel_label(draw, 84, 218, "01", "MOONSHOT AI")
panel_label(draw, 994, 218, "02", "ALIBABA")
panel_label(draw, 84, 554, "03", "DEEPSEEK")
draw.text((764, 554), "04", font=mono(24, True), fill=ACCENT)
draw.text((818, 554), "Z.AI / GLM", font=mono(24, True), fill="#AAB0B4")

kimi = Image.open(LOGO_DIR / "kimi-with-icon-light.png").convert("RGBA")
qwen = white_to_alpha(Image.open(LOGO_DIR / "qwen-logo.jpg").crop((0, 0, 1760, 597)))
deepseek = Image.open(LOGO_DIR / "deepseek-logo.png").convert("RGBA")
zai = remove_connected_light_background(
    Image.open(LOGO_DIR / "zai-logo-900.png").crop((40, 40, 860, 860))
)

paste_center(canvas, fit(kimi, 710, 214), (84, 266, 938, 506))
paste_center(canvas, fit(qwen, 540, 178), (994, 270, 1588, 500))
paste_center(canvas, fit(deepseek, 568, 150), (84, 620, 704, 842))

# The official Z.ai icon is paired with a neutral text label; the icon itself is unaltered.
zai_icon = fit(zai, 174, 174)
zai_x, zai_y = 906, 638
canvas.alpha_composite(zai_icon, (zai_x, zai_y))
draw.text((1110, 665), "Z.ai", font=mono(116, True), fill="#F4F5F6")
draw.text((1116, 790), "GLM", font=mono(34, True), fill="#AAB0B4")

# Thin calibration marks add structure without competing with the brand identities.
for x in (56, 204, 352, 500, 648, 796, 944, 1092, 1240, 1388, 1536, 1616):
    draw.line((x, 896, x, 906), fill=MUTED, width=2)
draw.text((56, 914), "EDITORIAL BRAND ROSTER / 2026.08.21", font=mono(18), fill=MUTED)
draw.text((1616, 914), "NO AFFILIATION IMPLIED", font=mono(18), fill=MUTED, anchor="ra")

RAW.parent.mkdir(parents=True, exist_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(RAW, format="PNG")
canvas.convert("RGB").save(OUT, format="PNG", optimize=True)
print(OUT)
