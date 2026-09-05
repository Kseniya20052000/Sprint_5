#вход через клик "личный кабинет"

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import VALID_USER

class TestLoginFlow:
    
    def test_click_personal_account_redirects_to_login(self, driver):
        
        # 1. Инициализируем страницы
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # 2. Открываем главную страницу
        login_page.open() 
        
        # 3. Кликаем на кнопку "Личный кабинет"
        main_page.click_personal_account()
        
        # 4. Ждем, пока URL изменится на /login
        # Это доказывает, что произошел переход на новую страницу (или состояние)
        login_page.wait_for_url_contains("/login")
        
        
        login_page.enter_email(VALID_USER["email"])
        login_page.enter_password(VALID_USER["password"])
        login_page.click_login_button()
        
        # 5. Финальная проверка URL 
        assert "/login" in driver.current_url, f"Ожидался URL с '/login', но получен: {driver.current_url}"


