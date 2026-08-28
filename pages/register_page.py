# RegisterPage.py
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
import logging

logger = logging.getLogger(__name__)

class RegisterPage(BasePage):
    """
    Страница регистрации пользователя.
    Содержит методы для взаимодействия с формой регистрации:
    - переход к форме;
    - ввод данных (имя, email, пароль);
    - отправка формы;
    - проверка состояния страницы и результатов регистрации.
    """

    def click_register_link(self):
        """Кликает на ссылку «Зарегистрироваться»."""
        try:
            register_link = self.wait.until(
                EC.element_to_be_clickable(RegisterPageLocators.LINK_REGISTER)
            )
            register_link.click()
            logger.info("Нажали ссылку «Зарегистрироваться», переходим к форме...")
        except Exception as e:
            logger.error("Не удалось кликнуть на ссылку «Зарегистрироваться»: %s", str(e))
            raise

    def enter_name(self, name):
        """Вводит имя в поле ввода."""
        self.enter_text(RegisterPageLocators.INPUT_NAME, name)

    def enter_email(self, email):
        """Вводит email в поле ввода."""
        self.enter_text(RegisterPageLocators.INPUT_EMAIL, email)

    def enter_password(self, password):
        """Вводит пароль в поле ввода."""
        self.enter_text(RegisterPageLocators.INPUT_PASSWORD, password)

    def click_register_button(self):
        """Кликает на кнопку «Зарегистрироваться»."""
        try:
            register_button = self.wait.until(
                EC.element_to_be_clickable(RegisterPageLocators.BUTTON_REGISTER)
            )
            register_button.click()
            logger.info("Нажали кнопку «Зарегистрироваться», отправляем форму...")
        except Exception as e:
            logger.error("Не удалось кликнуть на кнопку «Зарегистрироваться»: %s", str(e))
            raise

    def is_registration_form_visible(self):
        """Проверяет, видна ли форма регистрации (поле имени)."""
        try:
            self.wait.until(
                EC.visibility_of_element_located(RegisterPageLocators.INPUT_NAME)
            )
            return True
        except Exception as e:
            logger.warning("Форма регистрации не найдена: %s", str(e))
            return False

    def get_error_message(self):
        """Получает текст сообщения об ошибке, если оно есть."""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
            )
            return error_element.text
        except Exception:
            return None

    def is_registration_successful(self):
        """
        Проверяет, что регистрация прошла успешно.
        Логика: после регистрации пользователь должен увидеть кнопку «Оформить заказ».
        """
        from pages.main_page import MainPage
        main_page = MainPage(self.driver)
        return main_page.is_order_button_visible()
