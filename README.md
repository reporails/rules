# Reporails Rules

Validation rules for AI agent instruction files (CLAUDE.md, .cursorrules, copilot-instructions.md).
Community-maintained.

**Version:** 0.2.2

### Pre-1.0 — moving fast, API still evolving, feedback welcome.

## Quickstart

```bash
npx @reporails/cli install
```

This registers the MCP server with Claude Code. Then ask Claude:
```
> What ails claude?
```

Or run directly without MCP:
```bash
npx @reporails/cli check
```

## What's here
```
core/
  structure/     # S1-S4: File organization, size limits
  content/       # C1-C5: Clarity, completeness
  efficiency/    # E1-E2: Code blocks, imports
  maintenance/   # M1-M4: Versioning, review

agents/
  claude/       # Claude Code specific rules (CLAUDE_M1, CLAUDE_S1-S2)
  codex/        # OpenAI Codex (no rules yet)

schemas/        # Rule and config schemas

docs/           # Detailed documentation
  capability-levels.md
  methodology-thresholds.md
  sources.yml
```

18 core rules. For 26 additional recommended rules, see [reporails/recommended](https://github.com/reporails/recommended).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Documentation

- [Capability Levels](docs/capability-levels.md) — L1-L6 capability model
- [Rule Schema](schemas/rule.schema.yml) — How rules are structured

## License

[CC BY 4.0](LICENSE)
