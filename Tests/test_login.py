import pytest

from Pages.LoginPage import LoginPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/loginData.csv")

@pytest.mark.parametrize(("username", "password"), test_data)
def test_valid_login(username, password, driver):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Need to assert here hai
    assert "overview.htm" in driver.current_url.lower(), "Did not redirect to Account Overview page"
