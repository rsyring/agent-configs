# mise + uv

This repo uses:

- uv: for python dependencies and venv creation
- mise: for developer tools, environment variables, shell setup, and tasks

If mise or uv are not working as expected, STOP IMMEDIATELY, and ask for assistance.


## Environment Variables

Notable environment variables:

- `__MISE_SESSION`
    - IF present: mise is activated, you can run mise tools directly
    - IF absent: use `mise exec ...`
- `VIRTUAL_ENV`:
    - IF present: a python venv is activated, you can run python tools directly
    - IF absent: use `mise exec` which should be configured to activate the venv

NEVER create or activate a python virtualenv on your own.  If the above isn't working, STOP
IMMEDIATELY, and ask for assistance.

