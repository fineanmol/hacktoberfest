#!/usr/bin/env node
// tools/validate-scripts.js
// Simple validator for files in /scripts
// Usage: node tools/validate-scripts.js

const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const scriptsDir = path.join(repoRoot, 'scripts');

if (!fs.existsSync(scriptsDir)) {
  console.log(`No scripts directory found at ${scriptsDir} — nothing to validate.`);
  process.exit(0);
}

// Allowed extensions (lowercase)
const allowedExts = new Set([
  '.js', '.ts', '.py', '.java', '.c', '.cpp', '.cs', '.rb', '.go', '.rs', '.php', '.swift', '.kt'
]);

// Filename must start with hello_world_ and then username, then dot and ext.
const filenameRegex = /^hello_world_[a-z0-9_-]+\.[a-z0-9]+$/i;

// Required header keys to be present in first 10 lines
const requiredHeaderKeys = ['LANGUAGE', 'ENV', 'AUTHOR', 'GITHUB'];

let errors = [];
let warnings = [];

function readFirstNLines(filePath, n = 10) {
  const content = fs.readFileSync(filePath, 'utf8');
  return content.split(/\r?\n/).slice(0, n).join('\n');
}

function validateFile(filePath, relPath) {
  const fileName = path.basename(filePath);
  // name check
  if (!filenameRegex.test(fileName)) {
    errors.push(`${relPath} — INVALID NAME: file should match 'hello_world_<username>.<ext>'`);
  }

  const ext = path.extname(fileName).toLowerCase();
  if (!ext) {
    errors.push(`${relPath} — MISSING EXTENSION`);
  } else if (!allowedExts.has(ext)) {
    errors.push(`${relPath} — UNSUPPORTED EXTENSION: ${ext}`);
  }

  // header check (first 10 lines)
  const headerChunk = readFirstNLines(filePath, 10);
  const missingKeys = requiredHeaderKeys.filter(k => {
    const regex = new RegExp(k + '\\s*:\\s*', 'i'); // case-insensitive match like "LANGUAGE:"
    return !regex.test(headerChunk);
  });
  if (missingKeys.length) {
    warnings.push(`${relPath} — missing header keys: ${missingKeys.join(', ')}`);
  }
}

function walk(dir, baseRel = '') {
  const ent = fs.readdirSync(dir, { withFileTypes: true });
  ent.forEach(d => {
    const full = path.join(dir, d.name);
    const rel = path.join(baseRel, d.name);
    if (d.isDirectory()) {
      walk(full, rel);
    } else if (d.isFile()) {
      validateFile(full, `scripts/${rel}`);
    }
  });
}

// Run
console.log(`Validating scripts in: ${scriptsDir}`);
walk(scriptsDir);

if (errors.length) {
  console.error(`\nERRORS (${errors.length}):`);
  errors.forEach(e => console.error('- ' + e));
}
if (warnings.length) {
  console.warn(`\nWARNINGS (${warnings.length}):`);
  warnings.forEach(w => console.warn('- ' + w));
}

if (errors.length) {
  console.error('\nValidation failed — please fix the errors above.');
  process.exit(1);
} else {
  console.log('\nValidation passed.');
  // Non-zero exit if you want to force fixing warnings — but we treat warnings as non-fatal
  process.exit(0);
}
