# Common Pattern Fixes

## Exit Code 7: No Runnable Patterns

**Problem:** Only `pattern-not-regex` without positive pattern.

**Fix:** Add positive pattern first.

```yaml
# Before (invalid)
patterns:
  - pattern-not-regex: "EXCLUDE"

# After (valid)
patterns:
  - pattern-regex: "^#"
  - pattern-not-regex: "EXCLUDE"
```

## Exit Code 2: Syntax Error

**Problem:** Invalid YAML or regex syntax.

**Common causes:**
- Unescaped special characters in regex
- Bad indentation
- Missing quotes around patterns with special chars

**Fix:** Check YAML syntax and escape regex special chars.

## Missing File Detection

**Problem:** `pattern-regex: "^$"` to detect missing files.

**Reality:** OpenGrep can't detect missing files — it only scans existing files.

**Fix:** Either:
- Remove the check (can't be done deterministically)
- Change to semantic rule with LLM file existence check
- Use paths-only rule if OpenGrep supports it

## Metavariables Don't Work

**Problem:** Using `$KEY: $VALUE` in `pattern-regex`.

**Reality:** Metavariables only work in `pattern:` blocks with YAML language.

**Fix:** Use proper syntax:

```yaml
# For regex (generic language)
pattern-regex: "[a-z]+:"

# For YAML metavariables
languages: [yaml]
pattern: |
  $KEY: $VALUE
```

## Absence Detection

**Problem:** Need to detect when something is NOT present.

**Fix:** Use positive pattern + pattern-not combo:

```yaml
patterns:
  - pattern-regex: "^#"              # Match markdown files
  - pattern-not-regex: "REQUIRED"    # Flag if REQUIRED absent
```

## Template Variables

| Variable | Use in |
|----------|--------|
| `{{instruction_files}}` | Core + agent rules |
| `{{rules_dir}}` | Agent rules only |
| `{{skills_dir}}` | Agent rules only |
