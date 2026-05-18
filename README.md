# pytest-selenium-config

### Python - pytest project configuration for Selenium WebDriver tests

- Copyright (c) 2026 [Corey Goldberg](https://github.com/cgoldberg)
- [MIT License](https://raw.githubusercontent.com/cgoldberg/pytest-selenium-config/refs/heads/master/LICENSE)

----

## Features

This configuration provides a setup for web UI testing:

- Automatic Chrome browser management
- Optional headless execution
- Centralized Selenium fixtures
- Automatic browser cleanup
- HTML reporting
- Failure screenshot capture
- Global Logging Configuration

## Required Packages

- [selenium](https://pypi.org/project/selenium)
- [pytest](https://pypi.org/project/pytest)
- [pytest-html](https://pypi.org/project/pytest-html)

---

## Test Execution Lifecycle

#### 1. Session Starts

- Screenshot directory cleaned
- Browser configuration initialized

#### 2. Test Starts

- Browser launched
- Browser maximized

#### 3. Test Executes

- Selenium interactions

#### 4. Test Outcome

- Success
    - Browser closed
    - Driver quit
- Failure
    - Logging captured
    - Screenshot captured and attached to HTML report
    - Browser closed
    - Driver quit

---

## Example Usage

#### Install dependencies:

```
pip install -e .
```

#### Add tests:

i.e. `test_example.py`


#### Run tests:

```
pytest
```

#### Run tests in headless mode:

```
pytest --headless
```
