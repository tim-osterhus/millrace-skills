# Millrace Skills Index

This is the public index of optional Millrace skills available from the
`millrace-skills` repository.

Usage contract:
- open this index before selecting optional downloadable skills
- install only skills that are listed here or otherwise explicitly trusted
- once a skill is installed into a workspace, rely on the workspace-local
  `skills_index.md` and installed `SKILL.md` files as the source of availability
  truth

## Optional Skills

| Skill | Description | Tags | Path | Status |
| --- | --- | --- | --- | --- |
| `anti-llm-frontend-design` | Guardrail for frontend agents to avoid generic LLM-generated UI by starting from product-specific structure, density, states, and workflows. | `frontend`, `design` | `skills/anti-llm-frontend-design/SKILL.md` | available |
| `ai-app-integration` | Guardrail for choosing and separating AI SDK and ChatGPT Apps SDK integration seams. | `ai-sdk`, `chatgpt-apps`, `mcp`, `planning` | `skills/ai-app-integration/SKILL.md` | available |
| `aspnet-core-web-development` | Guardrail for choosing ASP.NET Core app models and composing host, middleware, DI, auth, testing, and deployment boundaries with current official docs. | `aspnet-core`, `web`, `planning`, `auth`, `testing` | `skills/aspnet-core-web-development/SKILL.md` | available |
| `browser-game-foundations` | Guardrail for choosing the browser-game fantasy, stack, boundaries, inputs, assets, and handoff before implementation. | `browser-games`, `game-foundations`, `planning` | `skills/browser-game-foundations/SKILL.md` | available |
| `browser-local-qa` | Guardrail for choosing the smallest reliable local browser verification surface and evidence type. | `browser`, `qa`, `local`, `playwright` | `skills/browser-local-qa/SKILL.md` | available |
| `cli-tool-creator` | Guardrail for deciding whether to build a durable CLI, then shaping command surfaces, auth, JSON, and companion skills. | `cli`, `planning`, `auth`, `json` | `skills/cli-tool-creator/SKILL.md` | available |
| `canva-design-ops` | Guardrail for Canva presentation, resize, and translation workflows. | `canva`, `design`, `presentation`, `translation` | `skills/canva-design-ops/SKILL.md` | available |
| `figma-design-to-code-rules` | Guardrail for translating Figma into code and compact repo rules with design-context-first evidence, screenshot validation, and repo-convention reuse. | `figma`, `design`, `frontend`, `planning` | `skills/figma-design-to-code-rules/SKILL.md` | available |
| `deployment-preview-workflows` | Guardrail for choosing Netlify, Render, or Vercel preview deploy paths with auth preflight, repo-shape detection, and smoke verification. | `deployment`, `preview`, `auth`, `qa`, `netlify`, `render`, `vercel` | `skills/deployment-preview-workflows/SKILL.md` | available |
| `docx-document-artifacts` | Guardrail for creating, editing, reviewing, redlining, redacting, and render-verifying DOCX artifacts. | `docx`, `documents`, `qa`, `redaction` | `skills/docx-document-artifacts/SKILL.md` | available |
| `dynamic-og-images` | Planning guardrail for Next.js App Router social preview images: route choice, runtime, fonts, assets, CSS subset, and proof. | `nextjs`, `satori`, `og-images`, `planning`, `preview` | `skills/dynamic-og-images/SKILL.md` | available |
| `cloudflare-agents-mcp` | Guardrail for defaulting generic stateful services with tools to plain Worker plus Durable Object, and escalating to Agents SDK or remote MCP only when an explicit external interface or agent loop is required. | `cloudflare`, `workers`, `durable-objects`, `agents-sdk`, `mcp`, `planning` | `skills/cloudflare-agents-mcp/SKILL.md` | available |
| `cloudflare-durable-objects` | Guardrail for planning and reviewing Cloudflare Durable Object solutions with a thin Worker ingress, SQLite-backed state, alarms, WebSocket hibernation, and docs-first verification. | `cloudflare`, `durable-objects`, `workers`, `wrangler`, `testing`, `planning` | `skills/cloudflare-durable-objects/SKILL.md` | available |
| `cloudflare-workers-platform` | Guardrail for choosing the smallest honest Cloudflare Workers seam, reviewing Worker code/config, and keeping Wrangler flows aligned with current docs. | `cloudflare`, `workers`, `wrangler`, `planning`, `review` | `skills/cloudflare-workers-platform/SKILL.md` | available |
| `frontend-product-builder` | Guardrail for building frontend product surfaces from real workflows, state, and browser-verified interaction instead of generic landing-page scaffolds. | `frontend`, `product-surface`, `planning` | `skills/frontend-product-builder/SKILL.md` | available |
| `game-asset-pipeline-expansion` | Guardrail for sprite-strip normalization, GLB / glTF prep, and browser-game asset verification. | `game-assets`, `sprite`, `3d` | `skills/game-asset-pipeline-expansion/SKILL.md` | available |
| `game-ui-playtest` | Guardrail for browser-game HUD, menu, overlay, and playtest review focused on readable playfields and screenshot-backed evidence. | `browser-games`, `game-ui`, `playtest`, `qa` | `skills/game-ui-playtest/SKILL.md` | available |
| `github-pr-ci-ops` | Guardrail for PR-centric GitHub triage, thread-aware review follow-up, GitHub Actions diagnosis, and safe publish flows once repository identity is confirmed. | `github`, `ci`, `pull-requests`, `planning` | `skills/github-pr-ci-ops/SKILL.md` | available |
| `gmail-inbox-ops` | Guardrail for Gmail inbox search, triage, reply drafts, forwarding notes, and confirmation-safe mailbox actions. | `gmail`, `inbox`, `ops`, `planning`, `qa` | `skills/gmail-inbox-ops/SKILL.md` | available |
| `javascript-monorepo-builds` | Guardrail for Turborepo build graphs, cache keys, workspace filters, boundaries, and incremental CI. | `javascript`, `typescript`, `turborepo`, `ci`, `cache` | `skills/javascript-monorepo-builds/SKILL.md` | available |
| `linear-issue-management` | Guardrail for reading, triaging, and safely mutating Linear issues, projects, and team workflows with confirmation-gated writes. | `linear`, `issues`, `projects`, `workflows`, `planning`, `qa` | `skills/linear-issue-management/SKILL.md` | available |
| `minecraft-mod-qa-automation` | Opinionated QA guide for Minecraft Java mods using layered checks, real client validation, bridge-driven assertions, screenshot artifacts, and bounded gameplay scenarios. | `minecraft`, `modding`, `qa` | `skills/minecraft-mod-qa-automation/SKILL.md` | available |
| `media-generation-transcription` | Guardrail for choosing and packaging OpenAI media workflows across Sora video, speech generation, and audio/video transcription with explicit artifact discipline and blocked-state handling. | `openai-media`, `sora`, `speech`, `transcription`, `video`, `planning`, `qa` | `skills/media-generation-transcription/SKILL.md` | available |
| `millrace-rs-contract-parity` | Guardrail for Rust Millrace prototype work that preserves Python runtime contracts, file-backed state, runner boundaries, and async daemon safety. | `rust`, `millrace`, `contract-parity`, `async` | `skills/millrace-rs-contract-parity/SKILL.md` | available |
| `notion-workspace-flows` | Guardrail for Notion workspace flows: capture, meeting prep, research synthesis, and spec-to-implementation handoff with citations and confirmation-gated writes. | `notion`, `workspace`, `flows`, `planning`, `qa`, `citations` | `skills/notion-workspace-flows/SKILL.md` | available |
| `postgres-query-performance` | Guardrail for evidence-first Postgres and Supabase query, schema, index, RLS, and migration performance reviews. | `postgres`, `supabase`, `performance`, `rls` | `skills/postgres-query-performance/SKILL.md` | available |
| `react-next-performance-review` | Guardrail for React/Next.js review and refactor work focused on hydration, loading states, rerender paths, and SWR cache behavior. | `react`, `nextjs`, `performance`, `swr` | `skills/react-next-performance-review/SKILL.md` | available |
| `shadcn-ui-composition` | Guardrail for shadcn/ui projects that keeps component selection, alias rewrites, theme tokens, and primitive composition aligned. | `shadcn`, `ui`, `composition`, `registry` | `skills/shadcn-ui-composition/SKILL.md` | available |
| `skill-evaluation-harness` | Guardrail for evaluating local skills or plugins, turning findings into rewrite briefs, and designing schema-compatible metric packs. | `planning`, `evaluation`, `qa`, `metrics` | `skills/skill-evaluation-harness/SKILL.md` | available |
| `tile-pixel-art-transitions` | Planning guide for tile-based pixel art transitions, adjacency models, variant sets, and seam-preview QA. | `pixel-art`, `game-assets` | `skills/tile-pixel-art-transitions/SKILL.md` | available |
| `visual-asset-pipeline` | Generate, edit, normalize, and verify browser-game visual assets through OAuth-authenticated Codex image generation plus deterministic local checks. | `game-assets`, `imagegen`, `qa` | `skills/visual-asset-pipeline/SKILL.md` | available |
| `durable-workflow-orchestration` | Guardrail for designing and reviewing crash-safe durable workflows with explicit checkpoints, retries, pause/resume, and recovery boundaries. | `workflow`, `durable`, `checkpoint`, `planning` | `skills/durable-workflow-orchestration/SKILL.md` | available |
