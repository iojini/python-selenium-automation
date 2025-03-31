from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
#SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('navigation to {product_id} product detail page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('user can click through color options')
def click_and_verify_colors(context):
    expected_colors = ['black white', 'navy blue', 'rainbow', 'yellow black']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()

        selected_color = color.get_attribute("alt").strip().lower()
        actual_colors.append(selected_color)
    print(actual_colors)

    assert expected_colors == actual_colors, f'Test Failed: Expected {expected_colors}; however, the actual colors were {actual_colors}'
