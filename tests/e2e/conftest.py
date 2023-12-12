import allure
import pytest
from playwright.sync_api import Page, expect, Playwright

from objects.register_creds import RegisterCreds
from pages.register_page import RegisterPage
from utils.register_creds_utils import save_register_creds, read_register_creds, get_random_register_creds, \
    REGISTER_CREDS_JSON


@pytest.fixture(scope="session")
def registration_creds():
    register_creds: RegisterCreds = get_random_register_creds()
    save_register_creds(register_creds)
    return read_register_creds()


@pytest.fixture(scope="session")
def sign_up_setup(playwright: Playwright, register_url, registration_creds):
    browser = playwright.chromium.launch()
    context = browser.new_context(base_url=register_url)
    page: Page = context.new_page()
    register_page: RegisterPage = RegisterPage(page)

    with allure.step("Open Login page"):
        page.goto(register_url)
    with allure.step("Fill in registration form"):
        register_page.fill_registration_form(registration_creds, page)
    with allure.step("Submit registration form"):
        register_page.submit_registration_form()
        expect(page.locator("#customer_menu_top")).to_contain_text(f"Welcome back {registration_creds.first_name}")

    context.storage_state(path=REGISTER_CREDS_JSON)
    browser.close()


@pytest.fixture()
def login_set_up(sign_up_setup, browser, base_url):
    context = browser.new_context(storage_state=REGISTER_CREDS_JSON)
    page = context.new_page()
    page.goto(base_url)
    yield page
    page.close()
