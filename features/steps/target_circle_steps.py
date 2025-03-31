from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


BENEFIT_CELLS = (By.CSS_SELECTOR, "div[class*='ctNgyP']")


@given("navigation to target.com/circle")
def navigate_to_target_circle(context):
    context.driver.get("https://www.target.com/circle")
    context.driver.wait.until(EC.visibility_of_element_located(BENEFIT_CELLS))


@then("at least 10 benefit cells are displayed")
def benefit_cells_displayed(context):
    benefit_cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(benefit_cells) >= 10, f'Test Failed: Expected at least 10 benefit cells; however, actual number is {len(benefit_cells)}'