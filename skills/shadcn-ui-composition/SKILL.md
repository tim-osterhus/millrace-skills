# Shadcn UI Composition

## Purpose
Help agents work inside shadcn/ui projects without breaking the project's component graph, aliases, theme tokens, or primitive-specific composition. This is a guardrail, not a generic frontend design guide or a browser QA manual.

### Use When
- the repo has `components.json`, a registry, or an explicit shadcn/ui add, update, or debug task
- you need to search, install, update, or repair shadcn components
- a copied component needs alias repair, token preservation, or composition cleanup
- the task is about component selection and structure, not broad UI invention

### Do Not Use When
- the work is generic frontend design, layout, or branding without shadcn/ui
- the task is only browser QA or screenshot review
- another more specific skill already owns the broader workflow
- the request does not touch `components.json`, a registry, or installed shadcn components

## Quick Start
1. Read project context first: package runner, alias, base, tailwind version, icon library, resolved paths, and installed components.
2. If the registry is not named, ask which registry to use instead of guessing.
3. Check whether the component already exists before you add or update it.
4. Search registries, read the docs, and only then install or update through the project's runner.
5. Prefer existing shadcn components and built-in variants before custom wrappers or raw markup.
6. After install or update, review the changed files for alias paths, group wrappers, required titles, trigger wiring, and token overrides.

## Operating Constraints
- Use the project's package runner for every shadcn CLI call; do not mix runners.
- Prefer existing components, built-in variants, and semantic tokens over custom `div` stacks or raw color classes.
- Keep imports aligned with the repo alias; rewrite third-party registry imports when they assume `@/components/ui/...` or another default path.
- Read `base` before deciding whether a trigger uses `asChild` or `render`.
- Keep primitive structure intact: items stay inside their groups, tabs triggers stay inside `TabsList`, overlays carry their required titles, and cards use their full composition when the surface needs them.
- Preserve project theme tokens and local styling decisions unless the task explicitly changes them.
- Use `className` for layout adjustments, not to override component colors or typography.
- Do not trust a screenshot alone; validate the installed files because import and composition mistakes can still render "fine" at first glance.
- Reject copy-pasted registry code that has not been reconciled with the repo.

## Inputs This Skill Expects
- the current shadcn project context and installed components
- the user request and any named registry
- the repo alias, base, tailwind version, icon library, and package manager
- the changed files or registry output that need review
- any local theme tokens or component conventions that must be preserved

## Output Contract
- a concise shadcn-specific plan or fix that names the component source, the project context used, and the reason for the choice
- the exact composition rule relied on when an overlay, menu, form, card, or tab is involved
- any alias or icon-library rewrites that were necessary
- the file-review result after add or update, including anything repaired before handoff

## Procedure
1. Inspect project context and installed components.
2. Search the registry for an existing fit before inventing custom UI.
3. Read the docs for the candidate component or block.
4. Add or update with the project's runner, using dry-run and diff when changing existing components.
5. Rewrite third-party imports to match the repo alias and icon library.
6. Review the added files for missing groups, missing titles, wrong trigger wiring, broken imports, and token overrides.
7. Prefer the narrowest fix that preserves the local component system.

## Pitfalls And Gotchas
- Rejected trope: copy raw registry code and trust the screenshot.
- Better alternative: search, read docs, add or update, then review the changed files because shadcn mistakes often hide in imports and composition.
- Rejected trope: build dialogs, sheets, or drawers from generic wrappers.
- Better alternative: use the shadcn primitive and include its required title, even if it is visually hidden.
- Rejected trope: hardcode `@/components/ui/...` imports or a default icon library in a repo that uses different aliases or icons.
- Better alternative: rewrite imports to the repo's actual alias and icon library before you hand off.
- Rejected trope: replace a shadcn primitive with hand-rolled markup when the library already has the right component.
- Better alternative: compose the native component and use its built-in variant or slot API.

## Progressive Disclosure
Keep SKILL.md compact and use it as the guardrail, not a full shadcn manual. Add support files only if repeated QA proves the skill needs them. Treat registry docs or examples as read-on-demand references, not blanket requirements. Do not widen into generic frontend design or browser QA.

## Verification Pattern
- Confirm the project context was read before any add or update advice.
- Confirm the registry choice was explicit.
- Confirm installed files were checked after add or update, not just the rendered screen.
- Confirm changed files do not contain stale aliases, missing group wrappers, missing overlay titles, wrong `asChild`/`render` usage, raw color overrides, or icon-library mismatches.
- Confirm at least one generic shortcut was rejected in favor of a shadcn-specific composition path.
- If the result only looks right, recheck the file-level composition instead of treating the screenshot as proof.
