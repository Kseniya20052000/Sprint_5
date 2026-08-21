# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self, url):
        self.driver.get(url)


    def enter_text(self, locator, text):
        # Явное ожидание + очистка поля
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()





    def wait_for_element_to_be_clickable(self, locator):
        """Ждет, пока элемент станет видимым и кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, substring):
        """Ждет, пока в URL появится нужная подстрока (например, '/login')"""
        return self.wait.until(lambda d: substring in d.current_url)

    def wait_for_url_equals(self, expected_url):
        """Ожидает, пока URL полностью совпадает с ожидаемым"""
        self.wait.until(lambda driver: driver.current_url == expected_url)