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

# Locate and populate search field
search = driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']")
search.clear()
search.send_keys('Hat')
time.sleep(5)

# Click search button
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
time.sleep(5)

# Verification
assert 'hat'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()