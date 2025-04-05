from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def select_first_product(self):
        sleep(10)

        # Scroll down to make sure products are visible
        self.driver.execute_script("window.scrollBy(0,300)", "")

        # Now click on the product
        self.wait_until_clickable_click(*self.PRODUCT_TITLE)