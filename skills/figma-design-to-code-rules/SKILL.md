---
asset_type: skill
asset_id: figma-design-to-code-rules
version: 1
description: Guardrail for translating Figma into code and compact repo rules with design-context-first evidence, screenshot validation, and repo-convention reuse.
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

# Figma Design To Code Rules

## Purpose
Help agents translate Figma into production code or compact repo rules without drifting into a generic Figma manual. This is a guardrail, not a canvas-editing skill or frontend course.

### Use When
- The user provides a Figma URL, node selection, screenshot, or export context and wants code in the repo.
- The user asks to implement, review, or refactor a Figma-driven UI surface.
- The user asks to create or update `AGENTS.md`, `CLAUDE.md`, or Cursor rules for Figma-to-code work.
- The task depends on design tokens, component mapping, screenshots, or visual comparison evidence.

### Do Not Use When
- The user wants to edit nodes inside Figma itself; use `figma-use` instead.
- The request is generic frontend design with no Figma source and no repo conventions to preserve.
- The task is pure screenshot QA with no implementation or rule-synthesis decision.
- Another more specific skill already owns the same surface.

## Quick Start
1. Classify the request first: implementation guidance or rules extraction.
2. If it is implementation guidance and Figma MCP is available, fetch design context and a screenshot before giving code advice.
3. If the design context is too large, use metadata to narrow the node set and fetch only the needed children.
4. Reuse existing repo components, tokens, and styling conventions before inventing new ones.
5. Keep asset handling local and use supplied Figma assets instead of new icon packages or stand-ins.
6. If it is rules extraction, inspect the codebase conventions first and write the smallest ruleset that preserves them.
7. End with the next verifier and the evidence captured.

## Operating Constraints
- Treat Figma output as evidence, not final code style.
- Require both design context and screenshot evidence before implementation guidance when Figma MCP is available.
- If Figma MCP is unavailable, proceed from the available screenshot or export and state the missing design data explicitly.
- Do not guess at token mapping, spacing, or component reuse when the source data is incomplete.
- Preserve unrelated instructions when writing `AGENTS.md`, `CLAUDE.md`, or Cursor rules; append or modularize instead of overwriting.
- Keep the fallback path explicit when MCP data is unavailable or truncated.
- Stay compact enough to behave like a guardrail, not a vendor tutorial.

## Inputs This Skill Expects
- Figma URL, node selection, screenshot, or export context.
- Repository path or rule target when the task is rules extraction.
- Existing component, token, and styling conventions when translating to code or rules.
- Asset payloads returned by Figma when available.

## Output Contract
- Implementation guidance: name the likely node or selection path, the design-context fields used, the screenshot evidence, the repo components or tokens reused, and any unavoidable deviations.
- Rules extraction: name the target rule file or family, the codebase conventions observed, and the smallest rule set that captures them.
- For both modes, include one concrete verification step and one rejected generic trope.
- Handoff: next verifier is the checker or implementer; evidence captured is a screenshot comparison, token mapping, or rule-file diff.

## Procedure
1. Classify the request as implementation guidance or rules extraction.
2. For implementation guidance:
   - get design context first
   - if it is too large, use metadata to narrow the node set
   - get a screenshot for the same target before coding guidance
   - translate the result into project conventions instead of copying Tailwind or literal Figma output
   - validate against the screenshot before marking complete
3. For rules extraction:
   - inspect the codebase conventions first
   - identify the smallest rule file or rule family that should change
   - encode the repo's real component, token, spacing, import, and testing conventions
   - preserve unrelated instructions and avoid generic design-system prose
4. Use Figma assets directly when provided; do not create stand-in icons or duplicate packages.
5. Redirect any canvas-edit request to `figma-use` instead of trying to edit Figma here.
6. Stop when the current request has enough evidence to act; do not widen into a general design handbook.

## Pitfalls And Gotchas
- Rejected trope: a generic Figma manual or broad frontend design course.
- Better alternative: one compact two-mode guardrail that separates implementation evidence from rule synthesis.
- Rejected trope: copying literal Figma output into code without repo conventions.
- Better alternative: map the design into the project's existing components and tokens first.
- Rejected trope: overwriting unrelated agent instructions while adding repo rules.
- Better alternative: append or modularize the new guidance.
- Rejected trope: pretending MCP data exists when the design context or screenshot is missing.
- Better alternative: say the task is blocked on missing design evidence or proceed with the explicit fallback.

## Progressive Disclosure
Start with the smallest useful read of the request, then widen only enough to decide mode and evidence. Keep implementation guidance and rules extraction distinct, but do not split them into separate skills unless they genuinely need different owners. If the fallback path is all that is available, make that fact explicit instead of filling gaps with invented detail.

## Verification Pattern
- Confirm the answer starts by classifying the request.
- Confirm implementation guidance cites both design context and screenshot evidence when MCP is available.
- Confirm rules extraction starts from existing repo conventions and produces the smallest useful rule delta.
- Confirm unrelated instructions are preserved instead of replaced.
- Confirm the answer ends with one concrete verifier artifact and one next step.
