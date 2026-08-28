import { defineConfig, globalIgnores } from 'eslint/config';
import nextVitals from 'eslint-config-next/core-web-vitals';
import nextTypeScript from 'eslint-config-next/typescript';

export default defineConfig([
  ...nextVitals,
  ...nextTypeScript,
  {
    rules: {
      // The current compatibility shell intentionally uses static <a> links and
      // one synchronous bootstrap script. Tighten these when the native shell lands.
      '@next/next/no-html-link-for-pages': 'off',
      '@next/next/no-sync-scripts': 'off',
    },
  },
  globalIgnores([
    '.next/**',
    'out/**',
    'node_modules/**',
    'src/generated/**',
    'scripts/legacy/**',
    'public/**',
  ]),
]);
