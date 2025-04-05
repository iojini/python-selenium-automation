from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "a[data-test='cartItem-linked-title']")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')

    def verify_product_in_cart(self, expected_text='twix'):
        product = self.find_element(*self.CART_ITEM_TITLE)
        assert expected_text.lower() in product.text.lower(), \
            f"Expected '{expected_text}' in cart, but got '{product.text}'"
