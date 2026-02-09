# MyApp

React application with established patterns.

## Patterns

New React components should follow this structure (see src/components/UserCard.tsx):

```tsx
export function UserCard({ user }: Props) {
  return <div className="card">{user.name}</div>;
}
```

## Commands

- `npm test` — run tests
