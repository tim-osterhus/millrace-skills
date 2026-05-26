---
asset_type: skill
asset_id: typer-cli-patterns
version: 1
description: "Guardrail for Typer-based Python control-plane CLIs that keep handlers thin, deterministic, testable, and separated from runtime behavior."
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

# Typer CLI Patterns

## Purpose
Help agents build or refactor Typer command surfaces that wrap a runtime or control API without moving engine logic into CLI handlers. This skill is for Python control-plane CLIs with deterministic output, explicit exits, and focused tests.

**Use When**
- adding or changing Typer commands for status, start, stop, pause, resume, queue inspection, config, or task intake
- introducing shared flags such as `--json`, `--format`, `--detail`, `--timeout`, or `--verbose`
- refactoring CLI handlers that contain runtime logic, queue mutation, or output formatting sprawl
- adding tests for command success, validation, and failure behavior

**Do Not Use When**
- building a REPL, shell, TUI, or generic command runner
- using Click directly without Typer conventions
- the task is mostly runtime behavior and the CLI surface is unchanged

## Quick Start
1. Keep each handler thin: parse inputs, call one control-layer operation, render output, and exit.
2. Keep reads pure and writes explicit.
3. Standardize one structured output mode, usually `--json` or `--format json`.
4. Keep machine output free of progress prose and nondeterministic field ordering.
5. Validate user input before runtime mutation.
6. Cover changed command groups with success and failure tests using Typer's runner or the repo's CLI test harness.

## Operating Constraints
- Importing the CLI module must not start runtime loops, load mutable queues, or mutate config.
- Handlers should not reach directly into engine internals when a control API exists.
- Read commands such as `status`, `queue`, and `config show` must not mutate runtime state.
- Mutating commands must call named control operations and make side effects explicit.
- Human output and JSON output must have stable shapes.
- User-facing errors should map to deterministic exit codes and concise messages.
- Help text should match the real command contract.

## Inputs This Skill Expects
- CLI entry module or package.
- Underlying control/API surface called by the CLI.
- Target command list, changed verbs, or desired runtime operations.
- Current help output, tests, snapshots, and exit-code policy when available.
- Sample control-layer success and failure payloads.

## Output Contract
- Provide a command tree or patch where handlers stay thin and deterministic.
- Name command-to-control mappings for changed commands.
- State read/write boundaries, output format policy, and exit behavior.
- Include focused tests for at least one success path and one failure or edge path per changed command group.
- Report help text or docs updates when the user-facing command surface changes.

## Procedure
1. Inspect CLI entrypoints, Typer app structure, imports, and control-layer operations.
2. Map each command to exactly one control operation or one composed read path.
3. Pull rendering into small deterministic helpers when handlers are getting noisy.
4. Validate parameters and options before invoking mutating control calls.
5. Implement JSON output with stable keys and human output with stable headings.
6. Add tests using isolated temp state and representative control-layer results.
7. Run help output and targeted CLI tests.

## Pitfalls And Gotchas
- Letting Typer handlers become the runtime layer.
- Running side effects at import time.
- Mixing logs, progress, or prose into JSON output.
- Adding both `--json` and `--format json` without a clear compatibility reason.
- Making `status` or `config show` mutate state as a side effect.
- Testing only the happy path and missing validation, missing config, or runtime-error mapping.

## Progressive Disclosure
Start with the changed command group. Expand to shared renderers, exit-code policy, command grouping, or docs only when the current change crosses those surfaces. Keep runtime design in the control layer and CLI design in the command layer.

## Verification Pattern
- Confirm CLI module import has no runtime side effects.
- Confirm each changed handler parses, calls control, renders, and exits without embedding engine logic.
- Confirm read commands are pure and write commands are explicit.
- Confirm JSON output parses and has stable keys.
- Run targeted CLI tests plus a `--help` smoke check for changed commands.
