from __future__ import annotations
from playwright.sync_api import expect
from .base_page import BasePage

class InventoryPage(BasePage):
    def open_direct(self) -> None:
        self.goto("/inventory.html")

    def assert_has_some_content(self) -> None:
        # Minimal assertion to keep demo generic
        expect(self.page.locator("body")).to_be_visible()
