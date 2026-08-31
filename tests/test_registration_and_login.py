#Тест регистрации нового пользователя с последующим входом в систему

import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
import logging
from locators import BASE_URL
from helpers.test_data_helper import TestDataHelper

logger = logging.getLogger(__name__)


class TestRegistrationAndLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_registration_followed_by_login(self, driver):
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        logger.info("1. Открываем главную страницу")
        login_page.open() 

        logger.info("2. Кликаем на кнопку «Войти»")
        login_page.go_to_login_form()

        logger.info("3. Ждём перехода на страницу входа (/login)")
        self.login_page.wait_for_url_contains("/login")

        logger.info("4. Кликаем на ссылку «Зарегистрироваться»")
        self.register_page.click_register_link()

        logger.info("5. Ждём перехода на страницу регистрации (/register)")
        

        # Генерируем случайные данные
        self.register_page.wait_for_url_contains("/register")

        # Получаем случайные данные через хелпер
        registration_data = TestDataHelper.get_registration_data()

        # Используем данные в тесте
        self.register_page.enter_name(registration_data['name'])
        self.register_page.enter_email(registration_data['email'])
        self.register_page.enter_password(registration_data['password'])

        registration_data = TestDataHelper.get_registration_data()

        

        logger.info("7. Кликаем на кнопку «Зарегистрироваться»")
        self.register_page.click_register_button()

        logger.info("8. Ждём перехода обратно на страницу входа (/login) после регистрации")
        self.login_page.wait_for_url_contains("/login")


        logger.info("9. Вводим данные, с которыми только что зарегистрировались")
        self.login_page.enter_email(registration_data['email'])
        self.login_page.enter_password(registration_data['password'])

        logger.info("10. Кликаем на кнопку «Войти»")
        login_page.click_login_button()


        
        logger.info("11. Ждём перехода на главную страницу после успешного входа")
        self.main_page.wait_for_url_contains(BASE_URL)  

        assert BASE_URL in self.driver.current_url, "Не перешли на главную страницу после входа"

