# OOXML Patching

Use OOXML patching only when the surface editor or higher-level helper cannot make the needed DOCX change safely.

## Use cases
- True Word comments
- True tracked changes
- Targeted relationship or content-type repair
- Small structural fixes that are awkward in the editor

## Comments
A comment needs all of the following:
- `word/comments.xml`
- `w:commentRangeStart` and `w:commentRangeEnd`
- a `w:commentReference`
- the comments relationship in `word/_rels/document.xml.rels`
- the content-type override in `[Content_Types].xml`

## Tracked changes
Tracked changes usually need:
- `w:trackRevisions` in `word/settings.xml`
- `w:ins` for inserted content
- `w:del` with `w:delText` for deleted content

## Safe habit
Patch the smallest structure that is actually wrong.
Then rerender and re-check the affected pages.

## Structural checks
- Confirm the ZIP contains the expected part files.
- Confirm the relationship targets are correct.
- Confirm `[Content_Types].xml` includes the needed override.
- For comments, confirm the anchor range and reference IDs line up.
