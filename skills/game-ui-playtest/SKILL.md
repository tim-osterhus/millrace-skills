# Game UI Playtest

## Purpose
Help agents keep browser-game HUDs, menus, overlays, and playtest reports focused on readable playfields and trustworthy evidence. This is a guardrail for UI design and playtest review, not a generic frontend or QA manual.

### Use When
- the request is about a browser-game HUD, pause menu, overlay, responsive UI, or playtest review
- the player can already see a live game surface and the question is whether the UI helps or hides play
- the claim depends on visible state, motion, or screenshot evidence

### Do Not Use When
- the task is engine choice, simulation architecture, or asset pipeline planning
- the task is only browser-surface selection or local browser tool choice
- the work is generic frontend design or generic browser QA rather than browser-game UI or playtest guidance

## Quick Start
1. Classify the task first: `UI-design` when you are shaping the surface, `playtest` when you are judging a live build.
2. Name the camera or viewpoint, the player verbs, and the UI surfaces at risk before you talk layout.
3. If it is a UI-design pass, define the playfield budget: keep the center readable, push persistent HUD to edges, and collapse secondary surfaces on mobile.
4. If it is a playtest pass, boot the game, exercise the main verbs, inspect scene transitions and state changes, and capture screenshots whenever the claim is visual.
5. Report findings in severity order with reproduction steps, what the player sees, the likely owning subsystem, and the evidence captured.

## Operating Constraints
- Do not claim stack choice, engine choice, or browser-surface selection; defer those to sibling skills such as `browser-game-foundations` and `browser-local-qa`.
- Do not treat text-heavy HUD and menu surfaces as canvas-first by default; prefer DOM overlays unless the game needs something stronger.
- Do not use DOM-only proof for visual obstruction, unreadable overlays, or other claims the player experiences through pixels.
- Do not use screenshot-only proof for interaction timing, input gating, or pause/menu behavior.
- Do not let the screen drift into generic SaaS chrome, floating-card dashboards, or full-width overlays that cover live play.
- Do not expand into a generic frontend design system or a generic browser-QA checklist.
- Do not overbuild separate skills for the UI and playtest halves unless a later pass proves the split is necessary.

## Inputs This Skill Expects
- The game camera or viewpoint and the player verbs that matter.
- The UI surfaces at risk: HUD, pause menu, inventory, map, prompt, overlay, chat, or similar.
- Whether the ask is a layout/design decision or a live playtest decision.
- Desktop and mobile expectations, including whether the playfield must stay mostly clear during normal play.
- Whether the scene is DOM-heavy, canvas-heavy, or WebGL-heavy.
- Any repeated states, transitions, or checkpoints the playtest should inspect.

## Output Contract
- Start with the task class, then the camera or viewpoint, player verbs, and at-risk surfaces.
- For UI-design answers, state the playfield budget, overlay placement, pause/menu gating, and mobile collapse plan.
- For playtest answers, state the first visible state, the boot/input/main-verb/scene-transition/state checks, and whether screenshots are required.
- Describe HUD weight in terms of viewport coverage and which parts of the playfield stay clear.
- Describe overlay placement by edge, corner, center, or drawer, and say whether the surface is live or gated.
- Describe responsive breakpoints by saying what collapses, stacks, or becomes contextual on mobile.
- Report findings in severity order with reproduction steps, what the player sees, the likely owning subsystem, and the evidence that proves it.
- End with a handoff line that says what the next verifier should inspect and what evidence was captured.

## Procedure
1. Decide whether the job is UI-design, playtest, or both.
2. Name the camera or viewpoint, player verbs, and at-risk surfaces before layout or QA advice.
3. Choose the UI budget: what stays visible, what docks to the edge, and what collapses on mobile.
4. If the claim is visual, capture screenshots or equivalent visual evidence; if the claim is interactive, pair steps with the control-state evidence that proves it.
5. Check boot, input, scene transitions, and any state changes that matter to the ask.
6. Write the result as a severity-ordered report or a design recommendation, not a generic review.
7. Close with the next verifier and the evidence artifact.

## Pitfalls And Gotchas
- Generic SaaS-style chrome.
- Full-width overlays over live play.
- DOM-only proof for visual obstruction.
- Screenshot-only proof for interaction or timing.
- Turning a playtest into a generic browser-QA checklist.
- Turning a UI request into a generic frontend style exercise.
- Hiding the player verbs behind dense panels, small chips, or a pause screen that still leaks input.
- Letting all HUD, controls, notes, and lore open at once on first load.

## Progressive Disclosure
Start with the smallest useful answer: classify the task, name the camera or viewpoint, name the player verbs, and name the surfaces at risk. Expand only enough to set the playfield budget, the responsive collapse rules, and the evidence type that actually proves the claim. If the surface is already fixed and the job is only execution, stay on the proof surface instead of re-arguing the layout.

## Verification Pattern
- Confirm the response class is explicit: UI-design, playtest, or both.
- Confirm the camera or viewpoint, player verbs, and at-risk UI surfaces are named before advice.
- Confirm visual claims have screenshot-backed evidence when the pixels matter.
- Confirm interaction claims have step-by-step reproduction and control-state proof.
- Confirm findings are severity-ordered and tied to a likely owning subsystem.
- Confirm the handoff names the next verifier and the captured evidence.
