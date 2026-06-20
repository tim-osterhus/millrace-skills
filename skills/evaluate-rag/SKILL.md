---
asset_type: skill
asset_id: evaluate-rag
version: 1
description: "Guardrail for evaluating RAG retrieval and generation quality, including retrieval datasets, Recall@k, chunking experiments, grounding, and leakage checks."
advisory_only: true
capability_type: evaluation-guardrail
recommended_for_stages:
  - planner
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

# Evaluate RAG

## Purpose
Help agents evaluate retrieval-augmented generation systems by separating retrieval quality from generation quality. This skill covers retrieval eval datasets, Recall@k, reranking metrics, chunking experiments, faithfulness, relevance, and training-data leakage checks.

## Quick Start
1. Do trace-level error analysis before selecting metrics.
2. Build query-to-relevant-chunk datasets for retrieval.
3. Optimize first-pass retrieval for recall.
4. Evaluate generation separately for faithfulness and relevance.
5. Grid-search chunking before tuning generation when retrieval is weak.

## Operating Constraints
- Do not rely on one end-to-end score.
- Do not tune generation before checking whether the needed context was retrieved.
- Use Recall@k for first-pass retrieval and precision, MRR, or NDCG for reranking as appropriate.
- Treat synthetic questions as useful but not sufficient without realism filtering.
- Check train/eval leakage when RAG traces become training data.

## Inputs This Skill Expects
- RAG traces showing query, retrieved chunks, context, and answer.
- Corpus chunks, chunking strategy, retriever, reranker, and prompt.
- Retrieval eval dataset or source documents from which to build one.
- Generation eval criteria such as grounding, relevance, citation support, and omissions.

## Output Contract
- State whether failures come from retrieval, generation, or both.
- Provide retrieval metrics and generation findings separately.
- Recommend chunking, embedding, reranking, prompt, or generation changes based on the diagnosed failure.
- Include leakage and source-alignment checks if traces become training rows.

## Procedure
1. Inspect failed traces and classify retrieval versus generation failures.
2. Build or review query-to-relevant-chunk labels.
3. Measure first-pass retrieval and reranking separately.
4. Test chunk size, overlap, and content-aware chunking when retrieval is weak.
5. Evaluate generated answers for faithfulness, relevance, omissions, and hallucinations.
6. If converting traces to training rows, audit final serialized rows for leakage, citation/source alignment, prompt residue, and malformed text.

## Pitfalls And Gotchas
- Using similarity metrics as primary answer-quality measures.
- Overfitting to synthetic retrieval questions.
- Ignoring multi-hop queries that need multiple chunks.
- Treating reranker precision as a fix when first-pass recall is too low.
- Training on RAG traces without checking final assistant text quality.

## Progressive Disclosure
Start with trace inspection and retrieval/generation separation. Expand into synthetic QA, adversarial retrieval, chunking grid search, reranking, multi-hop metrics, or training-data audits only when the problem requires it.

## Verification Pattern
- Confirm traces were inspected before metrics were chosen.
- Confirm retrieval and generation are measured separately.
- Confirm first-pass retrieval recall is adequate before generation tuning.
- Confirm chunking changes are evaluated against a labeled retrieval set.
- Confirm RAG-derived training rows are checked for leakage and source alignment.
