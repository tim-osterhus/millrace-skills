---
asset_type: skill
asset_id: durable-workflow-orchestration
version: 1
description: Guardrail for designing and reviewing crash-safe durable workflows with explicit checkpoints, retries, pause/resume, and recovery boundaries.
advisory_only: true
capability_type: planning-guardrail
recommended_for_stages:
  - builder
  - checker
  - fixer
  - planner
forbidden_claims:
  - queue_selection
  - routing
  - retry_thresholds
  - escalation_policy
  - status_persistence
  - terminal_results
  - required_artifacts
---

# Durable Workflow Orchestration

## Purpose
Help agents design or review durable workflows by forcing the durable boundary, state ownership, checkpoint plan, retry rules, and recovery path to be explicit before implementation. This is a guardrail, not a workflow-engine manual.

### Use When
- the task is about a long-running job, multi-step pipeline, agent loop, or background workflow
- the workflow must pause, resume, retry, wait for approval, or survive a crash, reconnect, or callback
- the answer depends on where side effects become irreversible or where state must persist between steps
- the prompt is a review and needs to find duplicate side effects, missing checkpoints, or unsafe retry boundaries

### Do Not Use When
- the work is a short stateless helper or one-off script
- the request is only about deployment, auth, browser QA, or generic infrastructure
- a more specific platform skill already owns the exact runtime seam

## Quick Start
Answer from the task prompt and any provided workflow evidence first; only inspect local files or environment state when implementation evidence is explicitly part of the task.
1. Name the durable unit first: one request, one job, one entity, one session, or another natural shard.
2. State who owns persistence and which fields are stored as resume state.
3. Mark the irreversible edges.
4. Place a checkpoint before and after the external side effect.
5. Make the approval pause/resume contract explicit.
6. Reconcile ambiguous success before issuing anything new.
7. End with one concrete verification step that proves the boundary or recovery path.

## Operating Constraints
- One durable unit should own one natural coordination atom.
- The orchestrator sequences work; side effects own their own idempotency and compensation.
- Persist the minimum resume state before a crash, pause, or handoff can occur.
- Do not rely on in-memory state to survive pause/resume, reconnect, process restart, or eviction.
- If an operation is irreversible, checkpoint before it and name the recovery outcome if it fails after the checkpoint.
- Answer from the task prompt and any provided workflow evidence first; only inspect local files or environment state when implementation evidence is explicitly part of the task.
- Keep vendor-specific bootstrap or API syntax out of the guardrail; choose the runtime later if needed.

## Inputs This Skill Expects
- the workflow goal, trigger, and natural durable boundary
- the current state model or persistence choice
- the step list, including any external calls, waits, approvals, or callbacks
- any existing workflow implementation or review evidence
- the target runtime only if it changes the seam decision

## Output Contract
- answer in this order: durable boundary -> persisted state owner and stored fields -> irreversible edges -> checkpoint before and after the external side effect -> approval pause/resume contract -> ambiguous-success reconciliation -> one proof step
- state who owns persistence and what is stored
- list the step boundaries and the irreversible edges
- specify retry policy, idempotency strategy, checkpoint plan, and recovery/resume path
- call out missing checkpoints, duplicate side effects, or unsafe retry boundaries when reviewing
- end with one concrete verification step and the evidence it should capture

## Procedure
1. Identify the workflow boundary and the recovery unit.
2. Split orchestration from side effects and from recovery logic.
3. Decide what must be persisted before the first irreversible action.
4. Define which steps are retriable, which are idempotent, and which need compensation instead of retry.
5. Make pause/resume and callback handling explicit when the workflow can stop midstream.
6. Verify with a concrete proof step such as a checkpoint round-trip, resume test, or review finding.

## Pitfalls And Gotchas
- One giant async function that hides every step boundary.
- Hidden in-memory state treated as durable truth.
- Retries without idempotency or dedupe keys.
- No checkpoint before an irreversible side effect.
- Assuming a paused workflow can resume from process memory.
- Mixing vendor bootstrap details into a vendor-neutral skill.

### Rejected Trope
- Rejected trope: "Just retry the whole workflow until it works."
- Better alternative: checkpoint before irreversible edges, resume from the last durable boundary, and compensate or dedupe any side effect that can repeat.

## Progressive Disclosure
Start with the smallest honest boundary and the minimum durable state needed to resume it. Expand only enough to cover retries, pause/resume, and recovery without turning the skill into a workflow-engine manual.

## Verification Pattern
Confirm the durable boundary is explicit, the state owner is named, the checkpoint sits before the irreversible edge, and the retry/idempotency/recovery story is concrete. Next verifier: workflow implementer or reviewer; capture the boundary, checkpoint, resume path, and one proof step.
