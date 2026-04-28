---
asset_type: skill
asset_id: browser-game-foundations
version: 1
description: "Guardrail for choosing the browser-game fantasy, stack, boundaries, inputs, assets, and handoff before implementation."
advisory_only: true
capability_type: planning-guardrail
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

# Browser Game Foundations

## Purpose
Help agents lock the non-negotiable foundation for a browser game before implementation starts: fantasy, core loop, engine, simulation/render boundaries, input, assets, save/debug/perf, and playtest handoff. This is a guardrail, not a browser-game course.

### Use When
- the user has not yet chosen Phaser, Three.js, React Three Fiber, or raw WebGL
- the request spans gameplay, UI, assets, and QA boundaries
- the architecture needs a first pass before code exists

### Do Not Use When
- the runtime track is already locked to one specialist engine and only implementation details remain
- the task is only asset production, UI polish, or QA
- the game architecture is already fixed and only a code change is needed

## Quick Start
1. Name the player fantasy and the core loop in one sentence each.
2. Choose the stack from the game shape: Phaser for 2D sprite or tile games, Three.js for plain TypeScript 3D, React Three Fiber for React-hosted 3D, raw WebGL only for shader-first projects.
3. Draw the seam: simulation owns game truth; rendering only presents it.
4. Keep HUD and menus in DOM overlays by default unless there is a clear reason not to.
5. Define the input action map once, then map physical controls to actions in one place.
6. Group assets by stable manifest keys, not ad hoc filenames.
7. Set save, debug, and performance boundaries before implementation.
8. End with a playtest handoff that says what the next specialist must verify.

## Operating Constraints
- Do not mix gameplay rules directly into scene callbacks or component render code.
- Do not treat the renderer as the source of truth for game state.
- Do not force HUD and menus into the canvas when DOM overlays will do.
- Do not let filenames become the public asset API.
- Do not hide debug toggles, perf probes, or save boundaries behind implementation noise.
- Do not write a generic engine comparison essay when one decisive stack choice is enough.
- When 3D is chosen, lock units, origins, and collision conventions early enough that the specialist implementation can stay consistent.

## Inputs This Skill Expects
- The player's fantasy, genre, and session shape.
- Whether the game is 2D or 3D, and whether an app already lives in React.
- The intended input devices and the actions the player must perform.
- The asset domains that need stable grouping: characters, environment, UI, audio, FX, or equivalent.
- Save, debug, and performance expectations that matter before code exists.

## Output Contract
- State the stack choice first and keep it explicit.
- State the core loop next, then the simulation/render boundary.
- Include an input action map, an asset grouping plan, and save/debug/perf boundaries.
- Prefer DOM overlays for text-heavy HUD and menu surfaces.
- Name one playtest hook or verification step that the next specialist should run.
- Keep the answer short enough that implementation can begin without renegotiating the architecture.

## Procedure
1. Lock fantasy and the core loop.
2. Choose the engine only after the game shape is clear.
3. Separate simulation from rendering and name the boundary in plain language.
4. Define the input action map in one place.
5. Group assets with stable manifest keys and clear domains.
6. Set save/debug/perf boundaries early.
7. Close with a playtest handoff that names the next proof step.

## Pitfalls And Gotchas
- Rejected trope: a long engine or framework comparison that postpones the real decision.
- Better alternative: one decisive stack choice plus a boundary contract that another specialist can implement directly.
- Mixing state ownership between game logic and render state.
- Treating renderer objects as save data.
- Leaving HUD, menu, and accessibility surfaces trapped inside the playfield by default.
- Letting debug hooks or perf probes appear only after implementation has already drifted.
- Expanding into a browser-game textbook instead of a planning guardrail.

## Progressive Disclosure
Start with the smallest useful answer: fantasy, loop, stack, boundary, inputs, assets, save/debug/perf, handoff. If the request needs deeper engine detail, route that detail to the specialist implementation skill instead of padding this one.

## Verification Pattern
- Confirm the answer names a stack and does not waffle.
- Confirm simulation owns game truth and rendering only presents it.
- Confirm the input map is explicit and the asset grouping uses stable keys.
- Confirm save/debug/perf boundaries are stated, not implied.
- Confirm one playtest hook is named.
- Confirm the response avoided turning into an engine manual or generic game-dev overview.
