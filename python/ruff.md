# Ruff command sequence

A full ruff check should be:

```
ruff format && ruff check --fix --extend-fixable F401 && ruff format
```

To avoid erronous errors from the check that the format will fix.


## Ruff Conditions

ONLY run ruff automatically when an actual `ruff.toml` file exists in the project repo.

A `[ruff]` section in a `pyproject.toml` file DOES NOT COUNT.
