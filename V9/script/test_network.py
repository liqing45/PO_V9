import sys, os
sys.path.append(os.getcwd())
from page.page import Page


from base.base_driver import init_driver
from page.setting_page import SettingPage
from page.more_page import MorePage
from page.mobile_network_page import MobilekWorkPage


class TestMore:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.page.setting.click_more_btn()
        self.page.more_page.click_mobile_btn()
        self.page.mobile_network_page.click_first_network()

    def test_more_2g(self):
        self.page.mobile_network_page.network_2g()

    def test_more_3g(self):
        self.page.mobile_network_page.network_3g()

    def teardown(self):
        self.driver.quit()
