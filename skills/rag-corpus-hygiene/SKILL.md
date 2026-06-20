---
asset_type: skill
asset_id: rag-corpus-hygiene
version: 1
description: "Guardrail for linting and reviewing RAG corpora before ingestion, with emphasis on prompt residue, retrieval magnets, public safety, and source hygiene."
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

# RAG Corpus Hygiene

## Purpose
Help agents clean and review a RAG corpus before indexing. This skill focuses on prompt residue, broad retrieval magnets, local paths, private data, malformed metadata, overbroad summaries, and source documents likely to attract wrong queries.

## Quick Start
1. Run available corpus lint checks before ingestion.
2. Review broad summaries, heavily cited docs, role/identity docs, and new evidence manually.
3. Replace broad positioning with concrete facts, dates, artifacts, roles, and limitations.
4. Move facts into narrow source-specific documents where possible.
5. Keep broad overview docs out of normal indexed evidence unless retrieval hooks are narrow.

## Operating Constraints
- Do not index prompt instructions or evaluator scaffolding as evidence.
- Do not index local absolute paths, secrets, or private identity details.
- Do not let source maps or broad summaries dominate retrieval for unrelated questions.
- Treat linter warnings as review prompts, not automatic truth.
- Prefer narrow, concrete source documents over catch-all answer banks.

## Inputs This Skill Expects
- Corpus root, evidence document schema, and ingestion settings.
- Lint output, changed documents, or known retrieval failures.
- Public/private display policy.
- Chunking defaults and documents excluded from normal retrieval.

## Output Contract
- Report corpus hygiene issues by severity.
- Provide exact document repairs or review instructions.
- State which files should be excluded, narrowed, split, or rewritten.
- State whether ingestion is safe or blocked.

## Procedure
1. Run corpus linting or perform structured review.
2. Inspect documents that influence retrieval most.
3. Identify prompt residue, evaluator scaffolding, broad retrieval magnets, local paths, secrets, and malformed metadata.
4. Repair or quarantine risky documents.
5. Re-run lint and spot-check retrieval for representative queries.
6. Document remaining warnings and accepted risks.

## Pitfalls And Gotchas
- Embedding the assistant's desired behavior inside evidence documents.
- Treating broad summaries as harmless when they dominate semantic retrieval.
- Letting prompt residue become source truth.
- Rewriting precise facts into flowery prose that retrieves poorly.
- Fixing warnings mechanically without reading the document context.

## Progressive Disclosure
Start with lint output and the highest-impact documents. Expand into chunking, source exclusion, metadata redesign, or retrieval evals only when hygiene findings explain actual failures.

## Verification Pattern
- Confirm lint or structured review was run.
- Confirm local paths, secrets, and prompt residue are removed or intentionally excluded.
- Confirm broad docs have narrow retrieval hooks or are excluded from normal evidence.
- Confirm representative retrieval queries no longer pull irrelevant source magnets.
