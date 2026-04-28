# Review Lifecycle

Use this reference for comments, tracked changes, and final cleanup.

## Separate the modes
- Review mode: keep comments or redlines visible because the document is still under review.
- Final mode: strip comments and accept or reject tracked changes before delivery.
- Do not mix the two modes without an explicit finalization request.

## Comments
Use the helper scripts for reliable comment operations:

```bash
python scripts/comments_add.py input.docx --out reviewed.docx --author "Reviewer" --add "Topic=Check this line"
python scripts/comments_extract.py reviewed.docx --out comments.json
python scripts/comments_apply_patch.py reviewed.docx patch.json --out reviewed_v2.docx
python scripts/comments_strip.py reviewed.docx --out final_clean.docx
```

Comments often do not render in headless PDF output, so verify them structurally as well as visually.

## Tracked changes
Use tracked changes for real redlines, then clean them only when final delivery is requested:

```bash
python scripts/add_tracked_replacements.py input.docx --out redlined.docx
python scripts/accept_tracked_changes.py redlined.docx --mode report
python scripts/accept_tracked_changes.py redlined.docx --mode accept --out accepted.docx
python scripts/accept_tracked_changes.py redlined.docx --mode reject --out rejected.docx
```

After accepting or rejecting revisions, rerender the DOCX and confirm no spacing drift or missing text remains.

## Final cleanup path
When the requested deliverable is a clean final DOCX:
1. Accept or reject tracked changes.
2. Strip comments.
3. Render again.
4. Inspect every page before delivery.
