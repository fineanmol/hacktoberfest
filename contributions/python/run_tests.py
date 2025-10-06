"""Simple test runner for json_utils that doesn't require external deps.

This script runs a few assertions similar to the pytest tests and exits with code 0 on success.
"""
import json
import sys
from pathlib import Path

from contributions.python import json_utils


def test_deep_merge_dicts_simple():
    a = {"x": 1, "y": {"a": 1, "b": 2}}
    b = {"y": {"b": 3, "c": 4}, "z": 5}
    merged = json_utils.deep_merge_dicts(a, b)
    assert merged["x"] == 1
    assert merged["y"]["a"] == 1
    assert merged["y"]["b"] == 3
    assert merged["y"]["c"] == 4
    assert merged["z"] == 5


def test_deep_merge_json_files(tmp_path: Path):
    f1 = tmp_path / "a.json"
    f2 = tmp_path / "b.json"
    f1.write_text(json.dumps({"outer": {"val": 1, "inner": {"a": 1}}}))
    f2.write_text(json.dumps({"outer": {"inner": {"b": 2}}, "new": True}))

    merged = json_utils.deep_merge_json_files([str(f1), str(f2)])
    assert merged["outer"]["val"] == 1
    assert merged["outer"]["inner"]["a"] == 1
    assert merged["outer"]["inner"]["b"] == 2
    assert merged["new"] is True


def main():
    # run tests
    test_deep_merge_dicts_simple()
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        from pathlib import Path as P

        test_deep_merge_json_files(P(td))

    print('All tests passed')


if __name__ == '__main__':
    try:
        main()
    except AssertionError:
        print('Tests failed', file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print('Error running tests:', e, file=sys.stderr)
        sys.exit(3)
    sys.exit(0)
