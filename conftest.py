import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    baseUrl = "https://parabank.parasoft.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    yield driver
    driver.quit()