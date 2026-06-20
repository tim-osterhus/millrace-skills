---
asset_type: skill
asset_id: golden-dataset
version: 1
description: "Guardrail for curating, versioning, validating, and protecting golden datasets used for evals, regression checks, and model comparisons."
advisory_only: true
capability_type: data-quality-guardrail
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

# Golden Dataset

## Purpose
Help agents create and maintain high-trust datasets for evaluation and regression checks. This skill covers schema, provenance, versioning, review, backups, train/eval separation, and quality metrics.

## Quick Start
1. Define dataset purpose and schema before adding rows.
2. Record provenance and review status for every row.
3. Keep train, dev, test, and golden regression sets separate.
4. Validate schema and labels automatically.
5. Version dataset changes with changelog-style notes.
6. Back up important releases before major edits.

## Operating Constraints
- Do not call a dataset golden because it is merely convenient or large.
- Do not mix generated labels and human labels without provenance.
- Do not allow training data leakage into held-out evaluation sets.
- Do not edit expected answers without preserving the old version or rationale.
- Prefer fewer reviewed examples over many weak examples.

## Inputs This Skill Expects
- Dataset purpose, schema, allowed labels, and consumers.
- Existing rows, source traces, documents, or seed examples.
- Reviewers, label policy, and quality thresholds.
- Storage, versioning, and backup location.

## Output Contract
- Produce or update a validated dataset with row IDs, provenance, labels, expected behavior, and review status.
- Include a summary of additions, removals, repairs, and quality risks.
- State split strategy and leakage checks.
- State backup or version tag created when relevant.

## Procedure
1. Define the dataset contract and consumers.
2. Normalize rows into a stable schema.
3. Add provenance, review status, and row IDs.
4. Validate schema, label values, duplicates, and split leakage.
5. Review high-impact rows manually.
6. Version the dataset and document changes.
7. Run a small consumer smoke test.

## Pitfalls And Gotchas
- Treating synthetic examples as golden without review.
- Editing expectations to match a new model instead of product truth.
- Losing provenance during deduplication.
- Ignoring class imbalance and coverage gaps.
- Letting old benchmark rows drift from current product behavior.

## Progressive Disclosure
Start with schema and provenance. Expand into backup, restore, label review, synthetic augmentation, or benchmark governance only when the dataset becomes release-critical.

## Verification Pattern
- Confirm schema validation passes.
- Confirm every row has provenance and review status.
- Confirm split leakage checks pass.
- Confirm important changes are versioned and reversible.
- Confirm a downstream eval or regression smoke run can consume the dataset.
