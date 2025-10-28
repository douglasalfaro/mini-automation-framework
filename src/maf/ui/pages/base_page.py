from __future__ import annotations
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/") -> None:
        self.page.goto(self.base_url + path)

    def assert_title_contains(self, text: str) -> None:
        expect(self.page).to_have_title(lambda t: text and text.lower() in t.lower())
