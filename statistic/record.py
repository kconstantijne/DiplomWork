import pygame
from statistic.statistic_settings import StatisticSettings


class Record:
    def __init__(self, ai_stats):
        self.settings = StatisticSettings()
        self.ai_stats = ai_stats
        self.screen = ai_stats.screen
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 28)

    def show_record(self, user_name, high_score, high_level):
        msg = f"Hello, {user_name}." \
              f"Your high score is: {high_score}. And level was {high_level}"
        self.record_image = self.font.render(msg, True, self.text_color, self.settings.background_color)
        self.record_rect = self.record_image.get_rect()
        self.record_rect.left = self.record_rect.left + 20
        self.record_rect.top = 20
        self.screen.blit(self.record_image, self.record_rect)
