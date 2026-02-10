# MyApp

Data processing pipeline.

## Pitfalls

The ORM silently truncates strings over 255 chars — always validate length before saving.
Avoid using raw SQL outside the `queries/` directory.

## Commands

- `npm test` — run tests
