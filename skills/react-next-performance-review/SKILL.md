---
asset_type: skill
asset_id: react-next-performance-review
version: 1
description: "Guardrail for React/Next.js review and refactor work focused on hydration, loading states, rerender paths, and SWR cache behavior."
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

# React Next Performance Review

## Purpose
Help agents review React and Next.js diffs by reading the first evidence first, then choosing the smallest safe change. This is a guardrail, not a React course or SWR manual.

### Use When
- React or Next.js component, route, or data-fetching behavior is involved
- hydration, loading, rerender, or SWR cache behavior may regress
- behavior must stay stable while performance changes

### Do Not Use When
- styling only
- backend only
- broad optimization advice without a concrete diff or render path

## Quick Start
1. Classify the task as `hydration-and-cache regression review` or `data-fetching render-performance refactor`.
2. Inspect the diff and first evidence: render path, server/client boundary, SWR key or mutation path, and any hydration or loading-state snapshot.
3. Check hydration and boundary first, then loading states, then SWR cache or mutation behavior when SWR appears, then rerender cause, then accessibility and state coverage.
4. Choose the smallest safe change class and the next verifier.

## Operating Constraints
- Do not collapse the task class to `review`, `debug`, or `refactor` alone.
- Do not preface the answer with a skill banner or self-introduction.
- Separate hydration and server/client concerns from loading-state concerns, and loading-state concerns from cache concerns.
- If SWR is in the diff, check key stability, mutation scope, and revalidation order.
- Do not lead with `useMemo` or `useCallback`; prove the rerender path first.
- For refactors, preserve request semantics, loading and error states, cache key behavior when present, and visible output.
- Prefer server-side restructuring, transitions, or `useDeferredValue` before memoization when they address the observed bottleneck.

## Inputs This Skill Expects
- diff or code region
- render path and server/client split
- loading, empty, and error states
- SWR details if present
- accessibility and state coverage when relevant

## Output Contract
- Start with the task class and first evidence to inspect.
- For Next.js diff reviews, use `hydration-and-cache regression review`.
- For fetch-driven React refactors, use `data-fetching render-performance refactor`.
- Name the likely regression class before suggesting changes on review prompts.
- Name the rerender path before suggesting optimization on refactor prompts.
- If SWR appears in the diff, keep the cache branch conditional and check key stability, mutation scope, and revalidation order.
- Keep hydration and server/client concerns separate from loading-state concerns, and loading-state concerns separate from cache concerns.
- For refactors, preserve request semantics, loading and error states, cache-key behavior when present, and visible output.
- End with the next verifier and the evidence intentionally captured.

## Procedure
1. Read the diff and render path before suggesting any change.
2. Classify the work by surface and shape, then decide whether the blocker is boundary, loading, cache, rerender, or state coverage.
3. If SWR appears, inspect key, mutation, and revalidation behavior only as needed.
4. Recommend the smallest safe change class and the next verifier.

## Pitfalls And Gotchas
- Blanket memoization without proof.
- Moving logic to the server when the bug is hydration or loading.
- Treating SWR as generic cache.
- Turning the answer into a React tutorial or SWR manual.

## Progressive Disclosure
Start from the smallest useful read of the request, then widen only enough to confirm the actual failure or optimization path. Keep the skill short enough that it steers the answer instead of becoming a generic guide.

## Verification Pattern
- Confirm the task class names both the surface and the shape.
- Confirm first evidence points to the diff or render path, not a guessed optimization.
- Confirm hydration and server/client checks happen before memoization advice.
- Confirm SWR checks appear only when SWR is present.
- Confirm the next verifier and evidence captured are named explicitly.
