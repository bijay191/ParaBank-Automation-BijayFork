from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import LoginPageLocators
from Utils.ElementHelper import ElementHelper


class LoginPage(ElementHelper):
    def login(self, username, password):
        self.element_send_keys(LoginPageLocators.username_xpath, username)
        self.element_send_keys(LoginPageLocators.password_xpath, password)
        self.element_click_call(LoginPageLocators.loginButton_xpath)

    def is_on_overview_page(self):
        return self.driver.current_url == "https://parabank.parasoft.com/parabank/overview.htm"

    def get_login_result(self):
        if self.is_on_overview_page():
            return "success"
        elif self.is_element_present(LoginPageLocators.error_message):
            return "failure"
        return "unknown"