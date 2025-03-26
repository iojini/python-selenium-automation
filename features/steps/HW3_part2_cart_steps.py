from selenium.webdriver.common.by import By
from behave import given, when, then
import time


@given("navigation to target.com")
def navigate_to_target_main(context):
    context.driver.get("https://target.com/")
    time.sleep(3)


@when("user clicks on cart icon")
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    cart_icon.click()
    time.sleep(3)


@then("Empty cart message is shown")
def empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]").text
    assert expected_text == actual_text, f'Test Failed: Expected {expected_text}; however, actual is {actual_text}'
