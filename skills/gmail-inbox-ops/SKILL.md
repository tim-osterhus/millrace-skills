---
asset_type: skill
asset_id: gmail-inbox-ops
version: 1
description: Guardrail for Gmail inbox search, triage, reply drafts, forwarding notes, and confirmation-safe mailbox actions.
advisory_only: true
capability_type: planning-guardrail
recommended_for_stages:
  - builder
  - checker
  - fixer
  - updater
forbidden_claims:
  - queue_selection
  - routing
  - retry_thresholds
  - escalation_policy
  - status_persistence
  - terminal_results
  - required_artifacts
---

# Gmail Inbox Ops

## Purpose
Guardrail for agents handling Gmail mailbox slices or threads. Keep search-first triage, thread-grounded reply and forward drafts, and confirmation-gated mailbox actions in one mailbox decision boundary. This is a guardrail, not a Gmail manual.
Use when the user wants inbox search, triage, thread summary, action extraction, reply drafting, forwarding notes, or safe mailbox organization.
Do not use when the request is generic email advice with no Gmail mailbox, thread, or query scope, when the user is asking for account setup or connector provisioning, or when another more specific skill already owns the same workflow boundary.

## Quick Start
1. Narrow the Gmail search scope first.
2. Read the smallest relevant set of messages or threads that can answer the request honestly.
3. Triage every message with explicit buckets and `Reply-needed` on every row.
4. Draft one reply or forward note from thread facts only.
5. Keep send, forward, archive, delete, and label changes pending explicit confirmation.

## Operating Constraints
- Prefer Gmail-native search and thread reads over broad summaries.
- Start with the narrowest useful scope, then expand only when the snippet is not enough.
- Do not claim full inbox coverage unless the scope actually supports it.
- Keep reply and forward drafts grounded in the source thread facts only.
- Call out missing context or assumptions briefly when they affect the recommendation.
- Do not turn analysis into action without explicit user go-ahead.
- Keep send, forward, archive, delete, and label changes pending explicit confirmation.

## Inputs This Skill Expects
- a mailbox slice, thread, or query scope
- a time window, sender focus, or other narrowing hint when available
- whether the goal is triage, summary, drafting, forwarding, or cleanup
- whether the answer should be analysis-only or action-ready

## Output Contract
When triaging, always do all of the following:
- state the search scope and confidence first
- use a markdown table with one row per message
- use these columns: `Bucket | Sender | Subject | Why it belongs there | Likely next action | Reply-needed`
- fill `Reply-needed` on every row with `explicit`, `inferred`, or `none`
- use explicit bucket labels such as `Urgent`, `Needs reply soon`, `Waiting`, `FYI`, and `Noise`
- treat `Urgent` as an answerable direct ask with a hard deadline or immediate business risk; a grounded yes/no or ETA reply still counts as `Urgent` when you can draft it now from the thread
- treat `Needs reply soon` as a direct ask that is time-sensitive but still blocked because the prompt withholds an attachment or context needed for a decisive answer, even if the sender names a deadline
- never label a thread `Urgent` when the thread itself still withholds the attachment or context needed to answer decisively
- if an answerable hard-deadline thread and an attachment-limited thread both exist, rank the answerable hard-deadline thread higher in both bucket severity and the single reply-draft choice unless the prompt explicitly asks you to inspect the missing material
- do not claim full inbox coverage unless the scope actually supports it

When drafting a single reply, choose candidates in this order:
1. the clearest direct ask that can be answered from the provided evidence
2. if no direct ask exists, the earliest hard deadline among answerable threads
3. only then an inferred reply-needed message

A thread that depends on a missing attachment or missing context must not be the single reply draft when another answerable thread exists, unless the prompt explicitly asks you to inspect that missing material. If two candidates still tie, choose the one with the clearest direct ask, then the earliest hard deadline. When forwarding is safer than replying, use this order: blocker facts first, missing attachment or approval second, explicit confirmation gate last.

If you recommend send, forward, archive, delete, or label changes, keep them pending explicit confirmation. Do not collapse that recommendation into a generic `No changes were made` sentence. If no changes are needed, still end with the exact confirmation-gated sentence below.

## Procedure
1. Narrow the mailbox scope with Gmail search.
2. Read the smallest relevant set of messages or threads that can answer the request honestly.
3. Expand to the full thread only when the surrounding conversation changes the classification or draft.
4. Group the findings into explicit buckets and identify the next responder or blocker.
5. Draft the single best reply or forward note using the reply priority rule above.
6. Keep all mailbox changes confirmation-gated.

## Pitfalls And Gotchas
- Summarizing the whole inbox before narrowing scope.
- Omitting `Reply-needed` or treating it as implicit.
- Picking an attachment-dependent thread when another answerable thread exists.
- Labeling a blocked thread `Urgent` just because it has a deadline.
- Writing unsupported claims into a reply or forward draft.
- Writing a forward note that does not name the blocker facts, the missing approval or attachment, and the confirmation gate.
- Ending with a generic no-changes sentence instead of keeping actions pending confirmation.
- Letting a cleanup recommendation become a hidden action instead of a confirmation-gated suggestion.

## Progressive Disclosure
Start with the smallest useful read: what scope is being checked, what the messages appear to need, and what action is safe next. Expand only enough to prove the bucket or draft, then stop. Keep the skill compact so it behaves like an inbox guardrail rather than an email handbook.

## Verification Pattern
- Scope and confidence are explicit.
- Every triage row has bucket, sender, subject, why, next action, and `Reply-needed`.
- The chosen reply draft matches the direct-ask or earliest-deadline rule and avoids missing-attachment traps.
- Mailbox changes remain pending explicit confirmation.

Any send, archive, delete, label, or forward changes remain pending explicit confirmation.
