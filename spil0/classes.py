
import pygame
import config, resources

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load
        self.image, self.rect = resources.load_image("wall.png")
        self.rect.move_ip(x,y)

        self.add(config.all_walls)
        
class Gold(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("gold.png")
        self.rect.move_ip(x,y)

        self.add(config.all_gold)


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite(self)
        self.image, self.rect = resources.load_image("monster.png")
        self.rect.move_ip(x,y)

        self.add(config.all_entities)
        self.add(config.all_monsters)

    


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
    
    def update():
        if self.direction == "STAY":
            pass
        if self.direction == "RIGHT":
            self.x += 32
        elif self.direction == "LEFT":
            self.x -= 32
        elif self.direction == "UP":
            self.y -= 32
        elif self.direction == "DOWN":
            self.y += 32
        else:
            pass
        
    def move(direction):
        self.direction = direction
