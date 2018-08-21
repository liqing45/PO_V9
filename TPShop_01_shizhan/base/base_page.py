from util import DriverUtil


class Basepage:
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        """
        定位元素
        :param location: 为元组，（元素的定位类型，元素定位内容）
        :return: 返回查找到的元素
        """
        return self.driver.find_element(location[0], location[1])

class BaseHandle:

    def input_text(self,element, text):
        """
        在输入框中输入内容
        :param element: 要输入的元素
        :param text: 要输入的内容
        """
        element.clear()
        element.send_keys(text)
