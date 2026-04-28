---
asset_type: skill
asset_id: aspnet-core-web-development
version: 1
description: Guardrail for choosing ASP.NET Core app models and composing host, middleware, DI, auth, testing, and deployment boundaries with current official docs.
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

# ASP.NET Core Web Development

## Purpose
Help agents choose the right ASP.NET Core app model and keep `Program.cs`, middleware, DI, auth, testing, and deployment review aligned with current official docs. This is a guardrail, not a .NET manual.

### Use When
- the task is a new ASP.NET Core app, a major refactor, or an upgrade
- the work touches Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller APIs, SignalR, or gRPC
- the request involves `Program.cs`, middleware order, dependency injection, configuration, authentication, authorization, testing, or deployment review
- the answer depends on version-sensitive APIs, defaults, or templates

### Do Not Use When
- the task is generic C# or backend work with no ASP.NET Core hosting or request pipeline
- the work is pure frontend UI with no ASP.NET Core surface
- another more specific skill already owns the exact surface
- the request is a fixed scaffold with no architecture choice

## Quick Start
1. Classify the request first as `app model choice`, `host/pipeline composition`, `cross-cutting concern`, or `upgrade/review`.
2. Name the current or target app model up front; if it is still unresolved, say so explicitly.
3. For a new app or major refactor, pick the smallest coherent model that fits the work:
   - Blazor Web App for component-driven interactive UI
   - Razor Pages for page-centric server rendering
   - MVC for controller/view separation
   - Minimal APIs or controllers for HTTP APIs
   - SignalR or gRPC only when the transport is the real requirement
4. Check current Microsoft Learn before relying on memory whenever the target framework, defaults, or APIs may have changed.
5. Prefer `WebApplicationBuilder` and `WebApplication` for modern apps; treat `Startup` and `WebHost` as migration-only unless the repo already depends on them.
6. Prefer built-in ASP.NET Core features before third-party infrastructure when the framework already solves the need.
7. Verify the changed seam directly instead of re-proving the whole framework.

## Operating Constraints
- Keep the existing app model unless the task explicitly needs a migration.
- Keep host setup, middleware order, DI registrations, config, auth, and tests in the owning boundary instead of scattering them across unrelated files.
- If middleware is involved, make the effective request order explicit in `Program.cs` or the repo's established equivalent.
- Do not inject scoped services into middleware constructors; use `Invoke` / `InvokeAsync` or factory-based middleware when scope matters.
- Check current official docs before giving advice on version-sensitive APIs, defaults, or templates.
- Prefer framework features such as ProblemDetails, OpenAPI, health checks, rate limiting, output caching, and Identity before inventing extra infrastructure.
- Do not rewrite Razor Pages to MVC or controllers to Minimal APIs just because another stack is familiar.
- Do not turn this skill into a full ASP.NET Core encyclopedia.

## Inputs This Skill Expects
- the user goal and whether the app is new, existing, or being upgraded
- the current app model, if one already exists
- the target framework or SDK, if known
- the relevant `Program.cs`, middleware, DI, auth, config, or test boundary
- any version-sensitive API or default that might have changed

## Output Contract
- name the app model, or say it is unresolved
- state the smallest coherent seam to work in next
- call out the owning boundary for host, middleware, DI, config, auth, and tests
- name any docs-first check needed before code or advice
- keep the plan scoped and avoid generic .NET advice
- end with the next verifier and the evidence it should capture

## Procedure
1. Classify the request and confirm the current framework and app model.
2. If the app is new or the refactor is major, choose the app model before discussing implementation details.
3. If the work touches `Program.cs`, spell out the host and middleware order before feature code.
4. If the work touches DI, auth, config, or tests, keep the owning boundary explicit and check the relevant current docs first when the surface is version-sensitive.
5. Use unit tests for isolated logic and integration tests with the ASP.NET Core test host when the claim crosses the request pipeline, auth, config, or infrastructure.
6. Prefer the smallest acceptable ASP.NET Core primitive and only add third-party pieces when the framework does not already cover the need.
7. Stop when the answer has a clear model, boundary, and proof surface.

## Pitfalls And Gotchas
- Rejected trope: rewrite the app model to match a favorite stack. Better alternative: keep the existing model unless the problem actually needs a migration.
- Rejected trope: trust old `Startup` or `WebHost` snippets from memory. Better alternative: check current Microsoft Learn and use `WebApplicationBuilder` / `WebApplication` for modern apps.
- Rejected trope: inject scoped services into middleware constructors. Better alternative: resolve scoped services through `Invoke` / `InvokeAsync` or factory-based middleware.
- Rejected trope: split auth, config, or tests across unrelated files without a clear owner. Better alternative: keep the owning boundary obvious.
- Rejected trope: turn the skill into a full framework manual. Better alternative: stay at the seam and proof surface the caller needs.

## Progressive Disclosure
Start with the smallest useful read: app model, host/pipeline boundary, and whether any version-sensitive APIs are involved. Expand into auth, config, tests, or deployment only when the task actually needs those seams. Keep the skill short enough that it steers decisions instead of becoming a reference book.

## Verification Pattern
- Confirm the app model is named or marked unresolved.
- Confirm the host or pipeline order is explicit when `Program.cs` is involved.
- Confirm any version-sensitive advice is backed by current Microsoft Learn.
- Confirm the test shape matches the claim: unit for isolated logic, integration for request pipeline or infrastructure, browser tests only when browser behavior is the claim.
- Confirm built-in ASP.NET Core features were preferred before third-party infrastructure.
- Next verifier: the implementation reviewer or checker; capture the chosen model, the boundary assumptions, and the docs consulted.
