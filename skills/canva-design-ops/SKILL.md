---
asset_type: skill
asset_id: canva-design-ops
version: 1
description: Guardrail for Canva presentation, resize, and translation workflows with exact source identification, preserve-original safety, brand-kit confirmation, and clear partial-failure reporting.
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

# Canva Design Ops

## Purpose
Help agents handle Canva designs without editing the wrong source, overwriting originals, or hiding failed variants. This is a guardrail, not a Canva tutorial.

### Use When
- The request is to create, resize, translate, localize, duplicate, export, or polish a Canva design.
- The user gives a Canva URL, design name, or design link and wants a Canva-based variant or export.
- The work needs an on-brand presentation, a multi-format resize set, or a translated copy.

### Do Not Use When
- The task is generic graphic design outside Canva.
- The request is raw image editing or browser QA.
- The source design is already fixed and no copy or variant is being made.

## Quick Start
1. Identify the exact source design first. If search returns multiple matches, stop until the exact one is proven.
2. Confirm the brand kit when more than one kit is available. If there is only one, use it.
3. Pick one mode.
4. Keep the original design untouched unless the user explicitly asked for a copy or variant.
5. Report successes and failures separately, with export or edit links named for each finished output.
6. In translation mode, warn about text expansion or layout risk before save.
7. End with a handoff line that names the next verifier and the evidence captured.

## Operating Constraints
- Do not guess at source identity, brand kit, or target formats.
- Do not edit the original when a copy or localized version is needed.
- Preserve names, dates, metrics, and brand language unless the user asks to change them.
- Do not hide partial failures behind a generic success claim.
- Do not turn the skill into a Canva how-to manual or a format catalogue.
- Prefer a single batched edit or save when the tool flow allows it.

## Inputs This Skill Expects
- A Canva URL, design name, or other identifier for the source design.
- The requested mode: presentation, resize, or translation.
- The target audience, language, or formats when relevant.
- The available brand kits when more than one kit exists.
- Any note that the user wants a copy, variant, or export.

## Output Contract
- State the confirmed source design and the mode first.
- Presentation mode: build a slide plan, show candidate directions, then create the final editable deck only after selection.
- Resize mode: create the requested variants from copies, use the exact target formats the user asked for, keep successful outputs even if one format fails, and list each result with its export link.
- Translation mode: duplicate first, translate in a batched pass when possible, preserve meaning and formatting cues, and name any text-expansion or layout risk before save.
- End with a concise handoff line naming the next verifier and the evidence captured.

## Procedure
1. Confirm the exact source design before acting.
2. Confirm the brand kit when multiple kits are available; use the single kit automatically.
3. Choose the mode and keep the original untouched unless the user explicitly asked for a copy or variant.
4. For presentation work, generate candidate directions before the final deck is created.
5. For resize work, use the exact target formats the user asked for, continue successful variants even if one format fails, and report failures separately.
6. For translation work, duplicate first, preserve meaning and formatting cues, and warn before save if layout risk is likely.
7. Return links or equivalent results for every completed output.
8. Finish with the next verifier and evidence captured.

## Pitfalls And Gotchas
- Rejected trope: a Canva how-to manual or an exhaustive social-format matrix.
- Better alternative: one guardrail with exact source identification, a clear mode switch, and explicit success/failure reporting.
- Editing the original file when the user wanted a copy or translated variant.
- Guessing the source design or brand kit instead of proving it.
- Hiding partial failures inside a single success summary.
- Saving a translated copy before calling out layout risk.

## Progressive Disclosure
Start with the smallest useful answer: source design, mode, kit, outputs, and risks. If the request needs deeper Canva-specific detail, keep it tied to the chosen mode instead of widening into a generic design guide.

## Verification Pattern
- Confirm the answer names the exact source design.
- Confirm the original stays untouched unless the user requested a variant.
- Confirm the mode-specific safety gate is visible.
- Confirm failed variants are reported separately from successful ones.
- Confirm translation mode warns about text growth before save.
- Confirm the result avoided becoming a tutorial or a format catalogue.

Handoff: next verifier is the checker child; evidence captured is exact source identity, brand-kit choice, target formats or language, candidate preview or translation risk, and the links for completed outputs.
