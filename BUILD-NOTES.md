# v2.7.2 Build Notes

The v2.7.2 implementation bundle is ready.

## Current GitHub blocker

The connected GitHub app can read the public repository but the repository is not present in the app's installed-repository list, so GitHub rejects content writes with:

`403 Resource not accessible by integration`

This is an installation/OAuth repository-access issue, not a code issue.

## Apply locally

Place these files in the repository root:

- `apply_v272.py`
- `ROADMAP-LOCKED-v2.7.2.md`

Then run:

```bash
python apply_v272.py
pnpm install
pnpm check
```

## Browser verification

1. Open a Data Foundations tutorial chapter.
2. Confirm **START HERE / What you will learn** is gone.
3. Confirm **Objectives** is gone from jump navigation.
4. Confirm EN/BN switch is gone.
5. Confirm theme still works.
6. Confirm Mark complete still works.
7. Confirm exercises work.
8. Confirm search works.
9. Confirm SQL/Python playgrounds execute.
10. Confirm a visited tutorial page works offline.

## Commit only after validation

```bash
git add .
git commit -m "release: v2.7.2 tutorial-first alignment"
git tag v2.7.2
git push origin main --tags
```
