---
asset_type: skill
asset_id: tauri-desktop
version: 1
description: "Implementation guardrail for Tauri 2 desktop and mobile apps spanning Rust backend commands, frontend IPC, plugins, capabilities, security, and packaging."
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

# Tauri Desktop

## Purpose
Help agents build or review Tauri 2 applications with a Rust backend, web frontend, IPC commands, plugin setup, capability permissions, updater paths, and platform packaging. This skill is for Tauri app implementation, not generic web UI or Rust-only work.

**Use When**
- creating or modifying a Tauri desktop or mobile app
- adding Rust commands invoked from frontend code
- configuring Tauri plugins, permissions, capabilities, updater, windows, menus, or packaging
- debugging frontend-to-backend IPC or platform-specific build behavior

**Do Not Use When**
- the task is purely web frontend with no Tauri boundary
- the work is an embedded terminal or PTY feature, which needs the narrower Tauri PTY skill
- the task is only Rust library logic unrelated to the app shell

## Quick Start
1. Identify the frontend framework, `src-tauri` layout, Tauri version, and package manager.
2. Add Rust commands in `src-tauri` and expose them through `generate_handler`.
3. Call commands from the frontend with typed `invoke` wrappers.
4. Configure plugins and capabilities before assuming frontend APIs are allowed.
5. Scope filesystem, shell, dialog, notification, updater, and network permissions narrowly.
6. Validate with dev, build, and a real app smoke path.

## Operating Constraints
- Treat Tauri's capability model as a security boundary, not a nuisance to bypass.
- Prefer plugin APIs over ad hoc shell commands when a first-party plugin exists.
- Do not expose arbitrary shell execution to the frontend.
- Keep Rust command inputs typed and serializable; return structured `Result` values with useful error messages.
- Keep long-running work off the UI thread and report progress through events or state.
- Store app data through Tauri path APIs rather than hardcoded platform paths.
- Keep mobile paths explicit; do not assume desktop-only APIs work unchanged on iOS or Android.
- Keep updater keys, signing material, bundle identifiers, and platform entitlements out of source examples unless they are placeholders.

## Inputs This Skill Expects
- The Tauri version and frontend stack.
- The feature being added: IPC command, plugin, filesystem access, updater, windowing, tray, mobile, or packaging.
- Existing `tauri.conf.json`, `Cargo.toml`, capabilities files, and frontend invocation code.
- Target platforms and distribution formats.
- Verification commands for the repo.

## Output Contract
- Name the Tauri boundary changed: Rust command, frontend invoke, plugin registration, capability, config, or packaging.
- State the permission scope added or changed and why it is narrow enough.
- Include the frontend and backend call contract when IPC is involved.
- Include platform caveats for macOS, Windows, Linux, Android, or iOS when relevant.
- Report the dev/build/smoke verification path.

## Procedure
1. Read `package.json`, `src-tauri/Cargo.toml`, `src-tauri/tauri.conf.json`, and capability files.
2. Locate existing command, plugin, and frontend invocation patterns.
3. Add or change the Rust command with typed arguments and a structured result.
4. Register the command or plugin in the Tauri builder.
5. Add or update capability permissions with the narrowest paths, windows, and plugin permissions possible.
6. Update frontend wrappers and UI state to handle loading, success, and error paths.
7. Run the repo's Tauri dev/build checks and manually smoke the feature in the app when feasible.

## Pitfalls And Gotchas
- Adding frontend API calls without capability permission.
- Using browser file inputs where a Tauri dialog or filesystem plugin is expected.
- Exposing broad shell or filesystem access to the webview.
- Returning unstructured string errors that the frontend cannot classify.
- Forgetting platform-specific bundle, signing, entitlement, or WebView runtime requirements.
- Testing only the web dev server and not the Tauri shell.
- Assuming mobile support without checking plugin compatibility.

## Progressive Disclosure
Start from the exact boundary the task touches. Load broader Tauri packaging, updater, plugin, or mobile guidance only when the current change crosses those areas. Keep ordinary frontend and Rust advice delegated to their narrower skills when Tauri is not the deciding factor.

## Verification Pattern
- Confirm Rust commands compile and are registered.
- Confirm frontend invokes use the correct command name and argument shape.
- Confirm capability files allow only the intended windows, plugins, paths, and operations.
- Run the repo's formatter, typecheck, and Tauri dev or build command.
- Smoke the app in a Tauri shell, not just in the browser.
