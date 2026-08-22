from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
import logging

logger = logging.getLogger(__name__)

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_sauces_tab(self):
        """Кликает на вкладку «Соусы»»"""
        logger.info("Кликаем на вкладку «Соусы»")
        sauces_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.TAB_SAUCES)
        )
        sauces_tab.click()

    def click_fillings_tab(self):
        """Кликает на вкладку «Начинки»»"""
        logger.info("Кликаем на вкладку «Начинки»")
        fillings_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.TAB_FILLINGS)
        )
        fillings_tab.click()

    def click_buns_tab(self):
        """Кликает на вкладку «Булки»»"""
        logger.info("Кликаем на вкладку «Булки»")
        buns_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.TAB_BUNS)
        )
        buns_tab.click()

    def is_sauces_header_visible(self):
        """Проверяет видимость заголовка «Соусы»»"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(ConstructorLocators.HEADER_SAUCES)
            )
            logger.info("Заголовок «Соусы» виден на странице")
            return True
        except:
            logger.error("Заголовок «Соусы» не найден на странице")
            return False

    def is_fillings_header_visible(self):
        """Проверяет видимость заголовка «Начинки»»"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(ConstructorLocators.HEADER_FILLINGS)
            )
            logger.info("Заголовок «Начинки» виден на странице")
            return True
        except:
            logger.error("Заголовок «Начинки» не найден на странице")
            return False

    def is_buns_header_visible(self):
        """Проверяет видимость заголовка «Булки»»"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(ConstructorLocators.HEADER_BUNS)
            )
            logger.info("Заголовок «Булки» виден на странице")
            return True
        except:
            logger.error("Заголовок «Булки» не найден на странице")
            return False
