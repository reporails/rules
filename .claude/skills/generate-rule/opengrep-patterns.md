# OpenGrep Pattern Examples

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
# AND: all must match
patterns:
  - pattern-regex: "PATTERN1"
  - pattern-regex: "PATTERN2"

# OR: any can match
pattern-either:
  - pattern-regex: "PATTERN1"
  - pattern-regex: "PATTERN2"
```

## Template Variables

Use in paths (defined in `agents/{agent}/config.yml`):

- `{{instruction_files}}` — Main instruction files
- `{{rules_dir}}` — Rules directory
- `{{skills_dir}}` — Skills directory

## Source Selection

1. Read `docs/sources.yml`
2. For core rules: use `generic` section
3. For agent rules: use `generic` + agent section
4. Match source `description` to rule topic
5. Prefer `type: official` over `community`
