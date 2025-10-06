import json
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
