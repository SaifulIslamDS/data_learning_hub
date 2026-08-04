# Migration from Statistics Learning Hub v1.2.0 to Data Learning Hub v2.0.0

## Baseline

The repository's `v1.2.0` tag remains the recoverable Statistics Learning Hub release. Main is transformed into Data Learning Hub v2.

## Product changes

- broader Data Analytics identity
- Statistics becomes a foundation rather than the entire product
- new Data Analyst career route
- new Projects, Career Paths, and Curriculum areas
- tool curricula added without publishing incomplete lessons

## Source migration

The former curriculum and generator logic is separated into:

```text
content/platform/
content/statistics/
content/tracks/
content/datasets/
```

The generator imports these sources and creates the deployable site.

## URL compatibility

- `/catalog/` redirects to `/learn/`
- `/paths/` redirects to `/career-paths/`
- existing `/topics/<id>/` lesson URLs remain stable
- existing `/tools/<id>/` lab URLs remain stable

## Browser-state compatibility

When a `dlh-*` key is absent, the runtime copies a compatible value from `slh-*`.

Migrated categories include:

- theme
- language
- completed lessons
- bookmarks
- current profile where compatible

Legacy values remain untouched. Migration can run repeatedly without overwriting newer v2 state.

## Repository workflow

The project owner requested direct development on `main`. The v1.2.0 tag is the rollback point. For v2.0.0:

```powershell
git checkout main
git pull origin main
# replace repository contents with this release
npm test
npm run test:browser
git add .
git commit -m "feat: transform platform into Data Learning Hub v2"
git push origin main
git tag -a v2.0.0 -m "Data Learning Hub v2.0.0 — Architecture and Curriculum Foundation"
git push origin v2.0.0
```
