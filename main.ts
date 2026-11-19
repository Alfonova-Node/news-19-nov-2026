// News image entry for make.fun bounty "news-image-20261119".
// The finished front page lives in this repository as entry.png (drawn
// by draw-entry.py from the verified news of 19 November 2026). This
// program only copies that image to the grader's output path, so the
// run needs no network and always writes the exact same bytes.
//
// Run locally:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1024 * 1024;

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

const bytes = readFileSync(source);
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG file");
}
if (bytes.length > MAX_BYTES) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(target, bytes);

// Read the copy back: the grader runs the program twice and requires
// byte-identical output, so prove here that what was written is exactly
// what the repository holds.
const written = readFileSync(target);
if (!written.equals(bytes)) {
  throw new Error("output differs from entry.png after writing");
}
console.log(`wrote ${target} (${bytes.length} bytes)`);
