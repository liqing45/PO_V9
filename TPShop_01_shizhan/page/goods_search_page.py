from selenium.webdriver.common.by import By
from base.base_page import Basepage

from util import DriverUtil
class GoodsSearchPage(Basepage):
    def __init__(self):
        super(GoodsSearchPage, self).__init__()

        self.find_goods_item = (By.LINK_TEXT, "{}")



    def find_goods_search(self, goods_name):

        location = (self.find_goods_item[0], self.find_goods_item[1].format(goods_name))

        self.find_element(location)

class GoodsSearchHandle:
    pass


