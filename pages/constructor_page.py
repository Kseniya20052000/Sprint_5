from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
import logging
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_sauces_tab(self):
        """Кликает на вкладку «Соусы»"""
        logger.info("Кликаем на вкладку «Соусы»")
        sauces_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        sauces_tab.click()

    def click_fillings_tab(self):
        """Кликает на вкладку «Начинки»"""
        logger.info("Кликаем на вкладку «Начинки»")
        fillings_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)
        )
        fillings_tab.click()

    def click_buns_tab(self):
        """Кликает на вкладку «Булки», гарантируя переключение"""
        logger.info("Проверяем текущее состояние вкладки «Булки»")

        if self.is_buns_tab_active():
            logger.info("Вкладка «Булки» уже активна, переходим на другую вкладку для теста")
            self.click_sauces_tab()
            self.wait.until(
                lambda driver: "tab_tab_type_current__2BEPc" in driver.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class")
            )

        logger.info("Кликаем на вкладку «Булки»")
        buns_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        buns_tab.click()
        self.wait.until(
            lambda driver: "tab_tab_type_current__2BEPc" in driver.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class")
        )

    def is_tab_active(self, tab_locator):
        """Проверяет, активна ли вкладка"""
        try:
            self.wait.until(
                lambda driver: "tab_tab_type_current__2BEPc" in driver.find_element(*tab_locator).get_attribute("class")
            )
            logger.info(f"Вкладка активна: {tab_locator}")
            return True
        except:
            logger.warning(f"Вкладка неактивна: {tab_locator}")
            return False

    def is_sauces_tab_active(self):
        return self.is_tab_active(ConstructorLocators.SAUCES_TAB)

    def is_fillings_tab_active(self):
        return self.is_tab_active(ConstructorLocators.FILLINGS_TAB)

    def is_buns_tab_active(self):
        return self.is_tab_active(ConstructorLocators.BUNS_TAB)
