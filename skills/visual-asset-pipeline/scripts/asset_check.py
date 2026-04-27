#!/usr/bin/env python3
"""Deterministically check generated browser-game image assets."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required. Install it with `python3 -m pip install pillow`.") from exc


SUPPORTED_EXTENSIONS = {".png", ".webp", ".jpg", ".jpeg"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check generated image assets.")
    parser.add_argument("--asset", action="append", default=[], type=Path, help="Asset path to check.")
    parser.add_argument("--dir", type=Path, help="Directory of image assets to check.")
    parser.add_argument("--glob", default="*.png", help="Glob used with --dir. Default: *.png.")
    parser.add_argument("--manifest", type=Path, help="Manifest JSON written by codex_asset_request.py.")
    parser.add_argument("--base-dir", type=Path, help="Base directory for manifest-relative paths.")
    parser.add_argument("--require-alpha", action="store_true", help="Require an alpha channel.")
    parser.add_argument("--min-alpha-coverage", type=float, help="Minimum non-transparent alpha coverage.")
    parser.add_argument("--max-alpha-coverage", type=float, help="Maximum non-transparent alpha coverage.")
    parser.add_argument("--expect-width", type=int, help="Expected image width in pixels.")
    parser.add_argument("--expect-height", type=int, help="Expected image height in pixels.")
    parser.add_argument("--max-bytes", type=int, help="Maximum file size in bytes.")
    parser.add_argument(
        "--strip-frames",
        type=int,
        help="Treat each checked asset as a horizontal sprite strip with this many frames.",
    )
    parser.add_argument("--expect-frame-width", type=int, help="Expected frame width for sprite strips.")
    parser.add_argument("--expect-frame-height", type=int, help="Expected frame height for sprite strips.")
    parser.add_argument(
        "--max-bottom-drift",
        type=int,
        help="Maximum allowed per-frame alpha bounding-box bottom drift for strips.",
    )
    parser.add_argument("--preview", type=Path, help="Write a checkerboard preview sheet.")
    parser.add_argument("--report", type=Path, help="Write JSON report to this path.")
    return parser.parse_args()


def load_manifest_assets(path: Path, base_dir: Path | None) -> list[Path]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_assets: list[Any] = []
    manifest_base_dir = base_dir
    if isinstance(payload, dict):
        if manifest_base_dir is None and isinstance(payload.get("workdir"), str):
            manifest_base_dir = Path(payload["workdir"])
        if manifest_base_dir is None and isinstance(payload.get("base_dir"), str):
            manifest_base_dir = Path(payload["base_dir"])
        if isinstance(payload.get("assets"), list):
            raw_assets = payload["assets"]
        elif isinstance(payload.get("files"), list):
            raw_assets = payload["files"]
    elif isinstance(payload, list):
        raw_assets = payload

    root = manifest_base_dir or path.parent
    assets: list[Path] = []
    for item in raw_assets:
        raw_path: str | None = None
        if isinstance(item, str):
            raw_path = item
        elif isinstance(item, dict) and isinstance(item.get("path"), str):
            raw_path = item["path"]
        if not raw_path:
            continue
        asset_path = Path(raw_path)
        if not asset_path.is_absolute():
            asset_path = root / asset_path
        assets.append(asset_path.resolve())
    return assets


def collect_assets(args: argparse.Namespace) -> list[Path]:
    assets: list[Path] = []
    assets.extend(path.expanduser().resolve() for path in args.asset)
    if args.dir:
        root = args.dir.expanduser().resolve()
        assets.extend(sorted(path.resolve() for path in root.glob(args.glob)))
    if args.manifest:
        assets.extend(load_manifest_assets(args.manifest.expanduser().resolve(), args.base_dir))

    unique: dict[str, Path] = {}
    for asset in assets:
        unique[str(asset)] = asset
    return list(unique.values())


def alpha_values(image: Image.Image) -> bytes | None:
    converted = image.convert("RGBA")
    return converted.getchannel("A").tobytes()


def alpha_bbox(image: Image.Image, threshold: int = 8) -> tuple[int, int, int, int] | None:
    alpha = image.convert("RGBA").getchannel("A").point(lambda value: 255 if value > threshold else 0)
    return alpha.getbbox()


def check_strip(
    image: Image.Image,
    *,
    frames: int,
    expect_frame_width: int | None,
    expect_frame_height: int | None,
    max_bottom_drift: int | None,
) -> tuple[dict[str, Any], list[str]]:
    issues: list[str] = []
    details: dict[str, Any] = {"frames": frames, "frame_metrics": []}
    if frames < 1:
        issues.append("--strip-frames must be at least 1")
        return details, issues
    if image.width % frames != 0:
        issues.append(f"width {image.width} is not divisible by {frames} strip frames")
        return details, issues

    frame_width = image.width // frames
    frame_height = image.height
    details["frame_width"] = frame_width
    details["frame_height"] = frame_height

    if expect_frame_width is not None and frame_width != expect_frame_width:
        issues.append(f"frame width {frame_width} != expected {expect_frame_width}")
    if expect_frame_height is not None and frame_height != expect_frame_height:
        issues.append(f"frame height {frame_height} != expected {expect_frame_height}")

    bottoms: list[int] = []
    for index in range(frames):
        left = index * frame_width
        frame = image.crop((left, 0, left + frame_width, frame_height))
        bbox = alpha_bbox(frame)
        metric: dict[str, Any] = {"index": index + 1, "bbox": bbox}
        if bbox is None:
            issues.append(f"frame {index + 1} has no visible alpha content")
        else:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            metric["content_width"] = width
            metric["content_height"] = height
            metric["bottom"] = bbox[3]
            bottoms.append(bbox[3])
        details["frame_metrics"].append(metric)

    if max_bottom_drift is not None and bottoms:
        drift = max(bottoms) - min(bottoms)
        details["bottom_drift"] = drift
        if drift > max_bottom_drift:
            issues.append(f"bottom drift {drift}px > allowed {max_bottom_drift}px")
    return details, issues


def check_asset(path: Path, args: argparse.Namespace) -> dict[str, Any]:
    result: dict[str, Any] = {
        "path": str(path),
        "ok": True,
        "issues": [],
    }
    issues: list[str] = result["issues"]

    if not path.is_file():
        issues.append("file does not exist")
        result["ok"] = False
        return result

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        issues.append(f"unsupported image extension {path.suffix}")

    size_bytes = path.stat().st_size
    result["bytes"] = size_bytes
    if args.max_bytes is not None and size_bytes > args.max_bytes:
        issues.append(f"file size {size_bytes} > max {args.max_bytes}")

    try:
        with Image.open(path) as opened:
            original_bands = opened.getbands()
            image = opened.convert("RGBA")
    except Exception as exc:  # pragma: no cover
        issues.append(f"could not open image: {exc}")
        result["ok"] = False
        return result

    result["width"] = image.width
    result["height"] = image.height
    if args.expect_width is not None and image.width != args.expect_width:
        issues.append(f"width {image.width} != expected {args.expect_width}")
    if args.expect_height is not None and image.height != args.expect_height:
        issues.append(f"height {image.height} != expected {args.expect_height}")

    alpha = alpha_values(image)
    assert alpha is not None
    has_partial_or_clear_alpha = any(value < 255 for value in alpha)
    nonzero_alpha = sum(1 for value in alpha if value > 0)
    alpha_coverage = nonzero_alpha / len(alpha) if alpha else 0.0
    result["has_alpha_channel"] = "A" in original_bands
    result["has_transparency"] = has_partial_or_clear_alpha
    result["alpha_coverage"] = alpha_coverage

    if args.require_alpha and not has_partial_or_clear_alpha:
        issues.append("alpha required but image is fully opaque")
    if args.min_alpha_coverage is not None and alpha_coverage < args.min_alpha_coverage:
        issues.append(f"alpha coverage {alpha_coverage:.4f} < min {args.min_alpha_coverage:.4f}")
    if args.max_alpha_coverage is not None and alpha_coverage > args.max_alpha_coverage:
        issues.append(f"alpha coverage {alpha_coverage:.4f} > max {args.max_alpha_coverage:.4f}")

    bbox = alpha_bbox(image)
    result["content_bbox"] = bbox
    if bbox is None:
        issues.append("no visible alpha content")

    if args.strip_frames:
        strip_details, strip_issues = check_strip(
            image,
            frames=args.strip_frames,
            expect_frame_width=args.expect_frame_width,
            expect_frame_height=args.expect_frame_height,
            max_bottom_drift=args.max_bottom_drift,
        )
        result["strip"] = strip_details
        issues.extend(strip_issues)

    result["ok"] = not issues
    return result


def paint_checkerboard(image: Image.Image, tile: int = 16) -> None:
    draw = ImageDraw.Draw(image)
    colors = ((238, 242, 246, 255), (218, 225, 232, 255))
    for top in range(0, image.height, tile):
        for left in range(0, image.width, tile):
            draw.rectangle(
                (left, top, left + tile, top + tile),
                fill=colors[((left // tile) + (top // tile)) % 2],
            )


def render_preview(paths: list[Path], out_path: Path, strip_frames: int | None) -> None:
    frames: list[Image.Image] = []
    for path in paths:
        with Image.open(path) as opened:
            image = opened.convert("RGBA")
        if strip_frames and image.width % strip_frames == 0:
            frame_width = image.width // strip_frames
            frames.extend(
                image.crop((index * frame_width, 0, (index + 1) * frame_width, image.height))
                for index in range(strip_frames)
            )
        else:
            frames.append(image)

    if not frames:
        return

    cell_width = max(frame.width for frame in frames)
    cell_height = max(frame.height for frame in frames)
    columns = min(8, max(1, math.ceil(math.sqrt(len(frames)))))
    rows = math.ceil(len(frames) / columns)
    gap = 8
    sheet = Image.new(
        "RGBA",
        (columns * cell_width + (columns - 1) * gap, rows * cell_height + (rows - 1) * gap),
        (255, 255, 255, 255),
    )
    paint_checkerboard(sheet)
    for index, frame in enumerate(frames):
        row = index // columns
        column = index % columns
        left = column * (cell_width + gap) + (cell_width - frame.width) // 2
        top = row * (cell_height + gap) + (cell_height - frame.height) // 2
        sheet.alpha_composite(frame, (left, top))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path)


def main() -> int:
    args = parse_args()
    assets = collect_assets(args)
    if not assets:
        raise SystemExit("No assets were provided. Use --asset, --dir, or --manifest.")

    results = [check_asset(path, args) for path in assets]
    ok = all(result["ok"] for result in results)
    report = {
        "schema_version": 1,
        "ok": ok,
        "asset_count": len(results),
        "assets": results,
    }

    if args.preview:
        render_preview(assets, args.preview.expanduser().resolve(), args.strip_frames)
        report["preview"] = str(args.preview.expanduser().resolve())

    if args.report:
        report_path = args.report.expanduser().resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
