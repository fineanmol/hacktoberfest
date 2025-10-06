"""Demo script showing usage of the project's JSON helpers.

This script intentionally imports the original `json.py` (keeps it unchanged)
and also demonstrates the safer helpers from `json_utils.py`.
"""
from __future__ import annotations

import os
from pathlib import Path

# import the existing simple helpers (kept unchanged)
try:
    # Relative import if run as module
    from . import json as simple_json
except Exception:
    # Fallback when run as script
    import json as simple_json

from contributions.python import json_utils


def demo():
    base = Path(__file__).parent
    cfg = base / "demo_config.json"

    # Use the safe atomic saver
    data = {"project": "Hacktoberfest", "contributors": ["you"]}
    json_utils.save_json_atomic(data, str(cfg), make_backup=True)
    print("Saved demo_config.json with atomic saver (backup created if existed)")

    # Show safe load
    loaded = json_utils.load_json_safe(str(cfg))
    print("Loaded with load_json_safe:", loaded)

    # Also show original helper still works (original file writes to config.json)
    # We call it with a different filename to avoid overwriting any project files.
    simple_json.save_json({"name": "Demo"}, "config_demo.json")
    print("Wrote config_demo.json using existing simple helper")

    # Merge example (creates another temp file)
    other = base / "demo_other.json"
    json_utils.save_json_atomic({"extra": True}, str(other))
    merged = json_utils.merge_json_files([str(cfg), str(other)])
    print("Merged content:", merged)


if __name__ == "__main__":
    demo()
