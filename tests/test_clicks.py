from __future__ import annotations

import pytest

try:
    from playwright.sync_api import expect
except ImportError as exc:  # pragma: no cover
    pytest.skip(f"Playwright is not installed: {exc}", allow_module_level=True)

from ui_click_tests.html_samples import COUNTER_APP_HTML


def test_click_increment_button(page) -> None:
    page.set_content(COUNTER_APP_HTML)

    page.click("#inc")
    page.click("#inc")

    expect(page.locator("#count")).to_have_text("2")


def test_click_decrement_button(page) -> None:
    page.set_content(COUNTER_APP_HTML)

    page.click("#dec")

    expect(page.locator("#count")).to_have_text("-1")


def test_click_checkbox_updates_status(page) -> None:
    page.set_content(COUNTER_APP_HTML)

    page.check("#agree")
    expect(page.locator("#agree_status")).to_have_text("Agreed")

    page.uncheck("#agree")
    expect(page.locator("#agree_status")).to_have_text("Not agreed")


def test_click_toggle_shows_message(page) -> None:
    page.set_content(COUNTER_APP_HTML)

    message = page.locator("#message")
    expect(message).to_be_hidden()

    page.click("#toggle")
    expect(message).to_be_visible()

    page.click("#toggle")
    expect(message).to_be_hidden()
