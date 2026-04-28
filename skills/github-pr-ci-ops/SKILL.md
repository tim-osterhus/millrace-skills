---
asset_type: "skill"
asset_id: "github-pr-ci-ops"
version: 1
description: "Guardrail for PR-centric GitHub triage, thread-aware review follow-up, GitHub Actions diagnosis, and safe publish flows once repository identity is confirmed."
advisory_only: true
capability_type: "planning-guardrail"
recommended_for_stages:
  - "builder"
  - "checker"
  - "fixer"
  - "updater"
forbidden_claims:
  - "queue_selection"
  - "routing"
  - "retry_thresholds"
  - "escalation_policy"
  - "status_persistence"
  - "terminal_results"
  - "required_artifacts"
---

# GitHub PR CI Ops

## Purpose
Help agents handle PR-centric GitHub work through one of four branches: repo or PR triage, review follow-up, CI debugging, or publish changes. This is a guardrail, not a GitHub command manual.

### Use When
- the task starts from a repository, PR number, PR URL, or current branch that is explicitly named or already confirmed by prior evidence
- unresolved review threads, failing GitHub Actions checks, or dirty-worktree publish safety matter
- the job needs connector-first PR context plus `gh` or `git` fallback after the repository identity is confirmed

### Do Not Use When
- the request is only generic GitHub browsing or issue triage with no PR, CI, or write-safety decision
- the prompt only says "local checkout" but does not explicitly name the repository, branch, PR number, or checkout path; treat that wording as scenario framing only, not permission to inspect the current QA harness workspace or nearby run directory for repo facts
- the prompt is hypothetical or lacks a concrete repo, branch, or PR identifier and would require inspecting the ambient checkout, QA harness files, run artifacts, or prior child outputs to guess it
- the repository scope cannot be confirmed from the prompt or prior evidence
- the task is unrelated to PR review, CI logs, or local publish flows

## Quick Start
1. Resolve repository and current branch only from the prompt or confirmed evidence before reading comments or logs. If the repo or PR identity is missing, state the missing identifiers, name the next legitimate evidence source, and stop; do not run local `git`, `pwd`, `ls`, `find`, or similar filesystem checks to prove the gap.
2. Classify the task as `repo or PR triage`, `review follow-up`, `CI debugging`, or `publish changes`.
3. Use connector-first PR reads when the surface is enough; switch to thread-aware review data or `gh` logs when state matters.
4. State what is being inspected, what is assumed, and what is out of scope before you edit, commit, or reply. For one-shot planning prompts, keep the answer on the smallest evidence ladder and do not inspect unrelated worktree dirtiness, QA harness folders, current-workspace directory listings, run artifacts, or parent-run file scans unless the repository is confirmed.
5. For publish work, inspect `git status -sb`, confirm which files belong, stage explicit paths, commit tersely, push, and open a draft PR.
6. End with the next verifier and the evidence captured.

## Operating Constraints
- Do not treat flat PR comments as complete review-thread state.
- Do not assume GitHub Actions logs are available through the connector alone.
- A generic mention of "local checkout" does not confirm the target repository, branch, PR number, or checkout path, and in an underspecified one-shot prompt it is scenario framing only.
- QA harness folders, run artifacts, current-workspace directory listings, and parent-run file scans are not valid PR scenario evidence unless the prompt explicitly names them as the target context.
- If the prompt is hypothetical or missing concrete repo, branch, or PR identity, do not inspect the ambient checkout, current workspace, QA harness files, run artifacts, or prior child outputs to infer it. Say the context is underspecified, name the assumption, and point to the next evidence source.
- Do not run local `git`, `pwd`, `ls`, `find`, or similar filesystem checks merely to prove missing identity.
- On one-shot planning responses, stay at the smallest evidence ladder needed for the prompt. Do not run local tests, inspect unrelated worktree dirtiness, or cite workflow files unless the prompt or confirmed context specifically identifies that repository.
- Do not resolve, reply to, or mark threads unless the user explicitly asked for that write action.
- Do not stage unrelated work silently or default to `git add -A` in a mixed worktree.
- Do not widen the skill into a generic GitHub or `gh` command manual.
- Do not keep issue summaries broad; only include them when they are linked to the current PR or fix flow.
- Do not infer scope from labels, reactions, or repo search if the repo or branch is still unclear.

