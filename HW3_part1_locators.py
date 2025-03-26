from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from HW2_locators import create_account_button

# Create a new Chrome browser instance
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# Open Amazon Sign-In page
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# CSS Locators
amazon_logo = driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
create_account_heading = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
name_field = driver.find_element(BY.CSS_SELECTOR, "input#ap_customer_name")
email_field = driver.find_element(BY.CSS_SELECTOR, "input#ap_email")
password_field = driver.find_element(BY.CSS_SELECTOR, "input#ap_password")
password_requirements_message = driver.find_element(BY.CSS_SELECTOR, "div#ap_password_context_message_section")
reenter_password_field = driver.find_element(BY.CSS_SELECTOR, "input#ap_password_check")
create_account_button = driver.find_element(BY.CSS_SELECTOR, "input#continue")
conditions_of_use_link = driver.find_element(BY.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
privacy_notice_link = driver.find_element(BY.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
sign_in_link = driver.find_element(BY.CSS_SELECTOR, "a[href*='signin']")
