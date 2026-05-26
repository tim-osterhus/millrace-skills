---
asset_type: skill
asset_id: python-repo-refactoring-hygiene
version: 1
description: "Guardrail for Python repository hygiene, module boundaries, import graphs, file-size pressure, public APIs, naming, docs, and refactoring discipline."
advisory_only: true
capability_type: review-guardrail
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

# Python Repo Refactoring Hygiene

## Purpose
Help agents keep Python codebases organized around coherent modules, clean import direction, explicit public APIs, precise names, reviewable diffs, and defensible refactoring. This skill is for structure and maintainability, not for broad rewrites or style-only churn.

**Use When**
- a file, class, or function is accumulating unrelated reasons to change
- the user asks whether a module is too large, how to split it, or how to clean up a Python repo
- reviewing import cycles, `utils.py` growth, package public surfaces, docs, or architecture notes
- refactoring a monolith without changing behavior

**Do Not Use When**
- the task is a small local bugfix and structure is not the problem
- a linter or formatter can enforce the requested change mechanically
- the user asked for a greenfield architecture rewrite without a scoped migration path

## Quick Start
1. Diagnose cohesion first: list the reasons the file or module changes.
2. Treat line counts as smoke signals, not verdicts.
3. Split by stable concepts and change reasons, not by arbitrary helper buckets.
4. Keep import direction acyclic and aligned from low-level primitives to high-level orchestration.
5. Make public APIs explicit with names, `__all__`, package exports, and typed signatures where useful.
6. Refactor in behavior-preserving slices with tests or golden output before and after.

## Operating Constraints
- Do not cite size thresholds as laws; use them to prompt a structural review.
- Avoid generic modules named `utils`, `helpers`, or `common` when a concept name is available.
- Do not introduce circular imports while splitting modules.
- Use `from __future__ import annotations` and `TYPE_CHECKING` for type-only cycles where appropriate.
- Keep public functions typed and internal helpers clearly internal.
- Do not mix behavior changes into a structural refactor unless explicitly required.
- Preserve external imports, CLI behavior, serialized state, and documented APIs unless a migration is planned.

## Inputs This Skill Expects
- The Python package or files under structural review.
- The reason for refactoring: size, cohesion, import cycle, naming, public surface, docs, or reviewability.
- Existing tests, fixtures, golden output, CLI behavior, or API compatibility constraints.
- Any modules or imports considered public by callers.

## Output Contract
- State the structural diagnosis in terms of reasons to change, import direction, and public surface.
- Propose the smallest behavior-preserving split or cleanup.
- Name files moved, new module responsibilities, and compatibility shims when needed.
- Include validation evidence that behavior did not change.
- If deferring a larger cleanup, leave a concrete follow-up boundary instead of a vague hygiene note.

## Procedure
1. Inspect module responsibilities, top-level imports, exports, tests, and call sites.
2. Identify the primary reason each file should change.
3. Choose a split plan that extracts cohesive concepts without changing behavior.
4. Move code in small slices and preserve import compatibility when callers depend on old paths.
5. Update tests, docs, and `__init__.py` exports deliberately.
6. Run targeted tests and import smoke checks after each significant split.
7. Remove obsolete aliases only when compatibility constraints allow it.

## Pitfalls And Gotchas
- Splitting a large cohesive state machine just to reduce line count.
- Creating `helpers.py` as a dumping ground during refactor.
- Moving code before identifying public callers.
- Reordering imports in a way that hides a new cycle.
- Changing behavior while calling the commit a refactor.
- Deleting compatibility exports without checking downstream imports.
- Treating `Any` and missing return types as harmless in public APIs.

## Progressive Disclosure
Start with the file or package in question. Expand to call-site search, import graphs, package exports, architecture docs, or migration notes only when the structural change reaches those boundaries. Use metrics as triage, then argue from cohesion and compatibility.

## Verification Pattern
- Confirm each resulting module has one clear reason to change.
- Confirm imports remain acyclic and abstraction direction is sensible.
- Confirm public exports and typed signatures are deliberate.
- Run targeted tests, import smoke checks, and any CLI or golden-output checks that cover moved code.
- Review the diff for behavior changes that snuck into the refactor.
