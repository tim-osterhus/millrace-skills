---
asset_type: skill
asset_id: postgres-query-performance
version: 1
description: "Guardrail for evidence-first Postgres and Supabase query, schema, index, RLS, and migration performance reviews."
advisory_only: true
capability_type: planning-guardrail
recommended_for_stages:
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

# Postgres Query Performance

## Purpose
Help agents diagnose slow Postgres or Supabase-backed paths by reading the query, plan, schema, indexes, and RLS policies first, then recommending the smallest safe change class. This is a guardrail, not a generic DBA manual.

### Use When
- the task is a slow query, suspect plan regression, missing index, late RLS filtering, or risky migration
- the database is Postgres or Supabase-backed Postgres
- the answer needs evidence before recommending a query rewrite, index change, schema change, or rollback shape

### Do Not Use When
- the issue is pure SQL syntax or correctness, not performance
- the database is not Postgres
- the work belongs to broad database administration, hosting, or connection-tuning advice

## Quick Start
1. Classify the task first: query review, schema/index review, RLS/perf review, or migration/rollback planning.
2. Inspect the query text and the first plan evidence available: `EXPLAIN`, `EXPLAIN ANALYZE`, actual row counts, and execution metrics.
3. Then inspect the schema facts that change plan shape: indexes, keys, table size, selectivity, and relevant RLS policies.
4. Rule in or out the likely bottleneck class: missing index, bad join shape, low selectivity or cardinality, policy evaluation cost, or migration risk.
5. If evidence is missing, say what you are assuming and name the next verifier instead of pretending the plan is proven.
6. End with the smallest safe change class and the evidence captured for the next check.

## Operating Constraints
- Do not tune without a plan or plan evidence.
- Do not guess indexes from column names alone.
- Do not treat RLS as free; account for policy cost and plan shape.
- Do not recommend a migration without rollback and verification.
- Do not expand into generic DBA advice, connection pooling, or platform-ops territory.
- Keep the recommended fix small: add or adjust one index, rewrite one query, change one schema detail, or split one migration.
- Prefer concrete evidence over theory when the claim is about performance.

## Inputs This Skill Expects
- The query text and any bind parameters or filters that affect selectivity.
- The current plan evidence, ideally `EXPLAIN ANALYZE` plus actual rows and timing.
- Existing indexes, keys, constraints, table sizes, and row-count context.
- Relevant schema details, joins, and RLS policy snippets.
- If a migration is involved, the rollback shape, deploy order, and verification target.

## Output Contract
- Start by naming the classification and the first evidence to inspect.
- Separate plan evidence from schema or policy assumptions.
- Identify the most likely bottleneck class before suggesting a fix.
- Give the smallest safe change class and the evidence that makes it safe enough.
- If evidence is missing, state the assumption and the next verifier explicitly.
- If a migration is part of the answer, include rollback and verification in the same pass.
- End with a handoff line naming the next verifier and the evidence intentionally captured.

## Procedure
1. Classify the request before recommending any change.
2. Inspect query text and plan evidence first, then compare the observed shape with indexes, schema, and policies.
3. Use `EXPLAIN` or `EXPLAIN ANALYZE` as the primary proof surface when available.
4. Decide whether the main issue is index coverage, join shape, selectivity or cardinality, policy evaluation cost, or migration risk.
5. If the needed evidence is missing, state the assumption, the next verifier, and the specific artifact still needed.
6. Recommend the smallest safe fix class and keep the change bounded to the observed bottleneck.
7. If the task involves a migration, add rollback and verification before concluding.

## Pitfalls And Gotchas
- Rejected trope: tuning without a plan or plan evidence. Better alternative: start from `EXPLAIN ANALYZE` and actual rows.
- Rejected trope: guessing indexes from column names. Better alternative: match the filter, join, and sort order to the observed plan and selectivity.
- Rejected trope: treating RLS as free. Better alternative: inspect the policy predicates and account for when they are evaluated.
- Rejected trope: recommending a migration without rollback or verification. Better alternative: include the rollback path and the evidence that proves the change safe.
- Rejected trope: broad DBA advice. Better alternative: stay within the smallest query, schema, index, or policy change that addresses the observed bottleneck.

## Progressive Disclosure
Start with the query and plan, then widen only if schema, policy, or migration facts change the bottleneck class. Keep one umbrella skill for query, index, schema, RLS, and migration guidance so the evidence loop stays in one place. Add deeper references only if later QA shows the plan-reading guidance needs more detail.

## Verification Pattern
- Confirm the first evidence named is the query and plan, not a guessed optimization.
- Confirm the bottleneck class matches the observed plan and schema facts.
- Confirm the recommendation is one small change class rather than a broad rewrite.
- Confirm RLS cost is checked separately from base query cost when policies exist.
- Confirm any migration includes rollback and verification.
- Confirm the handoff names the next verifier and the evidence intentionally captured.
