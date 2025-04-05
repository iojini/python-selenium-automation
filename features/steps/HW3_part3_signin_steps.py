#from selenium.webdriver.common.by import By
#from behave import given, when, then
#from selenium.webdriver.support import expected_conditions as EC


#SIGNIN_LINK = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
#SIGNIN_BUTTON = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
#SIGNIN_PAGE_HEADER = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")

#@when("user clicks on sign in link")
#def click_signin_link(context):
#    context.driver.find_element(*SIGNIN_LINK).click()
#    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BUTTON))


#@when("user clicks on sign in button from the navigation menu")
#def click_signin_button(context):
#    context.driver.find_element(*SIGNIN_BUTTON).click()
#    context.driver.wait.until(EC.visibility_of_element_located(SIGNIN_PAGE_HEADER))

#To verify that signin page is displayed, will check for "Sign into your Target account" message
#@then("Sign In page is displayed")
#def signin_page_displayed(context):
#    expected_text = 'Sign into your Target account'
#    actual_text = context.driver.find_element(*SIGNIN_PAGE_HEADER).text
#    assert expected_text == actual_text, f'Test Failed: Expected {expected_text}; however, actual is {actual_text}'
