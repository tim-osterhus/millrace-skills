---
asset_type: skill
asset_id: generate-synthetic-data
version: 1
description: "Guardrail for generating synthetic datasets from observed failure modes, seed examples, schemas, quality filters, and diversity requirements."
advisory_only: true
capability_type: data-generation-guardrail
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

# Generate Synthetic Data

## Purpose
Help agents generate synthetic data for evals, training, or retrieval tests without drifting away from real failure modes. This skill is for schema-bound, reviewed synthetic examples, not for inventing convenient data at random.

## Quick Start
1. Start from real traces, observed failures, seed examples, or source documents.
2. Define the schema and allowed labels before generation.
3. Generate in small batches.
4. Filter for validity, diversity, realism, privacy, and leakage.
5. Keep provenance and prompt/config records.
6. Reserve human review for high-impact or public-facing datasets.

## Operating Constraints
- Do not use synthetic data as a substitute for real traces when real traces exist.
- Do not generate unsupported facts or private personal details.
- Do not mix synthetic training rows into eval sets without clear split separation.
- Treat LLM-generated labels as provisional until validated.
- Keep prompts, seeds, model versions, and filtering criteria reproducible.

## Inputs This Skill Expects
- Dataset goal: eval, retrieval, SFT, preference data, adversarial cases, or red-team cases.
- Source traces, documents, seed examples, or failure categories.
- Output schema and validation rules.
- Diversity requirements and disallowed content.
- Review and split strategy.

## Output Contract
- Produce synthetic rows that validate against schema.
- Include generation provenance and filtering results.
- State which examples require human review.
- Separate train, dev, test, and holdout data where relevant.
- Summarize coverage and known blind spots.

## Procedure
1. Define the target failure modes or coverage categories.
2. Create a schema and examples before generating.
3. Generate a small batch and validate it.
4. Remove duplicates, invalid rows, prompt residue, unsafe content, and unrealistic examples.
5. Expand in batches only after quality is acceptable.
6. Assign splits without leakage.
7. Record prompts, model, seed data, and filters.

## Pitfalls And Gotchas
- Generating broad generic examples that do not match real usage.
- Letting the model invent facts that appear authoritative.
- Forgetting near-duplicate leakage between train and eval.
- Using synthetic labels without calibration.
- Treating quantity as quality.

## Progressive Disclosure
Start from the dataset purpose and schema. Expand into adversarial generation, role contrasts, multi-hop retrieval examples, or training augmentation only after the initial batch validates cleanly.

## Verification Pattern
- Confirm every row passes schema validation.
- Confirm generated facts are grounded where grounding is required.
- Confirm duplicates and near-duplicates are removed or labeled intentionally.
- Confirm splits prevent leakage.
- Confirm human review covers high-risk rows.
