---
asset_type: skill
asset_id: cloudflare-workers-platform
version: 1
description: Guardrail for choosing the smallest honest Cloudflare Workers seam, reviewing Worker code/config, and keeping Wrangler flows aligned with current docs.
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

# Cloudflare Workers Platform

## Purpose

Help agents choose the smallest honest Cloudflare Workers seam and review Worker code, config, secrets, and deploy or verify steps without turning the skill into a Cloudflare manual. Start from plain Worker, Pages Function, or Worker plus bindings, then hand off to `cloudflare-durable-objects` or `cloudflare-agents-mcp` when coordination or agent/MCP behavior is the real seam.

### Use When

- the task is building, reviewing, or debugging a Cloudflare Worker or Pages Function
- the work touches `wrangler.jsonc`, compatibility dates, bindings, secrets, routes, environments, local dev, deploy, or tail
- the prompt asks you to choose among Workers, Pages Functions, KV, R2, D1, Queues, Hyperdrive, service bindings, or observability
- the answer depends on current Cloudflare docs, Wrangler behavior, or config schema details
- the user wants production-readiness guidance for Cloudflare runtime code or config

### Do Not Use When

- the task is primarily about Durable Objects, Agents SDK, or remote MCP
- the problem is generic backend or frontend work with no Cloudflare-specific seam
- another more specific skill already owns the exact boundary
- the request is only about broad Cloudflare platform strategy with no Worker or Wrangler seam to choose

## Quick Start

1. Classify the request first as `seam selection`, `code review`, `config review`, or `deploy/verify`.
2. Pick the smallest honest seam first: plain Worker, Pages Function, or Worker plus bindings.
3. Before any version-sensitive advice, check current Cloudflare Workers docs, Wrangler docs, the Wrangler config schema, and generated Worker types.
4. Keep state, bindings, secrets, routes, and verification ownership explicit.
5. Prefer in-process bindings, service bindings, generated types, and schema-checked config over guesses.

## Operating Constraints

- Do not put request-scoped state in module globals.
- Do not leave background work as a floating promise; use `ctx.waitUntil()` or fully `await`, `return`, or `void` the promise.
- Do not hand-write `Env` or guess binding names; run `wrangler types` after config changes.
- Do not hardcode secrets in source or `wrangler.jsonc`; use `wrangler secret put` for secrets and `vars` for non-secrets.
- Do not rely on a stale `compatibility_date` or skip required compatibility flags for the code you are shipping.
- Do not call Cloudflare REST APIs from a Worker when an in-process binding or service binding exists.
- Do not hand-roll PostgreSQL or MySQL connectivity from a Worker when Hyperdrive is the intended seam.
- Do not choose Durable Objects, Agents SDK, or remote MCP unless that seam is actually required.
- Rejected trope: rewrite the task into a framework or agent architecture because it feels more scalable.
- Better alternative: keep the smallest Cloudflare surface that matches the request and wire bindings, types, and config directly.
- Rejected trope: trust memory for version-sensitive Workers or Wrangler APIs.
- Better alternative: check current docs and generated types before giving advice or commands.
- Rejected trope: use the public Cloudflare REST API from inside the Worker because it is already HTTP.
- Better alternative: use in-process bindings, service bindings, or the correct Cloudflare product surface instead.

## Inputs This Skill Expects

- the request goal and target Cloudflare surface
- whether code, config, bindings, secrets, routes, or deployment checks are in play
- current Worker, Pages, or Wrangler files when they exist
- current official docs for the APIs in scope
- any test or verification constraints already known

## Output Contract

- Name the seam class first.
- State the ownership boundary for code, config, bindings, secrets, routes, and verification separately.
- Name the smallest honest starting point, usually a plain Worker, a Pages Function, or a Worker plus bindings.
- Call out the current docs check needed before version-sensitive advice.
- For review prompts, flag module globals, missing `ctx.waitUntil()`, floating promises, hand-written `Env`, secrets in source, stale compatibility dates, and binding-name mismatches.
- Keep the answer planning-level unless implementation is explicitly requested.
- End with the next verifier and the evidence it should capture.

## Procedure

1. Read the request and classify it as `seam selection`, `code review`, `config review`, or `deploy/verify`.
2. Choose the smallest honest Cloudflare surface that fits the work.
3. Check current Cloudflare docs, Wrangler docs, the Wrangler config schema, and generated Worker types before any version-sensitive advice.
4. Prefer in-process bindings and service bindings over public HTTP when Cloudflare already exposes the capability directly.
5. Use `wrangler.jsonc` as the config source of truth and regenerate types after binding changes.
6. Verify the changed seam with the smallest proof step that matches the work.

## Pitfalls And Gotchas

- single request-scoped value in a module global
- background work that is neither awaited nor passed to `ctx.waitUntil()`
- hand-written `Env` that drifts from `wrangler.jsonc`
- secret values committed to source or config
- stale compatibility dates or missing flags for the chosen runtime behavior
- public HTTP between Workers when a service binding would be cheaper and safer
- choosing Durable Objects or agent or MCP surfaces when the prompt only needs a plain Worker or Pages Function

### Rejected Trope

- Rejected trope: split Workers guidance, Wrangler guidance, and review guidance into separate skills for v1.
- Better alternative: keep one compact Workers platform guardrail with explicit handoff boundaries to the more specialized Cloudflare skills.

## Progressive Disclosure

Start with the smallest useful decision: Cloudflare surface, docs check, and the owning boundary. Expand only enough to choose cleanly between code, config, bindings, secrets, routes, and deploy or verify details. Keep the skill short enough that it steers decisions instead of becoming a manual.

## Verification Pattern

- Confirm the seam class is explicit.
- Confirm code, config, bindings, secrets, routes, and verification are owned separately.
- Confirm the answer names the current docs check before version-sensitive advice.
- Confirm the review checklist catches the common Workers failure modes.
- Next verifier: implementation reviewer or checker; capture the docs consulted, the chosen surface, and one concrete proof step such as `wrangler types --check`, `wrangler check`, or a route or config diff.
