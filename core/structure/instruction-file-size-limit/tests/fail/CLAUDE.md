# Acme Platform Monorepo

This is the main instruction file for the Acme Platform monorepo.
It contains all coding standards, deployment procedures, testing
requirements, security policies, and operational guidelines for
every service in the platform. All contributors must read and
follow every section of this document before submitting any code.

Last updated: 2026-01-15

Maintainers: platform-team@acme.io

## Commands

Run the full test suite before every commit:

```bash
npm run test:unit -- --coverage --verbose
npm run test:integration -- --timeout 30000
npm run test:e2e -- --headless --retries 2
npm run lint -- --fix --ext .ts,.tsx,.js,.jsx
npm run typecheck
npm run build -- --mode production
```

For individual services:

```bash
cd services/api-gateway && npm run test && npm run build
cd services/user-service && npm run test && npm run build
cd services/billing && npm run test && npm run build
cd services/notifications && npm run test && npm run build
```

Database commands:

```bash
npm run db:migrate -- --env development
npm run db:seed -- --env development
npm run db:reset -- --env test
```

## Project Structure

```
acme-platform/
  services/
    api-gateway/          # Express-based API gateway
      src/
        routes/
        middleware/
        validators/
      tests/
    user-service/         # User management microservice
      src/
        controllers/
        models/
        repositories/
      tests/
    billing/              # Stripe-integrated billing
      src/
        handlers/
        webhooks/
      tests/
    notifications/        # Email and push notifications
      src/
        providers/
        templates/
      tests/
  packages/
    shared-types/         # Shared TypeScript types
    shared-utils/         # Shared utility functions
    db-client/            # Database client wrapper
    logger/               # Structured logging package
  infrastructure/
    terraform/            # IaC definitions
    docker/               # Dockerfiles
    k8s/                  # Kubernetes manifests
  docs/                   # Documentation
```

## Code Style and Conventions

All code must follow these style rules without exception.

### Naming Conventions

- Use camelCase for variables and functions
- Use PascalCase for classes, interfaces, and type aliases
- Use UPPER_SNAKE_CASE for constants and environment variables
- Use kebab-case for file names and directory names
- Prefix interfaces with I (e.g., IUserRepository)
- Prefix type aliases with T (e.g., TUserResponse)
- Suffix abstract classes with Base (e.g., ServiceBase)

### Import Ordering

Always order imports in this exact sequence:

```typescript
// 1. Node built-ins
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

// 2. External dependencies
import express from 'express';
import { z } from 'zod';

// 3. Internal packages
import { logger } from '@acme/logger';
import { DbClient } from '@acme/db-client';

// 4. Relative imports
import { UserController } from './controllers/user-controller';
import { validateRequest } from './middleware/validate';
```

## API Patterns

Every API endpoint must follow this exact pattern:

```typescript
import { Router, Request, Response, NextFunction } from 'express';
import { z } from 'zod';
import { logger } from '@acme/logger';
import { AppError } from '../errors/app-error';

const requestSchema = z.object({
  body: z.object({
    name: z.string().min(1).max(255),
    email: z.string().email(),
    role: z.enum(['admin', 'user', 'viewer']),
  }),
  params: z.object({
    id: z.string().uuid(),
  }),
});

export const updateUser = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const validated = requestSchema.parse({
      body: req.body,
      params: req.params,
    });
    const result = await userService.update(
      validated.params.id,
      validated.body
    );
    logger.info('User updated', {
      userId: validated.params.id,
      fields: Object.keys(validated.body),
    });
    res.status(200).json({ success: true, data: result });
  } catch (error) {
    next(error);
  }
};
```

Every endpoint must validate input with Zod. Every endpoint must
use structured logging. Every endpoint must return a consistent
response envelope. These requirements are mandatory for all services.

## Database Conventions

We use PostgreSQL with Prisma ORM. All database access must go
through the repository pattern.

