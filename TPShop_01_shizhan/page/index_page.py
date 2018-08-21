from util import DriverUtil
from selenium.webdriver.common.by import By
from base.base_page import Basepage
from base.base_page import BaseHandle


# 对象层
class IndexPage(Basepage):

    def __init__(self):
        super(IndexPage, self).__init__()

        self.login_link = (By.LINK_TEXT, "登录")

        self.search_input = (By.ID, "q")

        self.search_bar = (By.CSS_SELECTOR, "[type='submit']")

        self.my_cart_link = (By.ID, "hd-my-cart")

    def find_login_link(self):
        return self.find_element(self.login_link)

    def find_search_input(self):
        return self.find_element(self.search_input)

    def find_search_bar(self):
        return self.find_element(self.search_bar)

    def find_my_cart_link(self):
        return self.find_element(self.my_cart_link)


# 操作层
class IndexHandle(BaseHandle):

    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        self.index_page.find_login_link().click()

    def input_search_input(self, kw):
        self.input_text(self.index_page.find_search_input(), kw)

    def click_search_bar(self):
        self.index_page.find_search_bar().click()

    def click_my_cart_link(self):
        self.index_page.find_my_cart_link().click()


# 业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    def to_login_page(self):
        """
        跳转到登录页面：点击登录链接即可
        :return:
        """
        self.index_handle.click_login_link()

    def search_kw(self, kw):
        """
        搜索商品，并点击搜索按钮
        :param kw: 搜索商品的关键字，即商品名称
        :return:
        """
        self.index_handle.input_search_input(kw)

        self.index_handle.click_search_bar()

    def to_cart_page(self):
        self.index_handle.click_my_cart_link()
