# Netlify Deployment — v2.6.0

## Settings

```text
Production branch: main
Base directory:    empty
Build command:     empty
Publish directory: .
```

Generated HTML and assets are committed to the repository, so Netlify does not need to run Python or npm during deployment.

## Before pushing

```powershell
npm run build:workflows
npm run generate
npm test
npm run test:browser
```

## Production checks

After Netlify deploys, verify:

1. `/tutorials/data-analytics-workflows/`
2. `/projects/`
3. `/projects/retail-sales-360/`
4. download one project package
5. complete one project phase and refresh the page
6. switch EN/BN and light/dark mode
7. run one SQL example
8. run one Python example

## Site URL

Set the final production origin in `content/platform/config.py`, regenerate, retest, and push before tagging the release.
