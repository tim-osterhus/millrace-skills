# Codex Imagegen Bridge

This reference describes how Millrace should request visual assets without API keys.

## Boundary

Use `codex exec` as the model boundary:

```text
Millrace stage -> codex_asset_request.py -> codex exec with $imagegen -> project files -> asset_check.py
```

Do not extract or reuse Codex OAuth tokens. The Codex CLI owns authentication state.

## Request Script

`scripts/codex_asset_request.py` builds a non-interactive Codex prompt, runs `codex exec`, and asks Codex to:

- use built-in `$imagegen`
- avoid API-key and SDK fallback paths
- save final files under the requested project destination
- write a manifest JSON
- preserve references non-destructively when editing

Use `--dry-run` to inspect the generated command and prompt without spending a Codex image generation turn.

## Manifest Schema

The request asks Codex to write:

```json
{
  "schema_version": 1,
  "status": "complete",
  "mode": "generate",
  "workdir": "/mnt/f/_evolve/millrace-games/auto-games",
  "assets": [
    {
      "path": "games/example/assets/sprites/drone-strip.png",
      "role": "sprite-strip",
      "description": "4-frame transparent hover drone animation",
      "width": 256,
      "height": 64,
      "notes": "Frame slots are 64x64."
    }
  ],
  "notes": "Generated with Codex built-in image generation."
}
```

If blocked, Codex should still write a manifest with `status: "blocked"` and a concise reason.

## Prompt Template

For sprites:

```text
Use $imagegen built-in mode.
Create an original transparent PNG sprite strip for a browser game.
Asset role: <role>
Destination: <out-dir>/<file-name>
Frame layout: exactly <N> horizontal equal slots, <W>x<H> per slot.
Style: <pixel-art or painted or UI icon>, readable at game scale.
Preserve: <palette, silhouette, facing direction, proportions>.
Avoid: protected IP, text labels, scenery, shadows if transparency is required, watermarks.
After saving the file, write the requested manifest JSON.
```

For edits:

```text
Use $imagegen built-in mode.
Use the attached reference image as the edit target or identity reference.
Change only <specific change>.
Keep <silhouette, palette, frame size, face, pose, game readability>.
Save a new file; do not overwrite the source.
After saving the file, write the requested manifest JSON.
```

## Checks

Use `scripts/asset_check.py` to verify:

- file existence
- PNG/WebP/JPEG loadability
- dimensions
- alpha channel and alpha coverage
- file size
- sprite-strip slot count
- non-empty frame slots
- optional preview sheet

This checker is intentionally not a substitute for browser verification.
