import re

import allure
from allure_commons.types import Severity
from playwright.sync_api import Page, expect


@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sborisenco")
@allure.feature("Feature number")
@allure.story("Authorized user can create new")
def test_open_new_account(login_set_up, base_url, current_env, run_browser, sign_up_setup, storage_state_path):
    print(f" Browser --------> {run_browser}")
    allure.dynamic.link(base_url, name=current_env)
    page: Page = login_set_up
    with allure.step(f"Open main page: {base_url}"):
        page.goto(base_url)
    with allure.step("Open New Account"):
        page.get_by_role("link", name="Open New Account").click()
    with allure.step("Select type of account"):
        page.locator("#type").select_option("1")
    with allure.step("Click Open New Account"):
        page.get_by_role("button", name="Open New Account").click()
        expect(page.locator("h1")).to_contain_text("Account Opened!")
        expect(page.locator("#rightPanel")).to_contain_text("Congratulations, your account is now open.")
        expect(page.locator("#rightPanel")).to_have_text(re.compile("Your new account number: \\d{5}"))
