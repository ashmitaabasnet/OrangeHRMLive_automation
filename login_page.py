from locators import LoginPageLocators
from locators import HumanResourcePageLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.login_button).click()

#Class to switch to new tab
class HumanResourcePage:

    def __init__(self, driver):
        self.driver = driver

    def click_orangehrm_link(self):
        self.driver.find_element(*HumanResourcePageLocators.orangehrm_link).click()
