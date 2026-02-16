## Architecture

- `src/` — application source code
- `src/api/` — REST endpoints (Express)
- `src/models/` — Prisma schema and DB access
- `src/components/` — React components
- `tests/` — unit and integration tests
- `docs/` — architecture decisions and API docs

The API layer calls models directly; no service layer.
