---
name: validate-rules
description: Validate rules against schema, contracts, and sources
---

# /validate-rules

Validate rules against their sources and schema.

## Usage

```
/validate-rules [id] [options]
```

**Options:**
- `--agent <name>`: Agent for template resolution (default: `claude`)
- `--category <cat>`: Validate only rules in category
- `--source-check`: Deep source validation

**Examples:**
```
/validate-rules                        # All rules, claude agent
/validate-rules S1                     # Single rule
/validate-rules --agent cursor         # All rules, cursor agent
/validate-rules --category structure   # Category filter
/validate-rules --source-check         # Deep source validation
```

## Validation Levels

### Level 1: Schema Validation (Default)

Check rule files against schema. See [schema-checks.md](schema-checks.md) for details.

### Level 2: Contract Validation

Check .md ↔ .yml pairing. See [contract-checks.md](contract-checks.md) for details.

### Level 3: Source Validation (--source-check)

Deep validation against source URLs. See [source-checks.md](source-checks.md) for details.

## Quick Process

### Step 1: Collect Rules

```
Find all .md files in:
  - core/{category}/*.md
  - agents/{agent}/rules/*.md
```

### Step 2: Run Validations

For each rule:
1. Schema validation (required fields, type consistency)
2. Contract validation (.md ↔ .yml matching)
3. OpenGrep validation (pattern validity)
4. Source validation (if --source-check)

### Template Resolution

Before OpenGrep validation, resolve `{{var}}` placeholders:

1. Load agent config: `agents/{agent}/config.yml`
2. Replace variables from `vars:` section:
   - `{{instruction_files}}` → file patterns
   - `{{rules_dir}}` → rules directory
   - `{{skills_dir}}` → skills directory
3. Create temp resolved file for validation

### OpenGrep Validation

Check every .yml file (after template resolution):
- Has positive pattern (`pattern-regex` or `pattern`)
- `pattern-not-regex` is inside `patterns:` block
- Core rules use only `{{instruction_files}}`
- Test: `~/.reporails/bin/opengrep scan --config <resolved-file> .`

### Step 3: Report Results

```
Rules: 42 | Schema errors: 3 | Contract: 1 | Drift: 5
S1: ✓  S2: ✗ schema  C1: ✗ contract  E3: ⚠ drift
```

## Auto-fixable Issues

| Issue | Auto-fix |
|-------|----------|
| Title > 64 chars | Truncate with "..." |
| Missing .yml severity | Add based on mapping |
| Wrong check ID prefix | Rename to match rule ID |

## Manual Review Required

| Issue | Action |
|-------|--------|
| Source drift | Review source, update rule if needed |
| Missing source support | Find supporting source or reconsider check |
| Type mismatch | Change deterministic ↔ semantic |

## Reference Files

- [schema-checks.md](schema-checks.md) — Schema validation details
- [contract-checks.md](contract-checks.md) — Contract validation details
- [source-checks.md](source-checks.md) — Source validation details
