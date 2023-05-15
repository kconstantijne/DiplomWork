import pygame


class StatisticSettings:
    def __init__(self):
        self.screen_width = 100
        self.screen_height = 730
        self.background_color = (86, 55, 240)
        self.img = pygame.image.load('src/image/star.png')
        self.title = "Alien Invasion Statistics"

        self.previous_img = pygame.image.load('src/image/ufo.png')
        self.previous_title = "Alien Invasion"
        self.previous_window = (1800, 900)
