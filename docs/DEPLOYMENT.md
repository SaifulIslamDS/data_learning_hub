# Deployment — Netlify

Production URL: https://datalearninghub.netlify.app/

## Configuration

```text
Build command:     pnpm build
Publish directory: out
Production branch: main
Node version:      22
pnpm version:      11.20.0
```

`netlify.toml` is included and should be used as the source of truth.

## First Next.js deployment

```powershell
corepack enable
corepack prepare pnpm@11.20.0 --activate
pnpm install
pnpm check

git add -A
git commit -m "feat: migrate Data Learning Hub to Next.js PWA"
git push origin main
```

After Netlify deploy, perform the PWA and browser checks in `docs/TESTING.md`. Then tag:

```powershell
git tag -a v2.7.0 -m "Data Learning Hub v2.7.0 — Next.js Application and PWA"
git push origin v2.7.0
```

## Rollback

The stable v2.6.0 tag remains the static-release rollback point. Netlify also supports instant rollback to the previous successful deploy.
