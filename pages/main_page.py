from selenium.webdriver.common.by import By
from base_page import BasePage
from locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    # Локатор кнопки "Личный кабинет". 
    # Ищем ссылку, в которой есть текст "Личный Кабинет" или href="/account"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, '/account')]")

    def click_personal_account(self):
        button = self.wait_for_element_to_be_clickable(self.BUTTON_PERSONAL_ACCOUNT)
        button.click()


    def click_login_button(self):
        """Кликает на кнопку «Войти» на главной странице"""
        login_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        )
        login_button.click()