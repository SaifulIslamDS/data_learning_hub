# Netlify Deployment — v2.3.0

## Settings

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

Generated files are committed to the repository and served directly.

## Browser SQL dependency

The CSP allows scripts and WASM requests from `https://cdn.jsdelivr.net`. The SQL playground loads pinned `sql.js@1.14.1` assets from that origin. All queries execute in browser memory; no backend is used.

## Release commands

```powershell
npm run generate
npm test
npm run test:browser

git add -A
git commit -m "feat: add complete SQL analytics tutorial"
git push origin main

git tag -a v2.3.0 -m "Data Learning Hub v2.3.0 — Complete SQL for Data Analytics Tutorial"
git push origin v2.3.0
```
