from selenium.webdriver.common.by import By


class TransferFundPageLocators:
    url = "https://parabank.parasoft.com/parabank/transfer.htm"
    transfer_click = (By.XPATH,'/html/body/div[1]/div[3]/div[1]/ul/li[3]/a')
    amount= (By.ID, 'amount')
    from_account = (By.ID,'fromAccountId')
    to_account = (By.ID,'toAccountId')
    transfer_button=(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[2]/input')
    success_message=(By.CLASS_NAME,'title')