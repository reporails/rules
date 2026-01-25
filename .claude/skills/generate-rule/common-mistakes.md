# Common Mistakes

## Schema Structure Errors

**INVALID** - `pattern-not-regex` at top level:
```yaml
rules:
  - id: rule-id
    pattern-not-regex: "..."     # ❌ top-level = schema error
```

**VALID** - patterns inside `patterns:` wrapper:
```yaml
rules:
  - id: rule-id
    message: "..."
    severity: WARNING
    languages: [generic]
    patterns:                    # ✅ required wrapper
      - pattern-regex: "..."     # positive match FIRST
      - pattern-not-regex: "..." # exclusions INSIDE patterns:
```

## Quick Reference

| Mistake | Fix |
|---------|-----|
| `pattern-not-regex` at top level | Move inside `patterns:` block |
| Negative-only patterns (exit 7) | Add positive pattern before `pattern-not-regex` |
| Missing required fields (exit 2) | Add id, message, severity, languages |
| Using `{{rules_dir}}` in core rules | Core uses only `{{instruction_files}}` |
| Using source IDs | Use full URLs |
| Missing .yml file | Always create both files |
| Wrong check ID format | Must be `{rule_id}-{suffix}` |
| Semantic without question | Add question + criteria |
| Deterministic with question | Remove question + criteria |
| Hardcoded paths in .yml | Use `{{instruction_files}}` |
| Title > 64 characters | Shorten or abbreviate |
| Body > 40 lines | Extract to supporting docs |
| Missing severity mapping | critical→ERROR, others→WARNING |
| Citing L5-L6 as Anthropic docs | Use docs/capability-levels.md |
