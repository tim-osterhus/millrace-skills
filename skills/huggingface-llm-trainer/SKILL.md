---
asset_type: skill
asset_id: huggingface-llm-trainer
version: 1
description: "Guardrail for training, evaluating, exporting, and publishing local or cloud Hugging Face LLM fine-tuning runs."
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

# Hugging Face LLM Trainer

## Purpose
Help agents run Hugging Face-based LLM training workflows with clear hardware planning, dataset validation, Trainer or TRL configuration, checkpoint evaluation, Hub persistence, and optional export.

## Quick Start
1. Confirm model, dataset, objective, hardware, and license constraints.
2. Validate dataset format and token length before training.
3. Choose local or cloud execution based on fit and budget.
4. Run a smoke job before long training.
5. Evaluate checkpoints against a baseline.
6. Push or export artifacts only after validation and privacy checks.

## Operating Constraints
- Do not start cloud jobs without confirming cost and artifact destinations.
- Do not push private data, tokens, or unsafe model cards to the Hub.
- Do not assume CPU training is practical beyond demos.
- Do not export GGUF or merged adapters until checkpoint quality is known.
- Keep environment, package versions, model revision, and command records.

## Inputs This Skill Expects
- Base model, dataset, objective, expected output format, and split files.
- Hardware profile or cloud provider target.
- Training method: full fine-tune, LoRA, QLoRA, SFT, preference tuning, or export.
- Evaluation command, target metric, and baseline.
- Hub repo or local artifact policy.

## Output Contract
- Provide a training plan with hardware fit, data validation, command/config, smoke run, full run, evaluation, and artifact handling.
- State blocked conditions before training.
- Report checkpoint comparison and artifact locations.
- State whether the result should be adopted, iterated, or rejected.

## Procedure
1. Inspect dataset and model compatibility.
2. Choose training method and hardware path.
3. Validate tokenization, splits, and sensitive content.
4. Prepare config and smoke run.
5. Execute training and monitor logs.
6. Evaluate checkpoints against baseline.
7. Push, export, or archive artifacts according to policy.

## Pitfalls And Gotchas
- Discovering sequence length or memory problems after launching a long job.
- Losing artifacts from ephemeral cloud jobs.
- Publishing private data through model cards, examples, or repository names.
- Treating adapter merge/export as validation.
- Ignoring package version drift.

## Progressive Disclosure
Start with data, model, hardware, and objective. Expand into cloud jobs, Unsloth, TRL variants, GGUF export, Hub automation, or multi-GPU only when the run requires those branches.

## Verification Pattern
- Confirm dataset validation and token-length checks pass.
- Confirm smoke training finishes.
- Confirm checkpoint evaluation compares to baseline.
- Confirm artifacts are stored or pushed according to policy.
- Confirm final instructions include reproduce and rollback paths.
