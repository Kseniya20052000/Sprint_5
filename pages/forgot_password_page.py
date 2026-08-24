from base_page import BasePage
from locators import LoginPageLocators, MainPageLocators, ForgotPasswordPageLocators
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordPage(BasePage):
    def click_login_link(self):
        """Кликает на ссылку «Войти» на странице восстановления пароля"""
        login_link = self.wait.until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.BUTTON_LOGIN)
        )
        login_link.click()