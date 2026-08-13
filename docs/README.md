# Data Learning Hub Documentation

This directory is the documentation source of truth for Data Learning Hub.

The root `README.md` remains the public repository entry point. Detailed architecture, product, roadmap, quality, release, migration, deployment, testing, and continuation documents belong here.

## Documentation policy

Use these naming rules for future versions:

- `RELEASE-NOTES-vX.Y.Z.md` — one release record for every tagged release
- `PROJECT-CONTINUATION-vX.Y.Z.md` — current project handoff/continuation context when needed
- `MIGRATION-vA.B-to-vC.D.md` — migration-specific records
- `ROADMAP.md` — the single current roadmap
- `PRODUCT-VISION.md` — stable product identity and long-term scope
- `CONTENT-STANDARDS.md` — non-negotiable learning-content and practice rules
- `ARCHITECTURE.md` — current technical architecture
- `TESTING.md` — validation and release testing
- `DEPLOYMENT.md` — deployment configuration and procedure
- `PWA.md` — PWA/offline behavior

Do not create roadmap copies such as `ROADMAP-final.md`, `ROADMAP-new.md`, or `ROADMAP-latest.md`. Update `ROADMAP.md` so there is one current source of truth.

## Core documents

### Product and learning system

- [Product Vision](PRODUCT-VISION.md)
- [Content Standards](CONTENT-STANDARDS.md)
- [Roadmap](ROADMAP.md)

### Engineering

- [Architecture](ARCHITECTURE.md)
- [Testing](TESTING.md)
- [Deployment](DEPLOYMENT.md)
- [PWA](PWA.md)
- [Migration v2.6 → v2.7](MIGRATION-v2.6-to-v2.7.md)

### Version history and continuation

- [Release Report — v2.7.0](RELEASE-REPORT-v2.7.0.md)
- [Release Notes — v2.7.1](RELEASE-NOTES-v2.7.1.md)
- [Project Continuation — v2.7.0](PROJECT-CONTINUATION-v2.7.0.md)
- [Project Continuation — v2.7.1](PROJECT-CONTINUATION-v2.7.1.md)

## Documentation rules

1. The repository root stays lean.
2. `README.md` explains what the project is and how to run it.
3. Version-specific implementation detail belongs in `docs/`.
4. Every tagged version gets a release note.
5. The roadmap is updated whenever sequencing or release scope changes.
6. Product principles and content standards must not silently change inside implementation work.
7. Architecture documentation must describe the current implementation, not a future design.
8. Release notes must distinguish delivered work from planned work.
9. Dummy or placeholder documentation must not be committed.
10. Broken documentation links should fail release review.
