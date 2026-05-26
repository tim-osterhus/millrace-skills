---
asset_type: skill
asset_id: pydantic-v2-patterns
version: 1
description: "Guardrail for Pydantic v2 runtime models, config loaders, contract schemas, validators, and persisted state serialization in Python code."
advisory_only: true
capability_type: implementation-guardrail
recommended_for_stages:
  - planner
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

# Pydantic v2 Patterns

## Purpose
Help agents build or refactor Pydantic v2 models for typed runtime configuration, shared contracts, stage/result schemas, and persisted state snapshots. This skill is for validation and serialization boundaries, not arbitrary business logic.

**Use When**
- adding or changing `BaseModel` classes, validators, config loaders, contract models, or state snapshots
- replacing untyped `dict[str, Any]` blobs with typed nested models
- wiring file, environment, API, or object ingestion through a validation boundary
- removing Pydantic v1 idioms from edited code

**Do Not Use When**
- a dataclass, `TypedDict`, enum, or literal type is enough and no runtime validation boundary exists
- the task is broad environment-settings design across many deployment sources
- the change is business logic rather than model shape, validation, normalization, or serialization

## Quick Start
1. Identify the boundary: load, validate, normalize, mutate, dump, or persist.
2. Use v2-native APIs: `model_config`, `ConfigDict`, `model_validate`, `model_dump`, `field_validator`, and `model_validator`.
3. Default runtime config and contracts to closed-world behavior such as `extra="forbid"` unless unknown keys are part of the contract.
4. Keep validators pure: no filesystem reads, environment reads, subprocesses, network calls, or repo mutation.
5. Choose mutable working models or immutable snapshots deliberately.
6. Validate one representative load-to-dump round trip before claiming the boundary is correct.

## Operating Constraints
- Do not add new v1 idioms such as `class Config`, `@validator`, `@root_validator`, `parse_obj()`, `dict()`, or `json()`.
- Use explicit defaults and `Field(default_factory=...)` for mutable containers.
- Prefer nested models over deeply nested untyped dictionaries.
- Keep enums, literals, and discriminated unions aligned with persisted state names.
- Do not hide I/O, mutation, or expensive computation inside validators.
- Preserve serialized field names unless an explicit migration changes the persisted contract.
- Report any compatibility constraint if the repo still supports Pydantic v1.

## Inputs This Skill Expects
- Target Python files that define or consume models.
- Boundary call sites that load, validate, mutate, or dump those models.
- Representative raw payloads, config samples, fixtures, or persisted state examples.
- Existing tests for config, contracts, state, or control-plane behavior when available.
- Any serialized output compatibility constraints.

## Output Contract
- Provide v2-native model and boundary edits scoped to the touched area.
- Name the input boundary and output serialization shape.
- State extra-field, default, path, enum, mutation, and serialization policy when relevant.
- Include a representative round-trip test, fixture check, or smoke snippet.
- State any intentionally preserved v1 compatibility separately from new v2-native code.

## Procedure
1. Locate model definitions and loader/dumper call sites.
2. Identify the raw input shape and persisted output shape.
3. Choose closed-world or open-world extra-field behavior intentionally.
4. Implement v2-native fields, validators, computed fields, and serializers only where needed.
5. Replace nearby edited v1 idioms with v2-native calls.
6. Add or update focused tests for valid input, invalid input, defaults, and serialization.
7. Run the repo's targeted validation command and inspect serialized output.

## Pitfalls And Gotchas
- Putting file reads or environment lookups inside validators.
- Using `Any` because the model shape was not investigated.
- Forgetting `default_factory` for lists, dicts, and sets.
- Allowing unknown config keys silently in runtime contracts.
- Serializing with defaults or aliases accidentally changed from prior persisted state.
- Migrating a broad model graph when the task only touches one boundary.

## Progressive Disclosure
Start with the model and boundary being edited. Expand into migration, aliases, discriminated unions, custom serializers, or settings management only when the current payload requires them. Keep examples small and tied to fixtures or persisted artifacts.

## Verification Pattern
- Confirm new or edited code uses Pydantic v2 APIs.
- Confirm untrusted input enters through `model_validate` or `model_validate_json`.
- Confirm serialization uses `model_dump` or `model_dump_json` with deliberate flags.
- Confirm validators are pure and do not perform hidden I/O.
- Run a representative valid/invalid load test and a load-to-dump round trip.
