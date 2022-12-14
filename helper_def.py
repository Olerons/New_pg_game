import pygame as pg
import os
import sys


def load_img(name, path, colorkey=None):
    fullname = os.path.join('data', 'img', path, name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    #else:
        #image = image.convert_alpha()
    return image

def load_level(filename):
    fullname = os.path.join('data', 'map', filename)
    
    with open(fullname) as mapFile:
        level_map = [line.strip() for line in mapFile.readlines()]
    
    max_width = max(map(len, level_map))
    
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
        
    