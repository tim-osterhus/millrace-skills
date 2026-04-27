# Minecraft Mod QA Automation

## Purpose
Help agents design strong automated QA for Minecraft Java mods, especially when
compile-time checks and server-only smoke tests are not enough. Treat Minecraft
mod QA as a layered testing problem: white-box runtime checks first, structured
client bridge assertions second, and black-box desktop or image automation last.

## Quick Start
1. Run cheap checks first: formatting, build, unit tests, and loader-native tests.
2. Use Fabric GameTests or equivalent runtime tests for deterministic world
   interaction coverage.
3. Add a client bridge for command execution, player state, nearby block scans,
   camera control, logs, and screenshots.
4. Use Mineflayer or pathfinding only for bounded gameplay scenarios where
   movement, crafting, or repeated interaction adds signal.
5. Use native RPA or image matching only for GUI-visible behavior that cannot be
   asserted through commands, GameTests, bridge calls, or protocol state.

## Operating Constraints
- Do not treat every mod check as UI automation.
- Do not rely on Mineflayer alone and call it real client QA.
- Do not launch the client for tiny logic checks that unit tests can cover.
- Do not compare screenshots without fixed client, resource pack, GUI scale,
  camera pose, FOV, window geometry, and display scaling.
- Do not use public multiplayer servers for reproducible QA.
- Do not let automated play improvise without named setup, actions, checkpoints,
  assertions, and cleanup.
- Do not silently retry real logic failures. Retry only plausible flakes such as
  lost focus, unloaded chunks, startup races, or screenshot timing.
- Keep all automation constrained to local test worlds, private servers, or
  dedicated QA environments.

## Inputs This Skill Expects
- Minecraft version, mod loader, Java version, and Gradle wrapper command.
- The supported mod matrix and whether the target is Fabric, Forge, NeoForge, or
  another loader.
- The feature under test and its expected runtime, gameplay, and visual states.
- Available test hooks: unit tests, GameTests, commands, bridge mod, screenshots,
  prepared worlds, Mineflayer scripts, or desktop automation.
- Host constraints such as WSL/Windows split, client launch method, ports,
  window geometry, resource packs, and artifact directories.

## Output Contract
- Name the lowest reliable test layer that can prove the behavior.
- Define a deterministic fixture: seed, save, setup commands, configs, mod set,
  resource pack state, camera pose, and cleanup/reset path.
- Specify the exact observe-and-assert method: unit assertion, GameTest,
  command, bridge state query, screenshot comparison, bot scenario, or RPA step.
- Require an artifact bundle with logs, screenshots where relevant, state dumps,
  action traces, environment data, and a structured test summary.
- Classify failures as setup, launch/runtime, deterministic gameplay, visual,
  timing/flaky, unsupported test design, or unknown.

## Recommended Architecture
For WSL plus Windows setups, keep orchestration and repository work on the WSL
side, and keep the actual Minecraft client, native desktop automation, and
client-side helpers on the Windows side.

Recommended control flow:

```text
WSL agent -> local launcher/helper -> Minecraft client -> bridge/test mods -> artifacts -> WSL judge
```

Do not force visual validation through headless Linux when the real target is a
Windows client workflow. Use headless launchers for smoke coverage where they
fit, not as proof that the real rendered client works.

## Layer Selection
- Unit tests: logic, math, serialization, recipe eligibility, inventory
  transforms, and utility behavior.
- Fabric GameTests or loader-native tests: world interaction, block placement,
  machine progression, item behavior, persistence, and deterministic runtime
  assertions.
- Client bridge: command execution, player info, inventory and container state,
  nearby block scans, chat or command output capture, camera positioning, and
  screenshots.
- Mineflayer: bounded protocol-level gameplay scenarios involving movement,
  crafting, placement, gathering, or repeated interaction.
- Pathfinding or Baritone-like tooling: traversal, reachability, repeated
  navigation, or mining/building routes.
- Screenshot helpers: chunk-settled capture timing, naming discipline, visual
  baselines, and bulk evidence.
- PyAutoGUI, SikuliX, Java Robot, or similar RPA: exact GUI clicks, modal
  dialogs, HUD alignment, menus, and other behavior the game does not expose
  through a better hook.

## Test Classes
- Startup smoke: clean launch, mod load, no fatal exceptions, environment ready.
- Registration smoke: blocks, items, entities, screens, recipes, and commands
  exist and are usable.
- Interaction tests: place, use, open, insert, consume, produce, break, reload,
  and verify state or persistence.
- Visual assertion tests: HUD, overlay, tooltip, model variant, block state,
  particle, progress bar, or screen layout appears as expected.
- Scenario tests: multi-step gameplay flow with named fixture, action trace,
  checkpoints, screenshots, and terminal assertion.
- Regression replay: rerun a previously failing setup with the same seed, save,
  commands, scripts, and expected artifacts.
- Compatibility tests: only the loader, Minecraft, Java, and dependency
  combinations the mod actually supports.

## Artifact Contract
Every automated QA run should emit a structured artifact bundle.

Minimum contents:
- `run_manifest.json`
- `environment.json`
- `client.log` or extracted run log
- `test_summary.json`
- `screenshots/` when client-visible state matters
- `failures/`
- `commands_or_actions.log`
- `world_state/` dump or fixture reference
- `diffs/` when visual comparison is used

Useful manifest fields include mod version, git SHA, Minecraft version, loader
version, Java version, active mods, configs, world seed or fixture ID, scenario
name, start/end timestamps, pass/fail, failing step, screenshots, and exception
summary.

## Procedure
1. Define the feature behavior and pick the lowest reliable test layer.
2. Normalize the environment: Minecraft, loader, Java, mod set, configs,
   resource packs, render distance, GUI scale, FOV, keybinds, world seed,
   window size, display scaling, ports, and screenshot directory.
3. Run cheap checks first and stop if they fail.
4. Launch the client only after the basic checks pass.
5. Verify bridge/test helpers loaded, then enter a prepared world or fixture.
6. For each scoped test, run setup, act, observe, assert, capture artifacts, and
   cleanup/reset.
7. Escalate only when needed: GameTest or command assertion, bridge state query,
   screenshot comparison, Mineflayer scenario, then native RPA.
8. On failure, capture screenshot, player state, nearby block scan if relevant,
   inventory/container state, recent log tail, and failure class.

## Pitfalls And Gotchas
- A cinematic bot demo is not stronger than a boring deterministic harness.
- Screenshots without environment normalization are weak evidence.
- Protocol-level bot state does not prove the true rendered client experience.
- Client bridge inspection is usually more reliable than pixel clicking.
- Long 20-minute scenarios should be split into smaller named tests.
- Fixed seeds, prefab structures, prepared saves, or explicit setup commands are
  more useful than improvised worlds.
- Visual tolerances need a reason, and full original screenshots should still be
  kept as evidence.

## Progressive Disclosure
Start with the cheapest reliable layer and widen only when the feature needs
runtime, client, visual, or gameplay proof. Keep the QA plan as small as the
feature allows, but require enough artifacts that a future agent can reproduce a
failure from a clean checkout or documented fixture.

## Verification Pattern
- Confirm the plan names the test layer and explains why lower layers are not
  enough.
- Confirm the fixture and environment are deterministic.
- Confirm each test has setup, action, observation, assertion, artifacts, and
  cleanup/reset.
- Confirm screenshots are paired with normalized settings and structured state
  where possible.
- Confirm failures are classified instead of all being labeled mod bugs.
- Confirm RPA is justified as a last resort, not the default testing strategy.