```typescript
export class UserRepository {
  constructor(private readonly db: PrismaClient) {}

  async findById(id: string): Promise<User | null> {
    return this.db.user.findUnique({
      where: { id },
      include: {
        profile: true,
        organization: true,
        roles: { include: { permissions: true } },
      },
    });
  }

  async findByEmail(email: string): Promise<User | null> {
    return this.db.user.findUnique({ where: { email } });
  }

  async create(data: CreateUserInput): Promise<User> {
    return this.db.user.create({
      data: { ...data, createdAt: new Date(), updatedAt: new Date() },
    });
  }
}
```

### Migration Rules

- Never modify existing migrations
- Always create a new migration for schema changes
- Name migrations descriptively: add-user-organization-relation
- Test migrations on a fresh database before committing
- Include both up and down migrations
- Never drop columns in production without a deprecation period

## Testing Requirements

All code must have tests. Minimum coverage is 80% for lines
and 75% for branches. These thresholds are enforced in CI.

### Unit Tests

Unit tests must be colocated with source files:

```typescript
import { describe, it, expect, vi } from 'vitest';
import { UserService } from './user-service';

describe('UserService', () => {
  describe('createUser', () => {
    it('should create a user with valid input', async () => {
      const mockRepo = {
        create: vi.fn().mockResolvedValue({
          id: 'user-1',
          name: 'Test User',
          email: 'test@example.com',
        }),
        findByEmail: vi.fn().mockResolvedValue(null),
      };
      const service = new UserService(mockRepo as any);
      const result = await service.createUser({
        name: 'Test User',
        email: 'test@example.com',
      });
      expect(result.id).toBe('user-1');
      expect(mockRepo.create).toHaveBeenCalledOnce();
    });

    it('should reject duplicate emails', async () => {
      const mockRepo = {
        findByEmail: vi.fn().mockResolvedValue({ id: 'existing' }),
      };
      const service = new UserService(mockRepo as any);
      await expect(
        service.createUser({ name: 'X', email: 'dup@example.com' })
      ).rejects.toThrow(/duplicate/i);
    });
  });
});
```

### Integration Tests

Integration tests must use the test database. Always seed data
in beforeEach and clean up in afterEach. Never rely on test ordering.

## Security Policies

### Authentication

All endpoints except /health and /docs require authentication.
Use the authMiddleware on every router:

```typescript
import { authMiddleware } from '../middleware/auth';
import { rbacMiddleware } from '../middleware/rbac';

const router = Router();
router.use(authMiddleware);

router.get('/admin/users', rbacMiddleware('admin'), listUsersHandler);
router.post(
  '/users/:id/deactivate',
  rbacMiddleware('admin', 'manager'),
  deactivateUserHandler
);
```

### Secrets Management

- Never hardcode secrets in source code
- Never commit .env files
- Use AWS Secrets Manager for production secrets
- Use .env.example to document required variables
- Rotate secrets every 90 days
- Never log secrets or tokens, even partially
- Never include secrets in error messages
- Never pass secrets as URL query parameters
- Never store secrets in localStorage or cookies
- All secrets must be loaded at startup, not on demand

## Deployment Procedures

Deployments go through three environments: staging, canary,
and production. Each must pass health checks before promotion.

```bash
# Deploy to staging
npm run deploy -- --env staging --service api-gateway
npm run healthcheck -- --env staging --timeout 60

# Promote to canary (10% traffic)
npm run deploy -- --env canary --service api-gateway
npm run healthcheck -- --env canary --timeout 120
npm run smoke-test -- --env canary

# Promote to production
npm run deploy -- --env production --service api-gateway
npm run healthcheck -- --env production --timeout 180
npm run smoke-test -- --env production
npm run notify -- --channel deployments --status success
```

### Rollback Procedures

If any health check fails, immediately roll back:

```bash
npm run rollback -- --env production --service api-gateway
npm run notify -- --channel incidents --status rollback
```

## Error Handling

All services must use the shared AppError class hierarchy.
Never throw plain Error objects. Never swallow errors silently.
Always include context in error messages. Always log errors with
structured metadata including requestId, userId, and service name.
Never expose internal error details to API consumers. Map all
internal errors to appropriate HTTP status codes. Use 400 for
validation errors, 401 for authentication, 403 for authorization,
404 for not found, and 500 for unexpected server errors.

```typescript
export class AppError extends Error {
  constructor(
    message: string,
