---
asset_type: skill
asset_id: game-asset-pipeline-expansion
version: 1
description: "Guardrail for sprite-strip normalization, GLB / glTF prep, and browser-game asset verification."
advisory_only: true
capability_type: asset-pipeline
recommended_for_stages:
  - builder
  - checker
  - fixer
forbidden_claims:
  - queue_selection
  - routing
  - retry_thresholds
  - escalation_policy
  - status_persistence
  - terminal_results
  - required_artifacts
---

# Game Asset Pipeline Expansion

## Purpose

Use this skill when the asset already exists and the task is to make it browser-ready, not when the task is to create or repaint the art itself. It owns sprite-strip normalization and preview evidence for 2D assets, plus GLB / glTF preparation and deterministic verification for 3D assets. Keep the sprite details in `references/sprite-normalization.md` and the 3D details in `references/web-3d-asset-prep.md`; keep source-art generation in `visual-asset-pipeline`.

## Quick Start

1. Identify the branch: sprite-strip normalization or GLB / glTF prep.
2. Read the matching reference file before touching the asset.
3. Normalize or prep the asset with the package helper script or the external 3D export and optimization tools named in the reference.
4. Run the sibling deterministic check on the prepared output, then render or inspect browser-facing preview evidence.
5. Keep the source-art boundary explicit in your notes so downstream agents know whether they are still editing the art or only preparing it for ship.

## Operating Constraints

- Do not use this skill to generate or repaint source art.
- Do not own runtime scene code, camera work, HUD work, or engine choice.
- Do not collapse the sprite and 3D branches into one generic asset-management essay.
- Do not invent a new checker when the sibling `visual-asset-pipeline/scripts/asset_check.py` already covers deterministic validation.
- Do not hide browser verification behind a local file check.
- Keep the package portable: the scripts and references should be usable without private state.

## Inputs This Skill Expects

- A prepared sprite strip, sprite source frame, or GLB / glTF asset that is already ready for prep work.
- The intended game scale, frame count, output size, and anchor expectations for sprite work.
- Texture-budget, collision, LOD, and loadability expectations for 3D work.
- The target browser or browser-based runtime that will consume the asset.
- Any existing preview, reference frame, or seed asset needed to lock scale or anchors.

## Output Contract

- Normalized sprite frames and a preview sheet or contact sheet for 2D work.
- Browser-ready GLB / glTF output and a clear note about compression, collision, and LOD choices for 3D work.
- Deterministic asset-check results from the sibling checker where applicable.
- Honest blocker notes when an asset cannot be made ready without changing upstream art or runtime assumptions.

## Procedure

1. Classify the work as sprite or 3D and stay on that branch.
2. Read the matching reference and choose the smallest safe prep step.
3. Run the package helper script for sprite normalization or preview generation, or use the named 3D export and optimization tools from the reference.
4. Run deterministic validation and inspect the preview or browser-facing evidence.
5. If the asset still fails loadability, scale, transparency, or frame-slot checks, repair the asset before claiming readiness.
6. Leave the source-art skill boundary intact so future work can still distinguish creation from prep.

## Pitfalls And Gotchas

- Rejected trope: a single generic asset-pipeline manual that tries to own art creation, runtime integration, and ship validation in one blob.
- Better alternative: one narrow prep skill with a sprite reference, a 3D reference, and the sibling checker reused for deterministic checks.
- Do not regenerate source art in this package.
- Do not split sprite and 3D into separate skills unless the work itself needs that split.
- Do not rely on preview polish alone when a deterministic check or browser run would expose the problem.

## Progressive Disclosure

Start with the branch decision, then read only the matching reference. Pull in the other branch only when the task genuinely spans both sprite and 3D asset prep. Keep `visual-asset-pipeline` as the source-art sibling and this skill as the browser-game prep layer.

## Verification Pattern

- Confirm the sprite output has stable anchors, frame slots, and a preview sheet that exposes drift.
- Confirm the 3D output is loadable, scaled correctly, and still within the texture and material budget the runtime can afford.
- Confirm the sibling deterministic checker passes on the prepared asset where it applies.
- Confirm the final advice ends at browser-game readiness, not at a generic file conversion step.
