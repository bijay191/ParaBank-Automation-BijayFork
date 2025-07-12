
from selenium.webdriver.common.by import By

class OpenNewAccPageLocators:
    new_account = (By.CSS_SELECTOR, "#leftPanel ul li:first-child a")
    account_type = (By.ID, "type")
    account_number = (By.ID, "fromAccountId")
    open_account_button = (By.CLASS_NAME, "button")
    confirmation_message = (By.ID, "newAccountId")
    error_message = (By.ID, "openAccountError")
    url = "https://parabank.parasoft.com/parabank/openaccount.htm"
