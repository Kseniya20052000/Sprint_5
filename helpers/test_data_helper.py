import random
import string

class TestDataHelper:
    @staticmethod
    def generate_random_name(length=8):
        """Генерирует случайное имя заданной длины"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_email(domain="test.com", length=8):
        """Генерирует случайный email"""
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return f"{username}@{domain}"

    @staticmethod
    def generate_random_password(length=10):
        """Генерирует случайный пароль"""
        chars = string.ascii_letters + string.digits + "!@#$%"
        return ''.join(random.choice(chars) for _ in range(length))

    @classmethod
    def get_registration_data(cls):
        """Возвращает готовый набор данных для регистрации"""
        return {
            'name': cls.generate_random_name(),
            'email': cls.generate_random_email(),
            'password': cls.generate_random_password()
        }
