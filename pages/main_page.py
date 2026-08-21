from selenium.webdriver.common.by import By
from base_page import BasePage

class MainPage(BasePage):
    # Локатор кнопки "Личный кабинет". 
    # Ищем ссылку, в которой есть текст "Личный Кабинет" или href="/account"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, '/account')]")

    def click_personal_account(self):
        button = self.wait_for_element_to_be_clickable(self.BUTTON_PERSONAL_ACCOUNT)
        button.click()
