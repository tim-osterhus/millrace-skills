---
asset_type: skill
asset_id: cloudflare-durable-objects
version: 1
description: Guardrail for planning and reviewing Cloudflare Durable Object solutions with a thin Worker ingress, SQLite-backed state, alarms, WebSocket hibernation, and docs-first verification.
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

# Cloudflare Durable Objects

## Purpose

Make the Durable Object seam explicit before code or review prose. Start from the smallest honest surface: a thin Worker ingress that routes to one Durable Object core. Then decide the coordination atom, state ownership, storage model, RPC surface, alarm lifecycle, WebSocket lifecycle, config, and verification. This is a guardrail, not a Cloudflare manual.

### Use When

- the task is about chat rooms, multiplayer sessions, booking slots, per-user state, queues, or other per-entity coordination
- the prompt asks for Durable Object RPC methods, storage, alarms, WebSockets, migrations, or testing
- the task is reviewing a Durable Object for lifecycle, eviction, hibernation, storage ordering, or concurrency bugs
- the answer depends on current Cloudflare Durable Objects or Wrangler docs

### Do Not Use When

- the problem is generic stateless Worker plumbing
- the real decision is whether to use a plain Worker, Durable Object, Agents SDK, or remote MCP
- the work is broad Workers or Wrangler configuration with no Durable Object boundary question
- another more specific skill already owns the seam

## Quick Start

1. Name the coordination atom first: room, booking, document, user, match, or similar natural shard.
2. Keep the Worker ingress thin. Validate input, derive the object name, and hand off to a single Durable Object stub.
3. Before code or config changes, check the current Cloudflare docs for the exact API, lifecycle, and Wrangler details in scope.
4. Use `getByName` for deterministic routing from meaningful names. Reach for `idFromName` only when you already need the raw ID or are interoperating with a lower-level API.
5. Use SQLite-backed storage for new structured state. Put the class in `new_sqlite_classes` in the first migration if the class is new.
6. Use `sql.exec` for schema-backed, transactional state. Treat in-memory values as caches or derived data only.
7. Use `blockConcurrencyWhile` only for constructor setup or a narrowly bounded async bootstrap that must not interleave.
8. If sockets are required, start from the hibernation WebSocket model. If timers are required, prefer alarms over `setTimeout` or `setInterval`.
9. End the answer with one concrete verification step that matches the chosen seam.

## Operating Constraints

- One Durable Object instance should represent one natural unit of coordination.
- The Durable Object owns the truth. Module globals may cache derived data, but they should not hold critical state.
- Persist before you cache or publish side effects.
- Keep HTTP ingress as a thin adapter that routes to the stub and returns the response.
- Prefer class methods and RPC-style calls for ordinary operations; use `fetch()` only when HTTP semantics are truly part of the contract.
- Treat alarms as per-object future work, and assume alarm handling is at least once.
- If sockets are required, prefer the Hibernation WebSocket API and keep per-connection metadata in attachments or storage.
- Before code or config changes, check the current Cloudflare docs whenever APIs, limits, compatibility dates, or Wrangler fields matter.

## Inputs This Skill Expects

- the request goal and the intended coordination atom
- current Durable Object, Worker, or Wrangler files when they exist
- current Cloudflare docs for the APIs in scope
- any test or verification constraints already known
- whether the prompt is asking for planning, review, or a code change

## Output Contract

- Name the coordination atom explicitly.
- State the ownership boundary, storage model, RPC surface, alarm lifecycle, WebSocket lifecycle, config, and verification separately.
- Name the smallest honest starting point, usually a thin Worker ingress plus one Durable Object core.
- For review prompts, call out lifecycle, eviction, hibernation, storage ordering, alarm, and socket cleanup risks before suggesting code.
- Include one concrete proof step instead of vague confidence.

## Procedure

1. Identify the natural coordination atom and refuse a global object unless the whole system truly serializes around one queue.
2. Draw the ownership boundary: the Worker should stay thin, and the Durable Object should own the state and lifecycle.
3. Choose the storage model. Default new structured state to SQLite-backed storage and use `sql.exec` for transactional reads and writes.
4. Decide the RPC surface. Prefer class methods for ordinary operations and keep `fetch()` only when the contract needs HTTP semantics.
5. Decide the lifecycle path. Use alarms for durable future work and the Hibernation WebSocket model when live sockets are required.
6. Check the current docs before code or config changes when APIs, limits, or Wrangler fields matter.
7. Verify the seam with the smallest proof step that matches the work, such as a named-object call, a SQL round trip, an alarm trigger, or a WebSocket cleanup path.

## Pitfalls And Gotchas

- single global DO
- request-scoped module vars
- critical state only in memory
- `setTimeout` or `setInterval` for durable work
- `blockConcurrencyWhile` around external I/O or every request
- hidden migration assumptions
- ignoring hibernation cleanup
- alarms or sockets that rely on memory surviving eviction

### Rejected Trope

- Rejected trope: keep everything in the Worker and add a Durable Object later.
- Better alternative: decide the coordination atom first, route through a thin Worker, and let one Durable Object own state and lifecycle from the start.

## Progressive Disclosure

- Start with the smallest useful decision: coordination atom, ownership boundary, and docs check.
- Expand only enough to choose cleanly between storage, RPC, alarm, WebSocket, and migration details.
- Keep the skill short so it steers implementation instead of becoming a Cloudflare manual.
- Use the same guardrail for build and review prompts so the seam stays consistent across tasks.

## Verification Pattern

- Confirm the coordination atom is explicit.
- Confirm state ownership, storage model, RPC surface, alarm lifecycle, WebSocket lifecycle, config, and verification are named separately.
- Confirm the answer includes one concrete proof step instead of vague confidence.
- Next verifier: implementation reviewer or checker; capture the docs consulted, the chosen coordination atom, the migration tag, the lifecycle strategy, and one proof step.
