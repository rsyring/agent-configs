# CRITICAL: reinforced test/pytest expectations

- Use pytest-style test classes and fixtures
- Organize tests with one `Test...` class per view or unit under test.
- Test method names should not duplicate the class name.
- Moderate the length of test method names. Make them user oriented; NOT a string of words
  about what is under test.
- Reuse shared fixtures from `conftest.py` when they already exist; do not recreate them
  locally.
- DO NOT use monkeypatch, DO USE unittest.mock
- DO NOT overuse mocks. DO NOT create test anti-patterns by essentially testing only what
  your mocks setup. DO exercise real application code and realistic data flows. DO mock
  boundaries, not behavior: replace external dependencies sparingly, but let the code
  under test run through real logic and meaningful integrations.
