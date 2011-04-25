
import pygame
import resources

all_entities = pygame.sprite.RenderUpdates()
all_walls    = pygame.sprite.Group()
all_monsters = pygame.sprite.Group()
all_gold     = pygame.sprite.Group()

background, background_rect= resources.load_image("background2.png")


