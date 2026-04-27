#!/usr/bin/env python3
"""Request browser-game visual assets through OAuth-authenticated Codex."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a Codex CLI asset-generation request without using OpenAI API keys. "
            "The script shells out to `codex exec` and asks Codex to use built-in $imagegen."
        )
    )
    parser.add_argument("--prompt", required=True, help="Asset brief for Codex/imagegen.")
    parser.add_argument(
        "--mode",
        choices=("generate", "edit", "concept"),
        default="generate",
        help="Asset request mode. Default: generate.",
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        required=True,
        help="Working directory passed to Codex, usually the auto-games repo.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="Directory where final project-consumed assets should be written.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Manifest JSON Codex should write. Defaults to the request run directory.",
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        help="Scratch directory for prompt, logs, and summary. Defaults under _visual-check.",
    )
    parser.add_argument(
        "--reference",
        action="append",
        default=[],
        type=Path,
        help="Reference image to attach to Codex. Repeat for multiple images.",
    )
    parser.add_argument(
        "--codex-bin",
        default="codex",
        help="Codex executable. Default: codex.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.5",
        help="Optional Codex model override.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=("read-only", "workspace-write", "danger-full-access"),
        help="Codex sandbox mode. Default: workspace-write.",
    )
    parser.add_argument(
        "--approval",
        default="never",
        choices=("untrusted", "on-failure", "on-request", "never"),
        help="Codex approval policy. Default: never.",
    )
    parser.add_argument(
        "--skip-login-check",
        action="store_true",
        help="Do not run `codex login status` before the request.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write prompt and print the command without invoking Codex.",
    )
    return parser.parse_args()


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def resolve_under(base: Path, path: Path) -> Path:
    if path.is_absolute():
        return path.expanduser().resolve()
    return (base / path).expanduser().resolve()


def default_run_dir(workdir: Path) -> Path:
    if workdir.name == "auto-games":
        root = workdir.parent
    else:
        root = workdir
    return root / "_visual-check" / "asset-requests" / utc_stamp()


def redact_env(env: dict[str, str]) -> dict[str, str]:
    redacted: dict[str, str] = {}
    for key, value in env.items():
        lowered = key.lower()
        if "key" in lowered or "token" in lowered or "secret" in lowered:
            redacted[key] = "<redacted>"
        else:
            redacted[key] = value
    return redacted


def build_codex_prompt(
    *,
    mode: str,
    prompt: str,
    workdir: Path,
    out_dir: Path,
    manifest: Path,
    references: list[Path],
) -> str:
    reference_lines = "\n".join(f"- {path}" for path in references) or "- none"
    return f"""$imagegen

You are creating browser-game visual assets for a Millrace task.

Use Codex built-in image generation/editing only. Do not use OPENAI_API_KEY, the OpenAI SDK, the Images API, or any API-key fallback. Do not read or print Codex credential files.

Mode: {mode}
Working directory: {workdir}
Final asset destination directory: {out_dir}
Manifest path to write: {manifest}
Reference images attached or provided:
{reference_lines}

Asset brief:
{prompt}

Requirements:
- Create original assets only; do not copy protected game art, characters, names, logos, maps, or exact presentation.
- Save every final project-consumed asset under the final asset destination directory.
- Keep UI text, labels, scores, and controls out of raster assets unless the brief explicitly asks for baked-in text.
- For edits, preserve the source non-destructively and write a new output file.
- If transparency is needed, make the final file a PNG or WebP with usable alpha, or clearly report why that was not possible.
- Prefer stable, descriptive lowercase filenames.
- After generation or editing, write the manifest JSON exactly at the manifest path.

Manifest schema:
{{
  "schema_version": 1,
  "status": "complete | blocked",
  "mode": "{mode}",
  "workdir": "{workdir}",
  "assets": [
    {{
      "path": "absolute or workdir-relative path to an asset",
      "role": "sprite | sprite-strip | icon | background | texture | concept | other",
      "description": "short asset description",
      "width": null,
      "height": null,
      "notes": "generation or editing notes"
    }}
  ],
  "notes": "short summary, or blocker reason when status is blocked"
}}

