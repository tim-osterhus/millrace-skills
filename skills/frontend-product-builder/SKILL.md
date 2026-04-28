---
asset_type: skill
asset_id: frontend-product-builder
version: 1
description: "Guardrail for building frontend product surfaces from real workflows, state, and browser-verified interaction instead of generic landing-page scaffolds."
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

# Frontend Product Builder

## Purpose
Help agents build frontend product surfaces from the real workflow, state model, and browser-verified interaction instead of generic landing-page scaffolds. This is a guardrail, not a frontend course or a browser QA manual.

### Use When
- the task is a new frontend app, tool, dashboard, game, site, or redesign
- the first screen should be the real product, not a marketing wrapper
- the surface needs real state, controls, or responsive browser checks

### Do Not Use When
- the request is only a small style tweak inside a fixed design system
- the work is backend-only, copy-only, or already owned by a more specific skill
- you only need generic frontend advice or a browser-selection guide

## Quick Start
1. Classify the surface first: app, tool, dashboard, game, site, or other product UI.
2. Name the real job, primary objects, states, and actions before choosing layout or visuals.
   If the prompt is a one-shot build or design request with no follow-up available, infer reasonable defaults and keep moving to a complete first-pass answer.
3. Decide whether concepting or imagegen is actually needed. Use it only when the surface needs concrete visual direction or non-textual product art.
4. Build the working first screen and core workflow before polish.
5. Keep labels, numbers, and controls in code; use existing assets or imagegen only for visuals code cannot convincingly supply.
6. Verify the real surface in a browser on desktop and mobile before handoff.

## Operating Constraints
- Operational surfaces should read as usable product, not a promo page or hero section.
- One-shot build and design prompts should be answered directly in one response; do not default to clarification when a reasonable assumption can resolve the gap.
- Ask a clarifying question only when the request is genuinely ambiguous or unsafe.
- Preserve expressive categories such as games, portfolios, editorial work, and art-directed product surfaces; do not flatten them into generic SaaS cards.
- Make at least one concrete interaction or state change explicit: select, edit, filter, toggle, inspect, or step through a workflow.
- Reject at least one generic trope and name the better alternative, such as replacing a hero/card stack with a table, sidebar, or inspector that shows the actual workflow.
- Do not turn a dashboard, tool, or app request into a marketing shell.
- Keep text, labels, metrics, and controls in code; use assets or imagegen for visuals that code cannot convincingly supply.
- Use `browser-local-qa` for the smallest reliable verification surface; this skill only requires that the real page gets checked on desktop and mobile.

## Inputs This Skill Expects
- The product category and the user's real goal.
- Any existing UI, screenshot, brand system, or design system.
- The key entities, states, filters, and actions the surface must support.
- Any hard constraints on layout, tone, density, responsiveness, or art direction.
- Missing optional context is acceptable; turn it into stated assumptions instead of blocking on a narrowing question unless the request is genuinely ambiguous or unsafe.

## Output Contract
- Start from the product category and actual job to be done.
- For apps, tools, dashboards, and games, build the real workflow first, not a promo wrapper.
- For one-shot operational-surface prompts, answer in one response with the requested plan, named layout regions, at least one concrete interaction or state path, one rejected generic trope, and browser verification steps.
- If context is missing, surface the assumption and continue rather than asking a narrowing question unless the request is genuinely ambiguous or unsafe.
- For operational surfaces, translate at least three nouns from the prompt into named UI regions, controls, or state panels.
- For operational surfaces, show one concrete inspect-or-edit path for a selected object, not just a comparison table or summary strip.
- Choose domain-specific hierarchy, density, controls, and content.
- Make at least one interaction, mode, or state explicit on the screen.
- Explain at least one generic trope you rejected and the better product-specific alternative.
- Preserve intentional expressive design when the category calls for it, but keep the surface usable and legible.

## Procedure
1. Identify whether the request is a landing page or a product surface, and whether it is a one-shot prompt with no follow-up available.
2. Write down the core objects, states, and actions the user expects. If optional context is missing, state the assumption and continue unless the request is genuinely ambiguous or unsafe.
3. Start from those objects, not from a generic hero, feature grid, or card stack.
4. If the surface is operational, map prompt nouns to named regions first, then use the domain's native UI forms: tables, lists, filters, sidebars, drawers, timelines, or inspectors.
5. Use real sample data and states instead of fake metrics and social proof.
6. Include at least one inspect-or-edit path for a selected object.
7. Check the screen for vague labels, weak alignment, overflow, missing controls, or "looks polished but does nothing" behavior.
8. Tune density and whitespace to the product instead of defaulting to the same spacious demo layout every time.

## Pitfalls And Gotchas
- Turning every request into a SaaS dashboard.
- Using gradients, blobs, glassmorphism, glow, or orbs as default decoration.
- Inventing fake dashboards, fake charts, or fake testimonials to fill space.
- Making every UI rounded, airy, and shallow until it no longer matches the product.
- Fixing style while leaving the main workflow vague or inert.
- Banning all visual ambition and breaking games, portfolios, editorial work, or art tools.

## Progressive Disclosure
Start with the smallest useful reading of the request, then widen only as needed to support the actual workflow. If the surface is operational, favor clarity and task completion; if it is expressive, favor the art direction the category deserves. Keep the skill short enough that it steers decisions instead of becoming a generic design manifesto. When in doubt, preserve the product skeleton and make the design more specific, not more generic.

## Verification Pattern
- Check that the first screen shows the real task, not a generic promo page.
- Check that the controls, states, and copy are specific to the product.
- Check that any visual flourish helps the task instead of hiding missing substance.
- For operational surfaces, verify at least one interaction path such as filter, select, toggle, edit, or inspect.
- For expressive surfaces, verify that the chosen style is intentional and category-appropriate, not the default AI-generated look.
- Confirm the browser check covered the real page on desktop and mobile before handoff.
- If the result still feels generic, re-check whether it accidentally became a landing page or reused default component-library tropes.
