# MyApp

React application with TypeScript.

## Style Conventions

Use camelCase for variables and functions. PascalCase for React components.
Prefix custom hooks with `use`. Name files after their default export.

```tsx
// Example component structure
export function UserProfile({ userId }: Props) {
  const user = useUser(userId);
  return <ProfileCard user={user} />;
}
```

## Commands

- `npm test` — run tests
