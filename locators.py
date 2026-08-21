from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    # Ищем button, внутри которого есть текст "Войти в аккаунт"
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
class LoginPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

    
class RegisterPageLocators:
    LINK_REGISTER = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    INPUT_NAME = (By.NAME, "name")
    INPUT_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

