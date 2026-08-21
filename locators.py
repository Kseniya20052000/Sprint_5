from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    # Ищем button, внутри которого есть текст "Войти в аккаунт"
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
class LoginPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

    
