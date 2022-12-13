import sys
import pygame as pg
from constants import *

class Game:
    def __init__(self):
        pg.init()

        self.main_screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.event_process()
            self.render(self.main_screen)

            pg.display.flip()
        pg.quit()

    def event_process(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def render(self, screen):
        pass

if __name__ == '__main__':
    app = Game()
    app.run()
    sys.exit()