import os, pygame
from pygame.locals import *

data_dir = "data"
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print '%s could not be loaded' % fullname
        raise SystemExit, message
    
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
