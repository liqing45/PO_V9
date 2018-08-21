import sys, os

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SettingPage(BaseAction):
    display_btn = (By.XPATH, "//*[contains(@text,'显示')]")

    more_btn = By.XPATH, "//*[contains(@text,'更多')]"

    def click_display(self):
        self.click(self.display_btn)

    def click_more_btn(self):
        self.click(self.more_btn)
