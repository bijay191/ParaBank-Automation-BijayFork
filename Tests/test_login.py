import pytest

from Pages.LoginPage import LoginPage
from Utils.FileHelper import read_csv

test_data = read_csv("loginData.csv")

@pytest.mark.parametrize("data", test_data)
def test_valid_login(driver, data):
    login_page = LoginPage(driver)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    # Need to assert here hai