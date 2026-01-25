# OpenGrep Validation

## Template Resolution (Required for Validation)

Rules use template variables that must be resolved before OpenGrep can scan.

### Step 1: Load Agent Config

```
agents/{agent}/config.yml   # default: claude
```

### Step 2: Replace Variables

| Template | Config Key | Example Value (claude) |
|----------|------------|------------------------|
| `{{instruction_files}}` | `vars.instruction_files` | `**/CLAUDE.md`, `.claude/rules/**/*.md` |
| `{{rules_dir}}` | `vars.rules_dir` | `.claude/rules` |
| `{{skills_dir}}` | `vars.skills_dir` | `.claude/skills` |
| `{{local_file}}` | `vars.local_file` | `CLAUDE.local.md` |

### Step 3: Create Resolved File

For validation, create a temp file with resolved paths:

```yaml
# Original (keep in repo)
paths:
  include:
    - "{{instruction_files}}"

# Resolved (temp, for validation only)
paths:
  include:
    - "**/CLAUDE.md"
    - ".claude/rules/**/*.md"
```

## Validation Command

```bash
~/.reporails/bin/opengrep scan --config {resolved-file} .
echo $?
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Valid, no matches | OK to save |
| 1 | Valid, matches found | OK to save |
| 2 | Syntax error | Fix YAML/regex syntax |
| 7 | No runnable patterns | Add positive pattern |

## Required Schema Structure

```yaml
rules:
  - id: RULE-check-name
    message: "Human-readable description"
    severity: ERROR | WARNING | INFO
    languages: [generic]
    patterns:                     # ← REQUIRED wrapper
      - pattern-regex: "..."      # ← positive pattern FIRST
      - pattern-not-regex: "..."  # ← exclusions INSIDE patterns:
    paths:
      include:
        - "{{instruction_files}}"
```

**INVALID:** `pattern-not-regex` at top level (causes exit 7 or schema error)

## Required Fields

Every rule in .yml must have:
- `id` — Unique identifier
- `message` — Human-readable description
- `severity` — ERROR, WARNING, or INFO
- `languages` — Array (usually `[generic]` or `[yaml]`)
- Positive pattern — `pattern-regex` or `pattern` (FIRST in `patterns:`)

## Pattern Requirements

1. **Must have positive pattern first**
   - `pattern-regex: "..."` or `pattern: |`
   - `pattern-not-regex` alone fails with exit 7

2. **Core rules use only `{{instruction_files}}`**
   - Agent-specific vars (`{{rules_dir}}`) go in agent rules

3. **Regex must be valid PCRE**
   - Escape special chars: `\.`, `\(`, `\[`
   - Use `(?i)` for case-insensitive

## Full Validation

After updating, verify no conflicts:

```bash
find core agents -name "*.yml" ! -name "config.yml" \
  -exec ~/.reporails/bin/opengrep scan --config {} . \; 2>&1 \
  | grep -iE "error|failed|invalid"
```

Should return empty (no errors).
