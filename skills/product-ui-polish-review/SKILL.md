---
asset_type: skill
asset_id: product-ui-polish-review
version: 1
description: "Guardrail for reviewing and polishing product UI reward moments, typography, spacing, hierarchy, and perceived-quality details without drifting into manipulative retention design."
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

# Product UI Polish Review

## Purpose
Help agents review and improve product UI surfaces by finding meaningful result moments, then tightening typography, spacing, hierarchy, and perceived-quality details. This is a polish guardrail, not a growth-hacking manual or a substitute for a full design system.

### Use When
- a product screen, onboarding flow, generated-result page, dashboard, app, or tool needs final polish
- the work involves success states, milestones, matches, reports, scores, streaks, generated artifacts, unlocks, badges, or other user-receives-something moments
- typography, spacing, line length, alignment, or hierarchy make the UI feel amateur despite mostly-correct structure
- a frontend build or review needs product-specific delight without becoming generic decoration

### Do Not Use When
- the work is backend-only, copy-only, or a purely mechanical bugfix
- the user asks for dark-pattern retention, gambling-like engagement, compulsive loops, or deceptive urgency
- the product category is finance, trading, health, education for children, addiction-sensitive, or otherwise high-risk and the requested reward treatment could distort user judgment
- a specific design system already dictates the interaction and typography choices

## Quick Start
1. Classify the surface and its real job before adding polish.
2. Find the user-receives-something moments: result, report, score, match, milestone, unlock, generated artifact, payout, badge, save, or completion.
3. Decide whether each moment should stay a plain receipt or become a small gift moment.
4. If a gift moment is appropriate, design anticipation, reveal, and afterglow with restraint.
5. Tighten typography and spacing: line height, letter spacing, alignment, measure, hierarchy, and relationship spacing.
6. Check ethics and product fit before adding celebration or habit-forming ceremony.

## Operating Constraints
- Do not make manipulation the goal. Optimize clarity, perceived quality, confidence, and meaningful feedback.
- Do not add reward ceremony to irreversible, risky, financial, medical, safety, children, or addiction-sensitive actions.
- Do not celebrate trades, losses, purchases, health outcomes, or other moments where excitement can impair judgment.
- Do not hide latency with fake uncertainty unless the product truthfully has a real pending result.
- Do not use confetti, glow, sound, haptics, badges, or share prompts as default decoration.
- Do not interrupt expert or repeated workflows with ceremony after the novelty has worn off.
- Do not center-align long text, mix center-aligned headings with left-aligned body copy, or let body text run too wide.
- Do not overuse text sizes for hierarchy when weight, tone, color, and spacing can do the job.

## Inputs This Skill Expects
- the product category and target user
- the screen, flow, diff, screenshot, or implementation being reviewed
- the main user goal and the important objects, states, and actions
- any brand, design-system, accessibility, motion, or risk constraints
- the moments where the user receives a result, reward, confirmation, or generated output

## Output Contract
- Name the surface type and the primary job before proposing polish.
- Identify at least one receipt-or-gift decision and explain why it should stay plain or gain ceremony.
- If ceremony is used, specify anticipation, reveal, and afterglow as separate pieces.
- Include at least one typography or spacing correction with concrete values or rules.
- Reject at least one tempting but inappropriate polish move and name the safer alternative.
- Preserve existing product structure and workflow; polish should not replace missing functionality.

## Procedure
1. **Classify the surface.** Name whether it is onboarding, generated result, dashboard, operational tool, consumer loop, checkout, editor, game UI, or another product surface.
2. **Find receipt moments.** Look for places where the user receives something: success, match, score, report, streak, badge, export, generated file, completed task, unlocked item, saved state, or payout.
3. **Choose receipt or gift.** Keep the moment plain when speed, seriousness, reversibility, or risk matters. Consider gift treatment when the moment is earned, positive, safe, and important enough to remember.
4. **Design gift moments in three stages.**
   - Anticipation: brief loading, staged reveal, progress, or suspense that truthfully reflects an upcoming result.
   - Reveal: the result arrives with weight through layout, timing, contrast, animation, haptics, or sound when appropriate.
   - Afterglow: give the user a moment to save, share, compare, claim, continue, or attach identity to the result.
5. **Tune typography.**
   - Use heading line-height around `1.1-1.3`.
   - Use body line-height around `1.3-1.5`.
   - Use slight negative letter spacing only for large headings when the font benefits from it.
   - Avoid negative letter spacing in body text.
   - Keep body text around `50-75` characters per line; around `600px` is a useful desktop maximum for typical body copy.
6. **Tune alignment and hierarchy.**
   - Use left alignment for body text longer than about three lines.
   - Keep heading and body alignment consistent within the same text group.
   - Limit type-size count; prefer weight, color, opacity, spacing, and position for secondary hierarchy.
7. **Tune relationship spacing.**
   - Elements with a closer semantic relationship should be physically closer.
   - Use simple ratios: if heading-to-body spacing is `1x`, spacing between unrelated groups should usually be `2x` or more.
   - Make whitespace an active layout element, not leftover empty space.
8. **Verify the polish.** Check that the screen still communicates the real task, remains accessible, and does not slow down frequent users unnecessarily.

## Pitfalls And Gotchas
- Rejected trope: turn every success state into confetti.
  Better alternative: scale the ceremony to the importance and risk of the moment.
- Rejected trope: deliver every generated report as a flat bank-statement receipt.
  Better alternative: use a truthful anticipation and reveal sequence when the result is meaningful and safe.
- Rejected trope: fix a weak UI with glow, blur, gradients, or motion before typography and spacing.
  Better alternative: fix line height, measure, hierarchy, and relationship spacing first.
- Rejected trope: use center alignment because it looks premium in a mockup.
  Better alternative: left-align longer reading surfaces and reserve centered text for short, controlled chunks.
- Rejected trope: use many font sizes for every level of importance.
  Better alternative: use two or three type sizes, then adjust weight, color, and spacing.

## Verification Pattern
- Confirm the surface type and user job were named.
- Confirm at least one receipt moment was classified as plain receipt or gift moment.
- Confirm any gift moment has anticipation, reveal, and afterglow, not just a reveal animation.
- Confirm high-risk categories were not given manipulative celebration.
- Confirm heading and body line-height, text measure, alignment, hierarchy, and relationship spacing were checked.
- Confirm the final UI is more specific to the product, not just more decorated.
