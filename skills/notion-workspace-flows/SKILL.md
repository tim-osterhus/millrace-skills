---
asset_type: skill
asset_id: notion-workspace-flows
version: 1
description: "Guardrail for Notion workspace flows: capture, meeting prep, research synthesis, and spec-to-implementation handoff with citations and confirmation-gated writes."
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

# Notion Workspace Flows

## Purpose
Help agents choose the right Notion flow before they write anything. This skill covers capture, meeting prep, research synthesis, and spec-to-implementation handoff when the work needs Notion pages, backlinks, citations, or task linkage. It is a guardrail, not a Notion manual.

### Use When
- capturing conversations, decisions, or notes into Notion
- preparing agendas or pre-reads from Notion context
- synthesizing multiple Notion pages into a cited brief, report, or comparison
- turning a Notion spec into an implementation plan and task set
- updating an existing page instead of creating a duplicate

### Do Not Use When
- the work has no Notion destination
- the task is external research with no Notion synthesis or write-back
- another more specific skill already owns the workflow
- the prompt would require guessing the workspace schema, database names, or page IDs

## Quick Start
1. Classify the request first as `capture`, `meeting prep`, `research synthesis`, or `spec-to-implementation`.
2. If Notion MCP is unavailable, stop after a brief setup note: add the Notion MCP, enable the remote MCP client, and complete OAuth before any Notion read or write can continue.
3. Search with `Notion:notion-search` and fetch with `Notion:notion-fetch` before drafting or mutating anything.
4. If more than one page or database could fit, ask which one to use instead of guessing.
5. Confirm the destination database, template, or page type before any write.
6. Keep read-only synthesis separate from create/update actions, and require confirmation before mutation.
7. End with the next verifier and the evidence captured.

## Operating Constraints
- Do not invent database schemas, property names, template names, relations, or page IDs.
- Do not write until sources have been searched and fetched and the destination is confirmed.
- Do not mix read-only synthesis with mutation-ready content.
- Do not create a duplicate page when the existing page should be linked or updated.
- Do not smooth over contradictions, gaps, or open questions.
- Do not turn a small Notion decision into a generic productivity lecture.
- If Notion MCP is missing, pause instead of hand-waving around it.
- Keep source links and backlinks attached whenever a report, brief, or plan is synthesized.

## Inputs This Skill Expects
- The user goal, audience, and desired Notion artifact.
- Existing Notion pages, specs, or meeting notes to read first.
- Any confirmed destination database, template, or page type.
- A clear read-only vs write-enabled expectation.
- For spec-to-implementation, the source spec and any related task or planning pages.
- If multiple candidate pages or databases exist, a short prompt asking the user to choose one.

## Output Contract
- Start by naming the chosen mode and the artifact you are producing.
- Separate `Read first` findings from `Proposed writes`.
- Name the destination database, template, or page type before any mutation.
- Preserve source links, citations, open questions, contradictions, and follow-up tasks in synthesized output.
- Prefer updating or linking an existing page over creating a duplicate.
- End with one handoff line in the form `Next verifier: ... | Evidence captured: ...`.

## Procedure
1. Classify the request and state whether it is read-only or mutating.
2. If Notion MCP is missing, emit the brief setup note and stop.
3. Search first, then fetch with `Notion:notion-search` and `Notion:notion-fetch`. If multiple pages or databases fit, ask which one to use.
4. For capture, extract the decision, rationale, owner, related links, and follow-ups.
5. For meeting prep, extract the goal, attendees, decisions needed, blockers, and timeboxes; build the agenda or pre-read from fetched context.
6. For research synthesis, separate facts, interpretation, contradictions, and open questions; cite each source and add a references section.
7. For spec-to-implementation, extract requirements, ambiguities, plan scope, and tasks; confirm the task database schema before creating pages.
8. For any write, repeat the destination and wait for explicit confirmation before using `Notion:notion-create-pages` or `Notion:notion-update-page`.
9. If an existing page already owns the content, update or link it instead of duplicating it.

## Pitfalls And Gotchas
- Rejected trope: dumping every Notion note into one generic summary. Better alternative: choose the artifact type first, then keep citations, decisions, and open questions separate.
- Rejected trope: inventing a database schema from memory. Better alternative: search, fetch, and confirm the actual destination and properties before any write.
- Rejected trope: creating a duplicate page when the existing page should be linked or updated. Better alternative: update the owning page and add backlinks.
- Rejected trope: smoothing contradictions into a clean narrative. Better alternative: list contradictions explicitly so the next verifier can see the tradeoffs.

## Progressive Disclosure
Start with the smallest useful read: what artifact is needed, who it is for, and whether the result is read-only or mutating. Expand only enough to locate sources, confirm the destination, and preserve traceability. Keep the skill compact; if workspace-specific schema details are needed, ask rather than guessing.

## Verification Pattern
- The artifact mode is explicit before drafting begins.
- Relevant pages were searched and fetched before any write was proposed.
- The destination database, template, or page type was confirmed before mutation.
- Citations, backlinks, open questions, and contradictions survived the synthesis.
- Existing pages were updated or linked instead of duplicated when appropriate.
- Any mutation was gated by explicit confirmation.
- The final response ends with the exact handoff line format: `Next verifier: ... | Evidence captured: ...`.

