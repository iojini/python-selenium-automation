from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


HELP_HEADING = (By.XPATH, "//h2[contains(., 'Target Help')]")
SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input.search-input")
SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-btn[alt='search']")
TOP_HELP_TILES = (By.XPATH, "//div[contains(@class, 'container') and contains(@class, 'clearfix')][.//h2[contains(@class, 'custom-h2') and contains(@class, 'header') and contains(text(), 'What would you like to do?')]]")
BOTTOM_HELP_TILES = (By.XPATH, '//div[@class="col-lg-12" and contains(., "contact us") and contains(., "product recalls")]')
BROWSE_HELP_HEADING = (By.XPATH, "//h2[contains(., 'Browse')]")


@given("navigation to target help page")
def navigate_to_target_help(context):
    context.driver.get("https://help.target.com/help")
    context.driver.wait.until(EC.visibility_of_element_located(HELP_HEADING))


@then("user should see target help heading")
def target_heading(context):
    context.driver.find_element(*HELP_HEADING)


@then("user should see search input field")
def search_input(context):
    context.driver.find_element(*SEARCH_INPUT_FIELD)


@then("user should see search button")
def search_button(context):
    context.driver.find_element(*SEARCH_BUTTON)


@then("user should see the top help tiles")
def top_tiles(context):
    context.driver.find_element(*TOP_HELP_TILES)


@then("user should see the bottom help tiles")
def bottom_tiles(context):
    context.driver.find_element(*BOTTOM_HELP_TILES)


@then("user should see the browse help heading")
def browse_heading(context):
    context.driver.find_element(*BROWSE_HELP_HEADING)