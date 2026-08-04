# Netlify Deployment

## Settings

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

The generated HTML is committed to the repository. Netlify does not need Python, Node.js, or a build command.

## Production URL

The source currently uses:

```text
https://data-learning-hub.netlify.app
```

If the assigned Netlify URL or custom domain differs, update `site_url` in `content/platform/config.py`, then run:

```powershell
npm run generate
npm test
npm run test:browser
```

Commit the regenerated canonical URLs, sitemap, and robots file.

## Direct-main release workflow

```powershell
git checkout main
git pull origin main

npm run generate
npm test
npm run test:browser

git add -A
git commit -m "feat: add tutorial platform and Data Foundations course"
git push origin main

git tag -a v2.1.0 -m "Data Learning Hub v2.1.0 — Tutorial Platform Core and Complete Data Foundations"
git push origin v2.1.0
```

## Configuration

`netlify.toml` provides custom 404 handling, compatibility redirects, security headers, CSP, and cache-control rules.
