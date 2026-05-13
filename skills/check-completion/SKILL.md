---
asset_type: skill
asset_id: check-completion
version: 1
description: "Verification guardrail for auditing claimed-done work, classifying incomplete tasks with evidence, and driving the remainder to terminal status."
advisory_only: true
capability_type: verification-guardrail
recommended_for_stages:
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

# Check Completion

## Purpose
Help agents answer "are we done?" with evidence instead of confidence. This skill audits a session, plan, branch, PR, or custom task list, classifies each item, and remediates the non-terminal rows when the user wants completion rather than just a report.

**Use When**
- the user asks whether work is complete, what remains, or why something is still unfinished
- a plan or todo list may have drifted from reality
- a branch, PR, queue, or session needs a completion audit before handoff
- previous work crashed, timed out, paused, or was assumed complete

**Do Not Use When**
- the user asks for a single quick verification command
- the task is ordinary code review, runtime debugging, or future planning
- the user explicitly wants a narrow status answer with no remediation

## Quick Start
1. Declare the audit scope: session, plan, branch, PR, queue, or explicit custom list.
2. Enumerate tasks from the available sources instead of trusting a single todo list.
3. Assign each task exactly one status based on evidence.
4. Produce a discrete audit table before remediation.
5. If remediation is requested or implied, work blockers, broken items, missing items, and untested items in that order.
6. Finish with a completion report where every row is terminal or has a concrete external next step.

## Operating Constraints
- Evidence comes before status; no task is complete because an agent said it was.
- Do not default uncertain rows to `Implemented`.
- Use one status per task, not blended status prose.
- Every non-implemented row needs a concrete action, owner, or next command.
- Do not quietly remediate while enumerating; the audit table is its own artifact.
- Do not stop at the first blocker if other independent rows can still be completed.
- Terminal non-implemented outcomes must be deliberate: deferred, cancelled, out of scope, superseded with replacement verified, or blocked with an external next step.

## Inputs This Skill Expects
- The scope to audit, or enough context to choose a finite scope.
- Access to one or more evidence sources: conversation, plan/todo state, git diff/log, test output, CI, terminal history, queue state, or runtime artifacts.
- The user's expectation: audit only, audit plus remediation, or final readiness check.
- Any constraints on what may be changed during remediation.

## Output Contract
- State the audit scope and sources scanned.
- Provide an audit table with task, status, evidence, blocking flag, and action required.
- Use statuses from this controlled set: `Implemented`, `Partially Implemented`, `Implemented but Untested`, `Implemented but Broken`, `Implemented but Outdated`, `Assumed Complete`, `Incorrectly Implemented`, `Stalled`, `Timed Out`, `Crashed`, `Skipped`, `Forgotten`, `Blocked`, `Deferred to Human`, `Deprioritized`, `Superseded`, `Cancelled`, `Ambiguous`, `Duplicate`, `Planned / Queued`, `Not Planned`, `Out of Scope`.
- If remediation occurs, provide a completion report with starting status, ending status, and evidence.
- End with zero non-terminal rows unless the user requested audit-only output.

## Procedure
1. Define scope in one sentence before scanning.
2. Extract tasks from all relevant sources available in the environment.
3. Deduplicate tasks while preserving source evidence.
4. For each candidate `Implemented` row, identify the proof needed, run or locate that proof, and read the output.
5. For any row without proof, choose the most pessimistic applicable non-implemented status.
6. Write the audit table before making fixes.
7. Remediate in priority order: blockers, broken/outdated, incorrect, stalled/crashed/timed out, partial, missing/queued, untested/assumed, skipped, ambiguous, duplicate/superseded.
8. Re-verify each remediated row with the specific proof required for its task.
9. Produce the completion report and state any external blocker precisely.

## Pitfalls And Gotchas
- Treating "looks done" as evidence.
- Letting a todo list status override failing tests or missing files.
- Inventing a custom status that hides whether action remains.
- Marking `Superseded` without verifying the replacement.
- Leaving `Assumed Complete` rows untested.
- Halting remediation because one row needs human input even though unrelated rows remain.
- Calling the audit complete before reading the verification output.

## Progressive Disclosure
Start with the narrowest finite scope that matches the user's question. Expand source scanning only when the answer would otherwise be misleading. For large scopes, split the audit into named batches, but keep the same status taxonomy and evidence rules.

## Verification Pattern
- Confirm the audit table exists before remediation notes.
- Confirm each row has exactly one allowed status.
- Confirm every `Implemented` row cites concrete evidence.
- Confirm every non-implemented row has an action required.
- Confirm blockers do not halt unrelated remediation.
- Confirm the completion report ends every row in a terminal state, or explicitly says audit-only was requested.
