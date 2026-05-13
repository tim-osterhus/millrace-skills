---
asset_type: skill
asset_id: openai-docs
version: 1
description: "Guardrail for answering OpenAI API and product questions from current official documentation, with narrow upgrade advice and explicit citation discipline."
advisory_only: true
capability_type: research-guardrail
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

# OpenAI Docs

## Purpose
Help agents answer OpenAI API, model, SDK, Codex, Apps SDK, Realtime, media, and Agents SDK questions from current official documentation. This skill is for docs-grounded guidance, not memory-based speculation or broad provider migration.

**Use When**
- the user asks how to build with OpenAI APIs, models, SDKs, tools, or agent frameworks
- the request depends on current model names, defaults, capabilities, pricing, limits, or migration guidance
- code changes require confirming an OpenAI API surface or parameter
- the user asks for citations, links, or latest official behavior

**Do Not Use When**
- the task is unrelated to OpenAI products
- the user explicitly provides the full relevant docs content and does not need freshness
- the work is only ordinary application code with no OpenAI API decision

## Quick Start
1. Treat official OpenAI documentation as the source of truth.
2. Search or fetch the exact official page needed before answering latest/current questions.
3. Prefer developer documentation and platform reference pages over blog posts or third-party summaries.
4. Preserve explicitly requested model targets instead of silently upgrading them.
5. Keep migration changes narrow: active model defaults and directly related prompts or API parameters only.
6. Cite the official source used and call out uncertainty when docs are unavailable.

## Operating Constraints
- Do not invent model availability, pricing, limits, tool support, or deprecation timelines.
- Do not rely on memory for latest/current/default model questions.
- Use official OpenAI domains or official OpenAI developer-doc tooling when browsing or fetching remote docs.
- Keep quotes short and prefer paraphrase with links.
- If official pages conflict, name the conflict and avoid broad edits until the target behavior is clear.
- Do not broaden a model-string upgrade into SDK, provider, auth, infra, or eval-baseline migration unless the user asks.
- Preserve examples, fixtures, historical docs, and provider comparisons unless they are the active runtime path being updated.

## Inputs This Skill Expects
- The OpenAI product or API surface involved.
- Whether the user needs explanation, implementation, model selection, migration, or prompt upgrade guidance.
- Any explicitly requested model or API target.
- The code paths, config keys, or prompts that are in scope for edits.
- Access to official docs or a clear reason docs could not be fetched.

## Output Contract
- State the official source or docs path used for the answer.
- For model selection, name the use case and why the chosen model fits based on current docs.
- For migrations, identify the current target, requested target, files changed or to change, and behavior intentionally left alone.
- For implementation guidance, give the minimum API pattern and the verification command or smoke test.
- If current docs cannot be reached, say that the answer is fallback guidance and avoid latest/current claims.

## Procedure
1. Classify the request as docs lookup, implementation guidance, model selection, model upgrade, prompt upgrade, or broader migration.
2. Fetch or search official OpenAI docs for the exact surface before giving latest/current guidance.
3. If the user named a specific target model or API, keep that target unless they ask for latest.
4. For code changes, locate active runtime config and prompts before editing.
5. Make the smallest behavior-preserving change that satisfies the OpenAI docs requirement.
6. Verify syntax, tests, or a targeted smoke path without making real external calls unless authorized.
7. Report citations, changed scope, and any unresolved docs ambiguity.

## Pitfalls And Gotchas
- Treating stale local knowledge as current OpenAI guidance.
- Updating examples or historical references while leaving the active runtime unchanged.
- Changing provider abstractions, eval fixtures, or fallback models during a narrow model upgrade.
- Mixing Chat Completions, Responses, Realtime, Apps SDK, and Agents SDK patterns without checking the intended API.
- Claiming a model supports a feature before verifying the official page.
- Failing to mention when docs access was unavailable.

## Progressive Disclosure
Start with the product surface and the user's requested outcome. Fetch only the specific official pages needed for that branch. Load migration, prompting, or model-selection guidance only when the user asks for that decision or the implementation depends on it.

## Verification Pattern
- Confirm an official OpenAI source was consulted for latest/current claims.
- Confirm explicit target models were preserved unless the user requested a latest upgrade.
- Confirm code edits are limited to active runtime paths and directly related prompts.
- Confirm tests, typechecks, or smoke checks ran when code changed.
- Confirm the final answer cites sources or states why docs could not be reached.
