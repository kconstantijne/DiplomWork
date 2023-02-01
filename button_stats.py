import pygame.font


class ButtonStatistic:

    def __init__(self, ai_game, msg):
        """Ігіціалізація атрибутів кнопки"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Задати розміри та властивості кнопки
        self.width, self.height = 400, 50
        self.button_color = (86, 55, 240)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 35)

        # Створити об'єкт rect та відцентрувати його
        self.rect = pygame.Rect(120.0, 0, self.width, self.height)
        self.rect.bottomleft = self.screen_rect.bottomleft

        # Повідомлення на кнопці треба показати лише один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворити текст на зображення та розмістити його по центру кнопки"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.bottomleft = self.rect.bottomleft

    def draw_button(self):
        # Намалювати порожню кнопку, а потім - повідомлення
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
