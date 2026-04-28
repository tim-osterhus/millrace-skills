# Sprite Normalization Reference

Use this branch when the sprite art is already approved and you need consistent frame slots, a shared anchor, and preview evidence.

## Normalize

- Treat the input as one horizontal strip.
- Pick a reference pose or anchor frame before normalizing the strip.
- Crop visible alpha, scale every frame with the same factor, and paste each frame onto a fixed canvas with the same bottom-center anchor.
- Keep frame 1 locked to the seed pose when downstream review needs a stable base frame.

## Helper Scripts

- `scripts/normalize_sprite_strip.py` splits a strip into fixed-size frames, rescales them with one shared factor, and writes normalized PNG frames.
- `scripts/render_sprite_preview_sheet.py` assembles the normalized frames into a contact sheet on a checkerboard background.

## Deterministic Checks

- Run `../../visual-asset-pipeline/scripts/asset_check.py` with `--strip-frames`, `--expect-frame-width`, `--expect-frame-height`, `--require-alpha`, and `--max-bottom-drift` when the sprite should stay visually aligned.
- Use the preview sheet to inspect posture, silhouette drift, and slot correctness before calling the asset done.

## Rejected Approach

- Frame-by-frame normalization with different scales or anchors per frame. That hides drift instead of fixing it.
