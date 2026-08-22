import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.constructor_page import ConstructorPage


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)



@pytest.fixture(scope="function")
def setup_pages(driver, base_url):
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from pages.forgot_password_page import ForgotPasswordPage

    pages = {
        'driver': driver,
        'base_url': base_url,
        'main_page': MainPage(driver),
        'login_page': LoginPage(driver),
        'forgot_password_page': ForgotPasswordPage(driver)
    }
    return pages


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL приложения"""
    return "https://stellarburgers.education-services.ru/" 

@pytest.fixture
def constructor_page(driver, base_url):
    """Фикстура для инициализации страницы конструктора"""
    driver.get(base_url)
    return ConstructorPage(driver)