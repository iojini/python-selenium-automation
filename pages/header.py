from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER_SIGN_IN = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    RIGHT_MENU_SIGN_IN = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")


    def search(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.wait_until_clickable_click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_header_sign_in(self):
        self.wait_until_clickable_click(*self.HEADER_SIGN_IN)

    def click_right_menu_sign_in(self):
        self.wait_until_clickable_click(*self.RIGHT_MENU_SIGN_IN)
