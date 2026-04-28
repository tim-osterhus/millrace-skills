---
asset_type: skill
asset_id: browser-local-qa
version: 1
description: "Guardrail for choosing the smallest reliable local browser verification surface and evidence type."
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

# Browser Local QA

## Purpose
Help agents choose the smallest reliable browser-verification surface for local UI work, then capture evidence that actually proves the claim. This is a guardrail, not a browser automation manual.

### Use When
- the task is about localhost, file URLs, or another local UI surface
- the page is already open in the Codex in-app browser and needs inspection
- the work needs a repeatable browser flow, artifact capture, or regression proof
- the target is a desktop or native window and browser capture is not enough

### Do Not Use When
- the surface is already fixed and only execution remains
- the task is general web research or remote scraping
- the user wants implementation detail for one browser surface instead of surface selection

## Quick Start
1. Start with the live surface the task already has, not with the most powerful tool.
2. Choose the smallest reliable layer that can prove the claim: in-app browser, Playwright CLI, Playwright Interactive, or screenshot capture.
3. If the claim is visual, collect screenshot evidence; if it is structural, collect DOM or snapshot evidence.
4. Prefer Playwright Interactive only when the same browser state must be reused across iterations.
5. Stop once one authoritative signal proves the point; do not re-prove it through extra surfaces.
6. End with the next verifier and the evidence that was intentionally captured.

## Operating Constraints
- Do not use DOM-only proof for a visual claim.
- Do not use screenshot-only proof for a structural claim.
- Do not treat screenshot capture as a replacement for actual interaction.
- Do not start with persistent Playwright unless state reuse is the reason.
- Do not escalate to a heavier surface when the current surface already proves the claim.
- Do not turn this into a bootstrap or command-reference skill.
- Do not keep checking the same fact across multiple surfaces after one authoritative signal exists.

## Inputs This Skill Expects
- The local UI surface and whether it is already open.
- Whether the claim is visual, structural, interactive, or desktop-native.
- Whether the flow needs repeatable automation or persistent session reuse.
- Whether browser capture can reach the needed chrome or window boundary.

## Output Contract
- Name the chosen surface first.
- Name the first thing to inspect before the next action.
- Name the evidence artifact that will actually be useful to the next verifier.
- Explain why DOM-only proof or screenshot-only proof would be insufficient when that is the case.
- Keep the answer at planning level unless the task explicitly asks for execution detail.

## Procedure
1. Read the surface the user already has before switching tools.
2. Classify the claim as visual or structural, then pick the narrowest surface that can prove it.
3. Use the in-app browser when the Codex browser already has the context and the task is visible-state oriented.
4. Use Playwright CLI when the flow needs repeatable terminal-driven automation, snapshots, or artifacts.
5. Use Playwright Interactive when the same browser session must survive across iterations.
6. Use screenshot capture when the browser cannot reach the needed desktop or native chrome boundary.
7. Capture only the evidence that proves the claim and hand that forward.

## Pitfalls And Gotchas
- Rejected trope: defaulting to the most automated surface because it feels more rigorous.
- Better alternative: choose the smallest surface that can still prove the claim and keep the proof direct.
- Rejected trope: using screenshots to stand in for interaction evidence.
- Better alternative: interact on the real surface, then capture screenshots only as proof.
- Rejected trope: relying on DOM alone for visible layout, overlay, or pixel-sensitive state.
- Better alternative: pair structural evidence with screenshots only when the claim is visual.
- Rejected trope: bouncing across surfaces after one authoritative signal already answered the question.
- Better alternative: stop when the selected surface has already proven the point.

## Progressive Disclosure
Start with the narrowest read of the task: what surface exists, what kind of claim must be proven, and what evidence the next verifier will need. Expand only enough to choose between in-app browser, Playwright CLI, Playwright Interactive, and screenshot capture cleanly. Keep the skill compact so it behaves like a guardrail instead of a browser automation course.

## Verification Pattern
- Confirm the selected surface matches the claim type.
- Confirm visual claims have screenshot evidence when needed.
- Confirm structural claims have DOM or snapshot evidence when needed.
- Confirm Playwright Interactive is only chosen when session reuse matters.
- Confirm the response names one actionable artifact and one next verifier.
- Confirm the answer avoided redundant cross-surface re-checking.
