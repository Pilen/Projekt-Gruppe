
import pygame
import resources, model, mapping

size = width, height = 800, 600
tilesize = 32 #quadratic 
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
mapping.process_level()
