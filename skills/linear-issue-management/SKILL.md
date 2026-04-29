---
asset_type: skill
asset_id: linear-issue-management
version: 1
description: Guardrail for reading, triaging, and safely mutating Linear issues, projects, and team workflows with confirmation-gated writes.
advisory_only: true
capability_type: planning-guardrail
recommended_for_stages:
  - builder
  - checker
  - fixer
  - updater
forbidden_claims:
  - queue_selection
  - routing
  - retry_thresholds
  - escalation_policy
  - status_persistence
  - terminal_results
  - required_artifacts
---

# Linear Issue Management

## Purpose
Guardrail for Linear issue, project, and team-workflow work. Keep reads first, entity IDs explicit, and all mutations confirmation-gated. This is a guardrail, not a Linear handbook.

Use when the task involves Linear issues, projects, labels, cycles, comments, assignees, dependencies, or team workflow; when you need to turn discussion or notes into issue-ready fields; when you need a concise triage or status summary grounded in Linear records; or when any create, update, assign, status, label, cycle, or comment change must stay explicit and traceable.

Do not use when the work is generic planning with no Linear surface, when the prompt is only about connector provisioning or account setup with no actual Linear task, when another more specific skill already owns the same workflow boundary, or when the user would have to trust guessed team, project, cycle, or issue identifiers.

## Quick Start
1. Confirm Linear access and the target workspace, team, or project from the prompt or existing Linear context; stop if the identity is still unclear.
2. Clarify the goal and scope before naming actions.
3. Identify the exact Linear entities and read them first.
4. Batch related reads and writes by entity or workflow.
5. Keep create, update, assign, status, comment, label, and cycle changes pending explicit confirmation.
6. Summarize with IDs, urgency or priority, blockers, and any pending confirmation.

## Operating Constraints
- Do not guess identifiers, team keys, project names, or cycle names.
- Prefer reading the current issue, project, label set, or cycle list before proposing a change.
- Keep related writes together so the user can approve one coherent mutation set.
- For issue-ready discussion-to-issues output, extract the full draft issue list before collapsing leftovers into notes; preserve each material open question as its own follow-up item or draft issue when it could change implementation scope or rollout behavior, even if it belongs to a related issue.
- Require explicit confirmation before any create, update, assign, status, comment, label, or cycle mutation.
- Do not turn a triage answer into an action plan unless the mutation gate is satisfied.
- If the prompt names Linear work but does not include the actual issue list, discussion text, or exported slice, do not search the workspace or emit a terminal block; return a concise no-data summary and ask for the missing slice.
- Keep summaries short and traceable.
- Do not drown the answer in API prose or connector internals.
- If Linear access, workspace identity, or permissions are missing, say so and stop instead of inventing a fallback.

## Inputs This Skill Expects
- A Linear issue, project, team, label, cycle, or discussion slice.
- The actual issue list, discussion text, or exported Linear slice when the task asks for triage or issue drafting.
- A confirmed workspace, team, or project only when the prompt or existing context already provides it.
- A clear note on whether the answer should stay read-only or may prepare mutation-ready output.
- Explicit confirmation before any write.

## Output Contract
When answering, prefer a compact structure like:
- `Goal`
- `Linear entities`
- `Read first`
- `Proposed writes`
- `Pending confirmation`
- `Next action`

When the prompt asks for issue-ready output, give every material open question its own draft issue or explicit follow-up item if it could change implementation scope or rollout behavior, even when it is tied to a nearby issue, and do not collapse it into another item's note.

Summaries should include, when available:
- issue or project IDs
- urgency or priority
- blockers or dependencies
- owner or assignee only if confirmed
- whether anything is still pending confirmation

When proposing a mutation, say exactly what would change and what still needs approval. Do not imply that the change has already happened.

## Procedure
1. Clarify goal and scope before naming actions.
2. Identify the exact Linear entities and read them first.
3. For discussion-to-issues work, restate scope, extract dependency and blocker facts, create a separate follow-up item for each material open question that could change implementation scope or rollout behavior, keep the issue-ready list complete before folding any leftover open questions into notes, and keep any candidate create or update batched and confirmation-gated.
4. For triage work, read the relevant Linear slice, rank by urgency or impact from evidence only, and refuse to invent missing status, priority, ownership, or cycle values.
5. For update work, read the current object, group related field changes together, repeat back the exact fields that would change, and stop at the remaining approval gate.
6. Summarize with traceable next actions and note whether anything is still pending confirmation.

## Pitfalls And Gotchas
- Guessing identifiers or team membership.
- Silent status changes or hidden label edits.
- Ad hoc note dumps that do not name the Linear entity.
- Overbuilt API or tool prose that buries the actual decision.
- Mixing confirmed facts with inferred fields.
- Splitting one workflow into multiple tiny mutations when one batched change would be safer.
- Treating a summary as permission to mutate.

## Progressive Disclosure
Start with the smallest useful read. Expand only enough to prove the next read or write. Keep the skill compact so it behaves like a guardrail rather than a handbook.

## Verification Pattern
- The workspace and target Linear entity are explicit.
- Reads happen before writes.
- Any create, update, assign, status, comment, label, or cycle change is confirmation-gated.
- The summary is concise, ID-aware, and blocker-aware.
- The next verifier knows whether the task is read-only or awaiting approval.
- End by naming the next implementation or verification check: confirm the exact Linear IDs, confirm any still-pending mutation, or confirm that the task should remain read-only.
