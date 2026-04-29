---
asset_type: skill
asset_id: dynamic-og-images
version: 1
description: Planning guardrail for Next.js App Router social preview images: route choice, runtime, fonts, assets, CSS subset, and proof.
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
  - https://nextjs.org/docs/15/app/api-reference/functions/image-response
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
  - @vercel/og
---

# Dynamic OG Images

## Purpose

Help agents pick the smallest honest render seam for dynamic social preview images. This is a guardrail, not an OG-image cookbook or a generic design manual.

### Use When

- the repo has `opengraph-image`, `twitter-image`, or a dedicated OG route
- the task is about a share card, metadata image, font loading, asset loading, or preview proof
- the answer depends on current Next.js or Satori behavior

### Do Not Use When

- the task is only generic frontend design or raster art
- browser QA is the only problem
- another more specific skill already owns the seam

## Quick Start

1. Default to `app/blog/[slug]/opengraph-image.tsx` plus `ImageResponse` for a Next.js App Router blog. Use a route handler only when you need a custom URL, custom headers, or a shared endpoint. Use standalone Satori only outside Next.js or when SVG-first output is the point.
2. If the image is segment-based, say `params` is a Promise and must be awaited before reading slug data.
3. State the runtime, font source, asset source, CSS subset, and preview proof in the answer.
4. Keep the card poster-like: one hierarchy, one accent, no webpage layout.

## Operating Constraints

- Default to `runtime = 'edge'`; switch to Node.js only when local files must be read.
- Load fonts explicitly. Do not rely on system fonts or `next/font` to populate the image route.
- Use `ttf`, `otf`, or `woff`; prefer `ttf` or `otf`. Do not use `woff2`.
- Make every non-text asset source explicit: absolute URL, bundled bytes, or data URL. Do not use relative paths.
- Stay inside the documented render subset: inline flex layout, absolute positioning, borders, radii, backgrounds, text wrapping, and simple transforms. Avoid grid, external CSS, `<style>`, `<link>`, pseudo-elements, sticky/fixed positioning, or browser-only tricks.
- If local assets are needed in Next.js, say that Node.js runtime is the exception and the asset should be read relative to the project root.
- Keep CSS variables secondary: Satori supports them, but the layout should still be explicit and local.

## Inputs This Skill Expects

- The route surface or diff.
- The target route or helper.
- Runtime, font source, asset source, and preview step.
- Visual goal, dimensions, and any brand or content constraints.

## Output Contract

- Start with the classification.
- Then name the route/helper, runtime, font source, asset source, CSS subset, and preview step.
- Call out any missing font, asset, runtime, or verification boundary.
- Include one rejected trope and the narrower alternative.
- End with the next verifier and the evidence it should capture.

## Procedure

1. Identify the smallest honest seam.
2. Choose the surface that matches the repo and the output type.
3. Check current official Next.js and Satori docs before making API-specific claims.
4. Specify explicit font and asset loading.
5. Keep the render tree compact, flex-first, and auditable.
6. Verify by rendering the image locally or capturing a screenshot of the generated output.

## Pitfalls And Gotchas

- Rejected trope: copy a full marketing page into the OG route.
- Better alternative: render one compact poster with one hierarchy and one clearly loaded font.
- Rejected trope: hide assets behind relative paths or implicit defaults.
- Better alternative: use absolute URLs or bundled bytes and prove the preview render.
- Rejected trope: turn this into a generic frontend course.
- Better alternative: stay on the route boundary and keep the answer planning-level.

## Progressive Disclosure

Start with the smallest useful read of the request, then widen only enough to name the seam and proof surface. Keep the skill compact so it steers route choice and verification instead of becoming a cookbook.

## Verification Pattern

- Confirm the chosen surface matches the task.
- Confirm route, runtime, fonts, assets, and preview evidence are explicit.
- Confirm the answer stays within the documented render subset and does not rely on browser-only behavior.
- Confirm one generic trope was rejected in favor of a narrower OG-image alternative.
- Next verifier: implementation reviewer or browser QA; capture the generated PNG or screenshot plus any head-tag evidence needed to justify the route choice.
