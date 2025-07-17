from Locators.RequestLoanPageLocators import RequestLoanPageLocators
from Utils.ElementHelper import ElementHelper


class RequestLoanPage(ElementHelper):
    def request_loan(self):
        self.driver.get(RequestLoanPageLocators.url)

    def loan_pay(self,loan_amount):
        self.driver.click_call(RequestLoanPageLocators.transfer_click)
        self.driver.send_keys(RequestLoanPageLocators.loan_amount,loan_amount)

    def down_pay(self,down_payment):
        self.driver.click_call(RequestLoanPageLocators.transfer_click)
        self.driver.send_keys(RequestLoanPageLocators.loan_amount,down_payment)

