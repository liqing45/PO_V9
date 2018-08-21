from util import DriverUtil
from selenium.webdriver.common.by import By
from base.base_page import Basepage
from base.base_page import BaseHandle


# 对象层
class LoginPage(Basepage):

    def __init__(self):
        super(LoginPage, self).__init__()

        self.user_input = (By.ID, "username")

        self.pwd_input = (By.ID, "password")

        self.verify_input = (By.NAME, "verify_code")

        self.login_button = (By.NAME, "sbtbutton")

    def find_user_input(self):
        return self.find_element(self.user_input)

    def find_pwd_input(self):
        return self.find_element(self.pwd_input)

    def find_verify_input(self):
        return self.find_element(self.verify_input)

    def find_login_button(self):
        return self.find_element(self.login_button)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    def input_user_input(self, user):
        self.input_text(self.login_page.find_user_input(), user)

    def input_pwd_input(self, pwd):
        self.input_text(self.login_page.find_pwd_input(), pwd)

    def input_verify_input(self, verify):
        self.input_text(self.login_page.find_verify_input(), verify)

    def click_login_button(self):
        self.login_page.find_login_button().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, user, pwd, verify):

        self.login_handle.input_user_input(user)

        self.login_handle.input_pwd_input(pwd)

        self.login_handle.input_verify_input(verify)

        self.login_handle.click_login_button()
