---
asset_type: skill
asset_id: cli-tool-creator
version: 1
description: Guardrail for deciding when to build a durable CLI and shaping its command contract, auth, JSON, and companion skill.
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

# CLI Tool Creator

## Purpose
Help agents decide whether a source should become a durable CLI or stay a repo-local script, then shape the command contract so future Codex threads can run it safely from any repo. This is a guardrail, not a CLI implementation manual.

**Use When**
- the source is API docs, OpenAPI, SDK docs, curl examples, a web admin tool, or a local script
- the user wants a reusable command surface, not a one-off shell snippet
- the workflow needs discovery, stable IDs, read/write separation, machine-readable output, or repeated reuse
- the CLI must work from any repo and may need a companion skill afterward

**Do Not Use When**
- a short repo-local script solves the task
- there is no stable command surface to design
- the ask is generic prompt engineering or shell automation with no reusable tool
- the implementation already exists and only execution remains

## Quick Start
1. Ask the first question explicitly: durable CLI or one-off script?
2. Name the source type and the first real jobs it must do.
3. Check whether a command already exists before inventing a new install name.
4. Choose the smallest command surface that covers `doctor`, discover, resolve, read, write, and raw.
5. Make auth, JSON, and companion-skill handoff part of the contract before writing code.

## Operating Constraints
- Use product nouns, then verbs.
- Build around `doctor`, discovery, resolve, read, write, and raw escape hatches.
- Require `tool-name --help` to show the major capabilities.
- Require `tool-name --json doctor` to verify config, auth, version, endpoint reachability, fixture or offline mode when relevant, and missing setup.
- Prefer discovery commands for top-level containers such as accounts, workspaces, projects, queues, channels, repos, or dashboards.
- Prefer resolve commands that turn names, URLs, slugs, permalinks, or user input into stable IDs before reads and writes.
- Keep read commands exact and keep list or search output bounded.
- Keep write commands narrow, one action at a time, and grounded on the narrowest stable ID.
- Keep raw escape hatches read-first; raw writes stay explicit and are not the main interface.
- Return stable machine-readable output under `--json`, and keep errors machine-readable too.
- Document success shape, error shape, redaction behavior, and one example for each command family in the CLI docs or equivalent.

## Inputs This Skill Expects
- The source type: API docs, OpenAPI, SDK docs, curl history, web admin tool, or local script.
- The first real jobs the CLI must do.
- The auth and config story the service already expects, if any.
- The stable ID or lookup path the service exposes, if any.
- Any evidence that the job needs repeated reuse from any repo instead of a one-off script.

## Output Contract
- Decide durable CLI versus one-off script first.
- Name the first durable command family and the stable ID or resolve path.
- Show `doctor`, discover/resolve/read/write/raw, bounded pagination, auth/config precedence, and JSON policy.
- State how tokens are redacted and how errors surface without leaking credentials.
- Include a companion-skill handoff that teaches order, safety, and the safe read path.
- Keep the answer compact enough to steer a build, not to replace CLI documentation.

## Procedure
1. Read the source just enough to know whether the job is durable or disposable.
2. Name the job family and the nouns that should become commands.
3. Design discovery, resolve, read, write, and raw around stable IDs and bounded output.
4. Put auth in this order: standard environment variable, then user config, then one-off flags only when unavoidable.
5. Make `doctor --json` the first setup check and make it honest about missing auth, missing config, and offline or fixture mode.
6. Require a companion skill after the CLI exists so future Codex threads know the order of operations.
7. Keep the docs specific enough that a future thread can pick the next command without guesswork.

## Pitfalls And Gotchas
- One generic `request` command that hides the real workflow.
- Hidden writes inside broad verbs like `fix`, `debug`, or `auto`.
- Unbounded search or list output that cannot be consumed safely.
- Secrets leaking into JSON, logs, or examples.
- Treating raw requests as the main interface instead of a repair hatch.
- Splitting the same durable-CLI logic into separate source-specific skills when one command contract would do.

## Progressive Disclosure
Start with the narrowest reading of the source that lets you decide whether the CLI is durable. Expand only enough to map containers, IDs, reads, writes, and the raw escape hatch cleanly. If the design starts sounding like a generic command wrapper, go back and tighten the surface.

## Verification Pattern
- Check that the first question was durable CLI or one-off script.
- Check that the design names a first durable command family and a stable ID or resolve path.
- Check that `tool-name --help`, `tool-name --json doctor`, bounded pagination, auth/config order, redaction, and the companion skill are all explicit.
- Check that the docs or equivalent explain success shape, error shape, and one example per command family.
- If the answer still feels like a one-command wrapper, the design is too broad.
