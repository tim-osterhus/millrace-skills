---
asset_type: skill
asset_id: optimize-agentic-cli
version: 1
description: "Guardrail for auditing and designing CLIs that agents can drive through pure data channels, semantic exit codes, noninteractive flows, and repairable errors."
advisory_only: true
capability_type: implementation-guardrail
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

# Optimize Agentic CLI

## Purpose
Help agents audit or design command-line tools that another agent can call safely without human babysitting. This skill is for CLI contract quality after the surface is known to be a CLI, not for deciding whether a workflow should be MCP, API, UI automation, or shell script.

**Use When**
- stdout mixes JSON with progress, banners, or prose
- every failure exits with the same opaque code
- commands hang on prompts in headless contexts
- a CLI needs stable JSON, structured errors, dry runs, or repair-loop output
- the user asks to make a CLI agent-friendly or LLM-friendly

**Do Not Use When**
- the surface decision between CLI, MCP, API, or direct library call is still open
- the task is generic shell scripting rather than a reusable CLI contract
- a vendor-specific CLI skill already owns the workflow

## Quick Start
1. Check whether a machine-readable mode exists, usually `--json` or `--output json`.
2. Verify stdout is pure data and stderr carries progress, logs, and operator messages.
3. Map exit codes for success, usage, auth, not found, conflict, validation, and retryable failures.
4. Confirm headless commands never prompt unless an explicit interactive mode is requested.
5. Require structured error bodies with stable codes, retryability, and next-action hints.
6. For repairable generated artifacts, design an iterate-validate-repair loop.

## Operating Constraints
- Stdout is the data channel; stderr is the operator channel; exit code is the machine status channel.
- `--json` output must not include spinners, banners, warnings, or prose.
- Destructive commands require `--dry-run` and an explicit confirmation path such as `--yes` or `--force`.
- Noninteractive runs must fail deterministically instead of blocking.
- Error fields must be stable enough for automation: class, code, message, retryable, and suggestion or next action.
- Long-running operations need job IDs, polling, timeout behavior, and resumable status.
- Pagination, filtering, and field selection must prevent unbounded output.
- Help text should document examples, output fields, and exit codes.

## Inputs This Skill Expects
- The CLI name, target users, and main command families.
- Existing help output, command docs, or source files.
- Safe read-only commands that can be run for evidence.
- Known destructive paths that need confirmation or dry-run handling.
- Whether the workflow is one-shot, long-running, batch, or repairable.

## Output Contract
- For audits, provide a severity-ranked report with command evidence, observed stdout/stderr/exit behavior, agent impact, and recommended fix.
- For designs, provide command grammar, JSON envelope, error schema, exit-code map, noninteractive policy, destructive-flow safety, and examples.
- For repair loops, provide phase names, validation response shape, retry budget, `next_action`, and finalization criteria.
- State verification commands that prove the contract.

## Procedure
1. Capture top-level and relevant subcommand help.
2. Identify machine-readable flags, quiet flags, paging behavior, and config/auth discovery.
3. Run safe read-only commands to inspect stdout/stderr separation.
4. Exercise at least one success path and one validation or usage failure.
5. Classify findings by whether agents cannot parse, cannot continue, may retry incorrectly, may block, or only lose convenience.
6. Design or patch the CLI contract in this order: pure data output, structured errors, semantic exits, headless flags, destructive safeguards, repair loops, help docs.
7. Re-run evidence commands and confirm the contract holds.

## Pitfalls And Gotchas
- JSON printed after progress text is not machine-readable output.
- A single exit code `1` forces brittle string parsing.
- Hidden pagers, prompts, auth flows, and confirmations cause unattended runs to hang.
- Broad `fix` or `sync` commands can hide writes that should be explicit.
- Raw request escape hatches become dangerous when treated as the primary interface.
- Human-friendly help can still be useless to agents if it omits field shapes and exit codes.

## Progressive Disclosure
Start with the five core contract checks: pure machine output, stderr separation, semantic exits, noninteractive behavior, and structured errors. Load deeper async, pagination, auth, or repair-loop design only for commands that actually need those surfaces.

## Verification Pattern
- Confirm `--json` or equivalent output is parseable by a strict JSON parser.
- Confirm progress and logs go to stderr.
- Confirm success, usage, auth, not-found, validation, conflict, and retryable failures have distinct machine signals.
- Confirm headless commands complete or fail without prompting.
- Confirm destructive commands support dry-run and explicit confirmation.
- Confirm repairable workflows return enough structured feedback for an agent to fix and retry.
