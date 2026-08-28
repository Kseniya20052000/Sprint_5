# LoginPage.py
from base_page import BasePage
from locators import LoginPageLocators, MainPageLocators
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    
    def open(self):
        """Открывает страницу логина, используя BASE_URL из локаторов."""
        self.driver.get(LoginPageLocators.BASE_URL)

    def go_to_login_form(self):
        """
        Находит кнопку 'Войти в аккаунт' на главной и кликает по ней.
        Ждёт появления формы логина.
        """
        # Ждём кликабельность кнопки и нажимаем
        login_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN_ACCOUNT)
        )
        login_btn.click()
        logger.info("Нажали кнопку 'Войти в аккаунт', переходим к форме логина...")

        # Ждём появления поля Email (это сигнал, что форма загрузилась)
        self.wait.until(
            EC.presence_of_element_located(LoginPageLocators.INPUT_EMAIL)
        )
        logger.info("Форма входа успешно загружена.")

    def enter_email(self, email: str) -> None:
        """Вводит email в поле ввода."""
        self.enter_text(LoginPageLocators.INPUT_EMAIL, email)

    def enter_password(self, password: str) -> None:
        """Вводит пароль в поле ввода."""
        self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

    def click_login_button(self) -> None:
        """Кликает по кнопке 'Войти'."""
        self.click_element(LoginPageLocators.BUTTON_LOGIN)

    def is_logged_in(self, timeout=10):
        """
        Проверяет, выполнен ли вход в систему.
        Возвращает True, если элемент личного кабинета найден, иначе False.
        """
        logout_locator = LoginPageLocators.LOGOUT_BUTTON
        try:
            # Пытаемся найти элемент ЛК. Если он есть — вход успешен.
            self.wait.until(EC.visibility_of_element_located(logout_locator))
            return True
        except Exception:
            # Если элемент не найден за timeout секунд — вход не выполнен.
            return False

    def is_login_form_visible(self):
        """
        Проверяет, видна ли форма входа (конкретно поле Email).
        Логика: если вход НЕ удался, поле с name="name" должно остаться видимым.
        """
        try:
            # Таймаут 15 с для надёжности
            self.wait.until(EC.visibility_of_element_located(LoginPageLocators.INPUT_EMAIL))
            return True
        except Exception as e:
            logger.warning(f"Поле email не найдено: {e}")
            return False

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def click_forgot_password_link(self):
        """Кликает на ссылку «Восстановить пароль»."""
        forgot_password_link = self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LINK_FORGOT_PASSWORD)
        )
        forgot_password_link.click()
        logger.info("Нажали на ссылку «Восстановить пароль», переходим на страницу восстановления...")
