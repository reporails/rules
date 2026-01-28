# OpenGrep Pattern Guide

Guide for writing OpenGrep patterns in rule `.yml` files.

---

## Overview

OpenGrep is a static analysis tool that powers deterministic rule detection. It supports 30+ languages including a "generic" mode for markdown files.

All rules (deterministic and semantic) use OpenGrep patterns. The difference is what happens after:
- **Deterministic:** OpenGrep result is final
- **Semantic:** OpenGrep catches candidates, LLM evaluates gaps

---

## Basic Pattern Syntax

### Generic Mode (for Markdown)

Use `languages: [generic]` for CLAUDE.md and other instruction files:

```yaml
rules:
  - id: S1-root-too-long
    message: "Root file exceeds 200 lines"
    severity: ERROR
    languages: [generic]
    pattern-regex: "..."
    paths:
      include:
        - "{{instruction_files}}"
```

### Pattern Types

| Type | Use for | Example |
|------|---------|---------|
| `pattern-regex` | Exact text matching | `"NEVER.*instead"` |
| `pattern` | Structural matching | `paths: $VALUE` |
| `patterns` | Multiple conditions | AND logic |
| `pattern-either` | Alternative matches | OR logic |

---

## Pattern-Regex Examples

### Keyword Detection

```yaml
# Detect NEVER statements
pattern-regex: "NEVER"

# Detect NEVER with alternative (good pattern)
pattern-regex: "NEVER.*[—–-]|NEVER.*instead"

# Detect emphasis overuse
pattern-regex: "IMPORTANT|CRITICAL|MUST"
```

### Counting Patterns

```yaml
# Detect 6+ level-2 headings (file too large)
pattern-regex: "(?s)^## [^\\n]+.*?^## [^\\n]+.*?^## [^\\n]+.*?^## [^\\n]+.*?^## [^\\n]+.*?^## [^\\n]+"
```

### Line Count Proxy

```yaml
# Detect 100+ lines (proxy via newline count)
pattern-regex: "(?s)(?:[^\\n]*\\n){100,}"
```

### Code Block Detection

```yaml
# Detect code blocks over 15 lines
pattern-regex: "```[^\\n]*\\n(?:[^\\n]*\\n){15,}```"
```

---

## YAML Frontmatter Detection

OpenGrep natively parses YAML. Use `languages: [yaml]` for frontmatter:

```yaml
rules:
  - id: S5-paths-scoped
    message: "Rule file has path scoping"
    languages: [yaml]
    pattern: |
      paths: $VALUE
```

---

## Path Variables

Use template variables from agent config:

```yaml
paths:
  include:
    - "{{instruction_files}}"    # Main instruction file(s)
    - "{{rules_dir}}/*.md"       # Rules directory (if exists)
```

Variables are resolved at runtime based on agent config.

---

## Combining Patterns

### AND Logic (all must match)

```yaml
patterns:
  - pattern-regex: "^## "           # Has H2 headings
  - pattern-regex: "(?s).{5000,}"   # And is long
```

### OR Logic (any can match)

```yaml
pattern-either:
  - pattern-regex: "NEVER"
  - pattern-regex: "MUST NOT"
  - pattern-regex: "DO NOT"
```

### NOT Logic (must not match)

```yaml
patterns:
  - pattern-regex: "NEVER"
  - pattern-not-regex: "instead|—"   # NEVER without alternative
```

---

## Limitations

| Limitation | Workaround |
|------------|------------|
| Metavariables capture single words only | Use `pattern-regex` for phrases |
| Ellipsis (`...`) spans max 10 lines | Use regex for longer spans |
| No inline regex in patterns | Use `pattern-regex` instead |
| Can't assess semantic quality | Mark rule as `type: semantic` |

---

## Semantic Rules Still Need Patterns

**Important:** Semantic rules are NOT "LLM only."

They are: **OpenGrep first, LLM fills gaps.**

```
OpenGrep catches what it can
    ↓
Results passed to LLM:
  - "Found these patterns"
  - "At these locations"
    ↓
LLM evaluates only what OpenGrep couldn't determine
```

**Example: G2 Security Rules Ownership**

OpenGrep can detect:
- `@security-team` mentions
- `CODEOWNERS` references
- "security" + "owner" patterns

OpenGrep can't determine:
- Are these owners actually qualified?
- Is the review process appropriate?

**So you write both:**

```yaml
# G2-security-ownership.md (frontmatter)
type: semantic
checks:
  - id: G2-ownership-patterns
    name: Security ownership indicators
    severity: high
question: "Given what was found, are security rules properly owned?"
criteria:
  - Security rules have designated owners
  - Owners have relevant expertise
```

```yaml
# G2-security-ownership.yml (OpenGrep patterns)
rules:
  - id: G2-ownership-patterns
    message: "Security ownership pattern found"
    severity: WARNING
    languages: [generic]
    pattern-either:
      - pattern-regex: "@security|security-team|security.lead"
      - pattern-regex: "CODEOWNERS.*security"
      - pattern-regex: "security.*owner|owner.*security"
```

**The LLM receives:**
- What OpenGrep found (patterns, locations)
- What to evaluate (question + criteria)
- Only decides what patterns couldn't

This minimizes token cost and improves accuracy.

---

## Testing Patterns

Test your patterns locally before submitting:

```bash
opengrep scan --config your-rule.yml --target test-file.md
```

---

## Resources

- [OpenGrep GitHub](https://github.com/opengrep/opengrep)
- [Semgrep Generic Pattern Matching](https://semgrep.dev/docs/writing-rules/generic-pattern-matching)
- [Semgrep Pattern Syntax](https://semgrep.dev/docs/writing-rules/pattern-syntax)