from behave import given, when, then
from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage


@given("open Target sign in page")
def navigate_to_homepage(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open_main_page()

    context.header = Header(context.driver)
    context.header.click_header_sign_in()

    context.header.click_right_menu_sign_in()

    context.sign_in_page = SignInPage(context.driver)


@when("user enters correct email")
def enter_correct_email(context):
    email = "borenger@tmxttvmail.com"
    context.app.sign_in_page.enter_email(email)


@when("user clicks Continue")
def click_continue(context):
    context.app.sign_in_page.click_continue()


@when("user enters incorrect password")
def enter_incorrect_password(context):
    password = "123"
    context.app.sign_in_page.enter_password(password)


@when("user clicks Sign in with password")
def click_signin_password(context):
    context.app.sign_in_page.click_sign_in_with_password()


@then("error message should be displayed")
def password_error_massage_displayed(context):
    context.sign_in_page.verify_error_message_displayed()
