from selenium.webdriver.common.by import By
BASE_URL = "https://stellarburgers.education-services.ru"

class MainPageLocators:
    BASE_URL = BASE_URL
    # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    BUTTON_CONSTRUCTOR = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2")
    BURGER_ASSEMBLY_TEXT = (By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10")
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    # Кнопка «Личный кабинет»
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, '/account')]")


    # Кнопка «Выход» в личном кабинете
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Заголовок главной страницы (для проверки загрузки)
    MAIN_PAGE_HEADER = (By.CSS_SELECTOR, "h1.text.text_type_main-large")

    # Заголовок личного кабинета (для проверки загрузки)
    PERSONAL_ACCOUNT_HEADER = (By.CSS_SELECTOR, "h2.text.text_type_main-medium")


class LoginPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj' and contains(text(), 'Восстановить пароль')]")
    BASE_URL = BASE_URL

    
class RegisterPageLocators:
    LINK_REGISTER = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    INPUT_NAME = (By.NAME, "name")
    INPUT_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    BASE_URL = BASE_URL
class ForgotPasswordPageLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']")
    BASE_URL = BASE_URL

class ConstructorLocators:
    # Кнопки разделов (табы)
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")

    # Заголовки разделов на странице
    HEADER_BUNS = (By.XPATH, "//h2[text()='Булки']")
    HEADER_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    HEADER_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")
    BASE_URL = BASE_URL

    