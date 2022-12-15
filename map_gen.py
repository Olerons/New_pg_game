from helper_def import *
from constants import *

class Level:
    def __init__(self, group):
        self.group = group
        
        self.generation_level()
        
    
    def generation_level(self):
        level = load_level('level.map')
        print(level)
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y, self.group)
                if level[y][x] == '#':
                    Tile('wall', x, y, self.group)
                if level[y][x] == '@':
                    Player(x, y, self.group)
            
        
class Tile(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, group):
        super().__init__(group)
        self.image = tiles[tile_type]
        self.rect = self.image.get_rect().move(tile_w * pos_x, tile_h * pos_y)
        
class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = player
        self.rect = self.image.get_rect().move(tile_w * pos_x, tile_h * pos_y)
        
        
        
