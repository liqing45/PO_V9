import sys, os
sys.path.append(os.getcwd())

from page.page import Page


from page.display_page import DisplayPage

from base.base_driver import init_driver


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_display_input(self):
        self.page.display_page.click_display()
        self.page.display_page.click_search()
        self.page.display_page.input_text("hello")
        self.page.display_page.click_back()

    def teardown(self):
        self.driver.quit()
