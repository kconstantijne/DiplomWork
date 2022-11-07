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

        # Налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (55, 55, 55)
        self.bullets_allowed = 5
