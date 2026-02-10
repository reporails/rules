# Reporails Rules

Validation rules for AI agent instruction files (CLAUDE.md, .cursorrules, copilot-instructions.md).
Community-maintained.

**Version:** 0.3.1 <!-- source of truth: VERSION file -->

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
  structure/     # 12 rules: File organization, size limits, modularity
  content/       # 18 rules: Clarity, completeness, specificity

agents/
  claude/        # 10 rules: Claude Code specific
  codex/         # 7 rules: OpenAI Codex specific (CODEX:S:0001-0007)

schemas/         # Rule, agent, and config schemas
registry/        # Capabilities, levels, coordinate map
docs/            # Capability levels, sources
```

47 core rules. For additional recommended rules, see [reporails/recommended](https://github.com/reporails/recommended).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Documentation

- [Capability Levels](docs/capability-levels.md) — L1-L6 capability model
- [Rule Schema](schemas/rule.schema.yml) — How rules are structured

## License

[CC BY-SA 4.0](LICENSE)
