# ConstructorPage.py
from base_page import BasePage
from locators import ConstructorLocators
import logging
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class ConstructorPage(BasePage):
    """
    Страница конструктора бургеров.
    Содержит методы для взаимодействия с вкладками и ингредиентами:
    - переключение между вкладками («Булки», «Соусы», «Начинки»);
    - проверка активности вкладок;
    - выбор ингредиентов.
    """

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def _click_tab(self, tab_locator, tab_name):
        """
        Вспомогательный метод для клика по вкладке.
        :param tab_locator: локатор вкладки.
        :param tab_name: читаемое имя вкладки для логирования.
        """
        logger.info(f"Кликаем на вкладку «{tab_name}»")
        tab_element = self.wait.until(
            EC.element_to_be_clickable(tab_locator)
        )
        tab_element.click()
        self._wait_for_tab_activation(tab_locator, tab_name)

    def _wait_for_tab_activation(self, tab_locator, tab_name):
        """Ожидает активации вкладки."""
        try:
            self.wait.until(
                lambda driver: "tab_tab_type_current" in driver.find_element(*tab_locator).get_attribute("class")
            )
            logger.info(f"Вкладка «{tab_name}» активирована")
        except Exception as e:
            logger.error(f"Не удалось активировать вкладку «{tab_name}»: {e}")
            raise

    def click_sauces_tab(self):
        """Кликает на вкладку «Соусы»."""
        self._click_tab(ConstructorLocators.SAUCES_TAB, "Соусы")

    def click_fillings_tab(self):
        """Кликает на вкладку «Начинки»."""
        self._click_tab(ConstructorLocators.FILLINGS_TAB, "Начинки")

    def click_buns_tab(self):
        """Кликает на вкладку «Булки»."""
        self._click_tab(ConstructorLocators.BUNS_TAB, "Булки")

    def is_tab_active(self, tab_locator, tab_name):
        """Проверяет, активна ли вкладка."""
        try:
            is_active = self.wait.until(
                lambda driver: "tab_tab_type_current" in driver.find_element(*tab_locator).get_attribute("class")
            )
            if is_active:
                logger.info(f"Вкладка «{tab_name}» активна")
            else:
                logger.warning(f"Вкладка «{tab_name}» неактивна")
            return is_active
        except Exception as e:
            logger.error(f"Ошибка при проверке активности вкладки «{tab_name}»: {e}")
            return False

    def is_sauces_tab_active(self):
        """Проверяет, активна ли вкладка «Соусы»."""
        return self.is_tab_active(ConstructorLocators.SAUCES_TAB, "Соусы")

    def is_fillings_tab_active(self):
        """Проверяет, активна ли вкладка «Начинки»."""
        return self.is_tab_active(ConstructorLocators.FILLINGS_TAB, "Начинки")

    def is_buns_tab_active(self):
        """Проверяет, активна ли вкладка «Булки»."""
        return self.is_tab_active(ConstructorLocators.BUNS_TAB, "Булки")

    def select_ingredient(self, ingredient_locator, ingredient_name):
        """
        Выбирает ингредиент из текущей вкладки.
        :param ingredient_locator: локатор ингредиента.
        :param ingredient_name: название ингредиента для логирования.
        """
        try:
            ingredient = self.wait.until(
                EC.element_to_be_clickable(ingredient_locator)
            )
            ingredient.click()
            logger.info(f"Выбрали ингредиент: {ingredient_name}")
        except Exception as e:
            logger.error(f"Не удалось выбрать ингредиент {ingredient_name}: {e}")
            raise
