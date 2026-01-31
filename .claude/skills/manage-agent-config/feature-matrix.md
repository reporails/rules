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
  - E2   # Import Count — no imports (single file)
```

### Codex
```yaml
excludes:
  - E2   # Import Count — no imports (single file)
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
- S1 severity may need adjustment (longer files acceptable)
- S2 progressive disclosure less relevant

**Multi-file agents (Claude, Cursor):**
- Default severities generally appropriate
- Consider project-specific overrides

### By Rule

| Rule | Override consideration |
|------|----------------------|
| S1-size-limits | Single-file agents may need higher limit |
| C5-has-version-date | Some teams version differently |

## Adding New Agents

1. Research agent documentation
2. Fill in feature matrix row
3. Determine file patterns
4. Compile excludes based on unsupported features
5. Create config with `/manage-agent-config create {agent}`
6. Audit with `/manage-agent-config audit {agent}`
