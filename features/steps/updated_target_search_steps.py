from selenium.webdriver.common.by import By
from behave import given, when, then
import time

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_HEADER = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when("user searches for {search_word}")
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    time.sleep(5)

@then("user should see search results for {expected_text}")
def search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_HEADER).text
    assert expected_text in actual_text, f'Test Failed: Expected {expected_text} in header; however, text in header is {actual_text}'
