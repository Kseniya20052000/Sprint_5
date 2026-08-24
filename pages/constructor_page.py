from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
import logging
import time

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
        current_tab = self.driver.find_element(*ConstructorLocators.BUNS_TAB)
        is_already_active = "tab_tab_type_current__2BEPc" in current_tab.get_attribute("class")

        if is_already_active:
            logger.info("Вкладка «Булки» уже активна, переходим на другую вкладку для теста")
            # Кликаем на «Соусы», чтобы гарантированно деактивировать «Булки»
            self.click_sauces_tab()
            # Ждём стабилизации
            time.sleep(1)

        logger.info("Кликаем на вкладку «Булки»")
        buns_tab = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        buns_tab.click()
        # Ждём обновления интерфейса
        time.sleep(1)

    def is_sauces_tab_active(self):
        """Проверяет, активна ли вкладка «Соусы»"""
        tab = self.wait.until(
            EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB)
        )
        class_attr = tab.get_attribute("class")
        is_active = "tab_tab_type_current__2BEPc" in class_attr
        logger.info(f"Вкладка «Соусы»: активна = {is_active}, классы = {class_attr}")
        return is_active

    def is_fillings_tab_active(self):
        """Проверяет, активна ли вкладка «Начинки»"""
        tab = self.wait.until(
            EC.presence_of_element_located(ConstructorLocators.FILLINGS_TAB)
        )
        class_attr = tab.get_attribute("class")
        is_active = "tab_tab_type_current__2BEPc" in class_attr
        logger.info(f"Вкладка «Начинки»: активна = {is_active}, классы = {class_attr}")
        return is_active

    def is_buns_tab_active(self):
        """Проверяет, активна ли вкладка «Булки» с ожиданием"""
        try:
            self.wait.until(
                lambda driver: "tab_tab_type_current__2BEPc" in driver.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class")
            )
            logger.info("Вкладка «Булки»: активна")
            return True
        except:
            tab = self.driver.find_element(*ConstructorLocators.BUNS_TAB)
            class_attr = tab.get_attribute("class")
            logger.error(f"Вкладка «Булки»: неактивна, классы = {class_attr}")
            return False