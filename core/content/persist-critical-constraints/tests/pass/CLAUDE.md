# MyApp

Production API service.

## Critical Constraints

NEVER modify the production database directly — use migrations only.
ALWAYS run `npm test` before pushing to ensure nothing is broken.
MUST use parameterized queries for all database operations.

## Commands

- `npm test` — run tests
