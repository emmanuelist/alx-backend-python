# 0x03. Unittests and Integration Tests

This project focuses on creating unit and integration tests in Python using the `unittest` framework. The goal is to ensure that functions and code paths return expected results for various inputs, covering both standard cases and edge cases. The project also emphasizes common testing patterns such as mocking, parameterization, and fixtures.

## Learning Objectives

By the end of this project, you should be able to explain:

- The difference between unit tests and integration tests.
- Common testing patterns including mocking, parameterizations, and fixtures.
- The importance of testing for ensuring code reliability and correctness.

## Project Structure

The project consists of the following key components:

- **Unit Tests**: Focus on testing individual functions in isolation.
- **Integration Tests**: Test interactions between multiple parts of the codebase.
- **Mocking**: Used to simulate external dependencies, such as HTTP requests or database calls.
- **Parameterization**: Testing functions with various input sets to ensure robustness.
- **Fixtures**: Reusable data for setting up test environments.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all scripts should be `#!/usr/bin/env python3`.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules, classes, and functions should be properly documented.
- Functions and coroutines must be type-annotated.

## Tasks

### 0. Parameterize a Unit Test

Create unit tests for the `utils.access_nested_map` function using `@parameterized.expand`. The tests should cover:

- `nested_map={"a": 1}, path=("a",)`
- `nested_map={"a": {"b": 2}}, path=("a",)`
- `nested_map={"a": {"b": 2}}, path=("a", "b")`

### 1. Parameterize a Unit Test with Exceptions

Test that `utils.access_nested_map` raises `KeyError` for invalid paths using `@parameterized.expand`.

### 2. Mock HTTP Calls

Create tests for `utils.get_json`, using `unittest.mock.patch` to mock external HTTP requests.

### 3. Parameterize and Patch

Test memoization in `utils.memoize` by ensuring that a method is called only once when using the decorator.

### 4. Parameterize and Patch as Decorators

Test the `GithubOrgClient.org` method using `@patch` and `@parameterized.expand`.

### 5. Mocking a Property

Test `GithubOrgClient._public_repos_url` by mocking the `GithubOrgClient.org` property.

### 6. More Patching

Unit-test `GithubOrgClient.public_repos` by mocking `get_json` and `_public_repos_url`.

### 7. Parameterize `has_license`

Test `GithubOrgClient.has_license` by parameterizing the input data and expected results.

### 8. Integration Test: Fixtures

Create integration tests for `GithubOrgClient.public_repos`, using fixtures to mock HTTP responses.

### 9. Integration Tests

Implement and test the `public_repos` and `public_repos_with_license` methods using fixtures to verify correct functionality.

## Execution

Execute tests using the following command:

```bash
$ python -m unittest path/to/test_file.py
```

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-read-only-properties)
- [parameterized](https://github.com/wolever/parameterized)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
- [pycodestyle](https://pypi.org/project/pycodestyle/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## Authors

- **Emmanuel Paul** - [emmanuelist](https://github.com/emmanuelist)

## Repository

- **GitHub repository**: [alx-backend-python](https://github.com/emmanuelist/alx-backend-python)
- **Directory**: `0x03-Unittests_and_integration_tests`
