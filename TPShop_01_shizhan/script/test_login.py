import unittest
from util import DriverUtil
from page.login_page import LoginProxy
from page.index_page import IndexProxy
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DriverUtil.get_driver()


    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def test_login(self):
        self.index_proxy = IndexProxy()
        self.login_proxy = LoginProxy()

        self.index_proxy.to_login_page()

        self.login_proxy.login("15711111112", "123456", "8888")


