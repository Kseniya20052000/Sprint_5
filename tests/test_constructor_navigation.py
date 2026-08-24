#Тест перехода в конструктор после входа в аккаунт

import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL

logger = logging.getLogger(__name__)

    

    

class TestConstructorNavigation:
    def test_navigate_to_constructor_after_login(self, setup_pages):
        """
        Тест перехода в конструктор после входа в аккаунт:
        1. Открыть главную страницу
        2. Нажать «Войти в аккаунт»
        3. На странице входа нажать кнопку «Конструктор»
        4. Проверить наличие надписи «Соберите бургер»
        """
        driver = setup_pages['driver']
        URL = BASE_URL
        main_page = setup_pages['main_page']
        login_page = setup_pages['login_page']

        logger.info("1. Открываем главную страницу")
        login_page.open() 

        logger.info("2. Кликаем на кнопку «Войти в аккаунт»")
        login_page.go_to_login_form()
        
        login_page.wait_for_url_contains("/login")

        logger.info("3. На странице входа кликаем на кнопку «Конструктор» в шапке")
        main_page.click_constructor_button()

        logger.info("4. Ждём появления надписи «Соберите бургер»")
        main_page.wait_for_burger_assembly_text()

        logger.info("5. Проверяем, что надпись «Соберите бургер» отображается")
        assert main_page.is_burger_assembly_text_visible(), \
            "Надпись «Соберите бургер» не отображается на странице конструктора"

        
        current_url = driver.current_url
        assert BASE_URL in current_url, \
            f"Ожидался URL {BASE_URL}, но получен: {current_url}"
        logger.info("Тест пройден: пользователь успешно вошёл через поток восстановления пароля")
