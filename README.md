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

- selenium
- pytest
- pytest-html

```bash
pip install pytest selenium pytest-html
```

---

## Test Execution Lifecycle

#### 1. Session Starts

- Screenshot directory cleaned
- Browser configuration initialized

#### 2. Test Starts

- Chrome launched
- Browser maximized

#### 3. Test Executes

- Selenium interactions occur

#### 4. Test Outcome

- Success
    - Browser closes
- Failure
    - Logging captured
    - Screenshot captured and attached to HTML report
    - Browser closes

---

## Example Usage

#### Run tests

```bash
pytest
```

#### Run tests in headless mode

```bash
pytest --headless
```
