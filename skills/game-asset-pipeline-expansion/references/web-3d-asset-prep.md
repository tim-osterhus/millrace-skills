# Web 3D Asset Prep Reference

Use this branch when the asset is a prepared model that needs browser-ready cleanup, not fresh scene code or modeling guidance.

## Prep Contract

- Normalize transforms before ship.
- Keep scale and orientation consistent with the runtime's world units.
- Use GLB or glTF 2.0 as the shipping format.
- Reduce texture cost when the runtime budget is tight.
- Add collision proxies or LODs only when the target scene actually needs them.

## Typical Tooling

- Export from the DCC tool to GLB or glTF 2.0.
- Inspect and optimize with `gltf-transform inspect`, `gltf-transform optimize`, and related cleanup commands when available.
- Use `gltf-transform prune`, `gltf-transform dedup`, `gltf-transform meshopt`, or `gltf-transform ktx2` only when the target runtime supports the chosen decode path.
- Validate loadability in the target browser or engine runtime after export.
- Track texture formats, material reuse, and any compression choices in the handoff notes.

## Deterministic Checks

- Verify the asset loads without console or parser errors.
- Confirm the model scale matches the in-game reference unit.
- Confirm texture sizes and material counts stay within the runtime budget.
- If collision or LOD is present, confirm the runtime sees the intended proxy or level.

## Rejected Approach

- Treating the DCC export as automatically ready because it opened once in a viewer. Browser loadability and runtime scale still need a real check.
