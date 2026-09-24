import { rm } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');

// Keep the comparison available in Astro dev, but omit its temporary page and
// full TTF source files from the static build that could be published later.
for (const directory of ['specimen', '_specimen']) {
  await rm(resolve(root, 'dist', directory), { recursive: true, force: true });
}
