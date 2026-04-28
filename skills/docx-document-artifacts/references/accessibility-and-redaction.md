# Accessibility And Redaction

Use this reference when the DOCX needs heading, table, image, link, metadata, or privacy checks.

## Accessibility
Run the audit first, then apply only safe mechanical fixes:

```bash
python scripts/a11y_audit.py input.docx
python scripts/a11y_audit.py input.docx --out_json a11y_report.json
python scripts/a11y_audit.py input.docx --fix_image_alt from_filename --out a11y_fixed.docx
python scripts/a11y_audit.py input.docx --fix_table_headers first_row --out a11y_fixed.docx
```

Focus on the highest-ROI checks:
- Heading hierarchy
- Missing alt text
- Table header rows
- Non-descriptive hyperlinks

After any fix, rerender and inspect the affected pages.

## Redaction
Use layout-preserving redaction for sensitive text, then prove the result survived render:

```bash
python scripts/redact_docx.py input.docx --output redacted.docx --pattern "secret"
python scripts/privacy_scrub.py redacted.docx --out scrubbed.docx
```

Scope the patterns carefully.
Check the rendered pages and confirm the removed text is gone in the DOCX content, not just hidden visually.

## Boundaries
- Redaction does not remove images of text or embedded objects automatically.
- Filename-based alt text is only a baseline, not a final accessibility answer.
- Table header flags can change repeated header behavior, so always rerender after applying them.
