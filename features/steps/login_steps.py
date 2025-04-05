from behave import given, when, then


@given("user navigates to target home page")
def open_target(context):
    context.app.main_page.open_main_page()


@when("user clicks on sign in")
def click_header_signin(context):
    context.app.header.click_header_sign_in()


@when("user clicks on sign in button in right navigation menu")
def click_side_nav_signin(context):
    context.app.header.click_right_menu_sign_in()


@when("user enters email")
def enter_email(context):
    email = "borenger@tmxttvmail.com"
    context.app.sign_in_page.enter_email(email)


@when("user clicks on continue button")
def click_continue(context):
    context.app.sign_in_page.click_continue()


@when("user enters password")
def enter_password(context):
    password = "BorTarget123!"
    context.app.sign_in_page.enter_password(password)


@when("user clicks Sign in with password button")
def click_sign_in_with_password(context):
    context.app.sign_in_page.click_sign_in_with_password()


@when("user clicks Skip link")
def step_click_skip(context):
    context.app.sign_in_page.click_skip_link()


@then("user should be logged in (sign in form should disappear)")
def verify_login_success(context):
    context.app.sign_in_page.verify_sign_in_form_disappears()
