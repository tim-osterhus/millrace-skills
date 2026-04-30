---
asset_type: "skill"
asset_id: "phaser-2d-game-development"
version: 1
description: "Guardrail for Phaser 2D browser-game implementation and review."
advisory_only: true
capability_type: "planning-guardrail"
recommended_for_stages:
  - "builder"
  - "checker"
  - "fixer"
forbidden_claims:
  - "queue_selection"
  - "routing"
  - "retry_thresholds"
  - "escalation_policy"
  - "status_persistence"
  - "terminal_results"
  - "required_artifacts"
---

# Phaser 2D Game Development

## Purpose
Use this skill for Phaser 2D browser-game work after the stack is already Phaser, TypeScript, and Vite. It keeps scene code thin, keeps rules outside the scene when practical, and treats DOM HUDs and screenshot proof as first-class.

### Use When
- implementing or reviewing a Phaser 2D browser game
- the request needs scene boot or preload flow, gameplay scenes, camera logic, input mapping, collisions, animation, or DOM HUDs
- the task includes playable-state verification or evidence for a visual claim

### Do Not Use When
- engine choice is still open
- the task is generic browser-game planning, generic frontend UI, or pure asset production
- the work is not Phaser-based

## Quick Start
1. Classify the request first: `implement`, `review`, `fix`, `verify`, or `refactor`.
2. Draw the boundary first: simulation owns game truth; Phaser scenes adapt it for rendering and input.
3. Check the preload path, stable asset manifest keys, camera model, input map, collision setup, HUD placement, and proof requirement.
4. Prefer DOM overlays for text-heavy HUDs and menus unless the canvas presentation is part of the game.
5. End with the next verifier and the evidence it should capture.

## Operating Constraints
- Keep boot, preload, and scene orchestration thin.
- Keep game rules, objectives, movement, and progression outside scene-local mutation where practical.
- Treat sprites, emitters, tweens, and camera rigs as view state.
- Keep asset lookups on stable manifest keys instead of scattered file paths.
- Keep dense HUD and menu surfaces in the DOM unless there is a reason not to.
- Do not turn this into a Phaser manual or a browser-game foundation essay.

## Inputs This Skill Expects
- The scene layout and game loop already chosen for a Phaser project.
- The gameplay verbs, UI surfaces, and camera behavior that matter.
- The asset domains that need stable keys.
- The proof surface: runtime behavior, screenshots, or both.

## Output Contract
- State the scene/system boundary before implementation details.
- Name the preload, manifest, camera, input, HUD, and verification checks that matter.
- Distinguish render-state evidence from interaction-state evidence.
- Call out when screenshot-backed proof is required for a visual or gameplay claim.
- Close with a concrete next verifier and what it should inspect.

## Procedure
1. Confirm the task class and the seam you are changing.
2. Keep game truth in systems or state modules; let scenes orchestrate and render.
3. Wire preload and manifest keys before gameplay logic depends on assets.
4. Set camera, input, and HUD ownership explicitly.
5. Verify the playable state with the narrowest proof that actually answers the claim.
6. Stop once the contract is satisfied; do not widen into extra framework advice.

## Pitfalls And Gotchas
- Scene-local mutation becoming the source of truth.
- Asset paths duplicated across gameplay code.
- HUD and menus forced into the canvas just because it is convenient.
- Camera motion hiding the actual problem.
- Screenshot-only proof for interaction timing, or DOM-only proof for visual obstruction.

## Progressive Disclosure
Start with the smallest useful answer: task class, scene/system boundary, preload and manifest checks, camera and input ownership, HUD placement, and proof type. Expand only enough to fix the request without turning the skill into a tutorial.

## Verification Pattern
- Confirm the answer names the task class first.
- Confirm the scene/system boundary is explicit.
- Confirm stable asset keys, input mapping, camera behavior, and HUD placement are called out.
- Confirm visual claims mention screenshot or browser proof when needed.
- Confirm the handoff names the next verifier and the evidence to capture.
