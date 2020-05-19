from Pages.LoginPage import Login
import pytest
from Data.Testdata import *


@pytest.mark.usefixtures("test_setup")
class TestloginPage():
    def test_fblogin(self):
        driver=self.driver
        lg=Login(driver)
        lg.enter_un()
        lg.enter_pwd()
        lg.click_login()
