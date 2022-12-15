from helper_def import load_img

FPS = 30
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

tiles = {
            'wall': load_img('wall.png', 'loc'),
            'empty': load_img('empty.png', 'loc')}
        
player = load_img('1hero_stand.png', 'hero')
        
tile_w = tile_h = 50