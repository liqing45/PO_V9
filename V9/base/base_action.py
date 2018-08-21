from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=1):
        loc_By, loc_value = loc
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc_By, loc_value))
        # return self.driver.find_element(loc_By, loc_value)

    def find_elements(self, loc, timeout=10, poll=1):
        loc_By, loc_value = loc
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(loc_By, loc_value))
        # return self.driver.find_elements(loc_By, loc_value)

    def click(self, loc):
        return self.find_element(loc).click()

    def send_keys(self, loc, kw):
        return self.find_element(loc).send_keys(kw)




