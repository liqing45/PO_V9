import sys, os

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MobilekWorkPage(BaseAction):
    first_network_btn = By.XPATH, "//*[contains(@text,'首选网络类型')]"

    network_2g_btn = By.XPATH, "//*[contains(@text,'2G')]"

    network_3g_btn = By.XPATH, "//*[contains(@text,'3G')]"

    def click_first_network(self):
        self.click(self.first_network_btn)

    def network_2g(self):
        self.click(self.network_2g_btn)

    def network_3g(self):
        self.click(self.network_3g_btn)
