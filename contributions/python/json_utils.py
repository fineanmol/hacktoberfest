"""Small JSON utilities to complement the existing `json.py` helper.

This module intentionally does not remove or change existing files.

Features:
- atomic save (writes to a temp file then replaces) to avoid partial writes
- safe load with default value on error
- pretty-print helper
- simple merge function for multiple JSON files
- small CLI for quick operations
"""
from __future__ import annotations

import json
import os
import shutil
import tempfile
from typing import Any, Dict, Iterable, Optional


def save_json_atomic(data: Any, filename: str, *, indent: int = 2, encoding: str = "utf-8", make_backup: bool = False) -> None:
    """Save `data` to `filename` atomically.

    Writes to a temp file on the same filesystem and renames it over the target.
    If `make_backup` is True and the target exists, a `.bak` copy will be created.
    """
    dir_name = os.path.dirname(os.path.abspath(filename)) or "."
    fd, tmp_path = tempfile.mkstemp(prefix=".tmp-json-", dir=dir_name)
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        if make_backup and os.path.exists(filename):
            bak = filename + ".bak"
            shutil.copy2(filename, bak)
        os.replace(tmp_path, filename)
    except Exception:
        # Ensure temp file is removed on failure
        try:
            os.remove(tmp_path)
        except Exception:
            pass
        raise


def load_json_safe(filename: str, default: Optional[Any] = None, *, encoding: str = "utf-8") -> Any:
    """Load JSON from `filename` returning `default` on any read/parse error.

    By default `default` is an empty dict when not provided.
    """
    if default is None:
        default = {}
    try:
        with open(filename, "r", encoding=encoding) as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        # Return default when file is invalid JSON
        return default
    except Exception:
        return default


def pretty_print_json(data: Any, *, indent: int = 2) -> str:
    """Return a pretty-printed JSON string for `data`."""
    return json.dumps(data, indent=indent, ensure_ascii=False)


def merge_json_files(file_paths: Iterable[str]) -> Dict[str, Any]:
    """Merge multiple JSON files into a single dictionary.

    Later files override keys from earlier files. This is a shallow merge (dict keys only).
    """
    merged: Dict[str, Any] = {}
    for p in file_paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                merged.update(data)
        except Exception:
            # Skip files we can't read/parse
            continue
    return merged


def deep_merge_dicts(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dicts, returning a new dict.

    - If a key exists in both and both values are dicts, merge recursively.
    - Otherwise, the value from `b` overrides `a`.
    Lists and non-dict values are replaced by the value from `b`.
    """
    result: Dict[str, Any] = dict(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge_dicts(result[k], v)
        else:
            result[k] = v
    return result


def deep_merge_json_files(file_paths: Iterable[str]) -> Dict[str, Any]:
    """Deep merge multiple JSON files into a single dictionary.

    Later files override/merge into earlier ones using `deep_merge_dicts`.
    Non-dict JSON roots are ignored.
    """
    accumulated: Dict[str, Any] = {}
    for p in file_paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                accumulated = deep_merge_dicts(accumulated, data)
        except Exception:
            continue
    return accumulated


__all__ = [
    "save_json_atomic",
    "load_json_safe",
    "pretty_print_json",
    "merge_json_files",
    "deep_merge_dicts",
    "deep_merge_json_files",
]


if __name__ == "__main__":
    # Minimal CLI for quick testing: save or load or merge
    import argparse

    parser = argparse.ArgumentParser(prog="json_utils", description="Simple JSON utility CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_save = sub.add_parser("save", help="Save sample JSON to a file")
    p_save.add_argument("file")

    p_load = sub.add_parser("load", help="Load JSON from a file and print it")
    p_load.add_argument("file")

    p_merge = sub.add_parser("merge", help="Merge multiple JSON files and print result")
    p_merge.add_argument("files", nargs="+")
    p_merge_deep = sub.add_parser("merge-deep", help="Deep merge multiple JSON files and print result")
    p_merge_deep.add_argument("files", nargs="+")

    args = parser.parse_args()
    if args.cmd == "save":
        sample = {"name": "contributor", "tasks": []}
        save_json_atomic(sample, args.file)
        print(f"Saved sample JSON to {args.file}")
    elif args.cmd == "load":
        print(load_json_safe(args.file))
    elif args.cmd == "merge":
        print(pretty_print_json(merge_json_files(args.files)))
    elif args.cmd == "merge-deep":
        print(pretty_print_json(deep_merge_json_files(args.files)))
    else:
        parser.print_help()
