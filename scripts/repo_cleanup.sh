#!/usr/bin/env bash
# Remove Hacktoberfest PR cruft; keep core starter layout + react deploy paths.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "Removing junk top-level directories..."
junk_dirs=(
  "PROJECTS"
  "Python"
  "python"
  "Java"
  "JavaSolutions"
  "LeetcodeProblems"
  "C++ Programs"
  "C"
  "Cpp"
  "cpp"
  "cppcodes"
  "algorithms"
  "PatternChalange(PYTHON)"
  "Programs (in txt format)"
  "CALCULATOR USING PYTHON"
  "CO2 Calculator"
  "Chess-analyzer"
  "Digital Clock"
  "DartCode x Flutter"
  "currency converter js"
  "login project"
  "palindrome"
  "snake game"
  "hacktoberfest"
  "css"
)
for d in "${junk_dirs[@]}"; do
  [[ -e "$d" ]] && rm -rf "$d" && echo "  removed $d"
done

echo "Removing duplicate / stray markdown..."
for f in CONTRIBUTING2.md CONTRIBUTING12.md CONTRIBUTORS.md readme.md \
  "hacktoberfest_quick guide.md" Shivam.md; do
  [[ -f "$f" ]] && rm -f "$f" && echo "  removed $f"
done

echo "Removing root-level code and web junk (not in scripts/)..."
find "$ROOT" -maxdepth 1 -type f \( \
  -name '*.py' -o -name '*.cpp' -o -name '*.c' -o -name '*.java' -o \
  -name '*.js' -o -name '*.ts' -o -name '*.html' -o -name '*.css' -o \
  -name '*.kt' -o -name '*.exe' -o -name '*.class' -o -name '*.json' \
\) -delete

echo "Removing maintainer merge automation from scripts/..."
rm -f scripts/merge_pr_*.py scripts/land_pr_merge.py scripts/merge_*.sh \
  scripts/refresh_*.sh 2>/dev/null || true
find scripts -maxdepth 1 -type f \( -name '*.exe' -o -name 'tempCodeRunnerFile.*' \) -delete 2>/dev/null || true
rm -rf scripts/scripts scripts/number-guess-game-project-main 2>/dev/null || true

# Keep all .github/workflows/* (deploy, validate-scripts, auto-comment, auto-merge, etc.)
rm -f contributors/Mahi-Korrapati.md contributors/yeshuawm999.md 2>/dev/null || true

echo "Cleanup pass done."
