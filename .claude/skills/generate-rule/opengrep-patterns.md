# OpenGrep Pattern Examples

## Requirements

- Every rule MUST have a positive pattern (`pattern-regex` or `pattern`)
- Use `pattern-not-regex` only to filter false positives from a positive pattern
- Core rules use only `{{instruction_files}}` — agent vars go in agent rules

## Line Count Detection

```yaml
pattern-regex: "(?s)(?:[^\\n]*\\n){N,}"  # N+ lines
```

## Keyword Presence

```yaml
pattern-regex: "KEYWORD"
pattern-regex: "KEYWORD1|KEYWORD2"  # OR
```

## Keyword with Context

```yaml
pattern-regex: "NEVER.*[—–-]|NEVER.*instead"  # NEVER + alternative
```

## Heading Detection

```yaml
pattern-regex: "^#{1,6} "  # Any heading
pattern-regex: "^## "      # H2 specifically
```

## Section Detection

```yaml
pattern-regex: "(?i)^##?\\s*(commands?|scripts?)"  # Commands section
```

## Code Block Detection

```yaml
pattern-regex: "```[^\\n]*\\n(?:[^\\n]*\\n){10,}```"  # 10+ line blocks
```

## YAML Frontmatter

```yaml
languages: [yaml]
pattern: |
  paths: $VALUE
```

## Instruction Patterns

```yaml
pattern-regex: "(?i)(read|reading).*(strategy|purpose)"  # Reading strategy
pattern-regex: "(?i)files_with_matches|head_limit"       # Grep efficiency
```

## Combining Patterns

```yaml
# AND: all must match (first MUST be positive)
patterns:
  - pattern-regex: "POSITIVE"
  - pattern-not-regex: "EXCLUDE"

# OR: any can match
pattern-either:
  - pattern-regex: "OPTION1"
  - pattern-regex: "OPTION2"
```

## Absence Detection

To detect missing content, combine positive + negative patterns:

```yaml
patterns:
  - pattern-regex: "^#"              # Match markdown files
  - pattern-not-regex: "REQUIRED"    # Flag if REQUIRED absent
```

## Template Variables

| Variable | Use in | Description |
|----------|--------|-------------|
| `{{instruction_files}}` | Core + agent | Main instruction files |
| `{{rules_dir}}` | Agent only | Rules directory |
| `{{skills_dir}}` | Agent only | Skills directory |

Core rules must only use `{{instruction_files}}`.

## Source Selection

1. Read `docs/sources.yml`
2. For core rules: use `generic` section
3. For agent rules: use `generic` + agent section
4. Match source `description` to rule topic
5. Prefer `type: official` over `community`
