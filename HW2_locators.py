from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a new Chrome browser instance
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# Open Amazon Sign-In page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# Locators
amazon_logo = driver.find_element(By.XPATH, "//i[contains(@class, 'a-icon-logo')]")
email_field = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.ID, "continue")
conditions_of_use = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
privacy_notice = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
need_help = driver.find_element(By.XPATH, "//span[contains(@class, 'a-expander-prompt')]")
forgot_password = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_signin_issues = driver.find_element(By.ID, "ap-other-signin-issues-link")
create_account_button = driver.find_element(By.ID, "createAccountSubmit")
