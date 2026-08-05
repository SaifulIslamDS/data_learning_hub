# Netlify Deployment — v2.4.0

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

## Commit

```powershell
git checkout main
git pull origin main
git add -A
git commit -m "feat: add complete Power BI analytics tutorial"
git push origin main
```

## Tag after production verification

```powershell
git tag -a v2.4.0 -m "Data Learning Hub v2.4.0 — Complete Power BI for Data Analytics Tutorial"
git push origin v2.4.0
```

## Production URL

Update `content/platform/config.py` when the final Netlify URL changes, regenerate, test, and commit the generated canonical URLs and sitemap.
