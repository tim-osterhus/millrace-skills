# Render And Verify

Use this reference whenever a DOCX change could affect layout.

## Core rule
Do not treat a DOCX as correct until it has been rendered and the page PNGs have been inspected.

## Typical loop
1. Edit the DOCX.
2. Render it with `scripts/render_docx.py`.
3. Inspect every `page-*.png` at 100% zoom.
4. Fix any clipping, overlap, spacing drift, or header/footer issue.
5. Render again after the fix.

Example:

```bash
python scripts/render_docx.py input.docx --output_dir out_render
```

## What to inspect
- Page boundaries and margins
- Tables, lists, and wrapped text
- Headers and footers
- Clipping, overlap, and missing glyphs
- Any page that changed after a comment, revision, redaction, or OOXML patch

## Limits
- Rendering is strong for visual layout.
- Rendering is not a reliable proof of comments.
- If comments are part of the task, also inspect structure with `comments_extract.py` or direct ZIP checks.

## Good habit
After any layout-sensitive change, rerender immediately rather than stacking more edits on a stale render.
