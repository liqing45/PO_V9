from selenium import webdriver


class DriverUtil:
    __driver = None

    @staticmethod
    def get_driver():
        """
        获取浏览器对象，并完成初始化工作
        :return: 返回浏览器驱动对象
        """

        if DriverUtil.__driver is None:
            DriverUtil.__driver = webdriver.Chrome()

            DriverUtil.__driver.maximize_window()

            DriverUtil.__driver.implicitly_wait(30)

            DriverUtil.__driver.get("http://localhost/index.php")

        return DriverUtil.__driver

    @staticmethod
    def quit_driver():

        DriverUtil.get_driver().quit()