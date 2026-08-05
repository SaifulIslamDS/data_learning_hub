# Architecture — v2.7.0

## Purpose

v2.7.0 converts the complete v2.6.0 static release into a Next.js App Router application without changing or dropping published content, URLs, local progress, exercises, labs, downloads, or browser runtimes.

## Runtime model

1. Next.js statically generates the complete route set through `app/[...slug]/page.tsx`.
2. `src/generated/routes.json` maps every URL to one page payload.
3. Each payload contains metadata, body data attributes, the original `<main>` markup, route scripts, and redirect scripts where applicable.
4. `LegacyPage` renders the content through React and loads the existing v2.6 browser modules in deterministic order.
5. The global App Router layout provides the shared header/footer mount points and PWA registration.

This compatibility layer makes the migration safe and immediately deployable. It is not the final desired native-React architecture.

## Why the bridge exists

The v2.6.0 release contains 549 HTML routes, 363 tutorial chapters, 1,089 chapter exercises, 108 statistics lessons, 20 interactive statistical labs, six portfolio projects, SQL WebAssembly practice, Python/Pyodide practice, bilingual state, and local progress. Rewriting every interaction simultaneously would create unacceptable regression risk.

## Next.js choices

- Next.js 16.2.10
- App Router
- TypeScript
- Static export (`output: "export"`)
- Static `generateStaticParams()` for all routes
- Metadata APIs for canonical URLs, robots, sitemap, and manifest
- No backend, API, authentication, or database

## PWA architecture

`public/sw.js` provides:

- Core shell precaching
- Network-first navigation requests
- Offline fallback
- Stale-while-revalidate local assets
- Runtime caching of visited CDN resources
- Versioned cache cleanup

## Future native migration order

1. React header/footer and search
2. Shared language/theme/progress context
3. Native tutorial course/chapter components
4. Native exercise and quiz components
5. Native project center
6. Native statistics labs
7. Remove generated HTML payload bridge

Every stage must preserve existing URLs and localStorage keys.
