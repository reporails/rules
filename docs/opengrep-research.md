# OpenGrep Research for Rule Detection

Research conducted: 2026-01-24

## Overview

OpenGrep is a fork of Semgrep CE, providing static code analysis with semantic grep capabilities. It supports 30+ languages including a "generic" mode for markdown and other text files.

## Capabilities for CLAUDE.md Validation

### Generic Pattern Matching

OpenGrep can analyze markdown files using `languages: - generic`:

- **Metavariables** (`$X`): Capture single words (alphanumeric tokens)
- **Ellipsis** (`...`): Skip up to 10 lines
- **Sequence capture** (`$...X`): Capture word sequences
- **Nested structure recognition**: Based on indentation and ASCII braces
- **Operators**: `either`, `not`, `inside`, `pattern-regex`

### Pattern-Regex

PCRE expressions for exact matching:

```yaml
pattern-regex: "NEVER.*[—–-]|NEVER.*instead"
```

Named capturing groups for metavariables:

```yaml
pattern-regex: "(?P<KEYWORD>MUST|MUST NOT).*(?P<CONTEXT>—.*)"
```

### YAML Parsing

OpenGrep natively parses YAML, enabling frontmatter detection:

```yaml
rules:
  - id: paths-key-present
    languages: [yaml]
    pattern: |
      paths: $VALUE
```

## Limitations

- Metavariables capture only single words, not multi-word phrases
- Ellipsis spans maximum 10 lines
- No inline regex within patterns (use `pattern-regex` instead)
- Works best with short patterns on structured data
- Cannot assess semantic quality (actionability, completeness)

## Rule Type Classification Impact

### Deterministic (100% confidence with OpenGrep)

| Pattern | OpenGrep Detection |
|---------|-------------------|
| File/directory existence | `glob` + file check |
| YAML key presence | YAML language parser |
| Keyword count | `pattern-regex` with count |
| Heading structure | `pattern-regex: "^#{1,6} "` |
| Pattern + alternative | `pattern-regex: "NEVER.*—"` |

### Heuristic (80-95% confidence)

| Pattern | Limitation |
|---------|------------|
| @import detection | May miss custom pointer formats |
| Section heading names | Wording varies across projects |
| Style pattern detection | False positives possible |
| Table/list structure | Format variations |

### Semantic (requires LLM)

| Assessment | Why OpenGrep Can't Help |
|------------|------------------------|
| Instruction actionability | Subjective judgment |
| Philosophy vs instruction | Intent detection |
| Code block necessity | Context-dependent |
| Meaningful commits | Process quality |

## Rules Upgraded Based on Research

### Heuristic → Deterministic (9 rules)

| Rule | Detection Method |
|------|-----------------|
| S4 | Directory existence (.claude/rules/) |
| S5 | YAML frontmatter parse for "paths:" |
| C4 | `pattern-regex: "NEVER\|AVOID"` count |
| C5 | `pattern-regex: "SHOULD(?! NOT)"` detection |
| C7 | `pattern-regex: "IMPORTANT\|CRITICAL"` count |
| C10 | `pattern-regex: "NEVER.*[—–-]\|NEVER.*instead"` |
| G5 | YAML structure validation (quick_ref, contracts) |
| G6 | YAML structure validation (contracts, rules) |
| G8 | Workflow file existence check |

## Sources

- [OpenGrep GitHub](https://github.com/opengrep/opengrep)
- [Semgrep Generic Pattern Matching](https://semgrep.dev/docs/writing-rules/generic-pattern-matching)
- [Semgrep Pattern Syntax](https://semgrep.dev/docs/writing-rules/pattern-syntax)
- [OpenGrep Website](https://www.opengrep.dev/)
