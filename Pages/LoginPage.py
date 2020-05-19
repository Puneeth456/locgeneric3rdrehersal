from Pages.Webgeneric import Webgeneric
from Data.Testdata import *

class Login(Webgeneric):
    def __init__(self,driver):
        Webgeneric.__init__(self,driver)
        self.un="email"
        self.pwd="pass"
        self.Login="//input[@type='submit']"
        global wb
        wb=Webgeneric(driver)


    def enter_un(self):
        wb.enter("un",self.un,Username)

    def enter_pwd(self):
        wb.enter("pwd",self.pwd,Password)

    def click_login(self):
        wb.submit("submit",self.Login)