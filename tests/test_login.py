#тест на вход с корректными данными
#тест на ввод некорректного пароля

import logging
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO) 

class TestLogin:
    def test_valid_login_via_main_page(self, login_page, driver):
        """
        Сценарий: Главная -> Кнопка 'Войти в аккаунт' -> Форма -> Ввод данных -> Успех
        """
        wait = WebDriverWait(driver, 15)

        # 1. Открываем главную страницу
        login_page.open()

        # 2. Переходим к форме через кнопку на главной
        login_page.go_to_login_form()

        # 3. ВВОДИМ ДАННЫЕ (сначала email, потом пароль)
        login_page.enter_email("kseniya_kraeva_50131@mail.ru")
        login_page.enter_password("12345678789")

        # 4. Теперь нажимаем кнопку "Войти"
        login_page.click_login_button()

     

    def test_invalid_password_keeps_user_on_login_page(self, login_page, driver):
        """
        Тест: Неверный пароль оставляет пользователя на странице входа.
        Проверка: Поле ввода Email (name="name") должно оставаться видимым.
        """
        import logging
        logger = logging.getLogger(__name__)

        # 1. Действия
        login_page.open()
        login_page.go_to_login_form()
    
        # Вводим данные
        login_page.enter_email("Kseniya_Kraeva_50131@mail.ru")
        login_page.enter_password("wrong_password_123")  # Неверный пароль
    
        login_page.click_login_button()

        # 2. ЕДИНСТВЕННАЯ ПРОВЕРКА (1 тест = 1 проверка)
        # Мы утверждаем, что поле с name="name" ВИДНО.
        # Если вход успешен -> поле исчезнет -> тест упадет.
        # Если вход не успешен -> поле останется -> тест пройдет.
        assert login_page.is_login_form_visible(), \
            "Ошибка: Поле ввода Email исчезло. Это значит, что пользователь успешно вошёл с неверным паролем!"
        logger.info("Тест пройден: пользователь остался на странице входа, поле Email видно.")





