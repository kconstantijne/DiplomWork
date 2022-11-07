import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Загальній клас, який керую повединкою та ресурсами гри"""

    def __init__(self):
        """Ініціалізує гру та створює ресурси гри"""

        pygame.init()
        self.settings = Settings()
        # Запуск гри в повноекранному режимі
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def _check_events(self):
        """Реагує на натискання клавіш та миші"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Реагує на натискання клавіші"""

        if event.key == pygame.K_END:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Реагує, коли клавіша не натиснута"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Оновлюється зображення на екрані та перемикається на новий екран"""

        # Наново перемальовуе екран на кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

    def run_game(self):
        """Розпочинае головний цикл гри"""

        while True:
            # Слідкуе за поведінкою миші та клавіатури та миші
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # Створюе екземпляр гри та запускае гру
    ai = AlienInvasion()
    ai.run_game()
