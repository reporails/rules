# MyApp

E-commerce platform built with Django.

## Commands

- `pytest tests/` — run tests

## API Patterns

When working on API files, use Django REST Framework serializers.
For authentication files, always use JWT tokens with 1-hour expiry.
In the payments directory, use Stripe SDK v3 with idempotency keys.
