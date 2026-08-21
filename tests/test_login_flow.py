import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginFlow:
    
    def test_click_personal_account_redirects_to_login(self, driver):
        
        # 1. Инициализируем страницы
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # 2. Открываем главную страницу
        login_page.open() 
        
        # 3. Кликаем на кнопку "Личный кабинет"
        main_page.click_personal_account()
        
        # 4. ПРОВЕРКА 1: Ждем, пока URL изменится на /login
        # Это доказывает, что произошел переход на новую страницу (или состояние)
        login_page.wait_for_url_contains("/login")
        
        # 5. ПРОВЕРКА 2: Убеждаемся, что форма входа действительно отрисовалась
        assert login_page.is_login_form_visible(), "Форма входа не появилась после перехода"
        
        # 6. Финальная проверка URL (для отчета в консоль)
        assert "/login" in driver.current_url, f"Ожидался URL с '/login', но получен: {driver.current_url}"
