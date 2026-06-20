---
asset_type: skill
asset_id: train-sentence-transformers
version: 1
description: "Guardrail for training sentence-transformers bi-encoders, cross-encoders, and sparse encoders with correct loss, evaluator, hard-negative, and publishing choices."
advisory_only: true
capability_type: training-guardrail
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

# Train Sentence Transformers

## Purpose
Help agents train or fine-tune sentence-transformers models for retrieval, similarity, reranking, learned sparse retrieval, clustering, classification, paraphrase mining, or deduplication.

## Quick Start
1. Identify model type: bi-encoder `SentenceTransformer`, `CrossEncoder` reranker, or `SparseEncoder`.
2. Match loss function to data shape.
3. Choose the evaluator that matches the task and primary metric.
4. Smoke-test with a tiny slice before long training.
5. Capture baseline score before training and emit an end-of-run verdict.
6. Push or publish only after validation.

## Operating Constraints
- Do not synthesize a training script from memory when production templates or examples exist.
- Do not train without baseline evaluation.
- Do not use cached losses with incompatible gradient-checkpointing settings.
- Do not use a reranker when first-pass recall is too weak.
- Do not publish models or cards containing private data.
- Keep run logs, seeds, model names, data versions, and primary metrics reproducible.

## Inputs This Skill Expects
- Task type and model class.
- Dataset shape: pairs, triplets, query-positive-negative, labels, rankings, or sparse targets.
- Base model, language/domain, hardware, and Hub policy.
- Evaluator and baseline metric.
- Hard-negative mining plan when relevant.

## Output Contract
- State model type, loss, evaluator, data shape, metric, and training command.
- Include smoke-test command and baseline evaluation.
- Report verdict: win, marginal, or regression.
- State publish, iterate, or reject decision with metric evidence.

## Procedure
1. Classify the model type from task wording.
2. Inspect dataset columns and labels.
3. Choose loss and evaluator from data shape and task.
4. Prepare training script/config from a known-good template.
5. Run smoke test.
6. Run training and log baseline plus final metrics.
7. Publish or archive artifacts only after the verdict is acceptable.

## Pitfalls And Gotchas
- Choosing a loss that silently mismatches columns or labels.
- Evaluating rerankers with first-pass retrieval metrics.
- Forgetting named-evaluator metric keys.
- Skipping hard-negative quality checks.
- Reporting high scores despite sparse dimension collapse.

## Progressive Disclosure
Start with model type and data shape. Expand into hard-negative mining, LoRA, Matryoshka, distillation, multilingual transfer, sparse regularization, or cloud execution only when the training objective needs it.

## Verification Pattern
- Confirm model type, loss, evaluator, and metric align.
- Confirm baseline evaluation ran before training.
- Confirm smoke test passed.
- Confirm final verdict compares baseline and trained model.
- Confirm publication respects privacy and artifact policy.
