# MyApp

Real-time collaboration platform built on WebSockets and React.

## Tech Stack

- TypeScript, React, Node.js
- PostgreSQL, Redis
- Docker, Kubernetes

## Commands

- `npm test` — run unit tests
- `npm run e2e` — run end-to-end tests
- `npm run build` — production build
- `npm run lint` — check code style

## Structure

```
src/
  api/         # REST endpoints
  ws/          # WebSocket handlers
  models/      # Database models
  services/    # Business logic
tests/
  unit/        # Unit tests
  e2e/         # End-to-end tests
```

## Testing

Use Jest for unit tests. Name test files `*.test.ts`.
Run `npm test -- --watch` during development.

## Constraints

- Never commit .env files
- Always use parameterized queries
- Keep API responses under 100ms
