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
2. If the prompt already supplies source excerpts for a read-only research synthesis, treat those excerpts as the fetched source set and draft directly. Do not check Notion availability, do not mention MCP or tool setup, and do not narrate search/fetch steps.
3. If live Notion reads or writes are required and Notion MCP is unavailable, stop after a brief setup note: add the Notion MCP, enable the remote MCP client, and complete OAuth before any Notion read or write can continue.
4. Search with `Notion:notion-search` and fetch with `Notion:notion-fetch` before drafting or mutating anything unless the prompt already supplied the excerpts for a read-only research brief.
5. If more than one page or database could fit, ask which one to use instead of guessing.
6. Confirm the destination database, template, or page type before any write.
7. Keep read-only synthesis separate from create/update actions, and do not add write-planning framing to a read-only research brief unless the prompt explicitly asks for it.
8. For research synthesis, keep every material caveat and source-limited follow-up question visible, use the section order `Facts`, `Interpretation`, `Contradictions`, `Open questions`, `References`, begin directly at `Facts` for excerpt-only prompts, prefer the fewest grouped claim bullets and shortest declarative phrases that still preserve each caveat, use compact inline citations instead of repeated `Source: ...` restatements, avoid repeated source narration unless it changes the analysis, and end with the exact `Next verifier: ... | Evidence captured: ...` line after the references section.

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
- For research synthesis, use the explicit section order `Facts`, `Interpretation`, `Contradictions`, `Open questions`, `References`.
- Do not add `Mode`, `Read first`, `Proposed writes`, or a read-only/process preamble such as `Read-only synthesis from the excerpts supplied in the prompt` to a read-only research brief unless the prompt explicitly asks for write planning.
- Name the destination database, template, or page type before any mutation.
- Preserve source links, citations, open questions, contradictions, follow-up tasks, and material caveats in synthesized output, but keep them compact with grouped claim bullets, inline citations, and the fewest words needed when no caveat is lost.
- For research synthesis, keep every distinct source-limited follow-up question visible instead of collapsing it into a generic next step, group multiple questions from the same source into one bullet when that keeps them visible, and do not repeat `Source: ...` on every bullet when one citation per grouped claim is enough.
- Prefer updating or linking an existing page over creating a duplicate.
- End with one handoff line after `References` in the form `Next verifier: ... | Evidence captured: ...`.

## Procedure
1. Classify the request and state whether it is read-only or mutating.
2. If the prompt already contains the source excerpts for a read-only research synthesis, treat them as the source set, skip any MCP availability check, and draft only the final brief.
3. If live Notion access is required and Notion MCP is missing, emit the brief setup note and stop.
4. Search first, then fetch with `Notion:notion-search` and `Notion:notion-fetch` unless the prompt already supplied the excerpts for a read-only research brief. If multiple pages or databases fit, ask which one to use.
5. For capture, extract the decision, rationale, owner, related links, and follow-ups.
6. For meeting prep, extract the goal, attendees, decisions needed, blockers, and timeboxes; build the agenda or pre-read from fetched context.
7. For research synthesis, separate facts, interpretation, contradictions, and open questions; preserve every material caveat and each source-limited follow-up question from the fetched inputs; cite each source in the relevant section with compact inline citations; merge same-source facts into one bullet when doing so does not hide a caveat or contradiction; group same-source follow-up questions into one bullet separated by semicolons when that preserves visibility; avoid duplicating the same implication in both facts and interpretation when one sentence can carry both; use short declarative fragments rather than explanatory prose; add a `References` section; keep the synthesis compact, start directly at `Facts` for excerpt-only prompts, and avoid extra mode/process framing or repeated source narration unless it changes the analysis.
8. For research synthesis, finish with one exact handoff line after the references section: `Next verifier: ... | Evidence captured: ...`. Make the handoff line point first at whether support load was reduced or merely reassigned, then at the measurement window.
9. For spec-to-implementation, extract requirements, ambiguities, plan scope, and tasks; confirm the task database schema before creating pages.
10. For any write, repeat the destination and wait for explicit confirmation before using `Notion:notion-create-pages` or `Notion:notion-update-page`.
11. If an existing page already owns the content, update or link it instead of duplicating it.

## Pitfalls And Gotchas
- Rejected trope: dumping every Notion note into one generic summary. Better alternative: choose the artifact type first, then keep citations, decisions, and open questions separate.
- Rejected trope: inventing a database schema from memory. Better alternative: search, fetch, and confirm the actual destination and properties before any write.
- Rejected trope: creating a duplicate page when the existing page should be linked or updated. Better alternative: update the owning page and add backlinks.
- Rejected trope: starting an excerpt-only research brief with a setup or availability check. Better alternative: begin at `Facts` and keep the output compact.
- Rejected trope: smoothing contradictions into a clean narrative. Better alternative: list contradictions explicitly so the next verifier can see the tradeoffs.

## Progressive Disclosure
Start with the smallest useful read: what artifact is needed, who it is for, and whether the result is read-only or mutating. Expand only enough to locate sources, confirm the destination, and preserve traceability. Keep the skill compact; if workspace-specific schema details are needed, ask rather than guessing.

## Verification Pattern
- The artifact mode is explicit before drafting begins.
- Relevant pages were searched and fetched before any write was proposed.
- The destination database, template, or page type was confirmed before mutation.
- Citations, backlinks, open questions, contradictions, and material caveats survived the synthesis.
- Research synthesis kept every distinct source-limited follow-up question and ended with the required handoff line.
- Existing pages were updated or linked instead of duplicated when appropriate.
- Any mutation was gated by explicit confirmation.
- The final response ends with the exact handoff line format: `Next verifier: ... | Evidence captured: ...`.
