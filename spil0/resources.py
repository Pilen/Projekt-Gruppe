import os, pygame
from pygame.locals import *

data_dir = "data"
map_dir = "maps"
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

def load_map(name):
    try:
        f = open("maps/map0.txt") #open(os.path.join(map_dir, name))
    except IOError, message:
        print "Map not found"
        raise SystemExit, message
    
    try:
        map = []
        for line in f:
            if len(line) > (800/32)+1:
                print "Map misformed, a map's width can be no bigger than %i characters wide" % (800/32)
                #raise SystemExit
            map.append(line)
        if len(map) > (600/32)+1:
            print "Map misformed, a map's height can be no bigger than %i characters wide" % (600/32)
            raise SystemExit
        return map
    except IOError, message:
        print "Could not read Map"
        raise SystemExit, message
    finally:
        f.close()
