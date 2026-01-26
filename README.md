# Reporails Rules

Community-maintained rules for linting AI coding agent instruction files.

**Version:** 0.0.1

## Quickstart (requires [uvx](https://docs.astral.sh/uv/getting-started/installation/))
```
# Add the MCP and restart Claude
claude mcp add reporails -- uvx --from reporails-cli ails-mcp
```

## What's here
```
core/
  structure/    # S1-S7: File organization, size limits
  content/      # C1-C12: Clarity, completeness
  efficiency/   # E1-E8: Token optimization
  governance/   # G1-G8: Ownership, security
  maintenance/  # M1-M7: Versioning, review

agents/
  claude/       # Claude Code specific rules

schemas/        # Rule and config schemas

docs/           # Detailed documentation
  capability-levels.md
  methodology-thresholds.md
  sources.yml
```

## Usage

These rules are automatically downloaded when you install the CLI:
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
