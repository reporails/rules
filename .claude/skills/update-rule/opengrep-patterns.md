# OpenGrep Patterns Reference

Pattern detection for rule validation.

## Required YAML Schema

```yaml
rules:
  - id: RULE-check-name
    message: "Human-readable description"
    severity: ERROR | WARNING | INFO
    languages: [generic]          # or [yaml] for metavariables
    patterns:                     # REQUIRED wrapper for multiple patterns
      - pattern-regex: "..."      # positive pattern MUST come first
      - pattern-not-regex: "..."  # exclusions go INSIDE patterns:
    paths:
      include:
        - "{{instruction_files}}"
```

**Common error:** `pattern-not-regex` at top level instead of inside `patterns:`.

## Pattern Types

| Type | Use | Example |
|------|-----|---------|
| `pattern-regex` | Regex matching | `"(?s)(?:[^\\n]*\\n){200,}"` |
| `pattern` | YAML metavariables | `$KEY: $VALUE` |
| `pattern-either` | OR matching | Multiple options |
| `patterns` | AND matching + exclusions | Combine patterns |
| `pattern-not-regex` | Exclusions (inside patterns:) | Filter false positives |

## Template Variables

| Variable | Core | Agent | Description |
|----------|------|-------|-------------|
| `{{instruction_files}}` | Yes | Yes | Main instruction files |
| `{{rules_dir}}` | No | Yes | Rules directory |
| `{{skills_dir}}` | No | Yes | Skills directory |
| `{{local_file}}` | No | Yes | Local config file |

**Core rules must only use `{{instruction_files}}`.**

## Template Resolution

1. Load agent config: `agents/{agent}/config.yml`
2. Replace `{{var}}` with values from `vars:` section
3. Validate resolved file with OpenGrep

**Save files with `{{var}}` templates intact. Resolution is only for validation.**

## Validation Commands

```bash
~/.reporails/bin/opengrep scan --config path/to/rule.yml .
```

| Exit | Meaning | Action |
|------|---------|--------|
| 0 | Valid, no matches | OK to save |
| 1 | Valid, matches found | OK to save |
| 2 | Syntax/schema error | Fix YAML structure |
| 7 | No runnable patterns | Add positive pattern |

## Severity Mapping

| .md severity | .yml severity |
|--------------|---------------|
| critical | ERROR |
| high | WARNING |
| medium | WARNING |
| low | WARNING |

## Common Patterns

### Line Count Detection

```yaml
pattern-regex: "(?s)(?:[^\\n]*\\n){N,}"  # N+ lines
```

### Keyword Presence

```yaml
pattern-regex: "KEYWORD"
pattern-regex: "KEYWORD1|KEYWORD2"  # OR
```

### Keyword with Context

```yaml
pattern-regex: "NEVER.*[—–-]|NEVER.*instead"
```

### Heading Detection

```yaml
pattern-regex: "^#{1,6} "  # Any heading
pattern-regex: "^## "      # H2 specifically
```

### Section Detection

```yaml
pattern-regex: "(?i)^##?\\s*(commands?|scripts?)"
```

### Code Block Detection

```yaml
pattern-regex: "```[^\\n]*\\n(?:[^\\n]*\\n){10,}```"  # 10+ line blocks
```

### YAML Metavariables

```yaml
languages: [yaml]
pattern: |
  $KEY: $VALUE
```

### Absence Detection

Combine positive + negative to detect missing content:

```yaml
patterns:
  - pattern-regex: "^#"              # Match markdown files
  - pattern-not-regex: "REQUIRED"    # Flag if REQUIRED absent
```

### Combining Patterns

```yaml
# AND: all must match (positive FIRST)
patterns:
  - pattern-regex: "POSITIVE"
  - pattern-not-regex: "EXCLUDE"

# OR: any can match
pattern-either:
  - pattern-regex: "OPTION1"
  - pattern-regex: "OPTION2"
```
