# DOCX Document Artifacts

## Purpose
Use this skill for `.docx` artifact work where visual layout, review markup, final cleanup, accessibility, redaction, or OOXML repair matters.

Use when the task is to create, edit, review, finalize, verify, or redact a DOCX.
Do not use when the work is plain text drafting, PDF-only output, or generic office advice with no DOCX artifact boundary.

This skill is a guardrail, not a Word-processing manual.

## Quick Start
1. Classify the task as `create`, `edit`, `review`, `finalize`, `verify`, or `redact`.
2. Decide whether the document is in review mode or final delivery mode.
3. Choose the smallest honest seam: surface editing first, OOXML patching only if the surface tool cannot do the job cleanly.
4. Render every changed DOCX to PNGs, inspect every page at 100% zoom, and re-render after each layout-sensitive change.
5. End with the next verifier and the evidence artifact it should capture.

## Operating Constraints
- Do not claim visual correctness from XML inspection, text extraction, or a successful save alone.
- Do not trust headless PDF export to prove comments are correct; comments need structural checks too.
- Do not collapse review mode and final delivery mode into one indistinct cleanup pass.
- Do not use OOXML patching as the default path when the normal editor or helper script can make the change safely.
- Do not broaden the task into a generic document-authoring handbook.
- Do not skip re-rendering after comments, tracked changes, redaction, accessibility fixes, or targeted OOXML edits.

## Inputs This Skill Expects
- A DOCX file or working copy to create, edit, review, or verify.
- The desired mode: review, final cleanup, accessibility check, redaction, or targeted OOXML repair.
- The requested proof surface: render PNGs, comment structure, tracked-change cleanup, or audit output.
- Any scope constraints for what must stay visible, what must be removed, and what must remain unchanged.

## Output Contract
- A DOCX in the requested mode.
- The latest render PNGs used to verify layout before delivery.
- Comment or tracked-change structural evidence when review markup is involved.
- Accessibility or redaction evidence when those checks are part of the request.
- The next verifier to run and the artifact it should capture.

## Procedure
1. Classify the request as create, edit, review, finalize, verify, or redact.
2. Decide whether the working copy should keep comments/tracked changes or be cleaned for final delivery.
3. Make the smallest local change that honestly satisfies the request.
4. For comments or tracked changes, route through `references/review-lifecycle.md`.
5. For accessibility or redaction, route through `references/accessibility-and-redaction.md`.
6. For targeted OOXML fixes, route through `references/ooxml-patching.md`.
7. Render with `scripts/render_docx.py`, inspect every page, and iterate until the latest render is clean.
8. Deliver only the requested final artifact, not the internal QA intermediates.

## Pitfalls And Gotchas
- Do not trust XML, text extraction, or a save operation as proof that the document looks right.
- Do not assume comments will appear in headless renders.
- Do not mix review markup cleanup with final delivery unless the request explicitly asks for finalization.
- Do not use OOXML patching to replace the normal edit path when the surface editor can do the job.
- Do not turn this skill into a broad office handbook.

## Progressive Disclosure
Start with the smallest DOCX workflow that can satisfy the request honestly.
Pull in review, accessibility/redaction, or OOXML references only when that boundary is present.
Keep the top-level skill short and let the references carry the stable implementation detail.

## Verification Pattern
- Next verifier: `scripts/render_docx.py`.
- Evidence artifact: the latest `page-*.png` set, plus the relevant comment, accessibility, or redaction report when those modes are active.
