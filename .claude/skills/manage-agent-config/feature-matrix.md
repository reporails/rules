# Agent Feature Matrix

Quick reference for agent capabilities and resulting configuration.

## Feature Support

| Feature | Claude | Copilot | Cursor | Codex | Windsurf |
|---------|--------|---------|--------|-------|----------|
| Main instruction file | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multiple instruction files | ✓ | ✗ | ✓ | ✗ | ✓ |
| Rules directory | ✓ | ✗ | ✓ | ✗ | ? |
| Skills directory | ✓ | ✗ | ✗ | ✗ | ✗ |
| Session rituals | ✓ | ✗ | ✓ | ✗ | ? |
| Memory/context | ✓ | ✗ | ✓ | ✗ | ✓ |
| Backbone/maps | ✓ | ✗ | ✗ | ✗ | ✗ |
| Path-scoped rules | ✓ | ✗ | ✓ | ✗ | ? |
| Import references | ✓ | ✗ | ✓ | ✗ | ? |

Legend: ✓ = supported, ✗ = not supported, ? = unknown/verify

## File Patterns

| Agent | Main File | Rules Directory |
|-------|-----------|-----------------|
| Claude | `**/CLAUDE.md` | `.claude/rules/**/*.md` |
| Copilot | `.github/copilot-instructions.md` | — |
| Cursor | `**/.cursorrules` | `.cursor/rules/**/*.md` |
| Codex | `**/AGENTS.md` | — |
| Windsurf | `**/.windsurfrules` | ? |

## Recommended Excludes

Core rules only. For recommended rule excludes, see reporails/recommended.

### Copilot
```yaml
excludes:
  - CORE:S:0007   # Decomposed instruction system — single file only
```

### Codex
```yaml
excludes:
  - CORE:S:0007   # Decomposed instruction system — single file only
```

### Cursor
```yaml
excludes: []
# Cursor supports most core features
```

### Claude
```yaml
excludes: []
# Claude supports all core features
```

## Override Considerations

### By Agent Type

**Single-file agents (Copilot, Codex):**
- CORE:S:0005 severity may need adjustment (longer files acceptable without @imports)

**Multi-file agents (Claude, Cursor):**
- Default severities generally appropriate
- Consider project-specific overrides

### By Rule

| Rule | Override consideration |
|------|----------------------|
| CORE:S:0005 | Single-file agents may need higher line limit |

## Adding New Agents

1. Research agent documentation
2. Fill in feature matrix row
3. Determine file patterns
4. Compile excludes based on unsupported features
5. Create config with `/manage-agent-config create {agent}`
6. Audit with `/manage-agent-config audit {agent}`