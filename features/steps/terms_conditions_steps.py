from behave import given, when, then
from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage

@given('Open sign in page')
def open_signin(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open_main_page()

    context.header = Header(context.driver)
    context.header.click_header_sign_in()

    context.header.click_right_menu_sign_in()

    context.sign_in_page = SignInPage(context.driver)
    email = "*****"
    context.app.sign_in_page.enter_email(email)

    context.app.sign_in_page.click_continue()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_terms_link()


@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.sign_in_page.verify_terms_opened()


@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close()
    context.app.base_page.switch_to_window_by_id(context.original_window)