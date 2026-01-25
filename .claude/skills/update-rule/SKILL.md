---
name: update-rule
description: Update an existing rule based on user intent
---

# /update-rule

Update an existing rule's OpenGrep patterns based on user instruction.

## Usage

```
/update-rule <id> <instruction> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S6, C1, CLAUDE_S4)
- `<instruction>`: What to change (e.g., "fix invalid pattern", "more aggressive")
- `--agent <name>`: Agent name for template resolution (default: `claude`)

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

### Step 4: Resolve Template Variables

Before validation, replace `{{var}}` placeholders with values from agent config.

1. Read agent config: `agents/{agent}/config.yml` (default: `claude`)
2. Extract `vars:` section
3. Replace in .yml file:
   - `{{instruction_files}}` → glob patterns from config
   - `{{rules_dir}}` → rules directory path
   - `{{skills_dir}}` → skills directory path

**Example resolution (claude agent):**
```yaml
# Before (template)
paths:
  include:
    - "{{instruction_files}}"

# After (resolved)
paths:
  include:
    - "**/CLAUDE.md"
    - ".claude/rules/**/*.md"
```

### Step 5: Validate Before Saving

```bash
~/.reporails/bin/opengrep scan --config {resolved.yml} .
```

Exit codes:
- 0 or 1 = valid (0 = no matches, 1 = matches found)
- 2 = syntax error — fix before saving
- 7 = no runnable patterns — add positive pattern

See [validation.md](validation.md) for details.

### Step 6: Check Conflicts

- Rule ID must be unique
- Check IDs must not collide with other rules
- Run full validation if needed

### Step 7: Save

- Write updated .yml (with original `{{var}}` templates, NOT resolved values)
- Update .md if checks changed
- Report what changed

**Important:** Save files with template variables intact. Resolution is only for validation.

## Reference Files

- [validation.md](validation.md) — OpenGrep validation rules
- [common-fixes.md](common-fixes.md) — Pattern fix reference
