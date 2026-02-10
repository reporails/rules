# Rule Authoring Reference

Templates and validation for creating rule skeletons.

## .md File Template

```yaml
---
id: "NAMESPACE:CATEGORY:SLOT"
slug: slug-name
title: {Title}                    # max 64 chars
category: structure|content|efficiency|governance|maintenance
type: mechanical|deterministic|semantic
level: L1|L2|L3|L4|L5|L6
targets: "{{instruction_files}}"
checks:
  - id: NAMESPACE.CATEGORY.SLOT.check.NNNN
    name: {Description}
    severity: critical|high|medium|low
backed_by: []                     # source IDs from docs/sources.yml
---

# {Title}

One-sentence impact statement.

## Pass / Fail

**Pass:** example
**Fail:** example

## Limitations

{limitations}
```

### Question and Criteria

All rules can include `question` and `criteria` as documentation of what the rule verifies. For semantic rules these fields are **required** (they drive LLM evaluation). For mechanical and deterministic rules they are **optional** (human-readable description only).

```yaml
question: "{What the rule verifies}"
criteria:
  - {First criterion}
  - {Second criterion}
```

## .yml Placeholder Template

```yaml
rules:
  - id: NAMESPACE.CATEGORY.SLOT.check.NNNN
    message: "{description}"
    severity: WARNING
    languages: [generic]
    pattern-regex: "pattern"
    paths:
      include:
        - "{{instruction_files}}"
```

Mechanical rules have `rules: []` — no OpenGrep patterns needed.

## Coordinate Patterns

| Scope | Pattern | Example |
|-------|---------|---------|
| Core | `CORE:{S\|C\|E\|G\|M}:NNNN` | `CORE:S:0001` |
| Claude agent | `CLAUDE:S:NNNN` | `CLAUDE:S:0001` |
| Codex agent | `CODEX:S:NNNN` | `CODEX:S:0001` |

## Valid Values

| Field | Values |
|-------|--------|
| category | structure, content, efficiency, governance, maintenance |
| type | mechanical, deterministic, semantic |
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
| Wrong check ID format | Must be `NAMESPACE.CATEGORY.SLOT.check.NNNN` |
| Semantic without question | Add question + criteria (required for semantic) |
| Hardcoded paths in .yml | Use `{{instruction_files}}` |
| Title > 64 characters | Shorten or abbreviate |
| Body > 40 lines | Extract to supporting docs |

## Validation Checklist

### Frontmatter

- [ ] `id` matches coordinate pattern
- [ ] `slug` matches directory name
- [ ] `title` <= 64 characters
- [ ] `category` is valid
- [ ] `type` is valid (mechanical/deterministic/semantic)
- [ ] `level` is valid (L1-L6)
- [ ] `checks` array exists and non-empty
- [ ] `checks[].id` follows `NAMESPACE.CATEGORY.SLOT.check.NNNN` format
- [ ] `checks[].severity` is valid
- [ ] If semantic: `question` and `criteria` exist (required)
- [ ] If mechanical/deterministic: `question` and `criteria` optional (documentation only)

### Contract

- [ ] .yml file exists for every .md rule
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml (deterministic/semantic only)
- [ ] Mechanical rules have `rules: []` in .yml

### Content

- [ ] Body <= 40 lines
- [ ] Has "# {Title}" heading matching frontmatter
- [ ] Has Pass/Fail section with examples
