# OpenGrep Validation

## Before Saving Any .yml

```bash
~/.reporails/bin/opengrep scan --config {file} .
echo $?
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Valid, no matches | OK to save |
| 1 | Valid, matches found | OK to save |
| 2 | Syntax error | Fix YAML/regex syntax |
| 7 | No runnable patterns | Add positive pattern |

## Required Fields

Every rule in .yml must have:
- `id` — Unique identifier
- `message` — Human-readable description
- `severity` — ERROR, WARNING, or INFO
- `languages` — Array (usually `[generic]` or `[yaml]`)
- Positive pattern — `pattern-regex` or `pattern`

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
