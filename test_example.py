# Copyright (c) 2026 Corey Goldberg
# SPDX-License-Identifier: MIT


def test_example(driver):
    driver.get("https://example.com")
    assert driver.title == "Example Domain"
