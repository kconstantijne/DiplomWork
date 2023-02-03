import pygame
from statistic.statistic_settings import StatisticSettings
from statistic.record import Record


class AIStatistic:
    def __init__(self, ai_stats):
        self.settings = StatisticSettings()
        self.ai_stats = ai_stats
        self.screen = ai_stats.screen
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.record = Record(self)

    def stat_window(self, user_name, high_score, high_level):
        screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption(self.settings.title)
        pygame.display.set_icon(self.settings.img)
        screen.fill(self.settings.background_color)
        self.record.show_record(user_name, high_score, high_level)
        pygame.display.flip()
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.set_mode(self.settings.previous_window)
                    pygame.display.set_icon(self.settings.previous_img)
                    pygame.display.set_caption(self.settings.previous_title)
                    running = False
