import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://stellarburgers.education-services.ru"

class TestRegistrationAndLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_registration_followed_by_login(self, driver):
        """Тест регистрации нового пользователя с последующим входом в систему"""
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
        self.register_page.wait_for_url_contains("/register")

        # Генерируем случайные данные
        random_name = self.register_page.generate_random_name()
        random_email = self.register_page.generate_random_email()
        random_password = self.register_page.generate_random_password()

        logger.info(f"6. Вводим данные для регистрации: имя={random_name}, email={random_email}, пароль={random_password}")

        self.register_page.enter_name(random_name)
        self.register_page.enter_email(random_email)
        self.register_page.enter_password(random_password)


        logger.info("7. Кликаем на кнопку «Зарегистрироваться»")
        self.register_page.click_register_button()

        logger.info("8. Ждём перехода обратно на страницу входа (/login) после регистрации")
        self.login_page.wait_for_url_contains("/login")


        logger.info("9. Вводим данные, с которыми только что зарегистрировались")
        self.login_page.enter_email(random_email)
        self.login_page.enter_password(random_password)

        logger.info("10. Кликаем на кнопку «Войти»")
        login_page.click_login_button()


        logger.info("11. Ждём перехода на главную страницу после успешного входа")
        self.main_page.wait_for_url_contains(BASE_URL)

        logger.info("12. Проверяем, что пользователь успешно вошёл в систему")
        current_url = self.login_page.get_current_url()
        assert BASE_URL in current_url, \
            f"Ожидался URL {BASE_URL}, но получен: {current_url}"

        logger.info("Тест пройден: пользователь успешно зарегистрировался и вошёл в систему")
