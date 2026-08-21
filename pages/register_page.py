from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
import random
import string

class RegisterPage(BasePage):
    def click_register_link(self):
        """Кликает на ссылку «Зарегистрироваться»"""
        register_link = self.wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.LINK_REGISTER)
        )
        register_link.click()

    def enter_name(self, name):
        """Вводит имя в поле ввода"""
        name_field = self.wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.INPUT_NAME)
        )
        name_field.clear()
        name_field.send_keys(name)

    def enter_email(self, email):
        """Вводит email в поле ввода"""
        email_field = self.wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.INPUT_EMAIL)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Вводит пароль в поле ввода"""
        password_field = self.wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.INPUT_PASSWORD)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_register_button(self):
        """Кликает на кнопку «Зарегистрироваться»»"""
        register_button = self.wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.BUTTON_REGISTER)
        )
        register_button.click()

    def generate_random_name(self):
        """Генерирует случайное имя"""
        return ''.join(random.choices(string.ascii_letters, k=8))

    def generate_random_email(self):
        """Генерирует случайный email"""
        username = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"{username}@test.com"

    def generate_random_password(self):
        """Генерирует случайный 6‑значный пароль"""
        return ''.join(random.choices(string.digits, k=6))
