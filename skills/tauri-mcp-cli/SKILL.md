---
asset_type: skill
asset_id: tauri-mcp-cli
version: 1
description: "Operational guardrail for using a Tauri MCP CLI to manage driver sessions, automate webviews, inspect IPC, capture screenshots, and debug mobile or remote Tauri apps."
advisory_only: true
capability_type: operational-guardrail
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

# Tauri MCP CLI

## Purpose
Help agents operate Tauri apps through a Tauri MCP CLI: starting driver sessions, inspecting webviews, taking screenshots, executing JavaScript, driving UI interactions, reading logs, and debugging IPC. This skill is for CLI operation of a Tauri app, not for designing the Tauri app itself.

**Use When**
- a Tauri MCP bridge or CLI is available and the agent needs to interact with a running Tauri app
- the task needs screenshot evidence, selector interaction, webview JavaScript, IPC command execution, logs, or window inspection
- the app runs on a mobile simulator, emulator, real device, or remote host

**Do Not Use When**
- no Tauri MCP bridge or equivalent CLI is installed
- the task is ordinary browser automation outside a Tauri shell
- the job is to implement PTY or terminal behavior inside the app

## Quick Start
1. Confirm the Tauri app is running in development or test mode.
2. Confirm the MCP bridge plugin and global Tauri access are configured if the CLI requires them.
3. Start or verify a driver session before webview commands.
4. Check session status with JSON and require `connected: true`.
5. Use kebab-case flags and explicit output file paths for screenshots.
6. Stop or restart the daemon only when the background session is stale or unhealthy.

## Operating Constraints
- A successful driver-session start is not proof that the app is connected; status output must show a live connection.
- Prefer JSON status and list commands before interacting.
- Do not assume localhost works for mobile devices without port reversal or an explicit host.
- Screenshot commands should write files to disk when the image is evidence.
- Use selectors and wait commands before clicks or typing.
- Keep JavaScript snippets read-only unless the task explicitly requires mutation.
- Do not overwrite existing evidence files without using a deliberate path.
- Stop capture monitors after collecting the IPC or log evidence needed.

## Inputs This Skill Expects
- The CLI command name and installed version, if known.
- The app run command, driver port, host, and target device.
- Bridge plugin configuration and whether `withGlobalTauri` or equivalent access is enabled.
- The desired operation: inspect, click, type, screenshot, execute JS, read logs, inspect IPC, or manage window state.
- The evidence path where screenshots or logs should be stored.

## Output Contract
- State the active session host, port, connection status, and target window when known.
- For UI operations, name the selector, wait condition, action, and screenshot or state evidence.
- For IPC operations, name the command/event and the captured result or failure.
- For mobile or remote operations, state the connection route such as host, reverse port, emulator, simulator, or device.
- Include cleanup performed: monitor stopped, session left running intentionally, or session stopped.

## Procedure
1. Start the app if the user asked for operation and no app is already running.
2. Start or check the driver session on the expected host and port.
3. Read JSON session status and verify the app is connected before interacting.
4. Inspect windows or webview state to choose the target.
5. Use wait-for-selector or equivalent readiness checks before UI actions.
6. Capture before/after screenshots or logs when evidence matters.
7. For IPC debugging, start capture, perform one interaction, fetch captured messages, then stop capture.
8. If the session is stale, restart the daemon, then recreate and re-check the driver session.

## Pitfalls And Gotchas
- Treating driver-session start as proof of connection.
- Using camelCase flags when the CLI expects kebab-case.
- Expecting screenshot bytes on stdout instead of writing a file.
- Typing without a selector and sending text to the wrong focus target.
- Running JavaScript as a function literal that never executes.
- Forgetting `adb reverse` or equivalent routing on a real Android device.
- Leaving IPC monitors running and polluting later evidence.

## Progressive Disclosure
Start with session health and target selection. Only move into webview interaction, IPC capture, logs, or mobile routing after the session is connected. Keep implementation advice in Tauri app skills; this skill should stay focused on operating the CLI reliably.

## Verification Pattern
- Confirm status JSON shows a connected session before each interaction batch.
- Confirm selectors exist before clicks, typing, or style reads.
- Confirm screenshot files exist and represent the expected state.
- Confirm IPC capture is bracketed around the relevant action.
- Confirm mobile or remote commands name the host, port, and routing method.
- Confirm daemon restart is followed by a fresh status check.
