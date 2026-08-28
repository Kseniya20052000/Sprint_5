#тест на вход с корректными данными
#тест на ввод некорректного пароля

import logging
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators  

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class TestLogin:
    def test_valid_login_via_main_page(self, login_page, main_page, driver):
        """
        Сценарий: Главная -> Кнопка 'Войти в аккаунт' -> Форма -> Ввод данных -> Успех.
        Финальная проверка: Появление кнопки «Оформить заказ» подтверждает авторизацию.
        """
        wait = WebDriverWait(driver, 15)

        # 1. Открываем главную страницу
        login_page.open()

        # 2. Переходим к форме через кнопку на главной
        login_page.go_to_login_form()

        # 3. ВВОДИМ ДАННЫЕ
        login_page.enter_email("kseniya_kraeva_50131@mail.ru")
        login_page.enter_password("12345678789")

        # 4. Нажимаем кнопку "Войти"
        login_page.click_login_button()

        # 5. ФИНАЛЬНЫЙ АССЕРТ 
        # Проверяем, что на странице появилась кнопка «Оформить заказ».
        
        logger.info("Проверяем наличие кнопки «Оформить заказ» как признак успешной авторизации...")
        
        # Используем метод из MainPage, который мы создали ранее
        assert main_page.is_burger_assembly_text_visible(), \
            "Ошибка: Кнопка «Оформить заказ» не отображается. Пользователь не авторизован или страница не загрузилась."
        
        logger.info("Тест пройден: кнопка «Оформить заказ» видна, пользователь авторизован.")

    def test_invalid_password_keeps_user_on_login_page(self, login_page, driver):
        """
        Тест: Неверный пароль оставляет пользователя на странице входа.
        Проверка: Поле ввода Email должно оставаться видимым.
        """
        # 1. Действия
        login_page.open()
        login_page.go_to_login_form()
        
        # Вводим данные
        login_page.enter_email("Kseniya_Kraeva_50131@mail.ru")
        login_page.enter_password("wrong_password_123")  # Неверный пароль
        login_page.click_login_button()

        # 2. ЕДИНСТВЕННАЯ ПРОВЕРКА (1 тест = 1 проверка)
        assert login_page.is_login_form_visible(), \
            "Ошибка: Поле ввода Email исчезло. Это значит, что пользователь успешно вошёл с неверным паролем!"
        
        logger.info("Тест пройден: пользователь остался на странице входа, поле Email видно.")
