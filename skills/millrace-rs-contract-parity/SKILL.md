---
asset_type: skill
asset_id: millrace-rs-contract-parity
version: 1
description: "Guardrail for Rust Millrace prototype work that must preserve Python runtime contracts, file-backed state, runner boundaries, and async daemon safety."
advisory_only: true
capability_type: implementation-guardrail
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

# Millrace Rust Contract Parity

## Purpose
Help agents build Rust slices for Millrace without erasing the runtime contract the Python implementation already owns. This is a guardrail for contract-parity Rust work, not a generic Rust tutorial or a migration plan.

### Use When
- implementing or reviewing Rust code for a Millrace prototype, kernel, CLI, daemon, runner, workspace model, compiler, or queue component
- translating file-backed state, persisted JSON, Markdown queue documents, runner subprocess behavior, or stage-machine semantics from Python into Rust
- adding async Rust around daemon loops, runner supervision, cancellation, stdout/stderr streaming, or monitor output
- deciding whether a Rust slice is ready to replace or shadow an existing Python runtime boundary

### Do Not Use When
- the work is ordinary Rust unrelated to Millrace runtime contracts
- the task is to rewrite Millrace wholesale without a scoped parity target
- no persisted state, runner boundary, process lifecycle, or async runtime behavior is involved

## Quick Start
1. Name the exact Python-owned contract before writing Rust: workspace paths, schema files, queue document shape, runner request/result boundary, CLI output, or stage transition behavior.
2. Build a narrow contract-parity slice first. Do not start with the daemon or async orchestration before workspace, init, compiler, and persisted-state parity are covered.
3. Model persisted data with typed Rust structs and `serde`; keep file and process boundaries explicit with `PathBuf`, `OsStr`, `ExitStatus`, stdout, stderr, and structured errors.
4. Preserve `compiled_plan.json` authority, queue lineage fields, stage result enums, terminal results, and `StageRunRequest -> RunnerRawResult` behavior unless an explicit migration spec changes them.
5. Use custom error types for library/runtime boundaries and add context at CLI or application edges. Avoid `unwrap` and `expect` in runtime paths.
6. Add golden parity tests against real or fixture Millrace artifacts before claiming equivalent behavior.
7. Run targeted `cargo test`, `cargo fmt --check`, and `cargo clippy --all-targets -- -D warnings` for every completed slice.

## Operating Constraints
- Do not rewrite Python Millrace as a broad clean-room replacement.
- Do not invent new queue states, stage names, terminal results, status markers, or persisted schema fields while claiming parity.
- Do not parse structured JSON with ad hoc string handling when `serde` can represent the contract.
- Do not treat Markdown queue/spec files as free-form prose if the runtime relies on stable headers.
- Do not write state files in place when partial writes could leave the workspace corrupt; use atomic write patterns and preserve UTF-8/path boundary behavior.
- Do not hold mutex guards across `.await`, block the Tokio executor with filesystem or subprocess waits, or spawn tasks that cannot be cancelled and joined.
- Do not hide subprocess failures behind success-shaped output; carry exit code, stdout, stderr, timeout, and kill outcome forward.
- Avoid `unsafe`; if it is unavoidable, isolate it and document the invariant with a `SAFETY:` comment.

## Inputs This Skill Expects
- The Rust crate or slice being added.
- The Python module, CLI command, runtime artifact, or fixture that defines expected behavior.
- Whether the slice is synchronous state/compiler work, subprocess runner work, or async daemon work.
- The verification command that proves parity for this slice.

## Output Contract
- Name the contract being preserved and the Rust boundary that implements it.
- List any intentional behavioral differences from Python and why they are allowed.
- Identify the fixture, golden artifact, or live command used for parity evidence.
- Include the exact Rust validation commands that were run or still need to be run.
- Keep daemon/async advice scoped to runtime orchestration; keep compiler/state advice scoped to deterministic file-backed behavior.

## Procedure
1. Locate the Python source of truth and the persisted artifact shape before designing Rust types.
2. Define the smallest Rust boundary that can prove parity: data model, compiler output, queue reader/writer, runner adapter, CLI command, or daemon tick.
3. Use exhaustive enums for state machines and terminal results; avoid wildcard matches that silently accept future states.
4. Prefer synchronous, deterministic code for workspace loading, parsing, validation, and compiler output until async is required by process supervision or daemon orchestration.
5. For file-backed state, normalize paths at boundaries, preserve stable serialized field names, write through a temp file, and surface parse errors with file paths and context.
6. For subprocess runners, capture command, cwd, environment deltas, exit status, stdout, stderr, duration, timeout, and cancellation behavior in the result model.
7. For async daemon work, use explicit cancellation tokens, bounded channels where backpressure matters, joined task handles, and tracing spans around stage/run identifiers.
8. Add parity tests before broadening the slice. Golden tests should fail when a field is renamed, a terminal result changes, lineage drifts, or subprocess failure is flattened.
9. Run the relevant Cargo checks and report their exact outcomes.

## Pitfalls And Gotchas
- Rejected trope: starting with a new Rust daemon because async code feels like the hard part.
- Better alternative: prove workspace, init, compiler, queue, and runner contract parity first, then wrap those stable boundaries in async orchestration.
- Rejected trope: replacing Python's persisted artifacts with more idiomatic Rust shapes.
- Better alternative: use idiomatic Rust internally while serializing the same external contract.
- Rejected trope: using `anyhow` everywhere until recoverable runtime categories disappear.
- Better alternative: use typed errors inside runtime/library code and add `anyhow` context only at outer application edges.
- Rejected trope: treating process supervision as just `Command::output()`.
- Better alternative: model timeout, cancellation, stderr, exit status, and cleanup as first-class outcomes.
- Rejected trope: calling a Rust slice equivalent because unit tests pass.
- Better alternative: compare against golden Millrace artifacts and CLI behavior that represent the Python contract.

## Verification Pattern
- Confirm the Rust code names the Python contract or artifact it mirrors.
- Confirm persisted schemas use stable field names and `serde` models rather than string-spliced JSON.
- Confirm state transitions and terminal results are exhaustive and parity-tested.
- Confirm file writes are atomic where state corruption is possible.
- Confirm subprocess results cannot lose exit status, stderr, timeout, or cancellation information.
- Confirm async code has cancellation and does not hold locks across awaits.
- Confirm `cargo fmt --check`, targeted `cargo test`, and `cargo clippy --all-targets -- -D warnings` were run for the slice, or state the precise blocker.
