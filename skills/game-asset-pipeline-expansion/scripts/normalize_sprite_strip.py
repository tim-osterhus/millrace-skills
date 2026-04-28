#!/usr/bin/env python3
"""Normalize a horizontal sprite strip into fixed-size frames."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Horizontal sprite strip to normalize.")
    parser.add_argument("--out-dir", required=True, type=Path, help="Directory for normalized frames.")
    parser.add_argument("--frames", required=True, type=int, help="Number of frames in the strip.")
    parser.add_argument("--frame-size", required=True, type=int, help="Target square frame size in pixels.")
    parser.add_argument(
        "--anchor",
        type=Path,
        help="Optional reference image whose visible bounds participate in the shared scale calculation.",
    )
    parser.add_argument(
        "--padding",
        type=int,
        default=4,
        help="Minimum padding between visible content and the canvas edge. Default: 4.",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=8,
        help="Alpha threshold used to detect visible content. Default: 8.",
    )
    parser.add_argument(
        "--resample",
        choices=("nearest", "bilinear", "bicubic", "lanczos"),
        default="nearest",
        help="Resize filter used during normalization. Default: nearest.",
    )
    return parser.parse_args()


def resolve_resample(name: str) -> int:
    namespace = getattr(Image, "Resampling", Image)
    return getattr(namespace, name.upper())


def alpha_bbox(image: Image.Image, threshold: int) -> tuple[int, int, int, int] | None:
    alpha = image.convert("RGBA").getchannel("A").point(lambda value: 255 if value > threshold else 0)
    return alpha.getbbox()


def split_strip(image: Image.Image, frames: int) -> list[Image.Image]:
    if frames < 1:
        raise ValueError("--frames must be at least 1")
    if image.width % frames != 0:
        raise ValueError(f"strip width {image.width} is not divisible by {frames} frames")

    frame_width = image.width // frames
    return [image.crop((index * frame_width, 0, (index + 1) * frame_width, image.height)).convert("RGBA") for index in range(frames)]


def gather_bboxes(frames: list[Image.Image], anchor: Image.Image | None, threshold: int) -> list[tuple[int, int, int, int]]:
    bboxes = [bbox for frame in frames if (bbox := alpha_bbox(frame, threshold))]
    if anchor is not None:
        anchor_bbox = alpha_bbox(anchor, threshold)
        if anchor_bbox is not None:
            bboxes.append(anchor_bbox)
    return bboxes


def fit_scale(bboxes: list[tuple[int, int, int, int]], frame_size: int, padding: int) -> float:
    if frame_size < 1:
        raise ValueError("--frame-size must be at least 1")
    if padding < 0:
        raise ValueError("--padding cannot be negative")
    inner_size = frame_size - padding * 2
    if inner_size < 1:
        raise ValueError("--frame-size must be larger than twice --padding")

    if not bboxes:
        raise ValueError("no visible alpha content found in the input strip or anchor image")

    max_width = max(bbox[2] - bbox[0] for bbox in bboxes)
    max_height = max(bbox[3] - bbox[1] for bbox in bboxes)
    scale_x = inner_size / max_width if max_width else 1.0
    scale_y = inner_size / max_height if max_height else 1.0
    return min(scale_x, scale_y)


def normalize_frame(
    frame: Image.Image,
    *,
    frame_size: int,
    padding: int,
    scale: float,
    resample: int,
    threshold: int,
) -> Image.Image:
    canvas = Image.new("RGBA", (frame_size, frame_size), (0, 0, 0, 0))
    bbox = alpha_bbox(frame, threshold)
    if bbox is None:
        return canvas

    cropped = frame.crop(bbox)
    scaled_width = max(1, round(cropped.width * scale))
    scaled_height = max(1, round(cropped.height * scale))
    resized = cropped.resize((scaled_width, scaled_height), resample=resample)

    anchor_x = frame_size / 2
    anchor_y = frame_size - padding
    left = round(anchor_x - resized.width / 2)
    top = round(anchor_y - resized.height)
    canvas.paste(resized, (left, top), resized)
    return canvas


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"input strip does not exist: {args.input}")

    with Image.open(args.input) as opened:
        strip = opened.convert("RGBA")

    anchor_image: Image.Image | None = None
    if args.anchor is not None:
        if not args.anchor.is_file():
            raise SystemExit(f"anchor image does not exist: {args.anchor}")
        with Image.open(args.anchor) as opened:
            anchor_image = opened.convert("RGBA")

    frames = split_strip(strip, args.frames)
    bboxes = gather_bboxes(frames, anchor_image, args.threshold)
    scale = fit_scale(bboxes, args.frame_size, args.padding)
    resample = resolve_resample(args.resample)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for path in args.out_dir.glob("frame-*.png"):
        path.unlink()

    digits = max(2, len(str(args.frames)))
    written: list[Path] = []
    for index, frame in enumerate(frames, start=1):
        normalized = normalize_frame(
            frame,
            frame_size=args.frame_size,
            padding=args.padding,
            scale=scale,
            resample=resample,
            threshold=args.threshold,
        )
        output_path = args.out_dir / f"frame-{index:0{digits}d}.png"
        normalized.save(output_path)
        written.append(output_path)

    print(
        f"normalized {len(written)} frames from {args.input.name} "
        f"to {args.out_dir} at scale {scale:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
