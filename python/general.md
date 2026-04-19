# Python General Instructions

## Python Style

We want modern Python style with a preference for dataclasses and object oriented behaviors on those classes when warranted.

Avoid creating a lot of top-level functions when the logic is associated with it's data and should be on the class.


## Exception catching

Only catch exceptions when you have something meaningful to do with them.  DO NOT catch them just
to minimally wrap them or add a trivial message and re-throw.  We PREFER letting the original
exception surface.

## Filesystem paths

Use pathlib.Path for filesystem operations.  Path variable naming conventions:

- `_dpath`: suffix for directories
- `_fpath`: suffix for files


## Subprocess Args & pathlib.Path

`subprocess.run()` / `Popen` takes `pathlib.Path` objects directly as arguments.  Don't wrap in
str().


## Python pytest Tests

- Tests should be pytest style and class based.  That is, tests should usually be methods on a test
class, not top-level module functions.
- Use `unittest.mock` instead of pytest's `monkeypatch` fixture
