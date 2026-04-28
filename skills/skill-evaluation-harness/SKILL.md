---
asset_type: skill
asset_id: skill-evaluation-harness
version: 1
description: Guardrail for evaluating local skills or plugins, turning findings into rewrite briefs, and designing schema-compatible metric packs.
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

# Skill Evaluation Harness

## Purpose
Help agents decide whether a local skill or plugin should be evaluated, improved, or given a metric pack, then turn the evidence into the next concrete artifact. This is a guardrail, not a general evaluation manual.

### Use When
- a local skill or plugin package needs review before publication
- a weak score or report needs a rewrite brief
- a custom metric pack needs schema-compatible checks and metrics
- a repeatable benchmark scenario or local scoring signal needs to be named

### Do Not Use When
- the task is ordinary app, frontend, or backend work
- there is no local package, benchmark prompt, or metric-pack manifest to inspect
- the ask is generic prompt-engineering advice with no local artifact in scope

## Quick Start
1. Classify the request first: `evaluate`, `improve`, or `metric-pack design`.
2. Inspect the first evidence:
   - `evaluate`: the package root and current `SKILL.md`
   - `improve`: the latest eval output or comparison report, then the package
   - `metric-pack design`: the manifest and target scenario prompt
3. Separate trigger and scope from validation and budget before you judge.
4. Stop at the smallest next artifact that can be acted on safely.

## Operating Constraints
### Trigger And Scope
- Keep the request tied to the local artifact in hand.
- For `evaluate`, identify the likely failure class before recommending fixes.
- For `improve`, decide whether the blocker is trigger, scope, validation, or budget before writing the brief.
- For `metric-pack design`, confirm the scenario really needs custom checks or metrics before adding them.

### Evidence Quality
- Read the first evidence before any opinion.
- Package issues include frontmatter, `SKILL.md` structure, broken links, temporary filler, and oversized bodies.
- Evaluation issues include report quality, baseline comparison, missing evidence, and an unclear next verifier.
- Metric-pack issues include stable IDs, deterministic signals, and schema-compatible payloads.
- Do not turn this into a generic evaluation manual; inspect the actual package and write the next fix.

### Split Policy
- Do not split evaluation, improvement, and metric packs into separate skills for v1.
- Keep the shared decision path in one umbrella skill so the trigger stays strong.
- If the evidence says one branch is dominant, keep the other branches present but brief.

## Inputs This Skill Expects
- a local skill or plugin package root, or a concrete path to `SKILL.md`
- the latest eval output or comparison report when improving
- the benchmark prompt or scenario prompt when coverage matters
- the metric-pack manifest when custom checks or metrics are being designed
- any measured token or time data if the run already has it

## Output Contract
### Evaluate
- Name the likely failure class first.
- Name the evidence that proved it.
- Name the next verifier and the artifact it should capture.

### Improve
- Split required fixes from recommended fixes.
- Turn the findings into a rewrite brief instead of more commentary when the blocker is already clear.
- Name the rerun target and the comparison artifact.

### Metric-Pack Design
- Give the smallest useful `checks[]` and `metrics[]`.
- Keep IDs stable and the signals deterministic.
- Prefer a metric-pack manifest over more commentary once the scoring shape is clear.
- State how the pack stays schema-compatible.

## Procedure
### Token And Time
- Report measured token or time data when it exists.
- If it does not exist, do not invent it.
- Use budget observations to break ties, not to replace evidence.
- If two outputs are otherwise equal, the cheaper one wins only when the comparison is real and recorded.

### Scenario Coverage
- For evaluation, name a repeatable benchmark prompt or starter scenario that should run next.
- For improvement, include the rerun target and the evidence to compare before and after.
- For metric-pack design, keep the scenario planning-level and verify it stays local and schema-compatible.
- Do not widen the task into a rubric tutorial or a command catalog.

### Metric-Pack Compatibility
- Only use this branch when the request is about a custom rubric or scoring signal.
- Keep `checks[]` and `metrics[]` minimal and deterministic.
- Keep IDs stable across runs.
- Favor local signals over subjective prose.
- Do not overwrite the core score or summary.
- If the pack is too large, trim it before adding more explanation.

## Pitfalls And Gotchas
- Rejected trope: write a broad evaluation essay first.
- Better alternative: inspect the actual package or manifest and decide the next fix from evidence.
- Rejected trope: pad the answer with budget commentary when validation is the real problem.
- Better alternative: separate validation, scope, and budget into distinct findings.
- Rejected trope: split the umbrella skill into separate evaluation, improvement, and metric-pack packages.
- Better alternative: keep one shared decision path so the trigger stays strong and the handoff stays obvious.

## Progressive Disclosure
Keep the answer small enough that it behaves like a guardrail, not a reference manual. If the details start to repeat, stop and hand off instead of expanding into a generic evaluation course. Use the package root, eval output, scenario prompt, or manifest that is already in view, and avoid inventing missing context.

## Verification Pattern
Check that the request was classified first, that the first evidence was named, and that trigger, validation, and budget stayed separate. Check that an evaluation answer names the likely failure class, an improvement answer becomes a rewrite brief, and a metric-pack answer stays schema-compatible. Next verifier: the local evaluator or benchmark runner, with the package path, eval output, scenario prompt, or manifest intentionally captured.
