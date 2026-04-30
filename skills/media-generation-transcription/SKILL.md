---
asset_type: skill
asset_id: media-generation-transcription
version: 1
description: Guardrail for choosing and packaging OpenAI media workflows across Sora video, speech generation, and audio/video transcription with explicit artifact discipline and blocked-state handling.
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

# Media Generation Transcription

## Purpose

Guardrail for OpenAI media workflows across video generation, speech generation, transcription, and combined packages. Keep the mode choice explicit, the artifact tree deterministic, and blocked states honest. This is a guardrail, not a media manual.

### Use When

- the task asks to generate, edit, extend, poll, or download Sora video
- the task asks to generate narration, voiceover, or other spoken audio
- the task asks to transcribe audio or video, with or without speaker labels
- the task spans more than one media mode and needs local artifact separation
- the task needs a clear blocked-state explanation for missing key, missing access, or unavailable job

### Do Not Use When

- the work is generic media editing outside OpenAI media workflows
- the prompt is only creative direction with no generation or transcription action
- another more specific skill already owns the same surface
- the request would require the user to paste secrets or credentials into chat

## Quick Start

1. Classify the request first as `video generation`, `speech generation`, `transcription`, or `combined media package`.
2. For video, name the exact intent up front: `create`, `edit`, `extend`, `poll`, or `download`.
3. For speech, keep the text verbatim and decide single clip vs batch only when multiple prompts or files are actually requested.
4. For transcription, choose `text`, `json`, or `diarized_json` deliberately and surface speaker hints, uncertainty, and segment boundaries.
5. Before any live call, check `OPENAI_API_KEY` and access. If either is missing, stop and report a blocked state.
6. For combined work, keep each output separate and preserve downloads locally before URLs expire.
7. End with the next verifier and the evidence captured.

## Operating Constraints

- Never ask the user to paste secrets.
- Treat missing key, missing access, or unavailable job as a blocked state, not a hidden failure.
- Keep speech augmentation short and labeled; do not rewrite the user's text.
- For Sora, enforce the guardrails: no real people, no copyrighted characters or music, and no human-face input images.
- If a request spans modes, separate outputs by name and path; do not blur a transcript, a voiceover, and a video asset into one artifact.
- Use the supported media execution path for the task instead of inventing ad hoc shell commands.
- Keep the response compact and decision-oriented unless the user explicitly asks for deeper guidance.

## Inputs This Skill Expects

- the user request and any existing media asset links or file paths
- whether the work is video, speech, transcription, or combined
- exact text for speech requests
- audio or video source paths for transcription requests
- known speaker hints, output-format preferences, or naming requirements
- any stated retention or download requirements

## Output Contract

- Name the media mode first.
- State the chosen branch and why it fits.
- Preserve exact text for speech requests.
- Preserve speaker hints and uncertainty explicitly for transcription.
- Separate combined outputs into named artifacts and a local manifest or report.
- Call out blocked states plainly, with the missing key, access, or job noted.
- End with the next verifier and the evidence captured.

## Procedure

1. Classify the media work and decide whether it is single-mode or combined.
2. For video, choose `create`, `edit`, `extend`, `poll`, or `download` before writing the prompt.
3. For speech, preserve the input text exactly and only add short, labeled direction if the task needs it.
4. For transcription, choose the response format deliberately and state what is known versus uncertain.
5. If anything required for a live call is missing, stop and report the blocked state instead of guessing.
6. For combined packages, create separate named outputs and a local manifest or report listing each file and its purpose.
7. Verify that the outputs match the chosen mode, the local artifacts are separated, and the blocked-state explanation is faithful.

## Pitfalls And Gotchas

- Collapsing video, speech, and transcription into one generic media workflow
- Asking for secrets instead of telling the user to set them locally
- Rewriting speech text instead of preserving it verbatim
- Hiding transcription uncertainty or speaker ambiguity
- Letting downloaded assets expire before they are captured locally
- Combining unrelated outputs without a manifest or report
- Using a broad media tutorial tone instead of a guardrail tone

### Rejected Trope

- Rejected trope: split video, speech, and transcription into separate skills in v1.
- Better alternative: keep one umbrella guardrail because the mode selection, credential preflight, artifact handling, and blocked-state rules are shared.

## Progressive Disclosure

Start with the smallest useful decision: which media mode owns the request and whether access is already available. Expand only enough to name the branch, the artifacts, and the next verifier. Keep the body short enough that it steers decisions instead of becoming a manual.

## Verification Pattern

- Confirm the mode choice is explicit.
- Confirm access preflight happened before any live call.
- Confirm speech text stayed verbatim and transcription format was chosen deliberately.
- Confirm combined jobs have separate artifact names and a local manifest or report.
- Confirm blocked states are clearly stated when key or access is missing.
- Next verifier: checker or execution reviewer; capture the chosen branch, the access status, and the artifact tree or download set.
