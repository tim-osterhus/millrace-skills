---
asset_type: skill
asset_id: fine-tuning
version: 1
description: "Guardrail for using fine-tuning pipelines through CLI or YAML: SFT, preference tuning, LoRA settings, checkpoint evaluation, and experiment tracking."
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

# Fine Tuning

## Purpose
Help agents operate a fine-tuning workflow through an existing CLI or YAML configuration without modifying training system source code. This skill covers run planning, dataset requirements, LoRA settings, monitoring, checkpoint comparison, and adoption decisions.

## Quick Start
1. Confirm the task is to use the training system, not edit it.
2. Validate dataset schema, splits, labels, length, and sensitive content before training.
3. Start with a smoke run.
4. Log configuration, baseline metrics, checkpoint metrics, and artifacts.
5. Compare checkpoints against held-out evals before adoption.
6. Preserve rollback and reproducibility.

## Operating Constraints
- Do not train before validating data.
- Do not change source code when the requested surface is CLI or YAML usage.
- Do not adopt a checkpoint from training loss alone.
- Use held-out evals and task-specific metrics.
- Track seeds, model, dataset version, LoRA config, runtime, hardware, and commands.
- Keep secrets and private data out of logs, configs, and published artifacts.

## Inputs This Skill Expects
- Training CLI or YAML schema.
- Dataset files, split definitions, and validation rules.
- Baseline model and baseline eval results.
- Training objective, hardware, runtime, budget, and artifact destination.
- Checkpoint evaluation command or metric policy.

## Output Contract
- Provide a validated training plan or blocked status.
- Include exact CLI/YAML settings, dataset version, smoke command, full run command, and evaluation command.
- Report checkpoint results against baseline and held-out data.
- State adopt, reject, or iterate with the reason.

## Procedure
1. Identify training type and target behavior.
2. Validate dataset and split integrity.
3. Choose conservative initial hyperparameters and LoRA settings.
4. Run a one-step or tiny-slice smoke test.
5. Run the full job only after smoke passes.
6. Monitor logs and save artifacts.
7. Evaluate checkpoints and compare to baseline.
8. Record decision and rollback path.

## Pitfalls And Gotchas
- Treating lower training loss as product improvement.
- Leaking eval rows into training.
- Forgetting tokenizer length and truncation checks.
- Publishing private data through model cards or logs.
- Tuning many hyperparameters without controlled experiment records.

## Progressive Disclosure
Start with dataset validation and smoke execution. Expand into advanced tuning, preference methods, cloud jobs, or LoRA surgery only when baseline training evidence justifies it.

## Verification Pattern
- Confirm dataset validation passes before training.
- Confirm smoke run passes before full run.
- Confirm checkpoint evaluation uses held-out data.
- Confirm adoption criteria include quality, safety, latency, and rollback.
- Confirm run metadata is reproducible.
