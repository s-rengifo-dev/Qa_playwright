from pages.base_page import BasePage
from playwright.sync_api import Locator

class SecurePage(BasePage):
    """Page Object representing de secure page before of the login success"""

    def __init__(self, page) -> None:
        """
        Initialize SecurePage.
        """
        super().__init__(page)
        self._secure_url: str = "/secure"
        self._logout_button: Locator = self.page.get_by_role("link", name= "Logout")

    def get_logout_button(self) -> Locator :
        """
        return locator logout button
        """
        return self._logout_button
        
    def execute_logout(self) -> None :
        """
        Execute the sequential logout execution flow.
        """

        self._logout_button.click()
