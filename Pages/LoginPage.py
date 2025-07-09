from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, LoginPageLocators.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, LoginPageLocators.password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, LoginPageLocators.loginButton_xpath).click()