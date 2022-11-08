import pygame.mouse


class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики"""

        self.settings = ai_game.settings
        self.reset_stats()
        # Розпочати гру в активному стані
        self.game_active = False
        pygame.mouse.set_visible(True)

    def reset_stats(self):
        """ніціалізація статистики, що може змінюватись вродовж гри"""
        self.ships_left = self.settings.ship_limit
