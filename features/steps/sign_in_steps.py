from behave import given, when, then
from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage


@given("navigation to target home page")
def navigate_to_homepage(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open_main_page()


@when("user clicks on sign in link in header")
def click_header_sign_in(context):
    context.header = Header(context.driver)
    context.header.click_header_sign_in()


@when("user clicks on sign in button from the right navigation menu")
def click_right_menu_sign_in(context):
    context.header.click_right_menu_sign_in()


@then("Sign in form should be displayed")
def signin_form_displayed(context):
    context.sign_in_page = SignInPage(context.driver)
    context.sign_in_page.verify_signin_form_loaded()
