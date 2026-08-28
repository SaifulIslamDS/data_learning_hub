# Testing — v2.7.3

## Quality model

v2.7.3 introduces layered validation.

### Static/source audits

```powershell
pnpm audit
```

Runs:

- migration integrity audit
- PWA audit
- TypeScript source syntax audit
- tutorial-first UI audit

### Unit/component tests

```powershell
pnpm test:unit
```

Vitest covers pure learning-rendering logic. React Testing Library covers native React components such as the offline recovery page.

### Lint and formatting

```powershell
pnpm lint
pnpm format:check
```

### Type checking

```powershell
pnpm typecheck
```

### Production build

```powershell
pnpm build
```

### Complete pre-browser gate

```powershell
pnpm check
```

This runs:

**lint → format check → typecheck → audits → unit tests → build**

## Browser tests

Install Chromium once:

```powershell
pnpm exec playwright install chromium
```

Then:

```powershell
pnpm test:e2e
```

`test:e2e` builds the static export and tests it through `scripts/serve-static.mjs`.

Browser coverage includes:

- representative tutorial route
- direct-teaching objective-card regression
- absence of Bangla toggle
- theme interaction
- primary navigation
- accessibility scan

## Accessibility

```powershell
pnpm test:a11y
```

The first automated gate blocks critical/serious structural WCAG issues on the offline recovery page. Color contrast remains a dedicated design-system review item for the native React shell.

## GitHub Actions

`.github/workflows/ci.yml` runs on pushes to `main` and pull requests.

The CI job:

1. installs pnpm/Node
2. performs a frozen-lockfile install
3. runs `pnpm check`
4. installs Chromium
5. runs Playwright + axe
6. uploads the Playwright report

## Release gate

Do not tag v2.7.3 until:

- `pnpm install` has refreshed and committed `pnpm-lock.yaml`
- `pnpm check` passes
- Playwright tests pass
- GitHub Actions passes
- Netlify production deploy succeeds
- service worker activates
- a visited tutorial works offline
- SQL and Python playgrounds run online
