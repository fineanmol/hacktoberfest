# JSON utilities

This folder contains a small utility module `json_utils.py` that complements the existing `json.py` helper in the project. It provides:

- Atomic save to prevent partial writes.
- Safe load with default values on errors.
- Pretty-print helper.
- A simple merge function for multiple JSON files.
- A tiny CLI for quick testing.

Quick examples

Save a sample file using the module:

```powershell
python -m contributions.python.json_utils save sample.json
```

Load and print a file:

```powershell
python -m contributions.python.json_utils load sample.json
```

Merge multiple files:

```powershell
python -m contributions.python.json_utils merge a.json b.json
```

Deep merge multiple files (recursive merge of nested dicts):

```powershell
python -m contributions.python.json_utils merge-deep a.json b.json
```

Run tests (requires pytest):

```powershell
pip install pytest
pytest contributions/python/tests -q
```

Run the bundled no-deps test runner (works without installing pytest):

```powershell
python contributions/python/run_tests.py
```

