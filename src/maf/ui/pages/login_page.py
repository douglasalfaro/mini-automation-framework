from __future__ import annotations
from playwright.sync_api import Page, expect
from .base_page import BasePage

class LoginPage(BasePage):
    def open(self) -> None:
        self.goto("/")

    def login(self, username: str, password: str) -> None:
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def assert_error(self) -> None:
        expect(self.page.locator("[data-test='error']")).to_be_visible()
