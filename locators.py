from selenium.webdriver.common.by import By
class LoginPageLocators:

    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

class HumanResourcePageLocators:

    orangehrm_link = (By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")

    