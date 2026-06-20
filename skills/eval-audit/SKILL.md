---
asset_type: skill
asset_id: eval-audit
version: 1
description: "Guardrail for auditing LLM eval pipelines for missing error analysis, weak evaluator design, unvalidated judges, bad metrics, and stale labeled data."
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

# Eval Audit

## Purpose
Help agents inspect an existing LLM evaluation pipeline and produce prioritized findings with concrete fixes. This skill is for auditing trustworthiness, not for building a new evaluator from scratch.

## Quick Start
1. Gather traces, evaluator configs, judge prompts, labels, scripts, and dashboards.
2. Check error analysis, evaluator design, judge validation, human review, labeled data, and pipeline hygiene.
3. Prioritize findings by product impact.
4. Recommend concrete next steps rather than generic eval advice.

## Operating Constraints
- Do not recommend judges before error analysis exists.
- Prefer binary, failure-mode-specific evaluators over vague holistic scores.
- Use code-based checks for objective criteria.
- Validate LLM judges against human labels before trusting them.
- Treat stale evals as suspect after model, prompt, retrieval, or feature changes.

## Inputs This Skill Expects
- Eval traces, evaluator configs, judge prompts, labeled datasets, dashboards, notebooks, scripts, or exports.
- Product context and failure modes that matter.
- Any human review workflow and label provenance.
- Current metrics and candidate decisions based on those metrics.

## Output Contract
- Produce findings ordered by impact.
- For each finding, include status, evidence, why it matters, and a concrete fix.
- Group findings under error analysis, evaluator design, judge validation, human review, labeled data, and pipeline hygiene.
- State what could not be determined from available artifacts.

## Procedure
1. Inventory available eval artifacts and missing artifacts.
2. Check whether real trace error analysis exists.
3. Inspect evaluator prompts and code for specificity and objective checks.
4. Check judge validation data, TPR/TNR, splits, and leakage risk.
5. Check human review context and display quality.
6. Check label volume, class balance, and maintenance freshness.
7. Write prioritized findings.

## Pitfalls And Gotchas
- Auditing from metrics screenshots without reading traces or prompts.
- Treating raw accuracy as enough for imbalanced labels.
- Using similarity scores as primary generation correctness metrics.
- Outsourcing domain labels without expert review.
- Letting eval systems drift after pipeline changes.

## Progressive Disclosure
Start with available artifacts. If no eval infrastructure exists, recommend trace collection and error analysis first. Expand into judge prompt rewrites or validator design only after audit evidence identifies that need.

## Verification Pattern
- Confirm findings cite actual artifacts or state uncertainty.
- Confirm every recommended evaluator maps to an observed failure mode.
- Confirm unvalidated judges are flagged.
- Confirm code-checkable criteria are separated from interpretation-heavy criteria.
- Confirm the report has prioritized next steps.