Finish with a concise summary of files created and any checks the caller should run.
"""


def run_login_check(codex_bin: str, cwd: Path) -> None:
    command = [codex_bin, "login", "status"]
    result = subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise SystemExit(
            "Codex login check failed. Run `codex login` with ChatGPT/OAuth before using this asset bridge."
        )


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    codex_path = shutil.which(args.codex_bin)
    if codex_path is None:
        raise SystemExit(f"Could not find Codex executable: {args.codex_bin}")

    workdir = args.workdir.expanduser().resolve()
    if not workdir.is_dir():
        raise SystemExit(f"--workdir does not exist or is not a directory: {workdir}")

    out_dir = resolve_under(workdir, args.out_dir)
    run_dir = args.run_dir.expanduser().resolve() if args.run_dir else default_run_dir(workdir)
    manifest = (
        resolve_under(workdir, args.manifest)
        if args.manifest
        else run_dir / "asset-manifest.json"
    )
    references = [resolve_under(workdir, path) for path in args.reference]

    missing_refs = [path for path in references if not path.is_file()]
    if missing_refs:
        raise SystemExit("Missing reference image(s): " + ", ".join(str(path) for path in missing_refs))

    run_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest.parent.mkdir(parents=True, exist_ok=True)

    prompt_text = build_codex_prompt(
        mode=args.mode,
        prompt=args.prompt,
        workdir=workdir,
        out_dir=out_dir,
        manifest=manifest,
        references=references,
    )
    prompt_path = run_dir / "request-prompt.md"
    summary_path = run_dir / "codex-summary.md"
    stdout_path = run_dir / "codex-stdout.log"
    stderr_path = run_dir / "codex-stderr.log"
    meta_path = run_dir / "request-meta.json"
    prompt_path.write_text(prompt_text, encoding="utf-8")

    command = [codex_path, "--ask-for-approval", args.approval, "exec"]
    if args.model:
        command.extend(["--model", args.model])
    command.extend(
        [
            "--sandbox",
            args.sandbox,
            "--skip-git-repo-check",
            "-C",
            str(workdir),
            "-o",
            str(summary_path),
            "--add-dir",
            str(run_dir.parent),
        ]
    )
    if out_dir.parent != workdir and workdir not in out_dir.parents:
        command.extend(["--add-dir", str(out_dir.parent)])
    for reference in references:
        command.extend(["-i", str(reference)])
    command.append(prompt_text)

    write_json(
        meta_path,
        {
            "schema_version": 1,
            "created_at": utc_stamp(),
            "mode": args.mode,
            "workdir": str(workdir),
            "out_dir": str(out_dir),
            "manifest": str(manifest),
            "prompt_path": str(prompt_path),
            "summary_path": str(summary_path),
            "references": [str(path) for path in references],
            "command": command,
            "environment_redacted": redact_env(
                {key: os.environ[key] for key in ("CODEX_HOME", "PATH") if key in os.environ}
            ),
            "dry_run": args.dry_run,
        },
    )

    if args.dry_run:
        print("DRY RUN: Codex command would be:")
        print(json.dumps(command, indent=2))
        print(f"Prompt written to: {prompt_path}")
        print(f"Manifest target: {manifest}")
        return 0

    if not args.skip_login_check:
        run_login_check(codex_path, workdir)

    with stdout_path.open("w", encoding="utf-8") as stdout_file, stderr_path.open(
        "w", encoding="utf-8"
    ) as stderr_file:
        result = subprocess.run(
            command,
            cwd=str(workdir),
            text=True,
            stdout=stdout_file,
            stderr=stderr_file,
            check=False,
        )

    if result.returncode != 0:
        raise SystemExit(
            f"Codex asset request failed with exit code {result.returncode}. "
            f"See {stdout_path} and {stderr_path}."
        )

    if not manifest.is_file():
        raise SystemExit(
            f"Codex completed but did not write the requested manifest: {manifest}. "
            f"See {summary_path}."
        )

    print(f"Codex asset request complete: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
