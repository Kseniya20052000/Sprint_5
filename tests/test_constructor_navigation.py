#Тест перехода в конструктор после входа в аккаунт

import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL

logger = logging.getLogger(__name__)

    

    

class TestConstructorNavigation:
    def test_constructor_button_navigates_to_constructor(self, setup_pages):
        """
        Проверяет, что кнопка «Конструктор» на странице входа переводит пользователя
        в раздел конструктора (по наличию надписи «Соберите бургер»).
        """
        driver = setup_pages['driver']
        main_page = setup_pages['main_page']
        login_page = setup_pages['login_page']

        logger.info("1. Открываем главную страницу")
        login_page.open()

        logger.info("2. Кликаем на кнопку «Войти в аккаунт»")
        login_page.go_to_login_form()
        login_page.wait_for_url_contains("/login")

        logger.info("3. На странице входа кликаем на кнопку «Конструктор» в шапке")
        main_page.click_constructor_button()

        # Дополнительная проверка URL как часть ожидания 
        logger.info("4. Ждём загрузки страницы конструктора (проверка URL)")
        login_page.wait_for_url_contains(BASE_URL)

        logger.info("5. Ждём появления надписи «Соберите бургер»")
        main_page.wait_for_burger_assembly_text()

        logger.info("6. Проверяем, что надпись «Соберите бургер» отображается (главный ассерт)")
        assert main_page.is_burger_assembly_text_visible(), \
            "Надпись «Соберите бургер» не отображается на странице конструктора — " \
            "кнопка «Конструктор» не сработала или страница не загрузилась корректно"