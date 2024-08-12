from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize a new firefox browser session
driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)
#Username
driver.find_element(By.NAME, "username").send_keys("Admin")

#password
driver.find_element(By.NAME, "password").send_keys("admin123")

# login button
login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)

#go to orangehrm page
driver.find_element(By.XPATH, "//a[normalize-space()=\"OrangeHRM, Inc\"]").click()
time.sleep(6)
driver.quit()


