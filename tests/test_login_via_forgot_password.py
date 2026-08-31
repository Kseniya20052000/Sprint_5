#Тест входа через кнопку в форме восстановления пароля

import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL
logger = logging.getLogger(__name__)


class TestLoginViaForgotPassword:
    def test_login_through_forgot_password_flow(self, setup_pages):
        
        driver = setup_pages['driver']
        base_url = setup_pages['base_url']
        main_page = setup_pages['main_page']
        login_page = setup_pages['login_page']
        forgot_password_page = setup_pages['forgot_password_page']

        logger.info("1. Открываем главную страницу")
        login_page.open() 

        logger.info("2. Кликаем на кнопку «Войти в аккаунт»")
        login_page.go_to_login_form()

        login_page.wait_for_url_contains("/login")


        logger.info("3. Кликаем на ссылку «Восстановить пароль»")
        login_page.click_forgot_password_link()
        forgot_password_page.wait_for_url_contains("/forgot-password")

        logger.info("4. Кликаем на кнопку «Войти» на странице восстановления")
        forgot_password_page.click_login_link()
        login_page.wait_for_url_contains("/login")

        logger.info("5. Вводим рабочие email и пароль")
        login_page.enter_email("kseniya_kraeva_50131@mail.ru")
        login_page.enter_password("12345678789")

        logger.info("6. Кликаем на кнопку «Войти»")
        login_page.click_login_button()

        assert main_page.is_burger_assembly_text_visible(), \
            "Ошибка: Кнопка «Оформить заказ» не отображается. Пользователь не авторизован или страница не загрузилась."
                
        logger.info("Тест пройден: кнопка «Оформить заказ» видна, пользователь авторизован.")
