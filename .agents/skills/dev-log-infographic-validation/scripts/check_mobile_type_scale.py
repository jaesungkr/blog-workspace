#!/usr/bin/env python3
"""Check infographic typography at a 360 CSS-pixel display width."""

from __future__ import annotations

import argparse


BANDS = {
    "headline": (20.0, 24.0),
    "primary": (15.0, 18.0),
    "support": (12.0, 14.0),
    "caveat": (11.0, 12.0),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--canvas-width", type=float, required=True)
    parser.add_argument("--canvas-height", type=float, required=True)
    parser.add_argument("--header-height", type=float, required=True)
    for role in BANDS:
        parser.add_argument(f"--{role}", type=float, action="append", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scale = 360.0 / args.canvas_width
    failed = False

    for role, (minimum, maximum) in BANDS.items():
        source_sizes = getattr(args, role)
        equivalents = [size * scale for size in source_sizes]
        rendered = ", ".join(f"{size:.1f}px" for size in equivalents)
        passed = all(minimum <= size <= maximum for size in equivalents)
        failed = failed or not passed
        print(
            f"{role}: {rendered} at 360px "
            f"(band {minimum:.1f}-{maximum:.1f}px) "
            f"{'PASS' if passed else 'FAIL'}"
        )

    header_share = args.header_height / args.canvas_height * 100.0
    header_passed = header_share <= 22.0
    failed = failed or not header_passed
    print(
        f"header: {header_share:.1f}% of canvas "
        f"(maximum 22.0%) {'PASS' if header_passed else 'FAIL'}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
