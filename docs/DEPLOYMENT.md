# Netlify Deployment — v2.2.0

## Validate before publishing

```powershell
npm run generate
npm test
npm run test:browser
```

## Commit to main

```powershell
git checkout main
git pull origin main
git add -A
git commit -m "feat: add complete Excel analytics tutorial"
git push origin main
```

## Netlify configuration

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

The repository contains generated HTML, CSS, JavaScript, datasets, and the practice workbook, so Netlify serves the root directly.

## Production URL

The placeholder origin is configured in `content/platform/config.py`. After Netlify assigns or confirms the final URL:

1. update `SITE["site_url"]`;
2. run `npm run generate`;
3. run `npm test` and `npm run test:browser`;
4. commit and push the regenerated metadata and sitemap.

## Release tag

After the production deployment is verified:

```powershell
git tag -a v2.2.0 -m "Data Learning Hub v2.2.0 — Complete Excel for Data Analytics Tutorial"
git push origin v2.2.0
```

## Rollback

Netlify can roll back to a previous deploy, and Git tags preserve the source baseline for each release.
