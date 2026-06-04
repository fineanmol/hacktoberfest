#!/usr/bin/env node
// tools/validate-scripts.js
// Validate hello_world scripts. Pass specific paths, or validates all of scripts/ if none given.

const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const scriptsDir = path.join(repoRoot, 'scripts');

const allowedExts = new Set([
  '.js', '.ts', '.py', '.java', '.c', '.cpp', '.cs', '.rb', '.go', '.rs', '.php', '.swift', '.kt', '.dart',
]);

const filenameRegex = /^hello_world[_-][a-z0-9_-]+\.[a-z0-9]+$/i;

const requiredHeaderKeys = ['LANGUAGE', 'ENV', 'AUTHOR', 'GITHUB'];

const SKIP_DIR_PARTS = new Set(['__pycache__', '.vscode', 'node_modules']);

let errors = [];
let warnings = [];

function readFirstNLines(filePath, n = 10) {
  const content = fs.readFileSync(filePath, 'utf8');
  return content.split(/\r?\n/).slice(0, n).join('\n');
}

function validateFile(filePath, relPath) {
  const fileName = path.basename(filePath);
  if (!filenameRegex.test(fileName)) {
    errors.push(`${relPath} — INVALID NAME: file should match 'hello_world_<username>.<ext>'`);
  }

  const ext = path.extname(fileName).toLowerCase();
  if (!ext) {
    errors.push(`${relPath} — MISSING EXTENSION`);
  } else if (!allowedExts.has(ext)) {
    errors.push(`${relPath} — UNSUPPORTED EXTENSION: ${ext}`);
  }

  const headerChunk = readFirstNLines(filePath, 10);
  const missingKeys = requiredHeaderKeys.filter((k) => {
    const regex = new RegExp(k + '\\s*:\\s*', 'i');
    return !regex.test(headerChunk);
  });
  if (missingKeys.length) {
    warnings.push(`${relPath} — missing header keys: ${missingKeys.join(', ')}`);
  }
}

function walk(dir, baseRel = '') {
  const ent = fs.readdirSync(dir, { withFileTypes: true });
  ent.forEach((d) => {
    if (SKIP_DIR_PARTS.has(d.name)) return;
    const full = path.join(dir, d.name);
    const rel = path.join(baseRel, d.name);
    if (d.isDirectory()) {
      walk(full, rel);
    } else if (d.isFile()) {
      validateFile(full, `scripts/${rel}`);
    }
  });
}

function resolveInputs(argv) {
  return argv
    .map((p) => p.trim())
    .filter(Boolean)
    .map((p) => {
      const abs = path.isAbsolute(p) ? p : path.join(repoRoot, p);
      return { abs, rel: p.replace(/\\/g, '/') };
    })
    .filter(({ abs, rel }) => {
      if (!fs.existsSync(abs) || !fs.statSync(abs).isFile()) {
        warnings.push(`${rel} — skipped (not a file)`);
        return false;
      }
      return rel.startsWith('scripts/');
    });
}

const inputs = resolveInputs(process.argv.slice(2));

if (inputs.length) {
  console.log(`Validating ${inputs.length} changed script(s).`);
  inputs.forEach(({ abs, rel }) => validateFile(abs, rel));
} else if (fs.existsSync(scriptsDir)) {
  console.log(`Validating scripts in: ${scriptsDir}`);
  walk(scriptsDir);
} else {
  console.log(`No scripts directory found at ${scriptsDir} — nothing to validate.`);
  process.exit(0);
}

if (errors.length) {
  console.error(`\nERRORS (${errors.length}):`);
  errors.forEach((e) => console.error('- ' + e));
}
if (warnings.length) {
  console.warn(`\nWARNINGS (${warnings.length}):`);
  warnings.forEach((w) => console.warn('- ' + w));
}

const strict = process.env.VALIDATE_STRICT === 'true';

if (errors.length && !strict) {
  console.warn(
    `\nLENIENT MODE: ${errors.length} issue(s) logged as warnings (set VALIDATE_STRICT=true to fail CI).`
  );
  errors.forEach((e) => warnings.push(`[lenient] ${e}`));
  errors = [];
}

if (errors.length) {
  console.error('\nValidation failed — please fix the errors above.');
  process.exit(1);
}

console.log('\nValidation passed.');
process.exit(0);
