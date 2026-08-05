# PWA Guide

## Features

- Installable on supported desktop and mobile browsers
- Standalone display mode
- Offline fallback
- Cached visited pages and local assets
- Versioned cache invalidation
- Safe-area support for installed mobile mode

## Verification

After Netlify deploy:

1. Open DevTools → Application → Manifest.
2. Confirm name, icons, start URL, and standalone display.
3. Open Service Workers and confirm `/sw.js` is activated.
4. Visit two tutorial chapters.
5. Enable Offline mode and refresh one visited chapter.
6. Open `/offline/` for an uncached route fallback test.
7. Confirm Install App is offered in a supported browser.
8. Install, launch, and confirm theme/language/progress persist.

## Runtime limitation

SQL and Python execution engines are external WebAssembly/browser packages. Their first execution requires internet access. After the browser has cached those runtime files, they may continue to work offline, but that behavior depends on browser storage and cache eviction.
