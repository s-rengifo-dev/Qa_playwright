from pages.base_page import BasePage
from playwright.sync_api import Locator
from pages.secure_page import SecurePage

class LoginPage(BasePage):
    """Page Object representing the login screen on the real web application."""

    def __init__(self, page) -> None:
        """
        Initialize LoginPage.
        """
        super().__init__(page)
        self._url_path: str = "/login" 
        self._username_input: Locator = self.page.locator("#username")
        self._password_input: Locator = self.page.locator("#password")
        self._login_button: Locator = self.page.get_by_role("button", name="Login")
        self._alert_box: Locator = self.page.locator("#flash")

    def navigate(self):
        """
        Execute the redirection to login page.
        """
        self.page.goto(self._url_path)
        self.wait_for_ready()

    def get_login_button(self) -> Locator :
        """
        Return locator login button
        """
        return self._login_button

    def get_alert_message(self) -> str:
        """Return the alert text for test assertions."""
        text = self._alert_box.text_content() or ""
        text = text.replace("×", "")
        return " ".join(text.split())
         
        
    def execute_login(self, username_value: str, password_value: str) -> SecurePage:
        """
        Execute the sequential login execution flow.
        """
        if not username_value or not password_value:
            raise ValueError("Credentials cannot be empty")
        
        self._username_input.fill(username_value)
        self._password_input.fill(password_value)
        self._login_button.click()

        return SecurePage(self.page)

