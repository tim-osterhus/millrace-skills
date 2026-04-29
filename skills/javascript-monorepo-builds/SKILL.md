---
asset_type: skill
asset_id: javascript-monorepo-builds
version: 1
description: Guardrail for Turborepo-based JavaScript/TypeScript monorepo build graphs, cache keys, workspace filters, boundaries, and incremental CI.
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

# JavaScript Monorepo Builds

## Purpose

Help agents diagnose, plan, or review Turborepo-based JavaScript and TypeScript monorepo build problems by naming the real failure class first and then fixing the smallest honest seam. This is a guardrail, not a Turborepo manual.

### Use When

- the task involves `turbo.json`, package scripts, workspace filters, remote cache, or incremental CI
- a leaf package change causes too many rebuilds, missed dependents, or inconsistent cache hits
- the prompt is about `dependsOn`, `outputs`, `inputs`, `env`, `globalDependencies`, or `--affected`
- package boundaries or CI checkout depth are part of the failure
- the answer needs repo evidence before it can choose a fix

### Do Not Use When

- the work is not Turborepo-based
- the issue is a broad monorepo architecture discussion with no build-graph evidence
- another more specific skill already owns the exact runtime seam
- the prompt only needs generic JavaScript advice without graph, cache, boundary, or CI semantics

## Quick Start

1. Classify the request first as `graph fix`, `cache fix`, `boundary fix`, or `CI fix`.
2. Collect repo evidence: `turbo.json`, workspace manifests, package scripts, lockfile, CI config, and the exact `turbo` commands the repo runs.
3. Check `dependsOn`, `outputs`, `inputs`, `env`, `globalDependencies`, and `--affected` against that evidence before proposing implementation.
4. Choose the smallest honest change: a graph edge, cache key, workspace filter, boundary rule, or CI step.
5. Verify with the narrowest command or config diff that proves the claim.

## Operating Constraints

- Do not turn a graph or cache problem into a repo-wide rebuild or rewrite.
- Do not guess Turborepo semantics from memory when the repo evidence is available.
- Do not use all files as inputs unless the repo actually needs that hash surface.
- Do not omit `outputs` for tasks that produce cached artifacts.
- Do not let local and CI cache inputs drift without explaining the difference.
- Do not trust `--affected` on a shallow checkout or the wrong base ref.
- Do not hide boundary violations inside package scripts.
- Do not disable caching as the first response to a cache miss.
- Rejected trope: "just rebuild everything and move on."
- Better alternative: fix the exact graph edge, cache key, workspace filter, boundary rule, or CI checkout step that is wrong.
- Rejected trope: "rewrite the monorepo layout to make the build faster."
- Better alternative: keep the repo shape and adjust the task graph or cache contract first.

## Inputs This Skill Expects

- `turbo.json` or equivalent Turborepo config
- workspace manifests and package scripts
- lockfile(s)
- CI config, checkout settings, and cache settings
- the actual `turbo` invocation used by local scripts or CI
- package boundary evidence when the prompt mentions a boundary violation

## Output Contract

- Name the failure class first.
- State the smallest fix surface clearly.
- Tie the recommendation to the specific repo evidence.
- Explain `dependsOn`, `outputs`, `inputs`, `env`, `globalDependencies`, and `--affected` before implementation advice.
- Keep the fix limited to graph order, cache key, workspace filter, boundary rule, or CI wiring unless the evidence proves more is needed.
- End with the next verifier and the evidence it should capture.

## Procedure

1. Read the repo evidence and the exact `turbo` commands first.
2. Classify the problem as `graph fix`, `cache fix`, `boundary fix`, or `CI fix`.
3. Trace the smallest evidence-backed change in `dependsOn`, `outputs`, `inputs`, `env`, `globalDependencies`, workspace filters, or CI checkout and cache settings.
4. Prefer a local graph or cache correction over a broad refactor.
5. Verify with the narrowest command, diff, or config check that proves the chosen seam.
6. Hand off to the next verifier with the repo evidence that supports the decision.

## Pitfalls And Gotchas

- Cycles or overly broad edges in `dependsOn`
- Missing or wrong `outputs`
- Inputs that accidentally include everything
- Cache-key drift from environment or global dependency mismatch
- `--affected` on a shallow clone or wrong base ref
- Missing remote cache env in CI
- Boundary leakage hidden in package scripts
- Repo-wide rebuilds when one edge or cache key is enough

### Rejected Trope

- Rejected trope: treat a Turborepo cache miss as a reason to bypass the cache.
- Better alternative: inspect the hash surface, tighten `inputs` or `env`, and keep the cache contract honest.

## Progressive Disclosure

Start with the smallest useful decision: graph, cache, boundary, or CI fix. Expand only enough to prove the chosen seam. Keep the skill compact enough that it steers decisions instead of becoming a build-system manual.

## Verification Pattern

Confirm the failure class, the relevant config surface, the exact `turbo` command or CI step, and one concrete proof step. Next verifier: build reviewer or CI checker; capture `turbo.json`, package scripts, lockfile, CI config, and the exact command line or diff that justifies the fix.
