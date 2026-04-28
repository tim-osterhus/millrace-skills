---
asset_type: skill
asset_id: ai-app-integration
version: 1
description: Guardrail for choosing and separating AI SDK and ChatGPT Apps SDK integration seams.
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

# AI App Integration

## Purpose
Help agents decide whether an AI-powered feature should be built with AI SDK only, ChatGPT Apps SDK + MCP, or a hybrid, then make model, tool, UI, and persistence ownership explicit before implementation. This is a guardrail, not an API manual.

### Use When
- the task touches chat, streaming, structured output, tool calling, embeddings, or agent loops
- the task needs a ChatGPT host surface, widget, MCP tool, or app submission shape
- the current implementation mixes model logic, tool execution, UI state, and storage
- the answer depends on current AI SDK or Apps SDK API shapes

### Do Not Use When
- the task is pure prompt writing, evaluation, or model comparison with no app integration
- the work is generic backend plumbing that does not touch an AI surface
- deployment, auth, or launch logistics are the only problem
- another more specific skill already owns the surface

## Quick Start
1. Classify the request first as `AI SDK only`, `ChatGPT Apps SDK + MCP`, or `hybrid`.
2. Write the ownership map next: model, tools, UI, persistence.
3. Fetch current official docs before writing code whenever AI SDK v6 or Apps SDK APIs are involved.
4. Prefer AI SDK v6 for chat, streaming, structured output, tool calling, embeddings, and agent loops.
5. Use ChatGPT Apps SDK + MCP only when the user-visible surface needs ChatGPT host integration or a widget.
6. Treat `window.openai` compatibility as secondary to the MCP Apps bridge and current docs.
7. End with the next verifier and the evidence it should capture.

## Operating Constraints
- Do not let UI state leak into model tools.
- Do not hide persistence behind tool calls.
- Do not choose ChatGPT Apps when a plain AI SDK route is enough.
- Do not rely on v5-era AI SDK snippets or memory for v6 signatures.
- Do not teach wrapper helpers as the canonical surface when the docs expose a better current API.
- Do not turn this into a generic AI SDK cookbook or a ChatGPT Apps walkthrough.

## Inputs This Skill Expects
- the user goal and the target surface
- whether the feature needs a ChatGPT host surface, widget, or MCP tool exposure
- the current model, tool, UI, and persistence boundaries if any exist
- the official docs or package versions already in scope
- any existing route, server, or widget file that the request should fit into

## Output Contract
- Name the classification first.
- State which layer owns generation, tool execution, UI rendering, and persistence.
- State which current docs must be checked before code changes.
- Recommend the smallest viable starting point and what not to build.
- Keep the answer at planning level unless the task explicitly asks for implementation details.

## Procedure
1. Read the request and classify the surface.
2. Draw the boundary map before choosing code shape.
3. Check the current official docs for every AI SDK or Apps SDK API involved.
4. Choose the smallest architecturally coherent seam that satisfies the contract honestly.
5. Prefer AI SDK only unless the host surface materially changes the product.
6. Use ChatGPT Apps SDK + MCP when the product needs ChatGPT-hosted UI, widget metadata, or MCP tool wiring.
7. Verify the selected seam against the docs and the next runtime or browser check.

## Pitfalls And Gotchas
- Rejected trope: wire the model straight to the UI and let tools sort out the rest.
- Better alternative: separate model, tool, UI, and persistence ownership first, then connect them with explicit interfaces.
- Rejected trope: build a ChatGPT app because the feature is interactive.
- Better alternative: stay AI SDK only when the host surface does not add value.
- Rejected trope: follow old SDK snippets from memory.
- Better alternative: fetch current docs and match the current v6 or Apps SDK signatures.
- Rejected trope: hide storage inside tool handlers.
- Better alternative: keep persistence behind its own API or data layer.
- Rejected trope: turn the skill into a full API reference.
- Better alternative: keep it a guardrail that chooses seams and evidence.

## Progressive Disclosure
Start with the smallest useful decision: surface class, ownership map, and docs check. Expand only enough to choose between AI SDK only, ChatGPT Apps SDK + MCP, or hybrid cleanly. Keep the skill short so it steers implementation instead of becoming a manual.

## Verification Pattern
- Confirm the classification is explicit.
- Confirm model, tool, UI, and persistence boundaries are named separately.
- Confirm a docs-first check is named before code.
- Confirm the answer does not collapse into a generic prompt-engineering or app-architecture essay.
- Next verifier: the implementation reviewer or checker; capture the docs consulted, the selected architecture, and the boundary map.
