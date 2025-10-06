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

Notes

- This is an additive contribution — it doesn't modify or remove any existing files.
- The utilities are intentionally small and dependency-free.
