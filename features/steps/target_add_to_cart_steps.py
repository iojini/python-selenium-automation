from selenium.webdriver.common.by import By
from behave import given, when, then
import time


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
PRODUCT_TITLE_LINK = (By.CSS_SELECTOR, "a[data-test='product-title']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
VIEW_CART_CHECKOUT_BTN = (By.LINK_TEXT, "View cart & check out")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "a[data-test='cartItem-linked-title']")


@when("user searches for product")
def search_product(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys("water")
    context.driver.find_element(*SEARCH_BTN).click()
    time.sleep(10)


@when("user selects the product from results")
def select_product(context):
    context.driver.find_element(*PRODUCT_TITLE_LINK).click()
    time.sleep(3)

@when("user clicks on add to cart button")
def click_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    time.sleep(3)

@when("user clicks on view cart & check out button")
def click_view_cart_checkout_button(context):
    context.driver.find_element(*VIEW_CART_CHECKOUT_BTN).click()
    time.sleep(5)

@then("cart should contain product")
def verify_cart_contains_product(context):
    cart_product = context.driver.find_elements(*CART_ITEM_TITLE)
    assert len(cart_product) > 0, f'Test Failed: Expected 1 product in cart; however, actual number is {len(cart_product)}'

