---
name: generate-all-rules
description: Batch generate or regenerate all rules from specification
disable-model-invocation: true
---

# /generate-all-rules

Batch generate or regenerate all rules from a specification table.

## Usage

```
/generate-all-rules                    # Generate from default spec
/generate-all-rules --scope core       # Only core rules
/generate-all-rules --scope claude     # Only Claude-specific rules
/generate-all-rules --dry-run          # Show what would be generated
```

## Workflow

### Step 1: Read Specification

Read the rule specification table from provided input or default location.

### Step 2: For Each Rule

1. Parse rule spec (ID, category, type, title)
2. Gather sources from `docs/sources.yml`
3. Generate .md file using `/generate-rule` workflow
4. Generate .yml file with OpenGrep patterns
5. Validate against schema

### Step 3: Validate All

Run `/validate-rules` to check:
- All schema checks pass
- All contracts valid (.md ↔ .yml)
- No missing sources

### Step 4: Report Summary

```
Generated: 42 rules (37 core, 5 claude) | Schema: ✓ | Contract: ✓
```

## Rule Spec Format

| ID | Category | Type | Title |
|----|----------|------|-------|
| S1 | structure | deterministic | Size Limits |
| C1 | content | heuristic | Core Sections |

## Dependencies

- `/generate-rule` skill for individual rule generation
- `/validate-rules` skill for validation
- Sources file at `backbone.artifacts.sources`
- Rule schema at `backbone.schemas.rule`

Resolve all paths from `.reporails/backbone.yml`. See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md).
