from selenium.webdriver.common.by import By
from behave import given, when, then
import time

@when("user clicks on sign in link")
def click_signin_link(context):
    signin_link = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    signin_link.click()
    time.sleep(3)


@when("user clicks on sign in button from the navigation menu")
def click_signin_button(context):
    signin_button = context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
    signin_button.click()
    time.sleep(3)

#To verify that signin page is displayed, will check for "Sign into your Target account" message
@then("Sign In page is displayed")
def signin_page_displayed(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
    assert expected_text == actual_text, f'Test Failed: Expected {expected_text}; however, actual is {actual_text}'
