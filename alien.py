import random

import pygame
from pygame.sprite import Sprite


def random_alien_in_fleet():
    c = random.randint(0, 2)
    if c == 0:
        return 'src/image/alien_first.png'
    elif c == 1:
        return 'src/image/alien_second.png'
    elif c == 2:
        return 'src/image/alien_third.png'


class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""

    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""

        super().__init__()
        self.screen = ai_game.screen

        # Завантажує зображення прибульця та отримати його rect
        self.image = pygame.image.load(random_alien_in_fleet())
        self.rect = self.image.get_rect()

        # Створюється кожного нового прибульця з краю екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Зберегти десяткове значення для позиції прибульця
        self.x = float(self.rect.x)
