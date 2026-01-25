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

### Copilot
```yaml
excludes:
  - S4   # Hierarchical Memory — single file only
  - S5   # Path-Scoped Rules — no rules directory
  - S6   # YAML Backbone — not supported
  - E2   # Session Rituals — no session concept
  - E4   # Memory Reference — no memory feature
  - E7   # Import Count — no imports
  - M7   # Rule Snippet Length — no rules directory
```

### Codex
```yaml
excludes:
  - S4   # Hierarchical Memory
  - S5   # Path-Scoped Rules
  - S6   # YAML Backbone
  - E2   # Session Rituals
  - E4   # Memory Reference
  - E7   # Import Count
  - M7   # Rule Snippet Length
```

### Cursor
```yaml
excludes:
  - S6   # YAML Backbone — uses different structure
  # Most Claude features supported
```

### Claude
```yaml
excludes: []
# Claude supports all core features
# But review overrides for severity tuning
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
| S1-root-too-long | Single-file agents may need higher limit |
| E2-no-ritual-section | May be WARNING not ERROR for some agents |
| C12-no-version | Some teams version differently |

## Adding New Agents

1. Research agent documentation
2. Fill in feature matrix row
3. Determine file patterns
4. Compile excludes based on unsupported features
5. Create config with `/manage-agent-config create {agent}`
6. Audit with `/manage-agent-config audit {agent}`
