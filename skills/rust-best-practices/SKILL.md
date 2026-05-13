---
asset_type: skill
asset_id: rust-best-practices
version: 1
description: "Implementation guardrail for idiomatic Rust ownership, error handling, linting, performance discipline, testing, documentation, and public API review."
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

# Rust Best Practices

## Purpose
Help agents write and review idiomatic Rust that respects ownership, explicit errors, lint discipline, performance evidence, tests, and documentation. This skill is for ordinary Rust quality; use narrower domain skills when Rust is only one part of a larger platform contract.

**Use When**
- writing, refactoring, or reviewing Rust code
- deciding between borrowing, cloning, ownership transfer, generics, trait objects, or type-state patterns
- shaping library and binary error boundaries
- adding tests, docs, lint rules, or performance-sensitive changes

**Do Not Use When**
- a repo-specific Rust contract skill already owns the behavior
- the task is only cargo invocation with no code or design judgment
- the user explicitly wants a quick syntax answer

## Quick Start
1. Prefer borrowed parameters: `&str`, `&[T]`, and `&T` unless ownership is required.
2. Return `Result` for fallible runtime paths; avoid `panic!`, `unwrap`, and `expect` outside tests or startup invariants.
3. Use typed errors in libraries and contextual aggregate errors at binary/application edges.
4. Run `cargo fmt`, `cargo clippy`, and targeted tests before claiming completion.
5. Benchmark performance-sensitive changes in release mode before optimizing.
6. Document public APIs and leave comments for intent, invariants, or safety, not line-by-line narration.

## Operating Constraints
- Do not clone to satisfy the borrow checker until you know ownership is required.
- Prefer iterators and slices without adding intermediate collections unless the collection is needed.
- Keep `unsafe` rare, isolated, and documented with a `SAFETY:` invariant.
- Use `thiserror` or equivalent typed errors for library boundaries; use `anyhow` or similar context at application edges when appropriate.
- Avoid wildcard matches on domain enums when future variants should force a compile failure.
- Prefer generics for hot homogeneous paths and trait objects for heterogeneous collections or stable ABI-like boundaries.
- Use `#[expect(...)]` with a justification when suppressing lints, not broad unexplained `allow`.
- Keep public docs, examples, and doctests aligned with the actual API.

## Inputs This Skill Expects
- The Rust crate, module, or API being changed.
- Whether the code is library, binary, test support, async runtime, FFI, or performance-sensitive code.
- Existing lint, formatting, and test commands.
- Any constraints around MSRV, feature flags, no-std, async runtime, or public API compatibility.

## Output Contract
- Name the ownership and error-handling choices that matter for the change.
- Identify any intentional clones, allocations, dynamic dispatch, unsafe blocks, or lint suppressions.
- Include the validation commands run or the precise reason they could not run.
- For performance work, include benchmark or profiling evidence rather than intuition.
- For public API changes, state docs and compatibility impact.

## Procedure
1. Read the surrounding Rust style, crate boundaries, feature flags, and existing error types.
2. Choose borrowing, ownership, or `Cow` based on call-site needs.
3. Model fallible behavior with `Result` and domain errors before adding broad string errors.
4. Keep data transformations allocation-aware; remove redundant clones and needless collections.
5. Use type-state, sealed traits, or stronger enums only when they remove real invalid states.
6. Add focused unit, integration, or doctests around behavior that can regress.
7. Run formatting, linting, and tests with the repo's normal commands.

## Pitfalls And Gotchas
- Cloning inside loops because borrow errors were not understood.
- Returning `String` errors from library code that callers need to match.
- Using `unwrap` in runtime code because a failure seems impossible.
- Boxing or dynamic dispatch before measuring whether static dispatch is too limiting.
- Adding type-state complexity for a simple runtime check.
- Treating debug-mode timing as performance evidence.
- Writing comments that restate syntax instead of documenting the reason or invariant.

## Progressive Disclosure
Start with the local module and crate conventions. Expand into lint configuration, benchmarks, public API documentation, or deeper ownership redesign only when the change touches those boundaries. Keep advice scoped to the code under review rather than turning every Rust task into a full style audit.

## Verification Pattern
- Run `cargo fmt --check` or the repo's formatter command.
- Run `cargo clippy --all-targets --all-features -- -D warnings` when compatible with the repo.
- Run targeted `cargo test` commands for changed crates or modules.
- For feature-gated crates, test the relevant feature combinations.
- For performance claims, run release-mode benchmarks or profiling and report the evidence.
