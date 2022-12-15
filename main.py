import sys
import pygame as pg
from constants import *
from start_screen import Start_screen
from map_gen import Level

class Game:
    def __init__(self):
        pg.init()
        
        self.all_sprite = pg.sprite.Group()
        self.lvl = Level(self.all_sprite)
        
        self.main_screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.running = True
        
        self.start = Start_screen(self.main_screen)

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
            if event.type == pg.KEYDOWN:
                    self.start.running = True

    def render(self, screen):
        self.start.run(screen)
        screen.fill((225,23,4))
        
        self.all_sprite.draw(screen)

if __name__ == '__main__':
    app = Game()
    app.run()
    sys.exit()