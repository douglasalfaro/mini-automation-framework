# Mini Automation Framework (Page/Object)

This repo shows:
- UI tests with Playwright + pytest (Page/Object pattern)
- API tests with requests
- CLI runner (typer)
- Logging (loguru)
- Pre-commit hooks and CI

## Quickstart
1. Create venv and activate.
2. `pip install -e .[dev]`
3. `python -m playwright install`
4. Run tests: `pytest -q`
5. Run only UI: `pytest tests/ui -q`
6. Run only API: `pytest tests/api -q`

## CLI
- `python -m maf.core.runner ui`
- `python -m maf.core.runner api`
- `python -m maf.core.runner all`
