# Codex Agent Demo Repo

This repository is a small Python demo used to show:

- local `pytest` test execution
- GitHub Actions CI for Python
- a Codex-assisted auto-fix workflow for failing tests
- simple reusable command notes in `.codex/`

## Repo Contents

- `test_defs_utils.py`: a small pytest test file with 3 string utility tests
- `.codex/fix-test.md`: quick commands for running or fixing the test file with Codex
- `.github/workflows/ci.yml`: runs tests on Python 3.10, 3.11, and 3.12
- `.github/workflows/codex-autofix.yml`: runs Codex against a failing test workflow and opens a PR with the fix
- `.github/workflows/grade.yml`: runs the test file and converts the result into a grade from 1 to 5
- `.github/workflows/lint.yml`: runs `ruff check .` and `ruff format --check .`
- `.github/workflows/deploy.yml`: placeholder deployment workflow
- `.github/workflows/release.yml`: example Python package release workflow

## Prerequisites

- Python 3.10+
- `pip`
- `pytest`
- Optional: Codex CLI if you want to use the Codex command in `.codex/fix-test.md`

## Local Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the test dependency:

```bash
python -m pip install --upgrade pip
python -m pip install pytest
```

## Testing Commands

Run the full test file:

```bash
pytest -q test_defs_utils.py
```

Run all detected tests in the repo:

```bash
pytest -q
```

Run a single test by name:

```bash
pytest -q test_defs_utils.py -k palindrome
```

Rerun tests after making a change:

```bash
pytest -q test_defs_utils.py
```

## Codex Command

If Codex CLI is installed, you can ask it to fix a failing test and rerun the suite:

```bash
codex "Run pytest -q test_defs_utils.py. If any test fails, fix the failure, rerun pytest -q test_defs_utils.py, and stop when all tests pass."
```

This command is also documented in `.codex/fix-test.md`.

## GitHub Actions

### CI

The `Python CI` workflow:

- runs on pushes to `main` and on pull requests
- tests the repo on Python 3.10, 3.11, and 3.12
- installs `pytest` automatically when no `requirements-dev.txt` file exists

### Codex Auto-Fix

The `Codex Auto-Fix` workflow:

- can be run manually with `workflow_dispatch`
- also triggers after the `Python CI` workflow completes with a failure
- checks out the failing commit
- runs Codex against `test_defs_utils.py`
- verifies the fix with `pytest -q test_defs_utils.py`
- opens a pull request with the generated fix

To use it in GitHub, add the repository secret `OPENAI_API_KEY`.

### Test Grade

The `Test Grade` workflow:

- runs on pushes to `main`, pull requests, and manual dispatch
- runs `pytest -q test_defs_utils.py --junitxml=pytest-report.xml`
- reads the JUnit report and calculates a score from `1` to `5`
- writes the grade, passed count, and total count to the workflow summary

Grade scale:

- `1`: all tests fail or no tests are counted
- `2` to `4`: some tests pass
- `5`: all tests pass

## Notes

- The current local test command was verified in this repo with `pytest -q test_defs_utils.py`.
- The release and deploy workflows are example scaffolds and may need more project packaging or deployment configuration before they are usable in a real project.
