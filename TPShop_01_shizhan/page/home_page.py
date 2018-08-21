from selenium.webdriver.common.by import By
from base.base_page import Basepage


class HomePage:

    def __init__(self):
        self.my_shop = (By.LINK_TEXT, "我的商城")
        self.base_page = Basepage()

    def find_my_shop(self):
        return self.base_page.find_element(self.my_shop)


class HomeHandle:

    def exist_my_shop(self):

        try:
            element = HomePage().find_my_shop()
            return element is not None
        except:
            return False


class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    def is_home_page(self):
        return self.home_handle.exist_my_shop()
