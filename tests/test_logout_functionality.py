#тест для проверки выхода из аккаунта через кнопку «Выход» в личном кабинете

import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL

logger = logging.getLogger(__name__)

class TestLogoutFunctionality:
    def test_logout_via_personal_account(self, setup_pages):
        """
        Тест выхода из аккаунта через кнопку «Выход» в личном кабинете:
        1. Открыть главную страницу
        2. Войти в аккаунт с корректными данными
        3. Перейти в личный кабинет
        4. Нажать кнопку «Выход»
        5. Проверить переход на страницу авторизации
        """
        driver = setup_pages['driver']
        URL = BASE_URL
        main_page = setup_pages['main_page']
        login_page = setup_pages['login_page']

        logger.info("1. Открываем главную страницу")
        driver.get(URL)

        logger.info("2. Кликаем на кнопку «Войти в аккаунт»")
        login_page.go_to_login_form()

        logger.info("3. Вводим корректные данные для входа")
        login_page.enter_email("kseniya_kraeva_50131@mail.ru")
        login_page.enter_password("12345678789")

        logger.info("4. Выполняем вход в аккаунт")
        login_page.click_login_button()

        # Ждём загрузки главной страницы после входа
        main_page.wait_for_main_page_load()

        logger.info("5. Кликаем на кнопку «Личный кабинет»")
        main_page.click_personal_account()

        

        logger.info("6. Находим и нажимаем кнопку «Выход»")
        main_page.click_logout_button()


        logger.info("7. Ждём перехода на страницу входа (/login)")
        login_page.wait_for_url_contains("/login")

        # 8. Финальная проверка URL 
        assert "/login" in driver.current_url, f"Ожидался URL с '/login', но получен: {driver.current_url}"