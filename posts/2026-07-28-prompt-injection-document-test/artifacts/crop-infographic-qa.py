#!/usr/bin/env python3
"""Create full-resolution QA crops from the exact infographic candidate."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "assets" / "prompt-injection-defense-infographic-v3.png"
OUTPUT = ROOT / "infographic-v3-qa"

CROPS = {
    "01-header.png": (0, 0, 1200, 270),
    "02-sources-agent-connectors.png": (50, 250, 1150, 870),
    "03-boundaries.png": (50, 800, 1150, 1300),
    "04-result-caveat.png": (50, 1220, 1150, 1500),
}


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    with Image.open(SOURCE) as image:
        for name, box in CROPS.items():
            image.crop(box).save(OUTPUT / name)


if __name__ == "__main__":
    main()
