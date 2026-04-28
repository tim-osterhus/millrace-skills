#!/usr/bin/env python3
"""Render a checkerboard preview sheet for normalized sprite frames."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frames-dir", required=True, type=Path, help="Directory of normalized PNG frames.")
    parser.add_argument("--out", required=True, type=Path, help="Preview sheet output path.")
    parser.add_argument("--columns", type=int, default=4, help="Number of columns in the sheet. Default: 4.")
    parser.add_argument("--padding", type=int, default=12, help="Padding around and between cells. Default: 12.")
    return parser.parse_args()


def paint_checkerboard(image: Image.Image, tile: int = 16) -> None:
    draw = ImageDraw.Draw(image)
    colors = ((238, 242, 246, 255), (218, 225, 232, 255))
    for top in range(0, image.height, tile):
        for left in range(0, image.width, tile):
            color = colors[((left // tile) + (top // tile)) % 2]
            draw.rectangle((left, top, left + tile, top + tile), fill=color)


def load_frames(frames_dir: Path) -> list[tuple[Path, Image.Image]]:
    paths = sorted(path for path in frames_dir.glob("*.png") if path.is_file())
    frames: list[tuple[Path, Image.Image]] = []
    for path in paths:
        with Image.open(path) as opened:
            frames.append((path, opened.convert("RGBA")))
    return frames


def draw_label(draw: ImageDraw.ImageDraw, x: int, y: int, text: str) -> None:
    try:
        font = ImageFont.load_default()
    except Exception:  # pragma: no cover
        font = None
    if font is not None:
        draw.rectangle((x - 2, y - 2, x + 32, y + 12), fill=(20, 24, 28, 180))
        draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)


def main() -> int:
    args = parse_args()
    if args.columns < 1:
        raise SystemExit("--columns must be at least 1")
    if not args.frames_dir.is_dir():
        raise SystemExit(f"frames directory does not exist: {args.frames_dir}")

    frames = load_frames(args.frames_dir)
    if not frames:
        raise SystemExit(f"no PNG frames found in {args.frames_dir}")

    cell_width = max(image.width for _path, image in frames)
    cell_height = max(image.height for _path, image in frames)
    rows = math.ceil(len(frames) / args.columns)
    sheet_width = args.columns * cell_width + (args.columns + 1) * args.padding
    sheet_height = rows * cell_height + (rows + 1) * args.padding

    sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))
    paint_checkerboard(sheet)
    draw = ImageDraw.Draw(sheet)

    for index, (path, image) in enumerate(frames):
        row = index // args.columns
        column = index % args.columns
        left = args.padding + column * (cell_width + args.padding)
        top = args.padding + row * (cell_height + args.padding)
        offset_x = left + (cell_width - image.width) // 2
        offset_y = top + (cell_height - image.height) // 2
        sheet.paste(image, (offset_x, offset_y), image)
        draw.rectangle((left, top, left + cell_width, top + cell_height), outline=(40, 48, 56, 120), width=1)
        draw_label(draw, left + 6, top + 6, f"{index + 1:02d}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.out)
    print(f"wrote preview sheet to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
