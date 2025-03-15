from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a new Chrome browser instance
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# Open https://www.target.com/
driver.get('https://www.target.com/')
time.sleep(5)

#Click SignIn button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
time.sleep(5)

#Click SignIn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
time.sleep(5)

#Verify SignIn page opened
#Expected Result
expected_result = 'Sign into your Target account'

#Actual Result
actual_result = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading__HcGpD')]").text

#Compares expected results with actual results.
assert expected_result == actual_result, f'Test Failed: Expected {expected_result}; however, actual is {actual_result}'

#Verify SignIn button is shown
driver.find_element(By.XPATH, "//button[@id='login']")