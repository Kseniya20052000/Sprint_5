# MainPage.py
from selenium.webdriver.common.by import By
from base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class MainPage(BasePage):
    """
    Страница главной страницы приложения.
    Содержит методы для взаимодействия с элементами главной страницы:
    - переход в личный кабинет;
    - открытие конструктора бургеров;
    - проверка состояния страницы.
    """

    def click_personal_account(self):
        """Кликает на кнопку «Личный кабинет»."""
        personal_account_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        )
        personal_account_btn.click()
        logger.info("Нажали кнопку «Личный кабинет», переходим в профиль...")

    def click_login_button(self):
        """Кликает на кнопку «Войти» на главной странице."""
        login_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        )
        login_button.click()

    def click_constructor_button(self):
        """Кликает на кнопку «Конструктор» в шапке сайта."""
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_CONSTRUCTOR)
        )
        constructor_button.click()
        logger.info("Нажали кнопку «Конструктор», переходим к сборке бургера...")

    def is_burger_assembly_text_visible(self):
        """Проверяет, видна ли надпись «Соберите бургер»."""
        try:
            burger_text = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.BURGER_ASSEMBLY_TEXT)
            )
            return burger_text.is_displayed()
        except Exception as e:
            logger.warning("Надпись «Соберите бургер» не найдена: %s", str(e))
            return False

    def wait_for_burger_assembly_text(self):
        """Ожидает появления надписи «Соберите бургер»."""
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.BURGER_ASSEMBLY_TEXT)
        )
        logger.info("Надпись «Соберите бургер» появилась на странице")

    def wait_for_main_page_load(self):
        """Ожидает загрузки главной страницы после входа."""
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.MAIN_PAGE_HEADER)
        )
        logger.info("Главная страница загружена после входа в аккаунт")


    def wait_for_personal_account_load(self):
        """Ожидает загрузки страницы личного кабинета."""
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_HEADER)
        )
        logger.info("Страница личного кабинета загружена")

    def click_logout_button(self):
        """Кликает на кнопку «Выход» в личном кабинете."""
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGOUT)
        )
        logout_btn.click()
        logger.info("Нажали кнопку «Выход», инициируем выход из аккаунта...")
