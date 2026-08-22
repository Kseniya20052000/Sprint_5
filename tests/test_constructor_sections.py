#тест для проверки разделов конструктора

import pytest
import logging
from pages.constructor_page import ConstructorPage

logger = logging.getLogger(__name__)

class TestConstructorSections:

    def test_constructor_tabs_navigation(self, constructor_page):
        """
        Тест переходов между разделами конструктора:
        1. Открыть главную страницу
        2. Кликнуть на вкладку «Соусы»
        3. Проверить отображение заголовка «Соусы»
        4. Кликнуть на вкладку «Начинки»
        5. Проверить отображение заголовка «Начинки»
        6. Кликнуть на вкладку «Булки»
        7. Проверить отображение заголовка «Булки»
        """

        # 1. Переход к разделу «Соусы»
        logger.info("1. Кликаем на вкладку «Соусы»")
        constructor_page.click_sauces_tab()

        logger.info("2. Проверяем отображение заголовка «Соусы»")
        assert constructor_page.is_sauces_header_visible(), \
            "Заголовок «Соусы» не отображается после клика на вкладку"

        # 2. Переход к разделу «Начинки»
        logger.info("3. Кликаем на вкладку «Начинки»")
        constructor_page.click_fillings_tab()

        logger.info("4. Проверяем отображение заголовка «Начинки»")
        assert constructor_page.is_fillings_header_visible(), \
            "Заголовок «Начинки» не отображается после клика на вкладку"

        # 3. Переход к разделу «Булки»
        logger.info("5. Кликаем на вкладку «Булки»")
        constructor_page.click_buns_tab()
        logger.info("6. Проверяем отображение заголовка «Булки»")
        assert constructor_page.is_buns_header_visible(), \
            "Заголовок «Булки» не отображается после клика на вкладку"


        logger.info("Тест пройден: все разделы конструктора работают корректно")