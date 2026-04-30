---
asset_type: skill
asset_id: pdf-artifact-workflow
version: 1
description: "Guardrail for choosing the right PDF path for read/extract, create, review, or verify tasks, with render-first proof when layout matters and OCR as an explicit branch for scan-derived or image-only PDFs."
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

# PDF Artifact Workflow

## Purpose
Help agents choose the right PDF path for `read/extract`, `create`, `review`, or `verify` tasks, then prove the result with the smallest honest evidence set. This skill is a guardrail, not a PDF manual.

### Use When
- layout, page order, headers, footers, tables, annotations, or metadata matter
- the task needs OCR judgment for a scan-derived or image-only PDF
- the work involves creating a PDF artifact or checking a rendered output
- you need to decide whether render-first or extraction-first proof is appropriate

### Do Not Use When
- the task is plain text drafting with no PDF artifact boundary
- another more specific skill already owns the workflow
- the question is generic document advice without render, extraction, or OCR concerns

## Quick Start
1. Classify the request as `read/extract`, `create`, `review`, or `verify`.
2. If layout or visual correctness matters, render pages first; if not, use extraction or metadata as secondary evidence.
3. Choose the smallest tool chain that fits the source: `pdftoppm` or Poppler for rendering, `reportlab` for generation, `pdfplumber` or `pypdf` for extraction and metadata.
4. For `create` or edit tasks, separate born-digital, exported, and scanned or image-only PDFs before choosing the path.
5. Treat OCR as a separate branch for scanned or image-only PDFs before trusting text extraction.
6. Stop once one authoritative signal proves the claim; do not re-prove layout with extraction alone.
7. End with the next verifier and the evidence artifact it should capture.

## Operating Constraints
- Rendered pages are the authority for layout, not extracted text.
- Extraction tools are for text, metadata, and quick checks; they do not prove page fidelity.
- OCR is explicit, not implied: if the source is scan-derived or image-only, OCR before treating text as trustworthy.
- Do not skip a render check after generation or edit when visual correctness matters.
- Do not widen into a general office, publishing, or PDF-course handbook.
- Do not treat a successful save, a text dump, or a metadata readout as layout proof.
- When layout is the question, inspect the page image first and the extracted text second.

## Inputs This Skill Expects
- The task goal and whether the PDF is being read, created, reviewed, or verified.
- Whether the source is born-digital, exported, or scanned or image-only.
- Whether the claim is visual, structural, textual, or metadata-related.
- The smallest evidence surface the next verifier needs.
- Any constraints on page order, headers, footers, tables, annotations, or clipping.

## Output Contract
- A clear mode choice: `read/extract`, `create`, `review`, or `verify`.
- The first tool or verifier to run.
- The evidence artifact that actually proves the claim.
- For creation or edits, a note that rendering was checked after generation or change.
- For OCR-dependent PDFs, an explicit OCR branch before text extraction.
- A next-verifier handoff that names the artifact to capture.

## Procedure
1. Decide whether the job is about reading, creating, reviewing, or verifying a PDF.
2. For `read/extract` work, decide whether render evidence, extraction, metadata, or OCR is primary.
3. For `create` work, choose the PDF generation path first, then render the result and inspect page order, headers, footers, spacing, and tables.
4. For `review` or `verify` work, render the pages and compare them against the claim before trusting any extracted text or metadata.
5. Use extraction tools to confirm content, page numbers, or metadata after the render check when needed.
6. If the PDF is scanned or image-only, OCR it before making text claims.
7. Finish by naming the next verifier and the artifact it should capture.

## Pitfalls And Gotchas
- Rejected trope: trusting text extraction alone to prove layout fidelity.
- Better alternative: render pages and inspect the page images for the actual layout.
- Rejected trope: skipping render checks after generating a PDF.
- Better alternative: render the finished file and verify the visual result before delivery.
- Rejected trope: assuming scanned PDFs already have trustworthy text.
- Better alternative: branch to OCR explicitly and treat the OCR output as a separate claim from the page image.
- Rejected trope: checking only one page when page order, footers, or tables vary across the document.
- Better alternative: inspect the pages that can prove the claim, including the boundary pages.

## Progressive Disclosure
Start with the smallest honest proof surface: render when layout matters, extract when text or metadata is the claim, and add OCR only when the source demands it. Expand only enough to answer the task directly, and keep the skill compact so it stays a guardrail instead of a PDF manual.

## Verification Pattern
- Confirm the chosen mode matches the request.
- Confirm layout claims were checked on rendered pages, not just extracted text.
- Confirm OCR was explicit for scan-derived or image-only PDFs.
- Confirm page order, headers, footers, tables, annotations, and metadata were checked only when relevant.
- Next verifier: `pdftoppm` or the equivalent Poppler renderer.
- Evidence artifact: page PNGs, plus extraction or metadata notes only where they add proof.
