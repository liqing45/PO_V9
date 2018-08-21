import sys, os

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.more_page import MorePage
from page.setting_page import SettingPage
from page.mobile_network_page import MobilekWorkPage
from page.display_page import DisplayPage


class Page:
    def __init__(self, driver):
        self.driver = driver
    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def more_page(self):
        return MorePage(self.driver)

    @property
    def mobile_network_page(self):
        return MobilekWorkPage(self.driver)

    @property
    def display_page(self):
        return DisplayPage(self.driver)


