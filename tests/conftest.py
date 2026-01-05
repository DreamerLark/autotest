from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:  # pragma: no cover
    from playwright.sync_api import Browser, Playwright


@pytest.fixture(scope="session")
def playwright_instance() -> "Playwright":
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:  # pragma: no cover
        pytest.skip(f"Playwright is not installed: {exc}")

    try:
        with sync_playwright() as p:
            yield p
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"Playwright is not available in this environment: {exc}")


@pytest.fixture(scope="session")
def browser(playwright_instance: "Playwright") -> "Browser":
    try:
        browser = playwright_instance.chromium.launch(headless=True)
    except Exception as exc:  # pragma: no cover
        pytest.skip(
            "Playwright browser binaries are not available. "
            "Run: python -m playwright install chromium\n"
            f"Original error: {exc}"
        )

    yield browser
    browser.close()


@pytest.fixture()
def page(browser: "Browser") -> Any:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
