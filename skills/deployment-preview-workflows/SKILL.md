---
asset_type: "skill"
asset_id: "deployment-preview-workflows"
version: 1
description: "Guardrail for choosing deployment preview hosts, verifying auth and repo shape, defaulting to previews, and demanding smoke evidence before declaring a deploy ready."
advisory_only: true
capability_type: "planning-guardrail"
recommended_for_stages:
  - "builder"
  - "checker"
  - "fixer"
forbidden_claims:
  - "queue_selection"
  - "routing"
  - "retry_thresholds"
  - "escalation_policy"
  - "status_persistence"
  - "terminal_results"
  - "required_artifacts"
---

# Deployment Preview Workflows

## Purpose
Help agents choose the right deployment host, verify repo shape and auth before acting, default to preview or the smallest safe non-production equivalent, and require smoke evidence before calling a URL ready.

### Use When
- the prompt asks you to choose between Netlify, Render, and Vercel
- the repo may contain `package.json`, `netlify.toml`, `render.yaml`, or `vercel.json`
- the prompt is a planning or review scenario that describes repo shapes even if no live checkout is attached
- the task is to deploy a preview, make a production deploy, or verify an existing deploy
- auth, Git remote linkage, or host-specific build detection could block the run

### Do Not Use When
- the request is purely browser QA, GitHub PR publish flow, or generic cloud strategy with no web deployment decision
- the host is already fixed and the prompt only needs a host-specific command reference
- the repo is not a web app or service repo

## Quick Start
1. Classify the request first as `host selection`, `preview deploy`, `production deploy`, or `deploy verification`.
2. Inspect `git remote -v`, `package.json`, `netlify.toml`, `render.yaml`, and `vercel.json` before choosing a path.
   If no concrete checkout is available, use the repo shapes named in the prompt as the evidence surface and say which files you would inspect in a real repo.
3. Check the chosen host's auth or login state before deploying.
4. Default to preview or the smallest safe non-production equivalent; treat production as explicit opt-in only.
5. Run the smallest trustworthy smoke check and only then report the URL as ready.
6. If the repo shape or auth state is ambiguous, stop and name the blocker instead of guessing.

## Operating Constraints
- Do not guess the host from habit or brand preference.
- Do not treat missing auth as a warning; it is a blocker.
- Do not flatten preview and production into the same branch.
- Do not report a deployment URL as ready without smoke evidence.
- For Render, do not pretend it has the same preview semantics as Netlify or Vercel; name the smallest honest non-production path explicitly.
- For Render, choose Blueprint when the repo needs reproducible infra, more than one service, a database, a worker, a cron job, or other shared resources; choose direct creation only for a single-service or static repo with simple env vars and no extra infra.
- Rejected trope: turn the skill into a vendor CLI manual.
- Better alternative: keep host-specific commands in references and keep the main body focused on decision quality and safety.

## Inputs This Skill Expects
- The user request and whether production was explicitly requested.
- The repo-shape evidence from `git remote -v`, `package.json`, `netlify.toml`, `render.yaml`, and `vercel.json`, or the repo shapes named in the prompt when the task is planning-only.
- The chosen host's auth or login status.
- Any build, deploy, or smoke-test evidence already produced.
- Current docs or CLI behavior only when a command is version-sensitive.

## Output Contract
- State the classification first.
- Name the chosen host and why it fits the repo shape.
- Name the auth and project-detection checks that passed or blocked the run.
- State preview versus production explicitly.
- Return the deploy URL only with smoke evidence.
- For planning/review prompts, do not block solely because the ambient workspace is empty; say what evidence you would inspect and continue with the scenario answer.
- End with the next verifier and the evidence it should capture.

## Procedure
1. Classify the request.
2. Read the repo-shape signals and select the smallest honest host path.
3. Verify auth or login before attempting deploy.
4. Deploy as preview unless the user explicitly asked for production.
5. For Render, choose Blueprint for multi-service, datastore, cron, worker, or IaC repos; choose direct creation only for the single-service or static case.
6. Run the smallest trustworthy smoke check for the deployed app.
7. Report the URL, the smoke evidence, and any remaining follow-up.

## Pitfalls And Gotchas
- Rejected trope: pick the same host for every repo.
- Better alternative: let repo shape and existing config decide.
- Rejected trope: assume Netlify, Render, and Vercel have identical preview semantics.
- Better alternative: keep the host choice explicit and preview-first, then verify with host-appropriate smoke evidence.
- Rejected trope: use Render direct creation for a multi-service or datastore repo.
- Better alternative: use Blueprint when the repo needs reproducible infra or more than one service.
- Rejected trope: return only the deploy command output and call it done.
- Better alternative: capture smoke evidence before saying the URL is ready.

## Progressive Disclosure
Start with the smallest decision that matters: host selection and auth. Expand only enough to choose preview versus production safely, then verify the deployed preview with the smallest proof step. Keep host-specific CLI details and fallback paths in references so the main skill stays compact.

## Verification Pattern
- Confirm the task was classified first.
- Confirm repo-shape evidence was inspected before choosing a host.
- Confirm auth or login status was checked before deploy.
- Confirm preview was the default and production required explicit opt-in.
- Confirm smoke evidence exists before the URL is reported as ready.
- Next verifier: deploy checker or smoke-test consumer; capture the repo-shape evidence, auth status, deploy URL, and smoke result.
