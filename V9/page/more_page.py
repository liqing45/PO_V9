import sys, os

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MorePage(BaseAction):
    mobile_nework_btn = By.XPATH, "//*[contains(@text,'移动网络')]"

    def click_mobile_btn(self):
        self.click(self.mobile_nework_btn)
