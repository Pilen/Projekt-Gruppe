
import pygame
import resources, classes


entities = pygame.sprite.RenderUpdates()
walls    = pygame.sprite.Group()
monsters = pygame.sprite.Group()
gold     = pygame.sprite.Group()

background, background_rect= resources.load_image("background2.png")
level = resources.load_map("map0.txt")

for y in range(0,(600/32)):
    for x in range(0,(800/32)):
        if level[y][x] == '#':
            classes.Wall(x*32,y*32)
        elif level[y][x] == '@':
            classes.Player(x*32,y*32)

