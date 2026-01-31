# Reporails Rules

Gathered rules for linting AI coding agent instruction files.
Aims to become community-maintained.

**Version:** 0.2.0

## Quickstart (requires [uvx](https://docs.astral.sh/uv/getting-started/installation/))
```
# Add the MCP and restart Claude
claude mcp add reporails -- uvx --from reporails-cli ails-mcp
```

Then ask Claude: 
```
❯ What ails claude?
```

## What's here
```
core/
  structure/    # S1-S5: File organization, size limits
  content/      # C1-C12: Clarity, completeness
  efficiency/   # E1-E8: Token optimization
  governance/   # G1-G7: Ownership, security
  maintenance/  # M1-M6: Versioning, review

agents/
  claude/       # Claude Code specific rules
  codex/        # OpenAI Codex specific rules

schemas/        # Rule and config schemas

docs/           # Detailed documentation
  capability-levels.md
  methodology-thresholds.md
  sources.yml
```

## How it works

These rules are automatically downloaded when you install the MCP/CLI:
```bash
uvx reporails-cli init
ails check .
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Documentation

- [Capability Levels](docs/capability-levels.md) — L1-L6 maturity model
- [Rule Schema](schemas/rule.schema.yml) — How rules are structured
- [Sources](docs/sources.yml) — Research and references

## License

[CC BY 4.0](LICENSE)
