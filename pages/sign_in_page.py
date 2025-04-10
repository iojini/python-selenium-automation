from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, "username")
    CONTINUE_BTN = (By.ID, "login")
    PASSWORD_FIELD = (By.ID, "password")
    SIGNIN_BTN = (By.ID, "login")
    SKIP_LINK = (By.LINK_TEXT, "Skip")
    TERMS_LINK = (By.LINK_TEXT, "Target terms and conditions")
    ERROR_MSG = (By.ID, "password--ErrorMessage")


    def verify_signin_form_loaded(self):
        self.wait_until_visible(*self.EMAIL_FIELD)

    def enter_email(self, email):
        self.wait_until_visible(*self.EMAIL_FIELD)
        self.input_text(email, *self.EMAIL_FIELD)

    def click_continue(self):
        self.wait_until_clickable_click(*self.CONTINUE_BTN)

    def enter_password(self, password):
        self.wait_until_visible(*self.PASSWORD_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_sign_in_with_password(self):
        self.wait_until_clickable_click(*self.SIGNIN_BTN)

    def click_skip_link(self):
        self.wait_until_clickable_click(*self.SKIP_LINK)

    def verify_sign_in_form_disappears(self):
        self.wait_until_invisible(*self.SIGNIN_BTN)

    def open_signin_page(self):
        self.open_url('https://www.target.com/login')

    def click_terms_link(self):
        self.wait_until_clickable_click(*self.TERMS_LINK)

    def verify_terms_opened(self):
        self.verify_partial_url('terms-conditions')

    def verify_error_message_displayed(self):
        self.wait_until_visible(*self.ERROR_MSG)