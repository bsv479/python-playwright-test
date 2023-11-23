from playwright.sync_api import Page

from objects.register_creds import RegisterCreds


class RegisterPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name_locator = page.locator("[id=\"customer\\.firstName\"]")
        self.last_name_locator = page.locator("[id=\"customer\\.lastName\"]")
        self.address_locator = page.locator("[id=\"customer\\.address\\.street\"]")
        self.city_locator = page.locator("[id=\"customer\\.address\\.city\"]")
        self.state_locator = page.locator("[id=\"customer\\.address\\.state\"]")
        self.zip_code_locator = page.locator("[id=\"customer\\.address\\.zipCode\"]")
        self.phone_locator = page.locator("[id=\"customer\\.phoneNumber\"]")
        self.ssn_locator = page.locator("[id=\"customer\\.ssn\"]")
        self.username_locator = page.locator("[id=\"customer\\.username\"]")
        self.password_locator = page.locator("[id=\"customer\\.password\"]")
        self.repeated_password_locator = page.locator("#repeatedPassword")
        self.register_button_locator = page.get_by_role("button", name="Register")

    def fill_registration_form(self, register_creds: RegisterCreds) -> None:
        self.first_name_locator.fill(register_creds.first_name)
        self.last_name_locator.fill(register_creds.last_name)
        self.address_locator.fill(register_creds.address)
        self.city_locator.fill(register_creds.city)
        self.state_locator.fill(register_creds.state)
        self.zip_code_locator.fill(register_creds.zip_code)
        self.phone_locator.fill(register_creds.phone)
        self.ssn_locator.fill(register_creds.ssn)
        self.username_locator.fill(register_creds.username)
        self.password_locator.fill(register_creds.password)
        self.repeated_password_locator.fill(register_creds.password)

    def click_register_button(self):
        self.register_button_locator.click()
