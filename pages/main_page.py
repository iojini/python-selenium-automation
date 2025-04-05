from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')


    def open_main_page(self):
        self.open_url(self.base_url)
        self.wait_until_clickable(*self.SEARCH_FIELD)


