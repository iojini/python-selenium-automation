from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
EMPTY_CART_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")

@given("navigation to target.com")
def navigate_to_target_main(context):
    context.driver.get("https://target.com/")
    context.driver.wait.until(EC.visibility_of_element_located(CART_ICON))


@when("user clicks on cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    context.driver.wait.until(EC.visibility_of_element_located(EMPTY_CART_MESSAGE))


@then("Empty cart message is shown")
def empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*EMPTY_CART_MESSAGE).text
    assert expected_text == actual_text, f'Test Failed: Expected {expected_text}; however, actual is {actual_text}'