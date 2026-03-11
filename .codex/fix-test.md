# Fix Test Commands

Run the test file:

```bash
pytest -q test_defs_utils.py
```

Run a single test from the file:

```bash
pytest -q test_defs_utils.py -k palindrome
```

Rerun the test file after changes:

```bash
pytest -q test_defs_utils.py
```

Use Codex to fix failing tests and rerun them:

```bash
codex "Run pytest -q test_defs_utils.py. If any test fails, fix the failure, rerun pytest -q test_defs_utils.py, and stop when all tests pass."
```
