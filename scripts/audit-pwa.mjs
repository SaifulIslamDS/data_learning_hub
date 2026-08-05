import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const required = [
  'app/manifest.ts',
  'app/offline/page.tsx',
  'public/sw.js',
  'public/icons/icon-192.png',
  'public/icons/icon-512.png',
  'public/icons/maskable-512.png',
  'netlify.toml',
];
const errors = required.filter((file) => !fs.existsSync(path.join(root, file))).map((file) => `Missing ${file}`);
const sw = fs.readFileSync(path.join(root, 'public/sw.js'), 'utf8');
for (const token of ['install', 'activate', 'fetch', '/offline/', 'dlh-v2.7.0']) {
  if (!sw.includes(token)) errors.push(`Service worker missing token: ${token}`);
}
const syntax = spawnSync(process.execPath, ['--check', path.join(root, 'public/sw.js')], { encoding: 'utf8' });
if (syntax.status !== 0) errors.push(`Service worker syntax error: ${syntax.stderr || syntax.stdout}`);
const netlify = fs.readFileSync(path.join(root, 'netlify.toml'), 'utf8');
if (!netlify.includes('publish = "out"')) errors.push('Netlify publish directory is not out');
if (!netlify.includes('Service-Worker-Allowed')) errors.push('Netlify service worker header missing');
if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log('PWA manifest source, service worker, icons, offline page, and Netlify headers validated.');
