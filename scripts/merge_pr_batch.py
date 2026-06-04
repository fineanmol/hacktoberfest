#!/usr/bin/env python3
"""Apply open PR changes onto master (maintainer merge workflow)."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO = "fineanmol/hacktoberfest"
ROOT = Path(os.environ.get("HACKTOBERFEST_ROOT", Path(__file__).resolve().parents[1]))
CORE_EXACT = {
    "LICENSE",
    "CODE_OF_CONDUCT.md",
    "README.md",
    ".gitignore",
}
CORE_PREFIXES = (
    ".github/workflows/",
    "hacktoberfest-react/package.json",
    "hacktoberfest-react/vite.config.ts",
)

PLACEHOLDER = "#### Name: [Your Name](https://github.com/Oore2006)"


def run(*args: str, check: bool = True) -> str:
    r = subprocess.run(
        args, cwd=ROOT, capture_output=True, text=True, check=check
    )
    return r.stdout or ""


def gh_json(args: list[str]):
    import json

    r = subprocess.run(
        ["gh", *args, "-R", REPO],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(r.stdout)


def is_core(path: str) -> bool:
    if path in CORE_EXACT:
        return True
    return any(path.startswith(p) for p in CORE_PREFIXES)


def fetch_pr(num: int) -> str:
    ref = f"pr-{num}"
    run("git", "fetch", "origin", f"pull/{num}/head:{ref}", check=False)
    return ref


def changed_files(num: int, ref: str) -> list[str]:
    """Files introduced/changed on the PR branch since merge-base with master."""
    out = run(
        "git",
        "diff",
        "--name-only",
        "--diff-filter=ACMRT",
        f"origin/master...{ref}",
        check=False,
    )
    return [f.strip() for f in out.splitlines() if f.strip()]


def extract_contributing_blocks(diff_text: str) -> list[str]:
    """Pull added contributor sections from CONTRIBUTING.md diff."""
    blocks: list[str] = []
    current: list[str] = []
    in_contrib = False

    for line in diff_text.splitlines():
        if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
            if current and in_contrib:
                blocks.append("\n".join(current).strip())
                current = []
            in_contrib = "CONTRIBUTING.md" in line or (in_contrib and line.startswith("@@"))
            continue
        if not line.startswith("+") or line.startswith("+++"):
            if current and in_contrib and line.startswith("-") and line[1:].startswith("#### Name"):
                pass
            continue
        body = line[1:].strip()
        if body.startswith("- #### Name:"):
            body = body[2:].strip()
        if body.startswith("#### Name:"):
            if current:
                blocks.append("\n".join(current).strip())
            current = [body]
            in_contrib = True
        elif in_contrib and current:
            current.append(body)

    if current:
        blocks.append("\n".join(current).strip())
    return [b for b in blocks if b.startswith("#### Name:")]


def append_block(block: str) -> bool:
    path = ROOT / "CONTRIBUTING.md"
    content = path.read_text(encoding="utf-8")
    block = block.strip() + "\n\n"
    m = re.search(r"github\.com/([^/\)\s]+)", block, re.I)
    if not m:
        return False
    key = m.group(1).lower()
    if f"github.com/{key}" in content.lower():
        return False
    if PLACEHOLDER not in content:
        raise RuntimeError("CONTRIBUTING placeholder missing")
    path.write_text(content.replace(PLACEHOLDER, block + PLACEHOLDER, 1), encoding="utf-8")
    return True


def apply_pr(num: int) -> dict:
    ref = fetch_pr(num)
    files = changed_files(num, ref)
    if not files:
        return {"pr": num, "status": "skip", "reason": "no diff vs master"}

    non_core = [f for f in files if not is_core(f)]
    core_only = [f for f in files if is_core(f)]
    if not non_core:
        return {"pr": num, "status": "skip", "reason": f"core only: {core_only}"}

    applied_files: list[str] = []
    for f in non_core:
        if f == "CONTRIBUTING.md":
            continue
        r = subprocess.run(
            ["git", "checkout", ref, "--", f], cwd=ROOT, capture_output=True
        )
        if r.returncode == 0:
            applied_files.append(f)

    contrib_added = 0
    if "CONTRIBUTING.md" in files:
        diff = run(
            "git",
            "diff",
            f"origin/master...{ref}",
            "--",
            "CONTRIBUTING.md",
            check=False,
        )
        for block in extract_contributing_blocks(diff):
            if append_block(block):
                contrib_added += 1
        if contrib_added:
            applied_files.append("CONTRIBUTING.md")

    if not applied_files:
        return {"pr": num, "status": "skip", "reason": "nothing applied"}

    title = gh_json(["pr", "view", str(num), "--json", "title"])["title"]
    run("git", "add", "-A")
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=ROOT, capture_output=True
    )
    if staged.returncode == 0:
        return {"pr": num, "status": "skip", "reason": "empty staging area"}

    msg = f"Merge PR #{num}: {title}\n\nIntegrate contributor changes on master (2024 batch)."
    run("git", "commit", "-m", msg)
    return {
        "pr": num,
        "status": "committed",
        "files": applied_files,
        "contrib_blocks": contrib_added,
    }


def main():
    nums = [int(x) for x in sys.stdin.read().split() if x.strip()]
    results = []
    for num in nums:
        try:
            results.append(apply_pr(num))
            print(results[-1])
        except Exception as e:
            results.append({"pr": num, "status": "error", "reason": str(e)})
            print(results[-1])
    ok = sum(1 for r in results if r["status"] == "committed")
    print(f"\nDone: {ok}/{len(nums)} committed", file=sys.stderr)


if __name__ == "__main__":
    main()
