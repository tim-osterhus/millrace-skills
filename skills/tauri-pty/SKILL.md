---
asset_type: skill
asset_id: tauri-pty
version: 1
description: "Implementation guardrail for terminal emulator and PTY features in Tauri apps, covering Rust PTY setup, xterm integration, resizing, lifecycle, security, and multi-tab behavior."
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

# Tauri PTY

## Purpose
Help agents build or debug terminal emulator features inside Tauri apps. This skill covers PTY process lifecycle, Tauri plugin or manual Rust backend wiring, xterm-style frontend integration, resize handling, shell selection, streaming, multi-tab state, and security boundaries.

**Use When**
- the user is embedding a terminal, shell, PTY, interactive CLI, or terminal tab in a Tauri app
- code mentions `portable_pty`, `tauri-plugin-pty`, `xterm`, terminal panes, shell spawning, or PTY resizing
- the problem involves streaming terminal output or forwarding keyboard input to a shell

**Do Not Use When**
- the app only needs one-shot command execution, not an interactive terminal
- the work is ordinary Tauri IPC or packaging unrelated to PTY behavior
- the terminal is a web-only mock with no backend process

## Quick Start
1. Decide whether the standard PTY plugin is enough or manual `portable_pty` control is required.
2. Register the Rust-side plugin or PTY backend before writing frontend terminal code.
3. Install and wire a terminal frontend such as xterm with fit, links, and Unicode support as needed.
4. Pick the platform shell explicitly instead of assuming one shell exists everywhere.
5. Wire bidirectional data: PTY output to terminal, terminal input to PTY, resize events to PTY.
6. Dispose terminal and PTY resources on unmount, tab close, app shutdown, and failed spawn.

## Operating Constraints
- Treat interactive shells as powerful execution surfaces; do not expose arbitrary spawn options without policy.
- Do not confuse one-shot command APIs with a real PTY.
- Use platform-aware shell selection and environment setup.
- Preserve terminal dimensions and resize events; stale `cols` and `rows` cause broken full-screen apps.
- Avoid blocking the UI thread with PTY reads or process waits.
- Bound scrollback, output buffers, and retained session history.
- Sanitize or constrain launch directories, environment variables, and commands when users or agents can influence them.
- Clean up child processes and event listeners reliably.

## Inputs This Skill Expects
- The Tauri version, frontend framework, and terminal frontend library.
- Whether the desired implementation uses a PTY plugin or manual Rust PTY management.
- Platform targets and default shell expectations.
- Requirements for tabs, splits, persistence, working directories, environment, and command launch policy.
- Existing code for plugin registration, frontend terminal component, and lifecycle cleanup.

## Output Contract
- State the chosen PTY approach and why it fits the required control level.
- Name the Rust backend registration and frontend terminal component responsibilities.
- Include shell selection, env, cwd, resize, input/output, and cleanup behavior.
- Call out security constraints around command, cwd, env, and file access.
- Include verification steps for spawn, input, output, resize, multi-tab behavior, and shutdown cleanup.

## Procedure
1. Inspect current Tauri backend setup and frontend terminal dependencies.
2. Choose plugin-based PTY for ordinary terminal panels; choose manual backend only for lifecycle or protocol needs the plugin cannot expose.
3. Register backend plugin or commands and verify they compile.
4. Build the terminal component with stable container sizing and lifecycle hooks.
5. Wire PTY output, terminal input, resize, focus, copy/paste, links, and theme behavior.
6. Add multi-tab state only after one terminal session works end to end.
7. Add shutdown cleanup for tabs, app close, failed spawns, and backend errors.
8. Test on each target platform that changes shell behavior or permissions.

## Pitfalls And Gotchas
- Spawning a process without a PTY and expecting interactive terminal behavior.
- Forgetting to resize the PTY after the terminal fit calculation changes.
- Leaving shell child processes running after a tab closes.
- Capturing unlimited output and exhausting memory.
- Assuming `bash` exists on Windows or that PowerShell exists on every non-Windows target.
- Letting frontend-controlled strings become unrestricted commands.
- Testing only echo output and not full-screen terminal apps, control sequences, or resize.

## Progressive Disclosure
Start with one working terminal session. Add themes, links, Unicode, tabs, splits, persistence, and session restore only after spawn, input, output, resize, and cleanup are proven. Escalate from plugin use to manual PTY only when the required lifecycle control is concrete.

## Verification Pattern
- Confirm backend plugin or PTY commands compile.
- Confirm a shell starts, displays prompt output, accepts input, and returns command output.
- Confirm resize reaches the PTY and full-screen terminal apps render correctly.
- Confirm tab close and app shutdown terminate or detach processes as designed.
- Confirm output buffering stays bounded under high-volume commands.
- Confirm command, cwd, env, and permission policy is documented and enforced.
