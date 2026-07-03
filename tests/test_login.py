import pytest
from config import USER, PASSWORD
from pages.login_page import LoginPage
from playwright.sync_api import expect



def test_successful_login(login_page: LoginPage) -> None:
    """Verify that a user can log in successfully with valid credentials."""

    secure_page = login_page.execute_login(USER, PASSWORD)

    expect(secure_page.get_logout_button()).to_be_visible()


def test_unsuccessful_login(login_page: LoginPage) -> None:
    """Verify error message validation when injecting invalid credentials."""

    login_page.execute_login("SRQa", "SuperQA!")

    assert login_page.get_alert_message() == "Your username is invalid!"

@pytest.mark.parametrize("username, password, expected_message", [
    ("usuario_invalido", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "password_invalido", "Your password is invalid!"),
    ("", "", "Credentials cannot be empty"),
])

def test_login_scenarios(login_page: LoginPage, username, password, expected_message) -> None:
    if not username and not password:
        with pytest.raises(ValueError, match="Credentials cannot be empty"):
            login_page.execute_login(username, password)
        return

    login_page.execute_login(username, password)
    
    assert login_page.get_alert_message() == expected_message