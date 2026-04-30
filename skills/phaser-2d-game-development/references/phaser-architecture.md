# Phaser 2D Architecture Notes

## Purpose
Keep the shipped skill small while still giving agents a concrete seam for Phaser 2D browser games.

## Recommended Module Split

Use one shell around one gameplay seam:

```text
src/
  game/
    assets/
    camera/
    scenes/
    state/
    systems/
  ui/
    overlay/
```

- `game/scenes/` should boot, preload, and bridge to runtime state.
- `game/systems/` or `game/state/` should own game truth.
- `game/assets/` should expose stable manifest keys.
- `game/camera/` should hold shared camera helpers if the project needs them.
- `ui/overlay/` should hold DOM HUDs, menus, and pause surfaces when the game uses them.

## Scene Boundary

- Boot and preload scenes set up the world and load by manifest key.
- Gameplay scenes read state and emit intents, not rules.
- Optional shell or menu scenes should stay thin and only orchestrate transitions.
- If a scene starts holding score, inventory, progression, or objective truth, move that truth to a system or state module.

## Asset Discipline

- Group assets by domain: characters, environment, UI, audio, and effects.
- Keep keys human-readable and stable.
- Avoid letting file paths leak into gameplay code.
- Change the manifest once when a key changes; do not chase string literals across scenes.

## Camera And Presentation

- Choose the camera model early: locked, follow, room-based, or tactical pan.
- Keep camera logic separate from game rules.
- Use restrained shake, hit-stop, and parallax when they improve readability.
- If camera motion makes the problem harder to read, reduce it before adding more effects.

## Input And Collision

- Map physical controls to actions in one place.
- Let collisions and overlaps produce events or intents that systems can resolve.
- Keep input and collision wiring explicit so the scene does not become the rule engine.

## HUD And Menu Placement

- Default text-heavy HUDs and menus to DOM overlays.
- Keep the canvas for the world, motion, and combat readability.
- Put persistent HUD elements at edges and keep the playfield center clear unless the design needs otherwise.
- Move dense configuration or pause flows out of the canvas unless the project specifically needs in-canvas UI.

## Verification Notes

- Prove preload completeness before judging gameplay logic.
- Prove scene transitions with live browser state, not just static text.
- Prove visual claims with screenshots when pixels matter.
- Prove interaction claims with the control-state evidence that shows the player can move, collect, pause, or advance.
- For HUD overlap bugs, capture both the overlay and the playfield in the same frame.

## Anti-Patterns

- Storing game truth in scene-local mutation.
- Building a thick scene that owns both rendering and rules.
- Hard-coding asset file paths throughout gameplay code.
- Putting dense HUD text directly on the canvas without a reason.
- Using camera effects to hide readability problems.
