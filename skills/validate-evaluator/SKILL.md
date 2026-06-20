---
asset_type: skill
asset_id: validate-evaluator
version: 1
description: "Guardrail for validating LLM judges against human labels using data splits, TPR/TNR, disagreement review, and bias correction."
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

# Validate Evaluator

## Purpose
Help agents calibrate an LLM judge against human labels before trusting its outputs. This skill is for LLM judges, not deterministic code-based checks.

## Quick Start
1. Require a built judge prompt and human-labeled data.
2. Split labels into train, dev, and test sets.
3. Use training examples only for few-shot prompt examples.
4. Iterate on dev using TPR and TNR.
5. Run the held-out test set once for final measurement.
6. Apply bias correction and confidence intervals when estimating production success rate.

## Operating Constraints
- Do not use raw accuracy as the primary validation metric.
- Do not put dev or test examples into few-shot prompts.
- Do not report dev performance as final judge quality.
- Do not validate code-based checks with LLM judge calibration.
- Prefer domain-expert labels over generic outsourced labels for domain-specific criteria.
- Revalidate after changing judge prompt or judge model.

## Inputs This Skill Expects
- Judge prompt and model.
- Human-labeled examples with binary pass/fail labels for one failure mode.
- Candidate few-shot examples.
- Production judge outputs if aggregate success-rate correction is needed.

## Output Contract
- Provide train/dev/test split plan or actual split counts.
- Report dev TPR/TNR during iteration and final test TPR/TNR once.
- Summarize disagreement patterns and prompt changes.
- State whether the judge is usable, needs revision, or should be decomposed.
- Provide corrected production success estimate when requested.

## Procedure
1. Check label quality, balance, and failure-mode specificity.
2. Create disjoint train, dev, and test splits.
3. Run judge on dev and calculate TPR and TNR.
4. Inspect disagreements and refine prompt using only training examples.
5. Repeat until metrics stabilize.
6. Run the judge once on held-out test data.
7. Estimate corrected production pass rate and confidence interval if needed.

## Pitfalls And Gotchas
- Trusting an LLM judge because it sounds reasonable.
- Using percent agreement with imbalanced labels.
- Iterating after reading the test set.
- Combining multiple failure modes into one vague judge.
- Reporting a point estimate without uncertainty.

## Progressive Disclosure
Start with one judge and one failure mode. Expand into bias correction, bootstrap intervals, model pinning, or judge decomposition only after the basic validation split and TPR/TNR measurement are in place.

## Verification Pattern
- Confirm human labels are available and binary for one failure mode.
- Confirm train, dev, and test are disjoint.
- Confirm TPR and TNR are calculated.
- Confirm final test set is used once.
- Confirm production aggregate claims use correction and uncertainty when needed.
