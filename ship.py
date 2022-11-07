import pygame


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('src/image/space_ship.png')
        self.rect = self.image.get_rect()
        # Створюється кожний новий корабель по центру екрану
        self.rect.midbottom = self.screen_rect.midbottom
        # Зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)
        # Індикатор руху
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Оновити поточну позицію корабля на основі індикатору руху"""

        # Рух корабля та запобігання виходу його за межі екрану
        # З правого боку
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # З лівого боку
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Оновити об`ект rect з self.x
        self.rect.x = self.x

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""

        self.screen.blit(self.image, self.rect)
