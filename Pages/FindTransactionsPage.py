from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.FindTransactionPageLocators import FindTransactionPageLocators
from Utils.ElementHelper import ElementHelper


class FindTransactionsPage(ElementHelper):
    def load(self):
        self.driver.get(FindTransactionPageLocators.url)

    def search_by_transaction_id(self, txn_id):
        self.element_send_keys(FindTransactionPageLocators.transaction_id_input, txn_id)
        self.element_click_call(FindTransactionPageLocators.button_txn_id)

    def search_by_date(self, date_str):
        self.element_send_keys(FindTransactionPageLocators.date_input, date_str)
        self.element_click_call(FindTransactionPageLocators.button_txn_date)

    def search_by_date_range(self, from_date, to_date):
        self.element_send_keys(FindTransactionPageLocators.from_date_input, from_date)
        self.element_send_keys(FindTransactionPageLocators.to_date_input, to_date)
        self.element_click_call(FindTransactionPageLocators.button_txn_date_range)

    def search_by_amount(self, amount):
        self.element_send_keys(FindTransactionPageLocators.amount_input, amount)
        self.element_click_call(FindTransactionPageLocators.button_txn_amount)

    def has_error(self):
        return self.is_element_present(FindTransactionPageLocators.error_message)

    def has_result_rows(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(FindTransactionPageLocators.transaction_rows)
            )
            return len(self.driver.find_elements(*FindTransactionPageLocators.transaction_rows)) > 0
        except TimeoutException:
            return False

    def get_find_txn_result(self):
        if self.has_result_rows():
            return "success"
        elif self.has_error():
            return "failure"
        else:
            return "unknown"