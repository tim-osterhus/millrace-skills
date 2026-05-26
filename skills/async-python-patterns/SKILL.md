---
asset_type: skill
asset_id: async-python-patterns
version: 1
description: "Guardrail for Python runtime loops that must choose sync-first or asyncio with owned task lifetimes, cancellation, shutdown, and blocking-call isolation."
advisory_only: true
capability_type: implementation-guardrail
recommended_for_stages:
  - planner
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

# Async Python Patterns

## Purpose
Help agents decide whether a Python runtime component should stay synchronous or adopt asyncio, then implement async only where it solves a concrete coordination problem. This skill is for service loops, supervisors, queues, subprocess boundaries, cancellation, timeouts, and graceful shutdown.

**Use When**
- adding or repairing an engine supervisor, queue worker, adapter loop, file watcher, or runtime service
- shutdown hangs, leaked background tasks, swallowed exceptions, or timeout behavior need diagnosis
- blocking file I/O, SDK calls, or subprocess calls appear on an event-loop path
- a component must coordinate multiple waits without freezing the process

**Do Not Use When**
- a simple synchronous loop is fast enough and easier to reason about
- the task is framework-specific FastAPI, Trio, AnyIO, Celery, or web-handler work
- the desired behavior is a fire-and-forget task with no owner or shutdown contract

## Quick Start
1. Start sync-first: name the coordination or responsiveness problem that async must solve.
2. Identify the owner scope for every task, queue, subprocess, watcher, and cancellation signal.
3. Use structured ownership such as `asyncio.TaskGroup` or an explicit task registry with observed exceptions.
4. Move blocking calls behind `asyncio.to_thread()`, executor boundaries, asyncio subprocess APIs, or keep the component synchronous.
5. Treat cancellation as normal control flow and make cleanup idempotent.
6. Verify timeout, cancellation, slow callback, and shutdown behavior with targeted tests or a repeatable smoke run.

## Operating Constraints
- Do not add `async` by default; async needs a specific concurrency reason.
- Do not spawn naked background tasks. Every task must be awaited, cancelled, or supervised by an owner.
- Do not hold locks or mutable state guards across awaits unless the state model explicitly permits it.
- Do not block an event loop with filesystem polling, subprocess waits, SDK calls, sleep loops, or CPU-heavy work.
- Apply config and persisted-state reloads only at explicit boundaries.
- Keep shutdown ordered: stop intake, drain or abandon by policy, cancel remaining work, observe exceptions, then exit.
- Log task names, work identifiers, timeout boundaries, and cancellation paths where operators need diagnosis.

## Inputs This Skill Expects
- The runtime entrypoint, supervisor loop, worker, watcher, or adapter file.
- The shutdown contract: signal handling, stop marker, parent lifecycle, or operator command.
- The Python version floor and allowed async primitives.
- The repo validation path: tests, smoke command, or daemon run command.
- Any logs showing hangs, leaked tasks, missed cancellations, or blocking behavior.

## Output Contract
- Either recommend sync-first with minimal async changes, or justify a bounded async design.
- Name the owner for every task and the exit path for every long-running operation.
- State queue handoff, backpressure, timeout, cancellation, and blocking-call isolation policy.
- Include targeted tests or smoke evidence for timeout, cancellation, and shutdown.
- Report any compatibility downgrade if Python version constraints prevent modern primitives.

## Procedure
1. Confirm the runtime boundary and whether async is justified.
2. Locate task owners, queue boundaries, subprocess calls, sleeps, file I/O, and SDK calls.
3. Design the smallest concurrency model that solves the real problem.
4. Implement ownership, cancellation, timeout, and shutdown paths before adding new concurrent work.
5. Move blocking work off the event loop or keep the surrounding component synchronous.
6. Add diagnostics that expose slow callbacks, never-awaited coroutines, and never-retrieved exceptions.
7. Validate the normal path plus timeout, cancellation, and shutdown paths.

## Pitfalls And Gotchas
- Sprinkling `async` across a codebase without changing ownership or shutdown behavior.
- Creating tasks without retaining handles or observing exceptions.
- Treating `CancelledError` as an unexpected failure instead of a normal stop path.
- Mixing sync file/subprocess calls into an event-loop path.
- Letting reloads mutate active state in the middle of a stage or work item.
- Claiming shutdown is fixed without testing a live cancellation or stop sequence.

## Progressive Disclosure
Start with the single runtime boundary in scope. Expand into subprocess supervision, queue backpressure, config reloads, diagnostics, or daemon lifecycle only when the current component crosses those boundaries. Prefer tests over broad architecture essays.

## Verification Pattern
- Confirm async is either rejected with a sync-first reason or accepted with a concrete coordination reason.
- Confirm every spawned task has an owner and observed exception path.
- Confirm event-loop paths do not call blocking APIs directly.
- Confirm shutdown stops intake, drains or abandons by policy, cancels remaining tasks, and exits.
- Run targeted tests or a smoke harness for success, timeout, cancellation, and shutdown behavior.
