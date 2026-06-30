import pytest
from config import USER, PASSWORD
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    page_object = LoginPage(page)
    page_object.navigate()
    return page_object

@pytest.fixture
def logged_in_page(login_page: LoginPage) -> SecurePage:
    """Fixture login user and return secure page"""
    return login_page.execute_login(USER, PASSWORD)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "test-results/videos/",
    }