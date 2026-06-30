from pages.secure_page import SecurePage
from playwright.sync_api import expect

def test_successful_logout(logged_in_page: SecurePage) -> None :
    """Verify that a user can logout success"""

    logged_in_page.execute_logout()

    expect(logged_in_page.page).to_have_url("https://the-internet.herokuapp.com/login")