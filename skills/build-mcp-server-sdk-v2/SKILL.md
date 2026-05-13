---
asset_type: skill
asset_id: build-mcp-server-sdk-v2
version: 1
description: "Guardrail for building MCP servers on the v2 split-package TypeScript SDK with v2 APIs, schema discipline, transport choices, and validation."
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

# Build MCP Server SDK v2

## Purpose
Help agents build or review MCP servers that intentionally use the v2 split-package TypeScript SDK. This skill is for SDK-v2 correctness, not for generic MCP product design or v1 migration planning.

**Use When**
- `package.json` depends on `@modelcontextprotocol/server`, `@modelcontextprotocol/client`, `@modelcontextprotocol/core`, `@modelcontextprotocol/node`, `@modelcontextprotocol/express`, or `@modelcontextprotocol/hono`
- code uses `new McpServer(...)`, `registerTool`, `registerResource`, or `registerPrompt`
- the user explicitly asks for MCP SDK v2, split packages, Streamable HTTP, Express adapter, Hono adapter, or v2 handler context
- you need to review schema, transport, context, auth, or validation behavior in a v2 MCP server

**Do Not Use When**
- the project uses the v1 single package `@modelcontextprotocol/sdk`
- handlers use v1-style `extra.signal`, `extra.authInfo`, or `extra.sendNotification`
- the task is a broad MCP strategy decision rather than v2 SDK implementation
- the server-side question is Cloudflare-specific and already has a narrower Cloudflare MCP skill

## Quick Start
1. Inspect `package.json`, import paths, and handler signatures before changing code.
2. Confirm whether the server is v2 split-package, v1 single-package, or mixed.
3. For v2, require `McpServer` and `registerTool` / `registerResource` / `registerPrompt`.
4. Use full Zod schemas and keep recoverable tool failures inside tool results with `isError: true`.
5. Choose stdio for local tools and Streamable HTTP for remote or multi-client operation.
6. Run a build plus an MCP smoke path: initialize, list tools, call a valid tool, and call an invalid request.

## Operating Constraints
- Verify the currently published SDK version from the package registry or official docs before installing new dependencies.
- Pin alpha or prerelease SDK versions exactly; do not use caret ranges across prerelease packages.
- Use ESM and the Node version required by the selected SDK release.
- Use v2 split-package imports consistently; do not mix in `@modelcontextprotocol/sdk` unless the project is intentionally v1.
- Prefer the high-level `McpServer` API over low-level protocol server classes for ordinary servers.
- Use full schema objects such as `z.object({...})`; do not write new code around raw v1-style schema shapes.
- Keep authentication at the HTTP/framework layer when the SDK does not own the authorization server.
- Set tool annotations deliberately for read-only, destructive, idempotent, and open-world behavior.
- Treat thrown protocol errors and soft tool errors as different contracts.

## Inputs This Skill Expects
- The selected SDK generation: v2 split packages or a confirmed request to build v2.
- The intended transport: stdio, Streamable HTTP, Express, Hono, or another adapter.
- The list of tools, resources, or prompts the server should expose.
- The auth boundary, if HTTP is involved.
- Existing build/test commands or a package manager choice.

## Output Contract
- State whether the codebase is v2, v1, mixed, or undecidable from the evidence.
- Name the imports, transport, handler context, and schema style being used.
- For each tool with side effects, state the annotations and error behavior.
- Include the validation path used or required: build, inspector, and at least one valid and invalid tool call.
- Call out any prerelease-version risk separately from implementation correctness.

## Procedure
1. Read `package.json`, lockfile, TypeScript config, and MCP entrypoints.
2. Classify the server by dependency and source fingerprints.
3. If the project is v1 or mixed, stop and report the mismatch before making v2-native edits.
4. For new servers, choose stdio or Streamable HTTP from the deployment context before creating tools.
5. Register tools with full input schemas, output schemas when returning structured content, and explicit annotations.
6. Use the v2 handler context for cancellation, logging, auth info, notifications, elicitation, or sampling.
7. Keep recoverable domain failures as tool results with `isError: true`; reserve protocol errors for malformed protocol-level requests.
8. Add graceful shutdown and resource cleanup around transports and long-running handlers.
9. Validate with the local build/test stack and an MCP client or inspector smoke run.

## Pitfalls And Gotchas
- Accidentally importing from v1 because older examples still use `@modelcontextprotocol/sdk`.
- Treating a prerelease package as stable and allowing broad semver ranges.
- Returning structured content without an output schema.
- Throwing for ordinary domain errors, which prevents the model from self-correcting.
- Using HTTP without deciding where auth, origin checks, and request identity live.
- Omitting annotations on destructive or external-world tools.
- Assuming a copied v1 SSE transport still exists in v2.

## Progressive Disclosure
Start with dependency and import detection. Only load deeper SDK or protocol guidance after the project is confirmed v2 and the target transport is known. For a small tool addition, focus on schemas, handler context, annotations, and one smoke call instead of re-auditing the entire server.

## Verification Pattern
- Confirm the package imports are v2 split-package imports.
- Confirm every new tool uses `registerTool` and full schemas.
- Confirm side-effecting tools have explicit annotations.
- Confirm recoverable validation failures return a soft tool error.
- Run the project build or typecheck.
- Run an MCP smoke path that proves initialize, tool listing, one valid call, and one invalid call.
- If prerelease SDK packages are involved, confirm exact version pinning and document rollback risk.
