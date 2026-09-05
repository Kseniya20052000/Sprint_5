import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.constructor_page import ConstructorPage
from locators import BASE_URL
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Настраиваем опции браузера
    options = Options()
    # Раскомментируйте нужные опции:
    # options.add_argument("--headless")  # без GUI
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    # Автоматически скачиваем и настраиваем ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Создаём драйвер с сервисом и опциями
    driver = webdriver.Chrome(service=service, options=options)
    
    # Настройка неявного ожидания (опционально)
    driver.implicitly_wait(10)
    
    yield driver  # передаём драйвер в тест
    
    # Закрываем драйвер после теста
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)

@pytest.fixture
def constructor_page(driver):
    """Фикстура для инициализации страницы конструктора"""
    driver.get(BASE_URL)
    return ConstructorPage(driver)

@pytest.fixture(scope="function")
def setup_pages(driver):
    pages = {
        'driver': driver,
        'base_url': BASE_URL,
        'main_page': MainPage(driver),
        'login_page': LoginPage(driver),
        'forgot_password_page': ForgotPasswordPage(driver)
    }
    return pages
