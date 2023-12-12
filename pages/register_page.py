import random

from playwright.sync_api import Page

from objects.register_creds import RegisterCreds


class RegisterPage:

    def __init__(self, page: Page):
        self.firstname_locator = page.locator("#AccountFrm_firstname")
        self.lastname_locator = page.locator("#AccountFrm_lastname")
        self.email_locator = page.locator("#AccountFrm_email")
        self.telephone_locator = page.locator("#AccountFrm_telephone")
        self.fax_locator = page.locator("#AccountFrm_fax")
        self.company_locator = page.locator("#AccountFrm_company")
        self.address1_locator = page.locator("#AccountFrm_address_1")
        self.address2_locator = page.locator("#AccountFrm_address_2")
        self.city_locator = page.locator("#AccountFrm_city")
        self.postcode_locator = page.locator("#AccountFrm_postcode")
        self.country_locator = page.locator("#AccountFrm_country_id")
        self.country_locator_option = page.locator('#AccountFrm_country_id > option')
        self.zone_locator_option = page.locator('#AccountFrm_zone_id > option')
        self.zone_locator = page.locator("#AccountFrm_zone_id")
        self.login_name_locator = page.locator("#AccountFrm_loginname")
        self.password_locator = page.locator("#AccountFrm_password")
        self.confirm_password_locator = page.locator("#AccountFrm_confirm")
        self.no_option_locator = page.get_by_label("No")
        self.yes_option_locator = page.get_by_label("Yes")
        self.agree_checkbox_locator = page.get_by_label("I have read and agree to the")
        self.final_continue_button_locator = page.get_by_role("button", name="Continue")

    def fill_registration_form(self, register_creds: RegisterCreds, page: Page):
        self.firstname_locator.fill(register_creds.first_name)
        self.lastname_locator.fill(register_creds.last_name)
        self.email_locator.fill(register_creds.email)
        self.telephone_locator.fill(register_creds.phone)
        self.fax_locator.fill(register_creds.fax)
        self.company_locator.fill(register_creds.company)
        self.address1_locator.fill(register_creds.address_1)
        self.address2_locator.fill(register_creds.address_2)
        self.city_locator.fill(register_creds.city)
        self.postcode_locator.fill(register_creds.zip_code)
        self.__select_random_country()
        page.wait_for_timeout(500)
        self.__select_random_zone()
        self.login_name_locator.fill(register_creds.login_name)
        self.password_locator.fill(register_creds.password)
        self.confirm_password_locator.fill(register_creds.password)
        self.no_option_locator.check()
        self.agree_checkbox_locator.check()

    def __select_random_country(self):
        random_country_number = random.randint(1, self.country_locator_option.count() - 1)
        random_country_name = self.country_locator_option.nth(random_country_number).inner_text()
        self.country_locator.select_option(random_country_name)

    def __select_random_zone(self):
        random_zone_number = random.randint(1, self.zone_locator_option.count() - 1)
        random_zone_name = self.zone_locator_option.nth(random_zone_number).inner_text().strip()
        self.zone_locator.select_option(random_zone_name)

    def submit_registration_form(self):
        self.final_continue_button_locator.click()
