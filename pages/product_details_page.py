from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    VIEW_CART_CHECKOUT_BTN = (By.LINK_TEXT, "View cart & check out")


    #def wait_for_add_to_cart(self):
        #self.wait_until_visible(*self.ADD_TO_CART_BTN)

    def add_to_cart(self):
        sleep(5)

        # Scroll down to make sure button is visible
        self.driver.execute_script("window.scrollBy(0,500)", "")

        # Now click on the button
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)

    def view_cart(self):
        self.wait_until_clickable_click(*self.VIEW_CART_CHECKOUT_BTN)