# Netlify Deployment

## Recommended repository

Push the project root to:

```text
https://github.com/SaifulIslamDS/statistics_learning_hub
```

## Initial deployment

1. Create or open the GitHub repository.
2. Commit the complete project at repository root.
3. Push to `main`.
4. In Netlify, select **Add new site → Import an existing project**.
5. Authorize GitHub and select `statistics_learning_hub`.
6. Leave **Base directory** empty.
7. Leave **Build command** empty.
8. `netlify.toml` sets **Publish directory** to `.`.
9. Deploy.

## Production-origin update

The generated metadata currently uses:

```text
https://statistics-learning-hub.netlify.app
```

After Netlify assigns the final production URL or after a custom domain is connected:

1. Update `SITE_URL` in `scripts/generate.py`.
2. Update the sitemap address in `robots.txt` if necessary.
3. Run:

```bash
npm run generate
npm test
```

4. Commit the regenerated HTML files and sitemap.

This keeps canonical URLs, Open Graph URLs, robots metadata, and sitemap entries aligned with the real production origin.

## Netlify configuration included

`netlify.toml` provides:

- static publish directory;
- custom 404 fallback;
- clickjacking, MIME-sniffing, referrer, permissions, and content-security headers;
- cache rules for assets and HTML.

## Post-deploy validation

Verify these production URLs:

```text
/
/catalog/
/paths/
/tools/
/glossary/
/about/
/topics/central-limit-theorem/
/tools/summary-statistics/
/a-route-that-does-not-exist
```

Then confirm:

- the missing route displays the custom 404 page and HTTP 404 status;
- all fonts and Chart.js load without CSP errors;
- EN/BN and theme preferences survive navigation;
- one representative calculator works on desktop and mobile;
- the Netlify deploy log reports no build failure;
- `sitemap.xml` and `robots.txt` use the production origin.

## Suggested Git commands

```bash
git init
git branch -M main
git add .
git commit -m "feat: launch Statistics Learning Hub v1.0.0"
git remote add origin https://github.com/SaifulIslamDS/statistics_learning_hub.git
git push -u origin main
git tag -a v1.0.0 -m "Statistics Learning Hub v1.0.0"
git push origin v1.0.0
```
