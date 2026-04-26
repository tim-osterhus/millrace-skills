# Anti LLM Frontend Design

## Purpose
Help frontend agents avoid the generic, obviously LLM-generated look by choosing product-specific structure, density, and interactions first. This skill is a guardrail, not a universal visual style guide.

## Quick Start
1. Classify the surface: landing page, app/tool/dashboard, game, editorial, portfolio, or art-directed product.
2. Name the real task, primary objects, and the controls or states the screen must expose.
3. If the request is operational, build the workflow first; if it is expressive, preserve the art direction.
4. Replace generic AI-demo tropes with domain-specific structure, copy, density, and motion.
5. Make at least one concrete interaction or state explicit, and name one trope you rejected plus the better alternative.

## Operating Constraints
- Do not turn an app, tool, or dashboard request into a marketing page.
- Do not use oversized generic hero sections when the user asked for a working surface.
- Do not default to purple or blue gradients, blobs, glow, glass cards, decorative orbs, or other generic polish.
- Do not stack floating cards inside cards, fake metrics, fake charts, fake testimonials, lorem-style feature blocks, or generic nav bars.
- Do not add generic KPI summary rows or generic global action bars unless they directly drive the active workflow on screen.
- Do not replace the workflow with vague copy like "streamline your workflow" or "AI-powered".
- Do not ship low-information-density operational tools when the job needs comparison, monitoring, or repeated use.
- Do not rely on excessive rounded rectangles, weak alignment, inconsistent spacing, or text overflow to fake polish.
- Do not lean on one-note Tailwind/shadcn compositions when the product needs real controls or layout.
- Do not let polish hide missing states, controls, data, or interaction paths.
- Do not overcorrect into a sterile utilitarian dashboard when the category calls for expressive design.

## Inputs This Skill Expects
- The product category and the user's real goal.
- Any existing UI, screenshot, brand system, or design system.
- The key entities, states, filters, and actions the surface must support.
- Any hard constraints on layout, tone, density, responsiveness, or art direction.

## Output Contract
- Start from the product category and actual job to be done.
- For apps, tools, dashboards, and games, build the real workflow first, not a promo wrapper.
- For operational surfaces, translate at least three nouns from the prompt into named UI regions, controls, or state panels.
- For operational surfaces, show one concrete inspect-or-edit path for a selected object, not just a comparison table or summary strip.
- Choose domain-specific hierarchy, density, controls, and content.
- Make at least one interaction, mode, or state explicit on the screen.
- Explain at least one generic trope you rejected and the better product-specific alternative.
- Preserve intentional expressive design when the category calls for it, but keep the surface usable and legible.

## Procedure
1. Identify whether the request is a landing page or a product surface.
2. Write down the core objects, states, and actions the user expects.
3. Start from those objects, not from a generic hero, feature grid, or card stack.
4. If the surface is operational, map prompt nouns to named regions first, then use the domain's native UI forms:
   - use tables, lists, filters, sidebars, drawers, or timelines for operational work
   - use real sample data and states instead of fake metrics and social proof
   - use purposeful visual flourish only when it supports the subject
5. Include at least one inspect-or-edit path for a selected object.
6. Check the screen for vague labels, weak alignment, overflow, missing controls, or "looks polished but does nothing" behavior.
7. Tune density and whitespace to the product instead of defaulting to the same spacious demo layout every time.
8. Keep the chosen style intentional, not generic.

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
- If the result still feels generic, re-check whether it accidentally became a landing page or reused default component-library tropes.
