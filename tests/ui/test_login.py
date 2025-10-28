from playwright.sync_api import Page
from maf.core.config import CFG
from maf.ui.pages.login_page import LoginPage
from maf.ui.pages.inventory_page import InventoryPage

def test_inventory_page_structure(page: Page):
    login = LoginPage(page, CFG.base_url)
    inv = InventoryPage(page, CFG.base_url)
    login.open()
    login.login("standard_user", "wrong_password")
    login.assert_error()
    inv.open_direct()
    inv.assert_has_some_content()
