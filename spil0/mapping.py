
import data, model

def process_level():
    for y in range(0,(data.height/data.tilesize)):
        process_line(y)

def process_line(y):
    for x in range(0,(data.width/data.tilesize)):
        process_character(x,y)

def process_character(x,y):
    if data.level[y][x] == '#':
        model.Wall(x*data.tilesize,y*data.tilesize)
    elif data.level[y][x] == '@':
        model.Player(x*data.tilesize,y*data.tilesize)
    elif data.level[y][x] == 'M':
        model.Monster(x*data.tilesize, y*data.tilesize)
    elif data.level[y][x] == 'x':
        model.Gold(x*data.tilesize,y*data.tilesize)
