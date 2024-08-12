from selenium import webdriver
import time
from login_page import LoginPage, HumanResourcePage


# Initialize a new firefox browser session
driver = webdriver.Firefox()
driver.maximize_window()

# Open the login page
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(2)  # Wait for the page to load

# Create an instance of the login page and login
login_page = LoginPage(driver)
login_page.enter_username("Admin")
login_page.enter_password("admin123")
login_page.click_login()
time.sleep(5)  # Wait for the dashboard page to load after login


# Store the current window handle (original tab)
original_window = driver.current_window_handle

# To switch to new tab
HumanResource_page = HumanResourcePage(driver)
HumanResource_page.click_orangehrm_link()
time.sleep(6)  # Wait for the new page to load

# Validate if it switched to the new tab
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])
else:
    raise Exception("New tab did not open as expected.")

# Close the new tab
driver.close()

# Switch back to the original tab
driver.switch_to.window(original_window)
time.sleep(2)

# Assert the original tab is still correct
assert "dashboard" in driver.current_url.lower(), "Did not return to the original dashboard page."

# #Close the driver
# driver.quit()

