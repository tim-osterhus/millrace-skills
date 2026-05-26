---
asset_type: skill
asset_id: watchdog-file-watcher-patterns
version: 1
description: "Guardrail for Python watchdog adapters that turn filesystem activity into debounced, deduplicated, lifecycle-safe runtime queue events."
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

# Watchdog File Watcher Patterns

## Purpose
Help agents implement or repair Python watchdog adapters that convert local filesystem activity into stable runtime input events. This skill focuses on observer lifecycle, debounce, duplicate suppression, partial-write safety, queue handoff, and diagnosable shutdown.

**Use When**
- changing a watchdog-based intake path such as ideas folders, config watch paths, backlog files, or control markers
- debugging duplicate ingestion, partial reads, missed moves, or noisy modified events
- repairing shutdown hangs, leaked observer threads, or callbacks that do too much work
- deciding whether a watcher or simpler polling loop is safer

**Do Not Use When**
- a simple polling loop is clearly sufficient and lower risk
- the filesystem event should directly mutate runtime state from the callback
- the target is a distributed, remote, or cross-host event ingestion service

## Quick Start
1. Watch the smallest stable parent directory and filter the filenames you care about.
2. Treat created and modified events as "maybe changed" signals.
3. Prefer moved-into-place as the strongest ready signal.
4. Keep callbacks fast: normalize the event, enqueue lightweight work, and return.
5. Debounce duplicate event bursts and check file readiness before reading.
6. Own observer lifecycle explicitly: schedule, start once, stop, join, and surface errors.

## Operating Constraints
- Do not parse heavy content, sleep, block, or mutate runtime state inside watchdog callbacks.
- Do not assume editor save behavior, atomic renames, or close events are identical across platforms.
- Ignore temp files, swap files, partial suffixes, hidden files, and self-written artifacts where appropriate.
- Ensure one logical file action produces at most one runtime enqueue inside the configured debounce window.
- Hand off to a runtime queue or control API; keep the watcher as an adapter.
- Stop and join observer threads during shutdown without leaving orphans.
- Log enough event path, normalized action, debounce decision, and enqueue result to diagnose misses.

## Inputs This Skill Expects
- Watcher adapter entrypoint and observer lifecycle code.
- Watched path config, expected filenames, and runtime event types.
- Queue or control API used for handoff.
- Producer behavior when known: direct write, temp file plus rename, editor save, or marker touch.
- Logs or tests showing duplicates, partial reads, missed events, or shutdown hangs.

## Output Contract
- Provide watcher edits that filter, debounce, readiness-check, hand off, and shut down cleanly.
- State watch roots, filename filters, ignored patterns, debounce window, and readiness policy.
- Name the queue/control handoff and the runtime event emitted.
- Include tests or a smoke checklist for create, modify, move, temp-file, duplicate, and shutdown cases.
- State why watchdog remains appropriate or why polling is safer.

## Procedure
1. Locate watcher setup, handler callbacks, queue handoff, and shutdown path.
2. Identify actual producer behavior and file readiness signals.
3. Restrict watched roots and filters to the narrowest stable surface.
4. Normalize events into a small internal event shape.
5. Add debounce and duplicate suppression before content reads.
6. Move heavy parsing and runtime mutation out of callbacks into queue processing.
7. Implement explicit observer stop/join and error diagnostics.
8. Validate with create, modify, move-into-place, temp-file, duplicate burst, and shutdown scenarios.

## Pitfalls And Gotchas
- Treating every `modified` callback as a complete file.
- Watching a broad tree and then debugging unrelated event noise.
- Reading files before the producer has finished writing them.
- Doing slow parsing inside callback threads.
- Enqueueing duplicate work because save operations emit multiple events.
- Depending on `on_closed` as if it were a portable contract.
- Forgetting to join observers and leaving tests or daemons hanging.

## Progressive Disclosure
Start with the watched path and callback in scope. Expand into producer behavior, queue semantics, shutdown, or config reload only when the adapter crosses those boundaries. Keep business logic outside the watcher and use smoke scenarios to prove the adapter contract.

## Verification Pattern
- Confirm observer lifecycle has start, stop, and join behavior.
- Confirm callbacks only normalize and hand off lightweight work.
- Confirm temp and partial files are ignored until ready.
- Confirm duplicate event bursts collapse to one runtime enqueue.
- Confirm create, modify, move, duplicate, and shutdown scenarios are tested or smoke-checked.
