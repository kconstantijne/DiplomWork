class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізація всіх налаштувань гри"""

        # Задається розміри вікна
        self.screen_width = 1200
        self.screen_height = 800

        # Задається колір фону
        self.bg_color = (0, 128, 128)

        # Задається швідкість корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (55, 55, 55)
        self.bullets_allowed = 10

        # Налаштування прибульця
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # fleet_direction 1 означає напрямок руху праворуч, а -1 - ліворуч
        self.fleet_direction = 1
