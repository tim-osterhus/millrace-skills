# Preflight and Verification

This reference holds the command deltas and smoke-evidence expectations that would make the main skill too bulky.

## Preflight Checklist

1. Confirm the repo-shape evidence: `git remote -v`, `package.json`, and any host config file.
2. Check auth or login status for the selected host before attempting a deploy.
3. Decide preview versus production explicitly. Preview is the default; production requires explicit user intent.
4. Infer build settings only after the host choice is settled.
5. Stop on missing auth, missing Git remote for a Git-backed path, or conflicting host signals.

## Planning Prompts

- If the prompt is a planning or review scenario and already names the repo shapes, use that described evidence surface instead of blocking on an empty ambient workspace.
- In that case, say which files or checks you would inspect in a real repo, then answer the host-selection or workflow question at scenario level.

## Smoke Evidence

- The smallest trustworthy check that proves the deployed URL responds correctly.
- Acceptable evidence can be a health endpoint response, a root response, a browser-local QA result, or another host-appropriate probe.
- Do not report readiness if the check was not run or failed.
- Do not confuse a deploy command returning a URL with actual smoke proof.

## Host Notes

- Netlify: `npx netlify deploy` is the preview path; `--prod` is only for explicit production requests.
- Render: validate Blueprint when you use one, deploy through the smallest honest path, and confirm the latest deploy is live before relying on the URL.
- Vercel: `vercel deploy [path] -y` is the preview path; `--prod` is only for explicit production requests.

## Reporting Rule

Return the deploy URL only after smoke evidence is captured. If a host cannot provide a trustworthy smoke check in the current context, say so and stop rather than claiming readiness.
