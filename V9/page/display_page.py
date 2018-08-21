import sys, os

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    display_btn = (By.XPATH, "//*[contains(@text,'显示')]")

    search_btn = (By.ID, "com.android.settings:id/search")

    search_edit_text = (By.ID, "android:id/search_src_text")

    back_btn = (By.CLASS_NAME, "android.widget.ImageButton")

    # def __init__(self, driver):
    #     self.driver = driver

    def click_display(self):
        self.click(self.display_btn)

    def click_search(self):
        self.click(self.search_btn)

    def input_text(self, kw):
        self.send_keys(self.search_edit_text, kw)

    def click_back(self):
        self.click(self.back_btn)
