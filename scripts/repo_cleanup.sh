#!/usr/bin/env bash
# Remove Hacktoberfest PR cruft; keep core starter + deploy paths. Never touches .github/workflows/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

KEEP_ROOT=(
  README.md LICENSE CODE_OF_CONDUCT.md CONTRIBUTING.md
  pull_request_template.md .gitignore .mailmap
)

echo "Removing junk top-level directories..."
junk_dirs=(
  PROJECTS Python python Java JavaSolutions LeetcodeProblems
  "C++ Programs" C Cpp cpp cppcodes algorithms
  "PatternChalange(PYTHON)" "Programs (in txt format)"
  "CALCULATOR USING PYTHON" "CO2 Calculator" Chess-analyzer
  "Digital Clock" "DartCode x Flutter" "currency converter js"
  "login project" palindrome "snake game" hacktoberfest css
  C-Programs docker
)
for d in "${junk_dirs[@]}"; do
  [[ -e "$d" ]] && rm -rf "$d" && echo "  removed $d"
done

echo "Removing duplicate / stray markdown..."
for f in CONTRIBUTING2.md CONTRIBUTING12.md CONTRIBUTORS.md readme.md \
  "hacktoberfest_quick guide.md" Shivam.md; do
  [[ -f "$f" ]] && rm -f "$f" && echo "  removed $f"
done

echo "Removing stray root files (keep core docs only)..."
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  skip=0
  for k in "${KEEP_ROOT[@]}"; do
    [[ "$base" == "$k" ]] && skip=1 && break
  done
  [[ "$skip" -eq 1 ]] && continue
  rm -f "$f" && echo "  removed $base"
done < <(find "$ROOT" -maxdepth 1 -type f -print0)

echo "Removing maintainer merge automation from scripts/..."
rm -f scripts/merge_pr_*.py scripts/merge_*.sh scripts/land_pr_merge.py \
  scripts/refresh_*.sh 2>/dev/null || true
find scripts -maxdepth 1 -type f \( -name '*.exe' -o -name '*.class' -o -name 'tempCodeRunnerFile.*' \) -delete 2>/dev/null || true
rm -rf scripts/scripts scripts/number-guess-game-project-main 2>/dev/null || true

rm -f contributors/Mahi-Korrapati.md contributors/yeshuawm999.md 2>/dev/null || true

echo "Cleanup pass done."
