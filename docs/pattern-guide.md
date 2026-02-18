# Pattern Guide

Guide for writing regex patterns in rule `.yml` files.

---

## Overview

The regex engine powers deterministic rule detection. It uses a "generic" mode for markdown files and supports YAML structural matching.

All rules (deterministic and semantic) use regex patterns. The difference is what happens after:
- **Deterministic:** Pattern result is final
- **Semantic:** Patterns catch candidates, LLM evaluates gaps

---

## Basic Pattern Syntax

### Generic Mode (for Markdown)

Use `languages: [generic]` for CLAUDE.md and other instruction files:

```yaml
rules:
  - id: CORE.S.0005.exceeds-300-lines
    message: "Root file exceeds 300 lines"
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

The engine natively parses YAML. Use `languages: [yaml]` for frontmatter:

```yaml
rules:
  - id: CORE.S.0008.has-path-scoping
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

They are: **Patterns first, LLM fills gaps.**

```
Patterns catch what they can
    ↓
Results passed to LLM:
  - "Found these patterns"
  - "At these locations"
    ↓
LLM evaluates only what patterns couldn't determine
```

**Example: Cross-Agent Compatibility (CORE:G:0001)**

Patterns can detect:
- Agent-specific syntax (`@import`, `.claude/rules/`)
- References to agent-specific directories

Patterns can't determine:
- Is the file actually shared across agents, or agent-specific?
- Is the agent syntax intentional and scoped correctly?

**So you write both:**

```yaml
# core/governance/cross-agent-compatibility/rule.md (frontmatter)
type: semantic
checks:
  - id: CORE.G.0001.agent-specific-syntax
    name: agent-specific-syntax
    severity: medium
  - id: CORE.G.0001.semantic-evaluation
    name: semantic-evaluation
    severity: medium
question: "Does this shared instruction file avoid agent-specific syntax?"
criteria:
  - File uses standard markdown without agent-specific syntax
  - No references to agent-specific directories
```

```yaml
# core/governance/cross-agent-compatibility/rule.yml (regex patterns)
rules:
  - id: CORE.G.0001.agent-specific-syntax
    message: "Agent specific syntax"
    severity: WARNING
    languages: [generic]
    pattern-regex: "(?:@import|\\.\\.?claude/rules/|\\.github/instructions/)"
```

**The LLM receives:**
- What patterns found (matches, locations)
- What to evaluate (question + criteria)
- Only decides what patterns couldn't

This minimizes token cost and improves accuracy.

---

## Testing Patterns

Test your patterns locally before submitting:

```bash
ails test --rule <coordinate>
```

---

## Resources

- [Semgrep Generic Pattern Matching](https://semgrep.dev/docs/writing-rules/generic-pattern-matching)
- [Semgrep Pattern Syntax](https://semgrep.dev/docs/writing-rules/pattern-syntax)
