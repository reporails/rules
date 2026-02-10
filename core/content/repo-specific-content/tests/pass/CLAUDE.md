# MyApp

Our API uses the repository pattern in src/repos/. New endpoints must follow the existing UserRepo structure in src/repos/user.ts.

## Commands

- `pytest tests/ -v --cov=src` — run tests with coverage
- `npm run build` — production build via Dockerfile

## Structure

```
src/repos/   # Repository pattern implementations
src/api/     # Express route handlers
tests/unit/  # Unit tests matching src/ structure
```
