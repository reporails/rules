# Rule Templates

## .md File Template

**Frontmatter:**
```yaml
id: {ID}
title: {Title}                    # ≤64 chars
category: structure|content|efficiency|governance|maintenance
type: deterministic|semantic
checks:
  - id: {ID}-{check-slug}
    name: {Description}
    severity: critical|high|medium|low
```

**Body:** `# {Title}` + one-sentence impact + `## Pattern` with Good/Bad examples

## Semantic Rule Additions

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
    severity: {ERROR|WARNING|INFO}
    languages: [generic]
    pattern-regex: "{pattern}"
    paths:
      include:
        - "{{instruction_files}}"
```

## Severity Mapping

| Rule severity | OpenGrep severity |
|---------------|-------------------|
| critical | ERROR |
| high | WARNING |
| medium | WARNING |
| low | WARNING |

## Validation Checklist

### Frontmatter

- [ ] `id` matches pattern (core: `^[SCEGM][0-9]+$`, agent: `^[A-Z]+_[SCEGM][0-9]+$`)
- [ ] `title` ≤ 64 characters
- [ ] `category` is valid (structure, content, efficiency, governance, maintenance)
- [ ] `type` is valid (deterministic, semantic)
- [ ] `checks` array exists and is non-empty
- [ ] Each `checks[].id` starts with rule ID + hyphen
- [ ] Each `checks[].severity` is valid (critical, high, medium, low)
- [ ] If semantic: `question` and `criteria` exist
- [ ] If deterministic: `question` and `criteria` do NOT exist
- [ ] `sources` are valid URLs (if present)
- [ ] `see_also` references valid rule IDs (if present)

### Contract

- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md

### Content

- [ ] Body ≤ 40 lines
- [ ] Has "# {Title}" heading matching frontmatter
- [ ] Has impact statement (one sentence)
- [ ] Has Pattern section with Good/Bad examples

### OpenGrep

- [ ] .yml file parses as valid YAML
- [ ] Each rule has: id, message, severity, languages, paths
- [ ] Severity mapping is correct
- [ ] Paths use template variables, not hardcoded agent paths
