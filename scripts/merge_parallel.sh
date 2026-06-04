#!/usr/bin/env bash
# Run N parallel merge workers on disjoint PR number lists.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORKERS="${1:-4}"
LIST_FILE="${2:-/tmp/pr2023-remaining.txt}"

if [[ ! -f "$LIST_FILE" ]]; then
  echo "Missing PR list: $LIST_FILE" >&2
  exit 1
fi

# Stop single-worker batch to avoid git fights in the main clone
pkill -f "python3 scripts/merge_pr_proper.py" 2>/dev/null || true
sleep 2

mapfile -t ALL < <(sort -rn "$LIST_FILE")
total=${#ALL[@]}
echo "Splitting $total PRs across $WORKERS workers"

BASE="$REPO_ROOT/../hacktoberfest-worktrees"
mkdir -p "$BASE"

for ((i = 0; i < WORKERS; i++)); do
  wt="$BASE/worker-$i"
  chunk="/tmp/pr2023-worker-$i.txt"
  : > "$chunk"
  for ((j = i; j < total; j += WORKERS)); do
    echo "${ALL[j]}" >> "$chunk"
  done
  count=$(wc -l < "$chunk")
  echo "Worker $i: $count PRs -> $chunk"
  if [[ "$count" -eq 0 ]]; then
    continue
  fi
  if [[ -d "$wt" ]]; then
    git -C "$wt" fetch origin master
    git -C "$wt" reset --hard origin/master
  else
    git -C "$REPO_ROOT" worktree add -f "$wt" origin/master
  fi
  cp "$REPO_ROOT/scripts/merge_pr_proper.py" "$wt/scripts/" 2>/dev/null || mkdir -p "$wt/scripts" && cp "$REPO_ROOT/scripts/"*.py "$wt/scripts/"
  (
    export HACKTOBERFEST_ROOT="$wt"
    cd "$wt"
    tr '\n' ' ' < "$chunk" | python3 scripts/merge_pr_proper.py > "/tmp/merge2023-worker-$i.log" 2>&1
    echo "Worker $i done" >> "/tmp/merge2023-worker-$i.log"
  ) &
done

echo "Launched $WORKERS parallel workers. Logs: /tmp/merge2023-worker-*.log"
wait
echo "All workers finished."
