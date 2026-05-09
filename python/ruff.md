# Ruff command sequence

A full ruff check should be:

```
ruff format && ruff check --fix --extend-fixable F401 && ruff format
```

This avoids erroneous errors from the check that formatting will fix.

## Ruff Conditions

ONLY run ruff automatically when an actual `ruff.toml` file exists in the project repo.

A `[ruff]` section in a `pyproject.toml` file DOES NOT COUNT.
