# Rule Authoring Reference

Templates and validation for creating rule skeletons.

## .md File Template

```yaml
---
id: {ID}
title: {Title}                    # max 64 chars
category: structure|content|efficiency|maintenance
type: deterministic|semantic
checks:
  - id: "{NAMESPACE}.{CATEGORY}.{SLOT}.{descriptive-name}"
    name: {Description}
    severity: critical|high|medium|low
backed_by: []                     # empty by default
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

## .yml Placeholder Template

```yaml
rules:
  - id: "{NAMESPACE}.{CATEGORY}.{SLOT}.{descriptive-name}"
    message: "TODO: {description}"
    severity: WARNING
    languages: [generic]
    pattern-regex: "TODO"  # placeholder
    paths:
      include:
        - "{{instruction_files}}"
```

## ID Patterns

| Scope | Pattern | Example |
|-------|---------|---------|
| Core | `CORE:{CAT}:{SLOT}` | `CORE:S:0001`, `CORE:C:0005` |
| Agent | `{AGENT}:{CAT}:{SLOT}` | `CLAUDE:S:0001`, `CODEX:S:0003` |
| Recommended | `RRAILS:{CAT}:{SLOT}` | `RRAILS:C:0008`, `RRAILS:E:0002` |
| Recommended Agent | `RRAILS_{AGENT}:{CAT}:{SLOT}` | `RRAILS_CLAUDE:S:0001` |

**Check IDs**: `{NAMESPACE}.{CATEGORY}.{SLOT}.{descriptive-name}` — dots and kebab-case name in both rule.md and rule.yml.

## Valid Values

| Field | Values |
|-------|--------|
| category | structure, content, efficiency, maintenance |
| type | deterministic, semantic |
| severity (md) | critical, high, medium, low |
| severity (yml) | ERROR, WARNING, INFO |

## Severity Mapping

| .md severity | .yml severity |
|--------------|---------------|
| critical | ERROR |
| high | WARNING |
| medium | WARNING |
| low | WARNING |

## Common Mistakes & Fixes

| Mistake | Fix |
|---------|-----|
| Using `{{rules_dir}}` in core rules | Core uses only `{{instruction_files}}` |
| Missing .yml file | Always create both files |
| Wrong check ID format | Must be `NAMESPACE.CATEGORY.SLOT.descriptive-name` |
| Semantic without question | Add question + criteria |
| Deterministic with question | Remove question + criteria |
| Hardcoded paths in .yml | Use `{{instruction_files}}` |
| Title > 64 characters | Shorten or abbreviate |
| Body > 40 lines | Extract to supporting docs |

## Validation Checklist

### Frontmatter

- [ ] `id` matches pattern (core/agent)
- [ ] `title` <= 64 characters
- [ ] `category` is valid
- [ ] `type` is valid (deterministic/semantic)
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
