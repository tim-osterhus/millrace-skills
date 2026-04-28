# Host Matrix

Use this reference to pick the smallest honest deployment path after you have inspected the repo shape and auth state.

## Default Decision

- Netlify when `netlify.toml` is present or the repo is already linked to Netlify.
- Render when `render.yaml` is present or the repo needs Blueprint, multiple services, a database, a worker, a cron job, or other shared infra.
- Vercel when `vercel.json` is present or the repo is a web app whose normal path is a preview deployment.

If the signals conflict, stop and ask which host is already linked or which deployment history should be treated as authoritative.

## First Evidence

- `git remote -v`
- `package.json`
- `netlify.toml`
- `render.yaml`
- `vercel.json`

Use `package.json` to infer build scripts or output directories only after the host decision is already plausible. Do not let `package.json` alone force a host choice.

## Host-Specific Preflight

- Netlify: `npx netlify status`; if not authenticated, use `npx netlify login` or `NETLIFY_AUTH_TOKEN`.
- Render: `git remote -v`, then `render whoami -o json` when the CLI is available; if no Git remote exists, stop for Git-backed paths.
- Vercel: `command -v vercel`; if credentials are missing, use the fallback deploy flow or ask the user to authenticate.

## Render Choice Ladder

Use Blueprint when any of these are true:

- more than one service is needed
- a database, cache, worker, cron job, or other shared resource is needed
- the repo wants reproducible infrastructure as code
- the repo already contains `render.yaml`

Use direct creation when all of these are true:

- the project is a single service or static site
- env vars are simple
- no extra infra is needed
- the repo is already pushed to a Git provider

If the path is image-backed or there is no Git remote, stop and switch to the appropriate Dashboard/API flow instead of forcing MCP.
