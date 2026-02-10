# Rule Body Template

This template defines the body format for rule.md files.
Structured fields from rule skeletons fill the placeholders below.

---

## Body Format (below YAML frontmatter)

```markdown
# {title}

{statement}

## Pass / Fail

**Pass:** {pass_example}
**Fail:** {fail_example}

## Limitations

{limitations}
```

## Semantic Rule Additions

For semantic rules, `question` and `criteria` are added to the YAML frontmatter
(machine-parseable for CLI handoff to the coding agent):

```yaml
question: "Given the matched content, are there vague or aspirational instructions?"
criteria:
  - Each instruction targets a specific observed behavior
  - No vague qualifiers like "properly" or "well"
```

These fields are NOT rendered into the body — they stay in frontmatter for the CLI
to extract and pass to the evaluating agent.

## Field Sources

| Placeholder | Skeleton field | Required |
|-------------|---------------|----------|
| `{title}` | `title` | Always |
| `{statement}` | `statement` | Always |
| `{pass_example}` | `pass_example` | Always |
| `{fail_example}` | `fail_example` | Always |
| `{limitations}` | `limitations` | Always |
| `question` | `question` | Semantic only |
| `criteria` | `criteria` | Semantic only |

## Type-Specific Guidance

### Mechanical rules
- `statement` asserts a structural property: "File X must exist", "File must be under N lines"
- `pass_example` / `fail_example` describe file system state, not content
- `limitations`: what structural checks miss (e.g., "cannot assess content quality")

### Deterministic rules
- `statement` asserts a pattern presence or absence
- `pass_example` / `fail_example` describe content patterns
- `limitations`: what patterns can't catch (e.g., "regex can't distinguish code blocks from prose")

### Semantic rules
- `statement` asserts a quality property
- `pass_example` / `fail_example` describe content characteristics
- `question` is the LLM evaluation prompt — must be answerable from the matched content
- `criteria` are independently assessable rubric items
- `limitations`: what even LLM evaluation can't reliably determine
