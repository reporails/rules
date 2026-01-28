# Rule Authoring Reference

Templates and validation for creating rules.

## .md File Template

```yaml
---
id: {ID}
title: {Title}                    # max 64 chars
category: structure|content|efficiency|governance|maintenance
type: deterministic|semantic
confidence: confirmed|high|medium|low
checks:
  - id: {ID}-{check-slug}
    name: {Description}
    severity: critical|high|medium|low
backed_by:                        # optional
  - source: source-id
    claim: claim-id
---

# {Title}

One-sentence impact statement.

## Pattern

**Good:**
```
example
```

**Bad:**
```
example
```
```

### Semantic Rule Additions

For semantic rules, add to frontmatter:

```yaml
question: "{What LLM evaluates}"
criteria:
  - {First criterion}
  - {Second criterion}
```

## .yml File Template

```yaml
rules:
  - id: {ID}-{check-slug}
    message: "{What was detected}"
    severity: ERROR|WARNING|INFO
    languages: [generic]
    pattern-regex: "{pattern}"
    paths:
      include:
        - "{{instruction_files}}"
```

## ID Patterns

| Scope | Pattern | Example |
|-------|---------|---------|
| Core | `^[SCEGM][0-9]+$` | S1, C12, E3 |
| Agent | `^[A-Z]+_[SCEGM][0-9]+$` | CLAUDE_S4 |

## Valid Values

| Field | Values |
|-------|--------|
| category | structure, content, efficiency, governance, maintenance |
| type | deterministic, semantic |
| confidence | confirmed, high, medium, low |
| severity (md) | critical, high, medium, low |
| severity (yml) | ERROR, WARNING, INFO |

## Common Mistakes & Fixes

| Mistake | Fix |
|---------|-----|
| `pattern-not-regex` at top level | Move inside `patterns:` block |
| Negative-only patterns (exit 7) | Add positive pattern before `pattern-not-regex` |
| Missing required fields (exit 2) | Add id, message, severity, languages |
| Using `{{rules_dir}}` in core rules | Core uses only `{{instruction_files}}` |
| Missing .yml file | Always create both files |
| Wrong check ID format | Must be `{rule_id}-{suffix}` |
| Semantic without question | Add question + criteria |
| Deterministic with question | Remove question + criteria |
| Hardcoded paths in .yml | Use `{{instruction_files}}` |
| Title > 64 characters | Shorten or abbreviate |
| Body > 40 lines | Extract to supporting docs |
| Missing severity mapping | critical -> ERROR, others -> WARNING |

## Validation Checklist

### Frontmatter

- [ ] `id` matches pattern (core/agent)
- [ ] `title` <= 64 characters
- [ ] `category` is valid
- [ ] `type` is valid (deterministic/semantic)
- [ ] `confidence` is valid
- [ ] `checks` array exists and non-empty
- [ ] `checks[].id` starts with rule ID + hyphen
- [ ] `checks[].severity` is valid
- [ ] If semantic: `question` and `criteria` exist
- [ ] If deterministic: NO `question` or `criteria`

### Contract

- [ ] .yml file exists for every .md rule
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md

### Content

- [ ] Body <= 40 lines
- [ ] Has "# {Title}" heading matching frontmatter
- [ ] Has Pattern section with Good/Bad examples
