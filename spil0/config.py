
import pygame
import resources, classes

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
gamespeed = 30
clock = None

entities = pygame.sprite.RenderUpdates()
walls    = pygame.sprite.Group()
monsters = pygame.sprite.Group()
gold     = pygame.sprite.Group()
player   = None

background, background_rect= resources.load_image("background2.png")
level = resources.load_map("map0.txt")

def proccesCharacter(x,y):
    if level[y][x] == '#':
        classes.Wall(x*32,y*32)
    elif level[y][x] == '@':
        classes.Player(x*32,y*32)
    elif level[y][x] == 'M':
        classes.Monster(x*32, y*32)

for y in range(0,(600/32)):
    for x in range(0,(800/32)):
        proccesCharacter(x,y)
