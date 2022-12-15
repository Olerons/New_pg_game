import pygame as pg
from constants import *
from helper_def import load_img

class Hero(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        img_sprite = load_img('appear.png', 'hero')
        pass


