from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img')


@when("user conducts product search")
def conduct_product_search(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys("tea")
    context.driver.find_element(*SEARCH_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(SEARCH_RESULTS))


@then("each product in the search results should have a name and image")
def verify_name_image(context):
    products = context.driver.find_elements(*SEARCH_RESULTS)[:8]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title is missing'
        print(title)
        product.find_element(*PRODUCT_IMAGE)
