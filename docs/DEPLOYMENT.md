# Netlify Deployment

## Repository

The current GitHub repository can remain:

```text
https://github.com/SaifulIslamDS/statistics_learning_hub
```

The product displayed to learners is Data Learning Hub. Repository renaming is optional and not required for v2.0.0.

## Netlify settings

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

Generated HTML is committed, so deployment needs no build command.

## Configuration

`netlify.toml` provides:

- custom 404 behavior
- compatibility redirects
- security headers and CSP
- cache-control rules

## Production origin

The source currently uses:

```text
https://data-learning-hub.netlify.app
```

When the final Netlify site name or custom domain differs, edit:

```text
content/platform/config.py
```

Then regenerate and validate:

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
npm test
npm run test:browser
git add .
git commit -m "feat: transform platform into Data Learning Hub v2"
git push origin main
git tag -a v2.0.0 -m "Data Learning Hub v2.0.0 — Architecture and Curriculum Foundation"
git push origin v2.0.0
```

Netlify should deploy automatically from `main`.
