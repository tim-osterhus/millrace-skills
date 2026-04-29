---
asset_type: skill
asset_id: dynamic-og-images
version: 1
description: Guardrail for choosing Next.js metadata routes, route handlers with ImageResponse, standalone Satori, or hybrid render trees for dynamic OG and social preview images, with explicit font, asset, CSS, and preview boundaries.
advisory_only: true
capability_type: planning-guardrail
recommended_for_stages:
  - builder
  - checker
  - fixer
  - planner
forbidden_claims:
  - queue_selection
  - routing
  - retry_thresholds
  - escalation_policy
  - status_persistence
  - terminal_results
  - required_artifacts
priority: 4
docs:
  - https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image
  - https://github.com/vercel/satori
pathPatterns:
  - app/**/og/**
  - app/**/og.*
  - app/**/opengraph-image.*
  - app/**/twitter-image.*
  - src/app/**/og/**
  - src/app/**/og.*
  - src/app/**/opengraph-image.*
  - src/app/**/twitter-image.*
  - pages/api/og.*
  - pages/api/og/**
  - src/pages/api/og.*
  - src/pages/api/og/**
importPatterns:
  - next/og
  - ImageResponse
  - satori
  - satori/standalone
  - @vercel/og
bashPatterns:
  - '\bnpm\s+(install|i|add)\s+[^\n]*\bsatori\b'
  - '\bpnpm\s+(install|i|add)\s+[^\n]*\bsatori\b'
  - '\bbun\s+(install|i|add)\s+[^\n]*\bsatori\b'
  - '\byarn\s+add\s+[^\n]*\bsatori\b'
  - '\bnpm\s+(install|i|add)\s+[^\n]*@vercel/og\b'
  - '\bpnpm\s+(install|i|add)\s+[^\n]*@vercel/og\b'
  - '\bbun\s+(install|i|add)\s+[^\n]*@vercel/og\b'
  - '\byarn\s+add\s+[^\n]*@vercel/og\b'
---

# Dynamic OG Images

## Purpose

Help agents choose and review the smallest honest render surface for dynamic social preview images. This is a guardrail, not an OG-image cookbook or a generic design manual.

### Use When

- the repo has `app/**/opengraph-image.*`, `app/**/twitter-image.*`, or another OG-image surface
- the user wants a dynamic share card, social preview image, or metadata image route
- the task involves fonts, image dimensions, preview validation, or edge-runtime constraints
- the answer depends on current Next.js or Satori docs

### Do Not Use When

- the task is only generic frontend design
- the surface is pure raster art or photo editing
- browser QA is the only problem
- another more specific skill already owns the seam

## Quick Start

1. Classify the request first as `Next.js metadata route`, `standalone Satori`, or `hybrid`.
2. Name the render boundary next: route file, runtime, font source, asset source, CSS subset, and preview step.
3. Read the current official Next.js and Satori docs before writing code whenever either API is involved.
4. Prefer `next/og` / `ImageResponse`, `runtime = 'edge'`, explicit font loading, and `1200x630` unless the task explicitly says otherwise.
5. Keep the tree flex-first and inline-styled, then verify a local render or screenshot.
6. If the answer is planning-level, keep the surface choice explicit in one line:
   - `Next.js metadata route`: use `opengraph-image` or `twitter-image` when the segment should own the image and automatic `<head>` tags matter.
   - `route handler with ImageResponse`: use a dedicated route when you need a custom URL shape, query params, or a shared endpoint that is not tied to the convention file.
   - `standalone Satori`: use `satori` or `satori/standalone` when you need SVG-only output, a framework-agnostic helper, or a render check outside Next.
   - `hybrid`: use one shared pure render tree when a Next route and a standalone helper must stay in sync. Keep the wrapper thin.

## Operating Constraints

- Do not make the image look like a full webpage; OG images are poster frames, not browsers.
- Do not rely on default fonts.
- Do not use external CSS, `<style>`, `<link>`, or `<script>` inside the render tree.
- Do not depend on browser-only layout tricks such as sticky or fixed positioning, pseudo-elements, or media-query branching.
- Do not assume relative image paths will work.
- Do not treat CSS variables as a reason to move styling out of the tree; current Satori supports them, but keep style logic explicit and local.
- Prefer nested flex containers over grid-like page layouts; Satori is flexbox-first, and the render should stay easy to audit.
- If the task needs local file assets in Next.js, treat Node.js runtime as the exception and keep the asset source explicit.
- If you choose a segment metadata route, remember `params` is async in current Next.js docs and should be awaited before use.
- Do not turn this into a generic frontend or image-design course.

## Inputs This Skill Expects

- The repo surface or diff.
- The target route, runtime, font source, asset source, and preview step.
- The visual goal, dimensions, and any brand or content constraints.
- Current official docs when Next.js metadata or Satori behavior could affect the seam.

## Output Contract

- Start with the classification.
- Then name the route file or standalone helper, runtime, font source, asset source, CSS subset, and preview step.
- Call out any missing font, asset, runtime, or verification boundary.
- Name at least one trope you rejected and the narrower alternative.
- End with the next verifier and the evidence it should capture.

## Procedure

1. Identify the smallest honest seam.
2. Choose the surface that matches the repo and the output type.
3. Check current official docs before making API-specific claims.
4. Specify explicit font and asset loading.
5. Keep the render tree compact, flex-first, and auditable.
6. Verify by rendering the image locally or capturing a screenshot of the generated output.
7. If the output still looks generic, simplify the card before adding more decoration.

## Pitfalls And Gotchas

- Rejected trope: copy a full marketing page into the OG route.
- Better alternative: render one compact poster with one hierarchy, one accent, and one clearly loaded font.
- Rejected trope: use external CSS or browser layout assumptions to save time.
- Better alternative: inline the minimum styles and stay inside the documented render subset.
- Rejected trope: embed images or logos without making the source explicit.
- Better alternative: use absolute URLs or bundled data/ArrayBuffer sources and prove the preview render.
- Rejected trope: hard-ban CSS variables even when the current docs support them.
- Better alternative: keep variables secondary to explicit inline values and only use them when they reduce duplication materially.

## Progressive Disclosure

Start with the smallest useful read of the request, then widen only enough to name the seam, the asset path, and the proof surface. Keep the skill compact so it steers route choice and verification instead of becoming a generic rendering manual.

## Verification Pattern

- Confirm the chosen surface matches the task.
- Confirm route, runtime, fonts, assets, and preview evidence are explicit.
- Confirm the answer stays within the documented render subset and does not rely on browser-only behavior.
- Confirm one generic trope was rejected in favor of a narrower OG-image alternative.
- Next verifier: implementation reviewer or browser QA; capture the generated PNG or screenshot plus any head-tag evidence needed to justify the route choice.
