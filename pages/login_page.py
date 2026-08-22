# LoginPage.py
from base_page import BasePage
from locators import LoginPageLocators, MainPageLocators  
import json
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
INPUT_EMAIL = (By.NAME, "name")


class LoginPage(BasePage):
    
    URL = "https://stellarburgers.education-services.ru/"
    

    def open(self):
        """Открывает главную страницу."""
        self.driver.get(self.URL)

    def go_to_login_form(self):
        """
        Находит кнопку 'Войти в аккаунт' на главной и кликает по ней.
        Ждет появления формы логина.
        """
        wait = WebDriverWait(self.driver, 15)
    
        # Ждем кликабельность кнопки и нажимаем
        login_btn = wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN_ACCOUNT)
        )
        login_btn.click()
    
        logger.info("Нажали кнопку 'Войти в аккаунт', переходим к форме логина...")

        # Ждем появления поля Email (это сигнал, что форма загрузилась)
        wait.until(
            EC.presence_of_element_located(LoginPageLocators.INPUT_EMAIL)
        )
        logger.info("Форма входа успешно загружена.")


    def enter_email(self, email: str) -> None:
        self.enter_text(LoginPageLocators.INPUT_EMAIL, email)

    def enter_password(self, password: str) -> None:
        self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

    def click_login_button(self) -> None:
        self.click_element(LoginPageLocators.BUTTON_LOGIN)

   
    def is_logged_in(self, driver, timeout=10):
        """
        Проверяет, выполнен ли вход в систему.
        Возвращает True, если элемент личного кабинета найден, иначе False.
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        wait = WebDriverWait(driver, timeout)
    
        
        logout_locator = (By.XPATH, "//button[text()='Выйти']")
    
        try:
            # Пытаемся найти элемент ЛК. Если он есть — вход успешен.
            wait.until(EC.visibility_of_element_located(logout_locator))
            return True
        except Exception:
            # Если элемент не найден за timeout секунд — вход не выполнен.
            return False


    INPUT_EMAIL = (By.NAME, "name")


    def is_login_form_visible(self):
        """
        Проверяет, видна ли форма входа (конкретно поле Email).
        Логика: если вход НЕ удался, поле с name="name" должно остаться видимым.
        """
        
        try:
            #  таймаут 15 с для надёжности
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located(self.INPUT_EMAIL))
            return True
        except Exception as e:
            print(f"Ошибка поиска поля email: {e}")  # Отладка
            return False

    def get_current_url(self):
        return self.driver.current_url

    def click_forgot_password_link(self):
        """Кликает на ссылку «Восстановить пароль»"""
        forgot_password_link = self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LINK_FORGOT_PASSWORD)
        )
        forgot_password_link.click()


    def click_forgot_password_link(self):
        """Кликает на ссылку «Восстановить пароль»"""
        forgot_password_link = self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LINK_FORGOT_PASSWORD)
        )
        forgot_password_link.click()
        logger.info("Нажали на ссылку «Восстановить пароль», переходим на страницу восстановления...")        