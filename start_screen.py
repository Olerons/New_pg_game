import pygame as pg
from constants import *
from helper_def import load_img
import sys

class Start_screen:
    def __init__(self, screen):
        self.intro_text = ['ЗАСТАВКА', "",
                      "Правила игры",
                      "Если в правилах несколько",
                      "строк, то придется разбивать",
                      "их вручную"]
        self.fon = pg.transform.scale(load_img('fon.png', 'loc'), SIZE)
        self.running = True
        
    def draw(self, screen):
        screen.blit(self.fon, (0,0))
        font = pg.font.Font(None, 50)
        text_coord = 50
        
        for line in self.intro_text:
            string_rendered = font.render(line, 1, pg.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        
    def run(self, screen):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    self.running = False
                    
            self.draw(screen)
            pg.display.flip()
        
        
        
        
        
        
        
        