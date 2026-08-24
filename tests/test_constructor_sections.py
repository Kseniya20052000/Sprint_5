import pytest
import logging
from pages.constructor_page import ConstructorPage

logger = logging.getLogger(__name__)

class TestConstructorSections:

    def test_sauces_tab_navigation(self, constructor_page):
        """Тест перехода к разделу «Соусы» и проверки активности вкладки"""
        logger.info("Шаг 1. Кликаем на вкладку «Соусы»")
        constructor_page.click_sauces_tab()

        logger.info("Шаг 2. Проверяем активность вкладки «Соусы»")
        assert constructor_page.is_sauces_tab_active(), \
            "Вкладка «Соусы» не стала активной после клика"

        logger.info("Тест пройден: вкладка «Соусы» активна")

    def test_fillings_tab_navigation(self, constructor_page):
        """Тест перехода к разделу «Начинки» и проверки активности вкладки"""
        logger.info("Шаг 1. Кликаем на вкладку «Начинки»")
        constructor_page.click_fillings_tab()

        logger.info("Шаг 2. Проверяем активность вкладки «Начинки»")
        assert constructor_page.is_fillings_tab_active(), \
            "Вкладка «Начинки» не стала активной после клика"

        logger.info("Тест пройден: вкладка «Начинки» активна")

    def test_buns_tab_navigation(self, constructor_page):
        """Тест перехода к разделу «Булки» и проверки активности вкладки"""
        logger.info("Шаг 1. Кликаем на вкладку «Соусы», чтобы уйти с текущего раздела")
        constructor_page.click_sauces_tab()


        logger.info("Шаг 2. Кликаем на вкладку «Булки»")
        constructor_page.click_buns_tab()


        logger.info("Шаг 3. Проверяем активность вкладки «Булки»")
        assert constructor_page.is_buns_tab_active(), \
            "Вкладка «Булки» не стала активной после клика"

        logger.info("Тест пройден: вкладка «Булки» активна")

