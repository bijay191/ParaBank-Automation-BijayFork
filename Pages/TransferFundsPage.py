from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from Locators.TransferFundPageLocators import TransferFundPageLocators
from Utils.ElementHelper import ElementHelper

class TransferFundsPage(ElementHelper):
    def load(self):
        self.driver.get(TransferFundPageLocators.url)

    def transaction(self, amount):
        self.element_click_call(TransferFundPageLocators.transfer_click)
        self.element_send_keys(TransferFundPageLocators.amount, amount)

        # Wait for and select fromAccount
        WebDriverWait(self.driver, 10).until(
            lambda d: len(Select(d.find_element(*TransferFundPageLocators.from_account)).options) > 0
        )
        from_dropdown = Select(self.driver.find_element(*TransferFundPageLocators.from_account))
        if from_dropdown.options:
            from_dropdown.select_by_index(1)
        else:
            print("From Account dropdown is empty — skipping selection")

        # Wait for and select toAccount
        WebDriverWait(self.driver, 10).until(
            lambda d: len(Select(d.find_element(*TransferFundPageLocators.to_account)).options) > 0
        )
        to_dropdown = Select(self.driver.find_element(*TransferFundPageLocators.to_account))
        if to_dropdown.options:
            to_dropdown.select_by_index(0)
        else:
            print("To Account dropdown is empty — skipping selection")

        # Click Transfer button
        self.element_click_call(TransferFundPageLocators.transfer_button)

    def get_transaction_result(self):
        try:
            # First check for internal error
            if self.is_element_present(TransferFundPageLocators.internal_error_message):
                return "failure"

            # Then check for success message
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(TransferFundPageLocators.success_message)
            )
            return "success"
        except:
            return "unknown"


