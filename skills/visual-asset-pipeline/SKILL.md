---
asset_type: skill
asset_id: visual-asset-pipeline
version: 1
description: "Generate, edit, normalize, and verify browser-game visual assets through OAuth-authenticated Codex image generation plus deterministic local checks."
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

# Visual Asset Pipeline

## Purpose
Use this skill when a browser-game task needs new or edited raster assets such as sprites, sprite strips, icons, cutouts, tile textures, background plates, thumbnails, or UI concept references.

This skill keeps asset creation inside the OAuth-authenticated Codex boundary. It does not require `OPENAI_API_KEY`, does not call the OpenAI Images API directly, and does not read Codex auth files. It teaches the stage to request assets through `codex exec` with `$imagegen`, then verify the resulting files with local deterministic checks.

This skill does not own queue selection, stage routing, runtime status, acceptance criteria, or escalation. Treat it as an implementation and verification aid for the active work item only.

## Quick Start
1. Decide the concrete asset contract: role, destination, dimensions, transparency, style, and in-game use.
2. Use the package-local `scripts/codex_asset_request.py` to ask OAuth-authenticated Codex for generation or editing. In this repository it lives at `skills/visual-asset-pipeline/scripts/codex_asset_request.py`; after installation it lives under the installed skill directory.
3. Save final project-consumed assets under the normal game asset path, usually `auto-games/games/<slug>/assets/`.
4. Run `scripts/asset_check.py` against generated assets or the manifest written by the request script.
5. Integrate the checked assets into the game and perform browser or screenshot verification before presenting the work as done.

Example dry-run command:

```bash
python skills/visual-asset-pipeline/scripts/codex_asset_request.py \
  --workdir /mnt/f/_evolve/millrace-games/auto-games \
  --out-dir games/example/assets/sprites \
  --prompt "Create a 4-frame transparent pixel-art hover drone sprite strip, side view, 64 px game scale." \
  --dry-run
```

Example asset check:

```bash
python skills/visual-asset-pipeline/scripts/asset_check.py \
  --asset auto-games/games/example/assets/sprites/hover-drone-strip.png \
  --require-alpha \
  --strip-frames 4 \
  --expect-height 64 \
  --report millrace-games/_visual-check/hover-drone-asset-report.json
```

## Operating Constraints
- Use OAuth-authenticated Codex as the model boundary. Do not require or request `OPENAI_API_KEY`.
- The request script defaults to `gpt-5.5`. If a future machine rejects that model, upgrade the WSL-visible Codex CLI or pass a temporary `--model` override.
- Do not inspect, parse, copy, or print `~/.codex/auth.json` or other Codex credential state.
- Do not use the imagegen CLI fallback or OpenAI SDK path unless the active task explicitly authorizes API-key based work.
- Keep generated assets original. Do not copy protected characters, maps, logos, sprites, names, or exact presentation from commercial games.
- Keep assets project-local before code references them. Do not reference images only from `$CODEX_HOME`, temporary folders, or remote URLs.
- Preserve sources non-destructively when editing an existing image. Write edited assets to a new filename unless the task explicitly asks for replacement.
- Store QA-only request logs, prompt copies, previews, and reports under `_visual-check/` or another non-shipping scratch path unless the task asks to keep them with the game.
- Keep this skill advisory. It cannot decide that a task is complete; the active stage must still meet its own result contract.

## Inputs This Skill Expects
- A game slug or target repository path.
- A short asset brief naming the in-game role and style.
- Destination directory for final assets.
- Required dimensions, frame count, transparency, and file format when known.
- Optional reference image paths for edits or identity/style preservation.
- Optional QA thresholds such as maximum bytes, expected width or height, alpha requirement, and sprite-strip frame count.

## Output Contract
- Generated or edited image files in the requested destination directory.
- A JSON manifest for each Codex asset request, with generated asset paths and notes.
- A local asset-check report when deterministic validation is run.
- A browser-game integration that references project-local files only.
- Honest notes for any blocked asset request, missing manifest, failed check, or visual mismatch.

## Procedure
1. Read the active game files and current asset conventions before requesting anything.
2. Write a specific asset brief. Include intended use, dimensions, palette, camera angle, frame layout, transparency, and avoid-list.
3. For new assets, call `codex_asset_request.py --mode generate`. For edits, provide one or more `--reference` images and use `--mode edit`.
4. Ask Codex to use `$imagegen` built-in mode, save final files under the project asset path, and write the manifest requested by the script.
5. Run `asset_check.py` against the manifest or explicit asset path. For sprites, use `--strip-frames` or expected dimensions so the checker can inspect frame slots.
6. If checks fail, make one targeted retry or use local post-processing when appropriate. Do not keep regenerating without narrowing the prompt or constraints.
7. Integrate the asset into the game. Update manifests, preload lists, CSS, canvas draw paths, or release metadata only as needed for the task.
8. Verify the asset in context: boot the game, inspect the first playable state, and capture screenshots when the visual result matters.

## Pitfalls And Gotchas
- Codex built-in image generation is not a raw scriptable image API. The stable scriptable boundary is `codex exec`, not a copied OAuth token.
- Generated files may land first in Codex-managed storage; the Codex request must move or copy final project assets into the repo before code references them.
- Transparent assets may be produced through chroma-key removal rather than native alpha. Always check alpha on the final file.
- Sprite strips drift when frames are generated independently. Prefer one strip request with exact slot count and shared style constraints.
- Text inside generated images is fragile. Keep UI labels, stats, buttons, and captions in code unless the asset truly requires baked-in lettering.
- Large batches burn Codex usage quickly and make failures harder to diagnose. Batch only tightly related variants.
- A passing dimension check does not prove an asset works in game. Always inspect the integrated result.

## Progressive Disclosure
Start with this `SKILL.md` for the common flow.

Read `references/codex-imagegen-bridge.md` when you need the exact request-script behavior, manifest schema, prompt template, or guidance for using `codex exec` safely from Millrace.

Read the script help before running unfamiliar options:

```bash
python skills/visual-asset-pipeline/scripts/codex_asset_request.py --help
python skills/visual-asset-pipeline/scripts/asset_check.py --help
```

Load donor plugin guidance only when needed. The Codex Game Studio sprite-pipeline material is useful for strip-first 2D sprites, and Build Web Apps is useful for concept-first UI mockups, but this skill keeps the Millrace-facing contract narrower.

## Verification Pattern
Run static script checks first:

```bash
python -m py_compile \
  skills/visual-asset-pipeline/scripts/codex_asset_request.py \
  skills/visual-asset-pipeline/scripts/asset_check.py
```

Run the request script with `--dry-run` before the first live generation in a new workspace.

Run `asset_check.py` on every generated file that is referenced by game code. For sprite strips, include frame count and expected dimensions. For transparent sprites, include `--require-alpha`.

For final acceptance, verify the game in a browser or screenshot-based pass. Check that the asset loads, is framed correctly, does not obscure controls, and matches visible collision or interaction geometry when relevant.
