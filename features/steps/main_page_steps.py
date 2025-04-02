from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_FIELD = (By.ID, 'search')
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")


@given('navigation to target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_FIELD),
        message='Search field not clickable'
    )


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('user clicks on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) # "6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'
