import random

import allure
import pytest
from faker import Faker
from playwright.sync_api import Page, expect, Playwright

from objects.register_creds import RegisterCreds
from pages.register_page import RegisterPage
from utils.config_reader import read_config
from utils.creds_utils import save_creds, read_creds


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="LOCAL",
        action="store",
        choices=("LOCAL", "PROD"),
        help="Choose env param"
    )
    parser.addoption(
        "--run-browser",
        default="CHROMIUM",
        action="store",
        choices=("CHROMIUM", "FIREFOX", "WEBKIT"),
        help="Choose browser param"
    )


@pytest.fixture(scope="session")
def current_env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def run_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['en_US', 'ro_RO', 'it_IT']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 12345


@pytest.fixture(scope="session")
def storage_state_path() -> str:
    return "playwright/.auth/state.json"


@pytest.fixture(scope="session")
def base_url(current_env) -> str:
    return read_config(current_env, "BASE_URL")


@pytest.fixture(scope="session", autouse=True)
def registration_creds():
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    username = f"{first_name}-{last_name}_{random.randint(1, 999)}"
    register_creds: RegisterCreds = RegisterCreds(
        first_name=first_name,
        last_name=last_name,
        address=faker.address(),
        city=faker.city(),
        state=faker.state(),
        zip_code=faker.zipcode(),
        phone=faker.basic_phone_number(),
        ssn=faker.ssn(taxpayer_identification_number_type='SSN'),
        username=username,
        password=faker.password(),
    )
    save_creds(register_creds)


@pytest.fixture(scope="session")
def sign_up_setup(playwright: Playwright, base_url, storage_state_path):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(base_url=base_url)
    page: Page = context.new_page()
    register_page: RegisterPage = RegisterPage(page)
    register_creds: RegisterCreds = read_creds()

    with allure.step("Open main page"):
        page.goto(base_url)
    with allure.step("Go to register page"):
        page.get_by_role("link", name="Register").click()
    with allure.step("Fill in register form"):
        register_page.fill_registration_form(register_creds)
    with allure.step("Click register button"):
        register_page.click_register_button()
        expect(page.locator("h1")).to_contain_text(f"Welcome {register_creds.username}")
        expect(page.locator("#rightPanel")).to_contain_text(
            "Your account was created successfully. You are now logged in.")
    context.storage_state(path=storage_state_path)
    browser.close()


@pytest.fixture()
def login_set_up(sign_up_setup, browser, storage_state_path, base_url):
    context = browser.new_context(storage_state=storage_state_path)
    page = context.new_page()
    page.goto(base_url)
    yield page
    page.close()
