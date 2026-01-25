---
name: generate-rule
description: Generate a new rule with proper schema and OpenGrep patterns
---

# /generate-rule

Generate a new rule with proper schema and OpenGrep patterns.

## Usage

```
/generate-rule <id> <scope> <title> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S1, C1, CLAUDE_S1)
- `<scope>`: `core` or agent name (e.g., `claude`)
- `<title>`: Short title for the rule
- `--agent <name>`: Agent for template resolution during validation (default: `claude`)

## Examples

```
/generate-rule S1 core "Size Limits"
/generate-rule CLAUDE_S4 claude "Hierarchical Memory"
/generate-rule S1 core "Size Limits" --agent cursor
```

## Workflow

### Step 1: Gather Information

Before generating, collect:

1. **What it checks** — specific, measurable criteria
2. **Why it matters** — one sentence impact
3. **Type decision** — can OpenGrep fully decide?
4. **Good/Bad patterns** — concrete examples
5. **Sources** — find relevant URLs from `docs/sources.yml`

### Step 2: Determine Type

| Question | Answer | Type |
|----------|--------|------|
| Can OpenGrep fully decide? | Yes | `deterministic` |
| OpenGrep partial, LLM fills gaps? | Yes | `semantic` |

Refer to `.claude/rules/opengrep.md` for decision guide.

### Step 3: Generate Files

Create both .md and .yml files. For templates, see [templates.md](templates.md).

### Step 4: Resolve Templates & Validate

**Do not save files until all validations pass.**

1. Load agent config: `agents/{agent}/config.yml` (default: `claude`)
2. Replace `{{var}}` placeholders with values from `vars:` section
3. Run OpenGrep validation on resolved file:
   ```bash
   ~/.reporails/bin/opengrep scan --config {resolved.yml} .
   ```
4. Exit 0 or 1 = valid, Exit 2 or 7 = fix before saving

See [opengrep-patterns.md](opengrep-patterns.md) for validation details.

### Step 5: Save Files

| Scope | Location |
|-------|----------|
| core | `core/{category}/{id}-{slug}.md` and `.yml` |
| claude | `agents/claude/rules/{id}-{slug}.md` and `.yml` |

### Step 6: Update References

- [ ] Add to `see_also` in related rules if cross-referenced
- [ ] Update `capability-levels.md` if affects level detection
- [ ] Run `/add-changelog-entry`

## Reference Files

- [templates.md](templates.md) — Frontmatter and file templates
- [opengrep-patterns.md](opengrep-patterns.md) — OpenGrep pattern examples
- [common-mistakes.md](common-mistakes.md) — Common mistakes and fixes
