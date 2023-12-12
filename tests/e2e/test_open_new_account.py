import allure
from allure_commons.types import Severity
from playwright.sync_api import Page


@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sborisenco")
@allure.feature("Feature number")
@allure.story("Authorized user can create new")
def test_open_new_account(login_set_up, base_url, current_env, run_browser, sign_up_setup):
    allure.dynamic.link(base_url, name=current_env)
    page: Page = login_set_up
    with allure.step(f"Open main page: {base_url}"):
        page.goto(base_url)