import pygame as pg
import os
from alien_invasion import AlienInvasion
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (60, 60)
pg.display.set_caption("Welcome to Alien Invaders!")
img = pg.image.load('src/image/gear.png')
pg.display.set_icon(img)

screen = pg.display.set_mode((400, 300))
pg.init()
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
font = pg.font.Font(None, 32)
welcome_text_color = (255, 255, 255)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    ai = AlienInvasion(self.text)
                    ai.run_game()
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        msg = """What`s your name?"""
        welcome = font.render(msg, True, welcome_text_color)
        welcome_rect = welcome.get_rect()
        welcome_rect.left = welcome_rect.left + 90
        welcome_rect.top = 30
        screen.blit(welcome, welcome_rect)

        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


def main():
    clock = pg.time.Clock()

    input_box = InputBox(100, 150, 140, 32)
    input_boxes = [input_box]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
