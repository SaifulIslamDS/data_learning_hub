# Netlify Deployment — v2.5.0

## Netlify settings

```text
Production branch: main
Base directory:    empty
Build command:     empty
Publish directory: .
```

## Pre-deployment verification

```powershell
npm run generate
npm test
npm run test:browser
```

## Browser Python deployment requirements

`netlify.toml` permits:

- Version-pinned scripts and runtime files from `https://cdn.jsdelivr.net`
- WebAssembly compilation through `wasm-unsafe-eval`
- Runtime package and data connections to the same pinned CDN

Do not replace the pinned Pyodide URL with an unversioned or development path.

After deployment, open `/playground/python/`, run:

```python
print("Python runtime ready", 2 + 3)
```

Confirm that the output contains `Python runtime ready 5`. Then run one pandas chapter before tagging the release.

## Commit

```powershell
git checkout main
git pull origin main
git add -A
git commit -m "feat: add complete Python analytics tutorial"
git push origin main
```

## Tag after production verification

```powershell
git tag -a v2.5.0 -m "Data Learning Hub v2.5.0 — Complete Python for Data Analytics Tutorial"
git push origin v2.5.0
```

## Production URL

Update `content/platform/config.py` when the final Netlify URL changes, regenerate, test, and commit the generated canonical URLs and sitemap.
