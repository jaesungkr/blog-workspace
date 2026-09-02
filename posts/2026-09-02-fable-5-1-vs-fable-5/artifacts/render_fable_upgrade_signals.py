#!/usr/bin/env python3
"""Render the deterministic Fable 5.1 upgrade-signals infographic."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


WIDTH, HEIGHT = 1600, 1000
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "fable-5-1-upgrade-card-v3.png"
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

BG_TOP = (249, 246, 239)
BG_BOTTOM = (232, 228, 220)
INK = (32, 31, 36)
MUTED = (102, 99, 106)
GREEN = (32, 123, 99)
GREEN_LIGHT = (209, 232, 221)
VIOLET = (103, 75, 163)
VIOLET_LIGHT = (224, 217, 240)
AMBER = (181, 112, 33)
AMBER_LIGHT = (244, 224, 194)
HAIRLINE = (188, 181, 171)


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size, index=index)


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
             face: ImageFont.FreeTypeFont, fill: tuple[int, int, int],
             spacing: int = 4) -> tuple[int, int, int, int]:
    box = draw.multiline_textbbox((0, 0), text, font=face, spacing=spacing, align="center")
    w, h = box[2] - box[0], box[3] - box[1]
    x = int(xy[0] - w / 2 - box[0])
    y = int(xy[1] - h / 2 - box[1])
    draw.multiline_text((x, y), text, font=face, fill=fill, spacing=spacing, align="center")
    return (x + box[0], y + box[1], x + box[2], y + box[3])


def left(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
         face: ImageFont.FreeTypeFont, fill: tuple[int, int, int]) -> tuple[int, int, int, int]:
    box = draw.textbbox((0, 0), text, font=face)
    x = xy[0] - box[0]
    y = xy[1] - box[1]
    draw.text((x, y), text, font=face, fill=fill)
    return (x + box[0], y + box[1], x + box[2], y + box[3])


def glow_disc(base: Image.Image, center: tuple[int, int], radius: int,
              color: tuple[int, int, int], glow: tuple[int, int, int]) -> None:
    halo = Image.new("RGBA", base.size, (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    x, y = center
    hd.ellipse((x - radius - 26, y - radius - 26, x + radius + 26, y + radius + 26),
               fill=(*glow, 125))
    halo = halo.filter(ImageFilter.GaussianBlur(24))
    base.alpha_composite(halo)
    draw = ImageDraw.Draw(base)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                 fill=(*color, 255), outline=(255, 255, 255, 210), width=3)


def render() -> None:
    image = Image.new("RGBA", (WIDTH, HEIGHT), (*BG_TOP, 255))
    pixels = image.load()
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        row = tuple(round(BG_TOP[i] * (1 - t) + BG_BOTTOM[i] * t) for i in range(3))
        for x in range(WIDTH):
            vignette = max(0, int(((abs(x - WIDTH / 2) / (WIDTH / 2)) ** 2) * 5))
            pixels[x, y] = tuple(max(0, c - vignette) for c in row) + (255,)

    draw = ImageDraw.Draw(image)

    # Editorial header: under 18% of the canvas height.
    centered(draw, (WIDTH // 2, 82), "FABLE 5.1 전환 판단", font(25), VIOLET)
    headline_box = centered(
        draw,
        (WIDTH // 2, 145),
        "성능은 상승, 비용은 사용 방식에 따라 갈립니다",
        font(58, 7),
        INK,
    )
    assert headline_box[3] < 190

    # One continuous mechanism: three evidence signals converge on the model hub.
    hub = (800, 510)
    left_node = (305, 550)
    right_node = (1295, 550)
    cache_node = (800, 642)

    draw.line((left_node[0] + 13, left_node[1], hub[0] - 102, hub[1] + 10),
              fill=GREEN, width=7)
    draw.line((hub[0] + 102, hub[1] + 10, right_node[0] - 13, right_node[1]),
              fill=AMBER, width=7)
    draw.line((hub[0], hub[1] + 102, cache_node[0], cache_node[1] - 13),
              fill=VIOLET, width=7)

    for point, color in ((left_node, GREEN), (right_node, AMBER), (cache_node, VIOLET)):
        draw.ellipse((point[0] - 13, point[1] - 13, point[0] + 13, point[1] + 13),
                     fill=color, outline=(255, 255, 255), width=3)

    glow_disc(image, hub, 102, (45, 42, 51), (103, 75, 163))
    draw = ImageDraw.Draw(image)
    centered(draw, (hub[0], hub[1] - 29), "Fable", font(26, 5), (217, 210, 227))
    centered(draw, (hub[0], hub[1] + 23), "5.1", font(66, 7), (255, 255, 255))

    # Left: official comparison-table signal.
    left(draw, (120, 289), "공식 비교표", font(26, 5), GREEN)
    left_box = left(draw, (120, 331), "7개 평가군", font(51, 7), INK)
    left(draw, (120, 400), "9개 결과 행 모두 우위", font(30, 5), MUTED)
    left(draw, (120, 483), "성능 신호", font(24, 5), GREEN)

    # Right: external max setting shows a higher task-level cost.
    left(draw, (1112, 289), "외부 평가 · MAX", font(26, 5), AMBER)
    right_box = left(draw, (1112, 331), "$3.76", font(58, 7), INK)
    left(draw, (1112, 410), "Fable 5  $3.14 / 과제", font(27, 5), MUTED)
    left(draw, (1112, 483), "+20% 비용", font(24, 5), AMBER)

    # Bottom: cache-read pricing moves in the opposite direction.
    centered(draw, (800, 686), "캐시 읽기", font(24, 5), VIOLET)
    cache_box = centered(draw, (800, 757), "$0.25", font(61, 7), INK)
    centered(draw, (800, 818), "Fable 5  $1.00 / 100만 토큰", font(27, 5), MUTED)

    # Recommendation rail. It is visibly separate from measured values.
    rail_y = 874
    draw.line((180, rail_y, 1420, rail_y), fill=HAIRLINE, width=2)
    draw.ellipse((174, rail_y - 6, 186, rail_y + 6), fill=VIOLET)
    draw.polygon(((1420, rail_y), (1398, rail_y - 11), (1398, rail_y + 11)), fill=VIOLET)
    left(draw, (205, 902), "권장 시작점", font(24, 5), VIOLET)
    left(draw, (405, 895), "기존 Fable 작업  →  Fable 5.1 xhigh부터", font(35, 7), INK)
    centered(draw, (WIDTH // 2, 963), "max는 추가 성공률이 확인된 과제에만 적용합니다.", font(24, 5), MUTED)

    # Painted-bound and scene-envelope assertions.
    for box in (left_box, right_box, cache_box):
        assert box[0] >= 100 and box[2] <= WIDTH - 100
        assert box[1] >= 200 and box[3] <= 840
    assert left_box[2] < 620
    assert right_box[0] > 1040
    assert cache_box[1] > 700 and cache_box[3] < 810
    assert headline_box[0] >= 100 and headline_box[2] <= WIDTH - 100

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(OUTPUT, "PNG", optimize=True)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    render()
