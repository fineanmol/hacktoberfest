#!/usr/bin/env python3
"""Merge Hacktoberfest2025 PRs: fineanmol stays first; new contributors append at end."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = "fineanmol/Hacktoberfest2025"
ROOT = Path(os.environ.get("HACKTOBERFEST_ROOT", Path(__file__).resolve().parents[1]))

CORE_EXACT = {
    "LICENSE",
    "CODE_OF_CONDUCT.md",
    "README.md",
    ".gitignore",
    "pull_request_template.md",
}
CORE_PREFIXES = (".github/workflows/", ".github/ISSUE_TEMPLATE/")
CONTRIBUTOR_FILES = (
    "contributors/contributorsList1.js",
    "contributors/contributorslist.js",
)
MAINTAINER_USER = "fineanmol"
YEAR_FROM = re.compile(r"Hacktoberfest20(2[0-4])", re.I)
YEAR_TO = "Hacktoberfest2025"
DISPLAY_YEAR_FROM = re.compile(r"Hacktoberfest 20(2[0-5])", re.I)
DISPLAY_YEAR_TO = "Hacktoberfest 2026"


def run(*args: str, check: bool = True) -> str:
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=check)
    return r.stdout or ""


def gh_run(args: list[str], *, attempts: int = 6) -> subprocess.CompletedProcess:
    for attempt in range(attempts):
        r = subprocess.run(
            ["gh", *args, "-R", REPO],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        err = (r.stderr or r.stdout or "").lower()
        if r.returncode == 0:
            return r
        if "rate limit" in err or "api rate limit" in err:
            wait = min(120, 15 * (attempt + 1))
            time.sleep(wait)
            continue
        break
    return r


def gh_json(args: list[str]):
    r = gh_run(args)
    if r.returncode != 0:
        raise subprocess.CalledProcessError(
            r.returncode, r.args, r.stdout, r.stderr
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
    out = run(
        "git",
        "diff",
        "--name-only",
        "--diff-filter=ACMRT",
        f"origin/master...{ref}",
        check=False,
    )
    return [f.strip() for f in out.splitlines() if f.strip()]


def destructive_diff(num: int, ref: str) -> str | None:
    """Reject PRs that delete repo scaffolding."""
    stat = run(
        "git",
        "diff",
        "--numstat",
        f"origin/master...{ref}",
        check=False,
    )
    for line in stat.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        add_s, del_s, path = parts[0], parts[1], parts[2].strip()
        if not is_core(path):
            continue
        try:
            deleted = int(del_s) if del_s != "-" else 0
            added = int(add_s) if add_s != "-" else 0
        except ValueError:
            continue
        if deleted > added + 5:
            return f"destructive on {path} (-{deleted}/+{added})"
    return None


def extract_js_contributor_blocks(diff_text: str) -> list[dict]:
    blocks: list[dict] = []
    chunk: list[str] = []
    in_block = False

    for line in diff_text.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        body = line[1:].rstrip()
        stripped = body.strip()
        if not in_block and stripped in ("{", "{,"):
            in_block = True
            chunk = [stripped]
            continue
        if in_block:
            chunk.append(stripped)
            if stripped in ("},", "}"):
                blocks.append(_parse_js_block("\n".join(chunk)))
                chunk = []
                in_block = False

    return [b for b in blocks if b.get("username")]


def _parse_js_block(text: str) -> dict:
    entry: dict = {}
    m = re.search(r'id:\s*(\d+)', text)
    if m:
        entry["id"] = int(m.group(1))
    m = re.search(r'fullname:\s*"([^"]*)"', text)
    if m:
        entry["fullname"] = m.group(1)
    m = re.search(r'username:\s*"([^"]*)"', text)
    if m:
        entry["username"] = m.group(1)
    return entry


def github_key(username: str) -> str | None:
    m = re.search(r"github\.com/([^/\s\"']+)", username, re.I)
    return m.group(1).lower() if m else None


def max_contributor_id(content: str) -> int:
    ids = [int(x) for x in re.findall(r"\bid:\s*(\d+)", content)]
    return max(ids) if ids else 1


def file_has_user(content: str, user: str) -> bool:
    return f"github.com/{user.lower()}" in content.lower()


def format_contributor(entry: dict, new_id: int) -> str:
    fullname = entry.get("fullname", "Contributor").replace('"', '\\"')
    username = entry.get("username", "").strip()
    return (
        f"  {{\n"
        f"    id: {new_id},\n"
        f"    fullname: \"{fullname}\",\n"
        f"    username: \"{username}\",\n"
        f"  }},"
    )


def append_contributor(path: Path, entry: dict) -> bool:
    content = path.read_text(encoding="utf-8")
    user = github_key(entry.get("username", ""))
    if not user:
        return False
    if user == MAINTAINER_USER.lower():
        return False
    if file_has_user(content, user):
        return False
    new_id = max_contributor_id(content) + 1
    block = format_contributor(entry, new_id)
    body = content.rstrip()
    if not body.endswith("];"):
        raise RuntimeError(f"unexpected contributors file shape: {path}")
    body = body[:-2].rstrip().rstrip(",").rstrip()
    content = body + ",\n" + block + "\n];\n"
    path.write_text(content, encoding="utf-8")
    return True


def ensure_maintainer_first(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    if re.search(
        r'id:\s*1,\s*fullname:\s*"Anmol Agarwal"[^}]+fineanmol',
        content,
        re.I | re.S,
    ):
        return
    raise RuntimeError(f"maintainer block missing or moved in {path}")


def bump_year_in_text(text: str) -> str:
    text = DISPLAY_YEAR_FROM.sub(DISPLAY_YEAR_TO, text)
    return YEAR_FROM.sub(YEAR_TO, text)


def apply_contributor_diff(path_str: str, diff_text: str) -> int:
    added = 0
    path = ROOT / path_str
    if not path.exists():
        return 0
    for entry in extract_js_contributor_blocks(diff_text):
        if append_contributor(path, entry):
            added += 1
            ensure_maintainer_first(path)
    return added


def apply_changes(num: int, ref: str) -> tuple[list[str], int, str | None]:
    if reason := destructive_diff(num, ref):
        return [], 0, f"skipped: {reason}"

    files = changed_files(num, ref)
    if not files:
        return [], 0, "no diff vs master"

    non_core = [f for f in files if not is_core(f)]
    if not non_core:
        return [], 0, f"core only: {[f for f in files if is_core(f)]}"

    applied: list[str] = []
    contrib = 0

    for f in non_core:
        if f in CONTRIBUTOR_FILES:
            diff = run(
                "git", "diff", f"origin/master...{ref}", "--", f, check=False
            )
            n = apply_contributor_diff(f, diff)
            if n:
                contrib += n
                applied.append(f)
            continue

        r = subprocess.run(
            ["git", "checkout", ref, "--", f], cwd=ROOT, capture_output=True
        )
        if r.returncode != 0:
            continue
        full = ROOT / f
        if full.is_file() and f.endswith((".html", ".js", ".md", ".css")):
            text = full.read_text(encoding="utf-8", errors="replace")
            updated = bump_year_in_text(text)
            if updated != text:
                full.write_text(updated, encoding="utf-8")
        applied.append(f)

    if contrib and not applied:
        applied = [f for f in non_core if f in CONTRIBUTOR_FILES]
    if not applied:
        return [], contrib, "nothing applied"
    return applied, contrib, None


def pr_meta(num: int) -> dict:
    return gh_json(
        [
            "pr",
            "view",
            str(num),
            "--json",
            "title,state,mergedAt,isDraft,headRefName,headRepositoryOwner,headRepository",
        ]
    )


def contributor_author(owner: str, repo_name: str, branch: str) -> tuple[str, str]:
    r = subprocess.run(
        ["gh", "api", f"repos/{owner}/{repo_name}/commits/{branch}", "--jq", ".commit.author"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    name, email = "Contributor", f"{owner}@users.noreply.github.com"
    if r.returncode == 0 and r.stdout.strip():
        try:
            a = json.loads(r.stdout)
            name = a.get("name") or name
            email = a.get("email") or email
        except json.JSONDecodeError:
            pass
    return name, email


def merge_pr(num: int) -> str:
    pr = pr_meta(num)
    if pr.get("mergedAt"):
        return "already_merged"

    if pr.get("isDraft"):
        subprocess.run(["gh", "pr", "ready", str(num), "-R", REPO], cwd=ROOT, capture_output=True)

    if pr["state"] == "CLOSED":
        subprocess.run(["gh", "pr", "reopen", str(num), "-R", REPO], cwd=ROOT, capture_output=True)

    owner = pr["headRepositoryOwner"]["login"]
    head_repo = pr.get("headRepository")
    repo_name = (head_repo or {}).get("name")
    branch = pr["headRefName"]
    title = pr["title"]
    fork_deleted = not repo_name
    if fork_deleted:
        author_name, author_email = owner, f"{owner}@users.noreply.github.com"
    else:
        author_name, author_email = contributor_author(owner, repo_name, branch)

    fetch = subprocess.run(
        ["git", "fetch", "origin", "master"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if fetch.returncode != 0:
        subprocess.run(["git", "remote", "update", "origin"], cwd=ROOT, check=False)
        subprocess.run(["git", "fetch", "origin", "master"], cwd=ROOT, check=True)
    local = f"merge-pr-{num}"
    subprocess.run(["git", "checkout", "-B", local, "origin/master"], cwd=ROOT, check=True)

    ref = fetch_pr(num)
    applied, contrib, skip = apply_changes(num, ref)

    if skip and (skip.startswith("skipped") or skip.startswith("core only")):
        subprocess.run(["git", "checkout", "-f", "master"], cwd=ROOT, check=False)
        return skip

    if skip == "nothing applied":
        subprocess.run(["git", "checkout", "-f", "master"], cwd=ROOT, check=False)
        return "skipped: nothing applied"

    def git_commit(msg: str, *, allow_empty: bool = False) -> None:
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = author_name
        env["GIT_AUTHOR_EMAIL"] = author_email
        env["GIT_COMMITTER_NAME"] = author_name
        env["GIT_COMMITTER_EMAIL"] = author_email
        cmd = ["git", "commit", "-m", msg]
        if allow_empty:
            cmd.insert(2, "--allow-empty")
        subprocess.run(cmd, cwd=ROOT, env=env, check=True)

    if applied:
        for f in applied:
            subprocess.run(["git", "add", "--", f], cwd=ROOT, check=True)
        staged = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=ROOT, capture_output=True
        )
        if staged.returncode != 0:
            git_commit(f"{title} (#{num})")
        else:
            git_commit(f"{title} (#{num})", allow_empty=True)
    else:
        git_commit(f"{title} (#{num})", allow_empty=True)

    def cherry_pick_to_master() -> str | None:
        head_sha = run("git", "rev-parse", local, check=True).strip()
        subprocess.run(["git", "checkout", "master"], cwd=ROOT, check=True)
        subprocess.run(["git", "reset", "--hard", "origin/master"], cwd=ROOT, check=True)
        cp = subprocess.run(
            ["git", "cherry-pick", head_sha],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if cp.returncode != 0:
            subprocess.run(["git", "cherry-pick", "--abort"], cwd=ROOT, check=False)
            return (cp.stderr or cp.stdout or "cherry-pick failed").strip()[:240]
        ps = subprocess.run(
            ["git", "push", "origin", "master"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if ps.returncode != 0:
            subprocess.run(["git", "reset", "--hard", "origin/master"], cwd=ROOT, check=False)
            return ps.stderr.strip()[:240]
        return None

    push_err = ""
    if fork_deleted:
        push_err = cherry_pick_to_master() or ""
        if push_err:
            return f"push_failed: {push_err}"
    else:
        remote = f"git@github.com:{owner}/{repo_name}.git"
        pushed = False
        for target in (branch, f"cursor-merge-{num}"):
            push = subprocess.run(
                ["git", "push", remote, f"{local}:{target}", "--force"],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            if push.returncode == 0:
                pushed = True
                break
            push_err = push.stderr.strip()[:240]
        if not pushed:
            err = cherry_pick_to_master()
            if err:
                return f"push_failed: {err}"

    merge_err = ""
    merged_ok = False
    for attempt in range(4):
        time.sleep(2 if attempt == 0 else 5)
        merge = gh_run(
            ["pr", "merge", str(num), "--merge", "--admin"],
            attempts=6,
        )
        if merge.returncode == 0:
            merged_ok = True
            break
        merge_err = (merge.stderr or merge.stdout or "").strip()[:240]
        if "rate limit" in merge_err.lower():
            time.sleep(60)
            continue
        if "Base branch was modified" not in merge_err:
            break
    if not merged_ok:
        return f"merge_failed: {merge_err}"

    subprocess.run(["git", "fetch", "origin", "master"], cwd=ROOT, check=False)
    subprocess.run(["git", "checkout", "-f", "master"], cwd=ROOT, check=False)
    subprocess.run(["git", "reset", "--hard", "origin/master"], cwd=ROOT, check=False)
    return "merged"


def main():
    delay = float(os.environ.get("MERGE_PR_DELAY", "2"))
    nums = [int(x) for x in sys.stdin.read().split() if x.strip()]
    ok = skip = fail = 0
    for i, num in enumerate(nums):
        if i > 0 and delay > 0:
            time.sleep(delay)
        try:
            status = merge_pr(num)
            print(f"#{num}: {status}", flush=True)
            if status in ("merged", "already_merged"):
                ok += 1
            elif status.startswith("skipped") or status.startswith("core only"):
                skip += 1
            else:
                fail += 1
        except subprocess.CalledProcessError as e:
            fail += 1
            err = (e.stderr or e.stdout or str(e))[:240]
            print(f"#{num}: error {err}", flush=True)
            if "rate limit" in err.lower():
                time.sleep(90)
    print(
        f"\nSummary: merged={ok} skipped={skip} failed={fail} total={len(nums)}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
