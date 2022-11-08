class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізація всіх налаштувань гри"""

        # Задається розміри вікна
        self.screen_width = 1200
        self.screen_height = 800

        # Задається колір фону
        self.bg_color = (86, 55, 240)

        # Задається швідкість корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (214, 40, 40)
        self.bullets_allowed = 10

        # Налаштування прибульця
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Як швидко гра має прискорюватися
        self.speedup_scale = 1.5
        # Як швидко збільшуеться вартість прибульця
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # fleet_direction 1 означає напрямок руху праворуч, а -1 - ліворуч
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""

        self.ship_speed = 1.5
        self.ship_limit = 3
        self.alien_speed = 1.0
        # fleet_direction 1 означає напрямок руху праворуч, а -1 - ліворуч
        self.fleet_direction = 1
        # Отримання балів
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості та вартості прибульців"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
