---
name: update-rule
description: Update an existing rule based on user intent
---

# /update-rule

Update an existing rule's OpenGrep patterns based on user instruction.

## Usage

```
/update-rule <id> <instruction>
```

- `<id>`: Rule ID (e.g., S6, C1, CLAUDE_S4)
- `<instruction>`: What to change (e.g., "fix invalid pattern", "more aggressive")

## Workflow

### Step 1: Locate Rule Files

```
Core rules:    core/{category}/{ID}-*.md and .yml
Agent rules:   agents/{agent}/rules/{ID}-*.md and .yml
```

### Step 2: Read Current State

Parse from .md frontmatter:
- id, title, type, category
- checks[] with severity
- question + criteria (if semantic)

Parse from .yml:
- Pattern type (pattern-regex, pattern, patterns)
- Current detection logic

### Step 3: Apply Update

Based on user instruction:
- Modify .yml patterns
- Keep .md in sync if checks change

**NEVER change:**
- Rule ID (e.g., S6 stays S6)
- Filenames (e.g., S6-yaml-backbone.yml stays S6-yaml-backbone.yml)
- Category or type

### Step 4: Validate Before Saving

```bash
~/.reporails/bin/opengrep scan --config {new.yml} .
```

Exit codes:
- 0 or 1 = valid (0 = no matches, 1 = matches found)
- 2 = syntax error — fix before saving
- 7 = no runnable patterns — add positive pattern

See [validation.md](validation.md) for details.

### Step 5: Check Conflicts

- Rule ID must be unique
- Check IDs must not collide with other rules
- Run full validation if needed

### Step 6: Save

- Write updated .yml
- Update .md if checks changed
- Report what changed

## Reference Files

- [validation.md](validation.md) — OpenGrep validation rules
- [common-fixes.md](common-fixes.md) — Pattern fix reference
