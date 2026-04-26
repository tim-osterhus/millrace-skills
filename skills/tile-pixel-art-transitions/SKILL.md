# Tile Pixel Art Transitions

## Purpose
Help agents plan tile-based pixel art so adjacent terrain reads as deliberate transitions rather than isolated square stamps. Use this for top-down or side-view maps, sprite-sheet scenes, and web or canvas game prototypes that need believable boundaries between grass, dirt, water, stone, foliage, and similar regions.

## Quick Start
1. Decide whether the scene needs smooth transitions at all. If the art is intentionally hard-edged, modular, or decorative, keep the blocky look and stop forcing blends.
2. Pick one primary transition model first: Wang tiles, blob or autotile masks, edge or corner bitmasks, or rule-based terrain placement.
3. Derive the minimum practical variant set from that model, usually fill, edges, inner corners, outer corners, junctions, and an isolated fallback where the model needs them.
4. Choose the tool after the model is chosen: Tiled for terrain brushes and automapping, LDtk for IntGrid auto-layers, Pixelorama or Piskel for tile authoring, Pillow for terminal previews.
5. Include a repeatable seam-preview or contact-sheet check before calling the tileset done.

## Operating Constraints
- Do not treat every tile as a standalone stamp.
- Do not mix Wang, blob, bitmask, and rule-based systems without naming one primary model.
- Do not ship a tileset plan without the edge, corner, inner-corner, junction, and isolated variants the model actually requires.
- Do not hard-code the guidance to one editor or engine.
- Do not overbuild a full asset-production pipeline when a lightweight editor plus a terminal fallback is enough.
- Do not let polish hide visible seams, mismatched corners, or impossible adjacency rules.

## Inputs This Skill Expects
- Scene type and camera angle.
- Tile size, palette limits, and intended art style.
- Target engine, editor, or export format.
- Existing tile samples, adjacency rules, and the kinds of seams to avoid.
- Whether the map is authored, repeated from a small set, or intended to tile infinitely.

## Output Contract
- Name the primary transition model.
- List the minimum practical variant set.
- Choose the editor or tool only after the model is chosen.
- Include one deterministic seam-preview or contact-sheet QA step.
- State one generic trope rejected and the better alternative.
- Preserve explicit exceptions for intentionally hard-edged, modular, or decorative pixel art.

## Procedure
1. Classify the scene as transition-heavy or intentionally hard-edged.
2. Pick one adjacency model and write the rule language in plain English.
3. Trim the tile inventory to the smallest set that still closes the seams.
4. Pick the lightest tool that supports that model.
5. Build a repeatable preview: a contact sheet, a wrapped 3x3 map, or a seam grid that places every important boundary next to itself.
6. Check for repeated seams, corner errors, and breakpoints in the transition logic.
7. If the style is intentionally blocky, say so and stop forcing blends.

## Pitfalls And Gotchas
- Rejected trope: isolated square stamps for each terrain type.
- Better alternative: one primary transition model plus edge, corner, junction, and fallback variants, backed by a deterministic seam preview.
- Hard-coding one editor, one engine, or one export path.
- Mixing transition systems because the tile set started late.
- Painting one-off tiles that cannot repeat cleanly.
- Shipping only base tiles when the scene needs boundary variants.
- Expanding into a full art-production pipeline when a transition guardrail would do.
- Forcing smooth blends onto work that is meant to stay modular or decorative.

## Progressive Disclosure
Start with the scene type and adjacency model, then the variant set, then the tool, then the preview. Keep the skill narrow enough that it helps an agent decide, inspect, and validate without becoming a generic pixel-art manual.

## Verification Pattern
- Confirm the first answer names one primary transition model.
- Confirm the tile inventory covers the boundaries the model requires.
- Confirm the chosen tool matches the model instead of driving it.
- Confirm a deterministic preview or contact sheet exists and would expose seams.
- Confirm one generic trope was rejected in favor of a better transition-aware alternative.
- Confirm the final advice preserves hard-edge exceptions when transitions are not desired.
