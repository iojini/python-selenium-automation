from behave import given, when, then

@given("navigation to target.com")
def open_target_home(context):
    context.app.main_page.open_main_page()

@when("user searches for product")
def search_for_product(context):
    context.app.header.search("twix")

@when("user selects the product from results")
def select_product(context):
    context.app.search_results_page.select_first_product()

@when("user clicks on add to cart button")
def add_product(context):
    context.app.product_details_page.add_to_cart()

@when("user clicks on view cart & check out button")
def view_cart(context):
    context.app.product_details_page.view_cart()

@then("cart should contain product")
def verify_cart_product(context):
    context.app.cart_page.verify_product_in_cart("twix")
