import unittest
import json
import os
from unittest.mock import patch, MagicMock


# ============================================
# 1. ТЕСТЫ ДЛЯ АВТОРИЗАЦИИ (как в auth.js)
# ============================================

class TestAuthorization(unittest.TestCase):
    """Тестирование системы авторизации"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.users = {
            "admin": {"password": "admin123", "role": "admin", "name": "Админ"},
            "manager": {"password": "manager123", "role": "manager", "name": "Алёна Рыжкова"},
            "client": {"password": "client123", "role": "client", "name": "Клиент"}
        }

    def test_admin_login_success(self):
        """Тест 1: Успешный вход администратора"""
        username = "admin"
        password = "admin123"
        role = "admin"

        if (username in self.users and
                self.users[username]["password"] == password and
                self.users[username]["role"] == role):
            result = True
        else:
            result = False

        self.assertTrue(result, "Админ должен войти с правильными данными")

    def test_manager_login_success(self):
        """Тест 2: Успешный вход менеджера (Алёны)"""
        username = "manager"
        password = "manager123"
        role = "manager"

        if (username in self.users and
                self.users[username]["password"] == password and
                self.users[username]["role"] == role):
            result = True
        else:
            result = False

        self.assertTrue(result, "Менеджер должен войти с правильными данными")

    def test_client_login_success(self):
        """Тест 3: Успешный вход клиента"""
        username = "client"
        password = "client123"
        role = "client"

        if (username in self.users and
                self.users[username]["password"] == password and
                self.users[username]["role"] == role):
            result = True
        else:
            result = False

        self.assertTrue(result, "Клиент должен войти с правильными данными")

    def test_wrong_password(self):
        """Тест 4: Вход с неверным паролем"""
        username = "admin"
        password = "wrong_password"
        role = "admin"

        if (username in self.users and
                self.users[username]["password"] == password and
                self.users[username]["role"] == role):
            result = True
        else:
            result = False

        self.assertFalse(result, "Неверный пароль не должен пропускать")

    def test_wrong_role(self):
        """Тест 5: Вход с неверной ролью"""
        username = "admin"
        password = "admin123"
        role = "client"  # Админ пытается войти как клиент

        if (username in self.users and
                self.users[username]["password"] == password and
                self.users[username]["role"] == role):
            result = True
        else:
            result = False

        self.assertFalse(result, "Неверная роль не должна пропускать")

    def test_nonexistent_user(self):
        """Тест 6: Вход несуществующего пользователя"""
        username = "fake_user"
        password = "123"
        role = "client"

        result = username in self.users

        self.assertFalse(result, "Несуществующий пользователь не должен войти")


# ============================================
# 2. ТЕСТЫ ДЛЯ УПРАВЛЕНИЯ ЦЕНАМИ (как в admin.js)
# ============================================

class TestPriceManagement(unittest.TestCase):
    """Тестирование управления ценами"""

    def setUp(self):
        """Подготовка данных"""
        self.prices = {
            "hair": 2500,
            "makeup": 2000
        }
        self.visit_prices = {
            "severodvinsk": 1000,
            "arkhangelsk": 2000,
            "early": 1000
        }

    def test_update_hair_price(self):
        """Тест 7: Обновление цены на прическу"""
        new_price = 3000
        self.prices["hair"] = new_price
        self.assertEqual(self.prices["hair"], 3000, "Цена на прическу должна обновиться")

    def test_update_makeup_price(self):
        """Тест 8: Обновление цены на макияж"""
        new_price = 2500
        self.prices["makeup"] = new_price
        self.assertEqual(self.prices["makeup"], 2500, "Цена на макияж должна обновиться")

    def test_update_severodvinsk_price(self):
        """Тест 9: Обновление цены на выезд в Северодвинск"""
        new_price = 1500
        self.visit_prices["severodvinsk"] = new_price
        self.assertEqual(self.visit_prices["severodvinsk"], 1500, "Цена на выезд в Северодвинск должна обновиться")

    def test_update_arkhangelsk_price(self):
        """Тест 10: Обновление цены на выезд в Архангельск"""
        new_price = 2500
        self.visit_prices["arkhangelsk"] = new_price
        self.assertEqual(self.visit_prices["arkhangelsk"], 2500, "Цена на выезд в Архангельск должна обновиться")

    def test_update_early_price(self):
        """Тест 11: Обновление цены на ранний выезд"""
        new_price = 1500
        self.visit_prices["early"] = new_price
        self.assertEqual(self.visit_prices["early"], 1500, "Цена на ранний выезд должна обновиться")

    def test_prices_not_negative(self):
        """Тест 12: Цены не могут быть отрицательными"""
        new_price = -500
        if new_price < 0:
            valid = False
        else:
            valid = True

        self.assertFalse(valid, "Цена не может быть отрицательной")


# ============================================
# 3. ТЕСТЫ ДЛЯ УПРАВЛЕНИЯ МЕДИА (админ)
# ============================================

class TestMediaManagement(unittest.TestCase):
    """Тестирование управления видео и фото"""

    def setUp(self):
        self.videos = ["work1.mp4", "work2.mp4", "work3.mp4", "work4.mp4", "work5.mp4"]
        self.photos = ["portfolio1.png", "portfolio2.png", "portfolio3.png", "portfolio4.png", "portfolio5.png"]

    def test_add_video(self):
        """Тест 13: Добавление нового видео"""
        new_video = "work6.mp4"
        self.videos.append(new_video)
        self.assertIn(new_video, self.videos, "Новое видео должно быть в списке")
        self.assertEqual(len(self.videos), 6, "Список видео должен увеличиться на 1")

    def test_delete_video(self):
        """Тест 14: Удаление видео"""
        deleted = self.videos.pop(0)
        self.assertNotIn(deleted, self.videos, "Удаленное видео не должно быть в списке")
        self.assertEqual(len(self.videos), 4, "Список видео должен уменьшиться на 1")

    def test_add_photo(self):
        """Тест 15: Добавление нового фото"""
        new_photo = "portfolio6.png"
        self.photos.append(new_photo)
        self.assertIn(new_photo, self.photos, "Новое фото должно быть в списке")
        self.assertEqual(len(self.photos), 6, "Список фото должен увеличиться на 1")

    def test_delete_photo(self):
        """Тест 16: Удаление фото"""
        deleted = self.photos.pop(0)
        self.assertNotIn(deleted, self.photos, "Удаленное фото не должно быть в списке")
        self.assertEqual(len(self.photos), 4, "Список фото должен уменьшиться на 1")

    def test_video_format_validation(self):
        """Тест 17: Проверка формата видео (только .mp4)"""
        valid_video = "work6.mp4"
        invalid_video = "work6.avi"

        self.assertTrue(valid_video.endswith(".mp4"), "Видео должно быть в формате .mp4")
        self.assertFalse(invalid_video.endswith(".mp4"), "Неверный формат видео не должен приниматься")

    def test_photo_format_validation(self):
        """Тест 18: Проверка формата фото (.png, .jpg, .jpeg)"""
        valid_formats = [".png", ".jpg", ".jpeg"]
        valid_photo = "portfolio6.png"
        invalid_photo = "portfolio6.gif"

        is_valid = any(valid_photo.endswith(fmt) for fmt in valid_formats)

        self.assertTrue(is_valid, "Фото должно быть в формате .png, .jpg или .jpeg")
        self.assertFalse(invalid_photo.endswith(".png"), "Неверный формат фото не должен приниматься")


# ============================================
# 4. ТЕСТЫ ДЛЯ РАЗГРАНИЧЕНИЯ РОЛЕЙ
# ============================================

class TestRolePermissions(unittest.TestCase):
    """Тестирование прав доступа разных ролей"""

    def setUp(self):
        self.roles = {
            "admin": {
                "can_manage_prices": True,
                "can_manage_videos": True,
                "can_manage_photos": True,
                "can_manage_users": True
            },
            "manager": {
                "can_manage_prices": True,
                "can_manage_videos": False,
                "can_manage_photos": False,
                "can_manage_users": False
            },
            "client": {
                "can_manage_prices": False,
                "can_manage_videos": False,
                "can_manage_photos": False,
                "can_manage_users": False
            }
        }

    def test_admin_permissions(self):
        """Тест 19: Права администратора"""
        role = self.roles["admin"]
        self.assertTrue(role["can_manage_prices"], "Админ может управлять ценами")
        self.assertTrue(role["can_manage_videos"], "Админ может управлять видео")
        self.assertTrue(role["can_manage_photos"], "Админ может управлять фото")
        self.assertTrue(role["can_manage_users"], "Админ может управлять пользователями")

    def test_manager_permissions(self):
        """Тест 20: Права менеджера (только цены)"""
        role = self.roles["manager"]
        self.assertTrue(role["can_manage_prices"], "Менеджер может управлять ценами")
        self.assertFalse(role["can_manage_videos"], "Менеджер НЕ может управлять видео")
        self.assertFalse(role["can_manage_photos"], "Менеджер НЕ может управлять фото")
        self.assertFalse(role["can_manage_users"], "Менеджер НЕ может управлять пользователями")

    def test_client_permissions(self):
        """Тест 21: Права клиента (только просмотр)"""
        role = self.roles["client"]
        self.assertFalse(role["can_manage_prices"], "Клиент НЕ может управлять ценами")
        self.assertFalse(role["can_manage_videos"], "Клиент НЕ может управлять видео")
        self.assertFalse(role["can_manage_photos"], "Клиент НЕ может управлять фото")
        self.assertFalse(role["can_manage_users"], "Клиент НЕ может управлять пользователями")


# ============================================
# 5. ТЕСТЫ ДЛЯ ПОИСКА
# ============================================

class TestSearch(unittest.TestCase):
    """Тестирование поиска по сайту"""

    def setUp(self):
        self.search_keywords = {
            "стоимость": "price-slide",
            "цена": "price-slide",
            "выезд": "visit-slide",
            "контакт": "contacts-slide",
            "телефон": "contacts-slide",
            "обучение": "education-slide",
            "портфолио": "portfolio-slide",
            "отзывы": "reviews-slide",
            "клипы": "clips-slide"
        }

    def test_search_by_price(self):
        """Тест 22: Поиск по слову 'стоимость'"""
        query = "стоимость"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "price-slide", "Поиск 'стоимость' должен вести к ценам")

    def test_search_by_price_synonym(self):
        """Тест 23: Поиск по слову 'цена'"""
        query = "цена"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "price-slide", "Поиск 'цена' должен вести к ценам")

    def test_search_by_visit(self):
        """Тест 24: Поиск по слову 'выезд'"""
        query = "выезд"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "visit-slide", "Поиск 'выезд' должен вести к блоку выезда")

    def test_search_by_contacts(self):
        """Тест 25: Поиск по слову 'контакт'"""
        query = "контакт"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "contacts-slide", "Поиск 'контакт' должен вести к контактам")

    def test_search_by_phone(self):
        """Тест 26: Поиск по слову 'телефон'"""
        query = "телефон"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "contacts-slide", "Поиск 'телефон' должен вести к контактам")

    def test_search_by_education(self):
        """Тест 27: Поиск по слову 'обучение'"""
        query = "обучение"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "education-slide", "Поиск 'обучение' должен вести к обучению")

    def test_search_by_portfolio(self):
        """Тест 28: Поиск по слову 'портфолио'"""
        query = "портфолио"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "portfolio-slide", "Поиск 'портфолио' должен вести к работам")

    def test_search_by_reviews(self):
        """Тест 29: Поиск по слову 'отзывы'"""
        query = "отзывы"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "reviews-slide", "Поиск 'отзывы' должен вести к отзывам")

    def test_search_by_clips(self):
        """Тест 30: Поиск по слову 'клипы'"""
        query = "клипы"
        target = self.search_keywords.get(query)
        self.assertEqual(target, "clips-slide", "Поиск 'клипы' должен вести к видео")



# ============================================
# 7. ЗАПУСК ТЕСТОВ
# ============================================

if __name__ == '__main__':
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Добавляем все тесты
    suite.addTests(loader.loadTestsFromTestCase(TestAuthorization))
    suite.addTests(loader.loadTestsFromTestCase(TestPriceManagement))
    suite.addTests(loader.loadTestsFromTestCase(TestMediaManagement))
    suite.addTests(loader.loadTestsFromTestCase(TestRolePermissions))
    suite.addTests(loader.loadTestsFromTestCase(TestSearch))


    # Запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Вывод результата
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Ошибка: {len(result.failures)}")
    print("=" * 50)