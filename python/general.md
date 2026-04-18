# Python General Instructions

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
