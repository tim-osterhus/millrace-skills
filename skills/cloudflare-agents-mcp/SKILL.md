---
asset_type: skill
asset_id: cloudflare-agents-mcp
version: 1
description: Guardrail for defaulting generic stateful services with tools to plain Worker plus Durable Object, and escalating to Agents SDK or remote MCP only when an explicit external interface or agent loop is required.
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

# Cloudflare Agents MCP

## Purpose
Help agents choose the smallest honest Cloudflare surface for a request that may involve Workers, Durable Objects, Agents SDK, or remote MCP. Generic stateful or tool-service prompts start as plain Worker plus Durable Object ownership. Remote MCP, `McpAgent`, and Agents SDK are conditional, not default. Treat `tool service` as a capability label, not a transport decision. Then make state, tools, auth, transport, deployment, and verification ownership explicit before any code is written. This is a guardrail, not a Cloudflare manual.

### Use When
- the task needs a decision between a plain Worker, Durable Object, Agents SDK agent, remote MCP server, or hybrid
- the request touches stateful agents, callable methods, WebSockets, scheduled tasks, MCP tools, OAuth, or deployment boundaries
- the current code mixes state, transport, tools, and auth
- the answer depends on current Cloudflare docs or recent SDK or API behavior

### Do Not Use When
- the work is generic Workers, backend, or frontend plumbing with no agent or MCP boundary question
- deployment ops, account setup, or launch logistics are the only problem
- the request is only about prompt writing or generic architecture advice
- another more specific skill already owns the surface

## Quick Start
1. Classify the request first as `plain Worker`, `Durable Object`, `Agents SDK agent`, `remote MCP server`, or `hybrid`.
2. If the prompt only says `stateful service` or `tool service`, answer `plain Worker` or `Durable Object` first. That wording alone does not justify `remote MCP server`, `McpAgent`, or an Agents SDK surface.
3. Choose `plain Worker` when request/response is enough and no shared mutable state matters.
4. Choose `Durable Object` when per-key state, coordination, idempotency, or session continuity is the real need.
5. Choose `Agents SDK agent` only when first-class agent behavior, callable methods, or WebSockets are central.
6. Choose `remote MCP server` only when the prompt explicitly requires an external MCP-facing tool surface or host-independent client boundary.
7. Choose `hybrid` only when two distinct surfaces are explicitly required; do not use it to cover uncertainty.
8. Write the ownership map next: state, tools, auth, transport, deployment, verification.
9. Check current Cloudflare docs before code whenever Agents SDK, MCP, or Workers APIs are involved.
10. Prefer plain Worker or Durable Object when Agents SDK or MCP adds no value.
11. Call out `McpAgent`, `routeAgentRequest`, WebSocket handling, and scheduling only when they are actually part of the chosen seam.
12. End with the next verifier and the evidence it should capture.

## Operating Constraints
- Do not let state live inside transport handlers.
- Do not hide OAuth or persistence inside tool code.
- Do not choose remote MCP because the task is "AI adjacent" or because tools are mentioned.
- Do not choose Agents SDK for a simple request/response service.
- Do not choose `hybrid` just because the service is stateful and could also expose MCP.
- Do not rely on memory for Agents SDK, MCP, or Workers API names when current docs are available.
- Do not turn this into a full Cloudflare course.

## Inputs This Skill Expects
- the request goal and target surface
- whether state, tools, auth, WebSockets, scheduling, or MCP exposure matter
- current route, server, agent, or worker files if any exist
- current official docs for the APIs in scope
- any deployment or verification constraints already known

## Output Contract
- Name the architecture classification first.
- State ownership for state, tools, auth, transport, deployment, and verification separately.
- State which current docs must be checked before code.
- Recommend the smallest viable starting point and what not to build.
- Keep the answer at planning level unless implementation is explicitly requested.

## Procedure
1. Read the request and classify it as `plain Worker`, `Durable Object`, `Agents SDK agent`, `remote MCP server`, or `hybrid`.
2. Draw the ownership map before choosing code shape.
3. Check current Cloudflare docs for every Agents SDK, MCP, or Workers API involved.
4. Prefer plain Worker or Durable Object unless the request truly needs agent or MCP surface behavior.
5. Use Agents SDK when stateful agent behavior, callable methods, or WebSockets are central.
6. Use remote MCP when the main surface is tool exposure over MCP and the host app is not the real boundary.
7. Call out `McpAgent`, `routeAgentRequest`, WebSocket handling, and scheduling only when they are actually part of the chosen seam.
8. Verify the selected seam with the smallest proof step that matches the boundary.

## Pitfalls And Gotchas
- Rejected trope: wire state straight into transport handlers and hope the boundary stays clean.
- Better alternative: keep state, tools, auth, transport, deployment, and verification owned by separate seams.
- Rejected trope: use Agents SDK for a simple request/response Worker.
- Better alternative: stay plain Worker or Durable Object when agent semantics add no value.
- Rejected trope: use remote MCP because the feature is "AI adjacent."
- Better alternative: choose remote MCP only when tool exposure over MCP is the actual interface.
- Rejected trope: let `tool service` alone choose remote MCP server, `McpAgent`, or an Agents SDK surface.
- Better alternative: require an explicit external MCP interface, host-independent tool exposure, or first-class agent behavior first.
- Rejected trope: call it `hybrid` just because the service is stateful and could also expose MCP.
- Better alternative: choose `hybrid` only when two distinct surfaces are clearly required.
- Rejected trope: follow old examples from memory.
- Better alternative: check current Cloudflare docs before writing code.
- Rejected trope: turn this skill into a full Cloudflare manual.
- Better alternative: keep it as a narrow architecture guardrail.

## Progressive Disclosure
Start with the smallest useful decision: surface class, ownership map, and docs check. Expand only enough to choose cleanly between plain Worker, Durable Object, Agents SDK agent, remote MCP server, or hybrid. Keep the skill short so it steers implementation instead of becoming a manual.

## Verification Pattern
- Confirm the classification is explicit.
- Confirm state, tools, auth, transport, deployment, and verification are named separately.
- Confirm a docs-first check is named before code.
- Confirm the answer does not collapse into a generic Cloudflare essay.
- Next verifier: implementation reviewer or checker; capture the docs consulted, the selected architecture, and one concrete proof step.
