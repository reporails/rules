# Rule Template

Guide for contributors adding new rules to `core/` or `agents/{agent}/rules/`.

---

## Quick Start

Copy this template and fill in the fields:

```yaml
---
id: S1
title: Size Limits
category: structure
type: deterministic
checks:
  - id: S1-root-too-long
    name: Root file > 200 lines
    severity: critical
sources:
  - "https://docs.anthropic.com/en/docs/claude-code/best-practices"
see_also: [M7, C1]
---

# Size Limits

Prevents instruction degradation from token bloat.

## Why This Matters

One sentence explaining the impact of violating this rule.

## Pattern

**Good:** Root file under 100 lines with @imports
**Bad:** 300-line monolithic CLAUDE.md
```

---

## Rule ID Convention

| Scope | Pattern | Example |
|-------|---------|---------|
| Core | `{category}{number}` | `S1`, `C2`, `G2` |
| Agent | `{AGENT}_{category}{number}` | `CLAUDE_S1`, `COPILOT_E1` |
| Custom | `{PREFIX}_{category}{number}` | `ACME_S1`, `MYTEAM_G1` |

**Categories:**
- `S` = Structure
- `C` = Content
- `E` = Efficiency
- `G` = Governance
- `M` = Maintenance

**Agent prefixes (reserved):** CLAUDE, COPILOT, CODEX, CURSOR, WINDSURF, CLINE, AIDER, CONTINUE

---

## Rule Types

### Deterministic

OpenGrep decides. No LLM involved.

```yaml
type: deterministic
checks:
  - id: S1-root-too-long
    name: Root file > 200 lines
    severity: critical
```

**You must also create a matching `.yml` file** with OpenGrep patterns:

```yaml
# S1-size-limits.yml
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

### Semantic

OpenGrep runs first, LLM evaluates what patterns can't determine.

```yaml
type: semantic
checks:
  - id: G2-ownership-patterns
    name: Security ownership indicators
    severity: high
question: "Given what was found, are security rules properly owned?"
criteria:
  - Security rules have designated owners
  - Owners have relevant expertise
  - Review process exists for security changes
```

**Semantic rules also need a `.yml` file** — OpenGrep catches what it can, LLM fills gaps.

---

## Severity Levels

| Severity | When to use |
|----------|-------------|
| `critical` | Causes rework loops, major time waste |
| `high` | Causes clarification loops |
| `medium` | Causes brief confusion |
| `low` | Minor friction |

---

## File Structure

Each rule lives in its own directory with tests:

```
core/
  structure/
    S1-size-limits/
      S1-size-limits.md      # Rule definition (frontmatter + docs)
      S1-size-limits.yml     # OpenGrep patterns
      tests/
        fail.md              # Should trigger (true positive)
        pass.md              # Should not trigger (true negative)
```

**Directory:** `{id}-{slug}/`
**Files:** `{id}-{slug}.md` and `{id}-{slug}.yml`
**Tests:** `tests/fail.md` and `tests/pass.md`

**The `checks[].id` in `.md` must match `rules[].id` in `.yml`**

---

## Sources

Link to supporting references (official docs, articles, research):

```yaml
sources:
  - "https://docs.anthropic.com/en/docs/claude-code/best-practices"
  - "https://dev.to/author/relevant-article"
```

Good sources:
- Official agent documentation
- Well-researched articles
- Community best practices with evidence

---

## Checklist Before Submitting

- [ ] ID follows convention (category + number, or AGENT_category + number)
- [ ] ID doesn't collide with existing rules
- [ ] Frontmatter parses as valid YAML
- [ ] `.yml` file exists with matching check IDs
- [ ] Type is correct (deterministic or semantic)
- [ ] If semantic: includes `question` + `criteria`
- [ ] Sources are URLs, not numbers
- [ ] `see_also` references valid rule IDs
- [ ] Title is max 64 characters
- [ ] Body content is concise (< 40 lines)

---

## Full Schema Reference

See `schemas/rule.schema.yml` for the complete machine-readable schema.