## Inputs This Skill Expects
- a repository identifier, PR number or URL, or a current local checkout already confirmed by prior evidence
- `git status -sb` and the relevant diff when publish safety matters
- PR metadata and patch context from the GitHub connector when available
- thread-aware review data when unresolved thread state matters
- `gh auth status`, `gh pr checks`, and `gh run view` output when CI matters

## Output Contract
- Start with the repository, branch, and task classification only when they are explicitly named in the prompt or already confirmed by prior evidence. Otherwise start with the missing identifiers, the assumption, and the next legitimate evidence source; do not fill gaps from the ambient checkout, the current workspace, QA artifacts, run artifacts, or prior child outputs.
- Name the evidence source used next: connector, thread-aware review data, or `gh` logs.
- Separate actionable review threads from informational comments.
- If CI matters, say whether the failure is GitHub Actions, external, or unavailable.
- If publishing, say what is staged, what is left alone, and whether the PR is draft.
- State assumptions and out-of-scope items before any edit or publish action.
- End with the next verifier and the evidence captured.

## Procedure
1. Resolve the operating context first.
   - Use the provided repo, PR number, PR URL, or current branch when they are explicitly provided or already confirmed by prior evidence.
   - If the prompt is hypothetical or still ambiguous, do not inspect the open checkout, current workspace state, QA harness artifacts, run artifacts, current-workspace directory listings, or prior child outputs to guess the target; stop at the missing identifier, state the assumption, and name the next evidence source.
   - If the prompt says "local checkout" without a concrete repo, branch, PR, or checkout path, treat that wording as scenario framing only.
   - If the request is about a confirmed current branch, use that confirmed branch and only then use `gh` when needed.
2. Classify the request before acting.
   - `repo or PR triage`: summarize only the current PR, repository, and nearby context that matters.
   - `review follow-up`: fetch thread-aware review data, cluster actionable threads, and preserve resolution state.
   - `CI debugging`: confirm `gh auth status`, inspect `gh pr checks` and `gh run view`, and treat non-Actions checks as report-only.
   - `publish changes`: confirm scope before staging, use explicit file paths in a mixed worktree, commit, push, and open a draft PR.
3. Use the smallest source that proves the claim.
   - Connector for PR metadata and patch context.
   - Thread-aware review reads when unresolved thread state matters.
   - `gh` for GitHub Actions logs or fallback data the connector cannot show.
   - Local `git` only after repository identity is confirmed and publish safety matters.
4. Keep the scope narrow.
   - State what is being inspected, what is assumed, and what is out of scope.
   - Keep issue summaries narrow and only linked to the current PR or fix flow.
   - Do not answer with broad GitHub administration advice when the request is PR-centric.
5. Hand off cleanly.
   - Name the next verifier.
   - Name the evidence captured.
   - Leave thread state, log state, and staged files explicit.

## Pitfalls And Gotchas
- Rejected trope: treating top-level comments as complete review state.
- Better alternative: use thread-aware review data and preserve resolved or outdated state.
- Rejected trope: assuming the connector exposes GitHub Actions logs end to end.
- Better alternative: use `gh` for checks and log inspection, and say when logs are external or unavailable.
- Rejected trope: staging everything in a dirty worktree because it is faster.
- Better alternative: confirm scope and stage explicit paths.
- Rejected trope: replying to or resolving threads by default.
- Better alternative: leave thread state unchanged unless the user explicitly asked for that write action.
- Rejected trope: turning the skill into a general GitHub or `gh` command manual.
- Better alternative: keep the workflow PR-centric and stop once the next action is clear.

## Progressive Disclosure
Start with the smallest read needed to confirm the task context. If repo identity is missing, do not mine the checkout, current workspace, QA harness, run artifacts, current-workspace directory listings, or prior child outputs to guess it; state the assumption and the next evidence source instead. Expand only enough to get the next action safe: thread state for review, log state for CI, or diff scope for publish. Keep connector and CLI use aligned with confirmed evidence, not the ambient workspace, and do not widen into unrelated GitHub administration or one-shot local test runs.

## Verification Pattern
- Confirm the repository identity came from the prompt or prior evidence, not from ambient checkout inference.
- Confirm the repo and current branch were resolved before using comment or log data.
- Confirm unresolved review threads came from thread-aware evidence, not flat comments.
- Confirm CI failures were backed by `gh` checks or logs, or explicitly marked external or unavailable.
- Confirm publish actions staged only the intended files in the mixed worktree.
- Confirm the closing handoff names the next verifier and the evidence captured.
