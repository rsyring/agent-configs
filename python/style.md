# AGENTS.md

You MUST follow these rules when coding Python!

## General guidelines

- When ruff.toml is present, run `ruff check --fix` and `ruff format` after your code edits.
- Use double quotes for docstrings and to avoid escaping `'`
- Use single quotes everywhere else
- Wrap at 100. Add a `# noqa: E501` only where wrapping would break a URL, ARN, or similar token.
- When needed, use `from os import environ`
- Prefer modern Python with dataclasses and object oriented behaviors on those classes.
- Avoid creating a lot of top-level functions (i.e. function soup) when the behavior is closely
  associated with it's data and could be a method on a class.
- Before adding a new helper, function, or class, search for an existing project pattern and reuse
  or extend it. DO NOT create near-duplicate utilities.

## Module logger: Bind at module scope

Every module that logs defines `log` once at module level using `__name__`.

```python
log = logging.getLogger(__name__)
```

## Python version: Write for 3.12+

- Prefer typing, concrete types and `collections.abc` interfaces.
- Use PEP 604 unions (`X | None`), PEP 585 generics (`list[str]`, `dict[str, X]`, `type[X]`), `typing.Self`
- Avoid `Any` unless it is truly unavoidable.

```python
def list(self, name_prefix: str | None = None) -> dict[str, Queue]: ...
rec_cls: type[AWSRec]
```

## Paths: Use pathlib.Path

Construct filelsystem paths with `Path`:

```python
etc_dpath = Path('/etc/')
etc_mid_fpath = etc_dpath / 'machine-id'
machine_id = etc_mid_fpath.read_text() if etc_mid_fpath.exists() else ...
```

Path variable naming conventions:

- `_dpath`: suffix for directories
- `_fpath`: suffix for files

## Dataclasses: Prefer `@dataclass` with `field(default_factory=...)`

Use dataclasses for config, AWS record wrappers, and simple value objects. Default mutables with
`field(default_factory=...)`.

```python
@dataclass
class Config:
    env: str
    project_org: str
    aws_config: dict = field(default_factory=dict)
    policy_arns: list[str] = field(default_factory=list)
```

## Walrus: Assign-and-test in conditionals

Use `:=` when the tested value is also needed in the branch.

```python
if action_method := getattr(cls, action, None):
    return action_method(event, context)
```

## Abstract hooks: `raise NotImplementedError`

Declare extension points on a base class by raising `NotImplementedError`.

```python
def client_create(self) -> None:
    raise NotImplementedError
```

## Tests: Class-grouped with pytest fixtures

Group related tests in `TestX` classes with test methods and fixtures on the class.

```python
class TestLambda:
    @pytest.fixture(autouse=True)
    def fixture_example(self): ...

    def test_example(self): ...
```

## Mocking: Use `mock_patch_obj` / `mock_patch` NOT `monkeypatch`

Use `unittest.mock` instead of pytest's `monkeypatch` fixture. Patch with `testing.py` helpers; they
default to `autospec=True, spec_set=True`.

```python
@mock_patch_obj(config.utils, 'host_user')
def test_minimal_config_defaults(self, m_host_user):
    m_host_user.return_value = 'picard.science-station'
```

## Naming: Short, lowercased module names

Use short module names and shorten when a name shadows a builtin or keyword (`lamb.py` for lambda,
`exc.py` for exceptions, `logs.py` for logging). For shadowing parameters, suffix with `_`
(`from_`, `sqs_`).

```python
def take(from_: dict, *keys, strict=True): ...
```

## Comments: Only where intent is non-obvious

Match the surrounding density. Comment the "why", not the "what". Leave `TODO:` notes for known
follow-ups; do not leave commentary explaining edits.

```python
# Needed to create network interfaces and other vpc actions when it joins the vpc.
self.roles.attach_managed_policy(role_name, 'AWSLambdaVPCAccessExecutionRole')
```

## Keyword-only args: Put `*` before flags and disambiguators

Place a `*` before booleans, mode flags, and any argument whose meaning would be unclear
positionally. Callers must then pass them by name.

```python
def delete(self, *, force: bool): ...
def b3_sess(*, kind: str = 'fake'): ...
def push(self, image_name: str, *, tag_suffix: str | None = None): ...
```

## Exception chaining: Re-raise `from`

When translating an exception, preserve the cause with `from`.

```python
except self.lc.exceptions.InvalidParameterValueException as e:
    ...
    raise RuntimeError("Existing function is Zip type, can't update.") from e
```

DO NOT catch exceptions just to minimally wrap and/or re-reraise them, prefer to let the original
exception bubble up unless we need to take action due to the exception.

**Never swallow exceptions** with `pass` or just logging.

## Custom exceptions: Subclass and `pass`

Declare domain exceptions in `exc.py` as empty subclasses. Chain them into a project-specific
hierarchy when useful.

```python
class DeployAppException(Exception):
    pass
class DeployAppConfigMissing(DeployAppException):
    pass
```

## `Self` return: Type classmethod factories with `typing.Self`

A classmethod that returns `cls(...)` is annotated with `Self`.

```python
from typing import Self
@classmethod
def from_aws(cls, data: dict) -> Self:
    return cls(**cls.take_fields(data))
```

## Assertions: Use for internal invariants, not user input

Use `assert` to guard preconditions between cooperating internal code (mutually-exclusive args,
enum-like values, test-account safety). `assert` is preferrable when the error is due to a coding
mistake a developer will find/fix during QA.  Use exceptions for errors that can be triggered at
runtime in production.

```python
def policy_doc(*actions, resource=None, principal=None, effect='Allow', condition=None):
    assert resource or principal
    assert not (resource and principal)
```

## IMPORTANT! -- Control flow: Return early, do not nest

Handle the empty/missing/unsupported case first and `return`; keep the happy path at the outer
indentation level.

```python
def delete(self, ident: str, *list_args):
    rec = self.get(ident, *list_args)
    if not rec:
        return

    self.client_delete(rec, *list_args)
    self.clear_cache()
```

## Subprocesses: Use `sub_run`

Prefer utility function `sub_run` for subprocess code so output is captured and logged properly.

`subprocess.run()` / `Popen` takes `pathlib.Path` objects directly as arguments.  Don't wrap in
str().

## String formatting: Use f-strings

Always use f-strings for string interpolation. Do not use `.format()` or `%s` formatting.

## Print vs Logging: Keep output at the edge

Do not use `print()` or `click.echo()` unless explicitly writing a CLI command's output. Use the
module's `log` instance for library and runtime code. Keep input and output at the edge.

## Use furl for URL manipulations

https://github.com/gruns/furl

`uv add furl` then `from furl import furl; furl('https://...')`
