import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(process.cwd(), 'out');
const port = Number(process.env.PORT || 4173);
const host = '127.0.0.1';

const mime = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.txt': 'text/plain; charset=utf-8',
  '.wasm': 'application/wasm',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
};

function resolveRequest(urlPath) {
  const decoded = decodeURIComponent(urlPath.split('?')[0]);
  const relative = decoded.replace(/^\/+/, '');
  let file = path.resolve(root, relative);

  if (!file.startsWith(root)) return null;

  if (decoded.endsWith('/')) {
    file = path.join(file, 'index.html');
  } else if (!path.extname(file)) {
    const directoryIndex = path.join(file, 'index.html');
    if (fs.existsSync(directoryIndex)) file = directoryIndex;
  }

  return file;
}

const server = http.createServer((request, response) => {
  const file = resolveRequest(request.url || '/');

  if (!file || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
    response.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
    response.end('Not found');
    return;
  }

  response.writeHead(200, {
    'content-type': mime[path.extname(file).toLowerCase()] || 'application/octet-stream',
    'cache-control': 'no-store',
  });

  if (request.method === 'HEAD') {
    response.end();
    return;
  }

  fs.createReadStream(file).pipe(response);
});

server.listen(port, host, () => {
  console.log(`Data Learning Hub test server: http://${host}:${port}`);
});
