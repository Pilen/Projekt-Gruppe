
import pygame
import direction, config, resources

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




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("player.png",-1)
        self.rect.move_ip(x,y)
        self.add(config.all_entities)
        self.direction = direction.NONE
        self.SPEED = 2

        self.add(config.all_entities)
    
    def update(self):
        vector = [0,0]
        if self.direction == direction.NONE:
            vector = [0,0]
        elif self.direction == direction.EAST:
            vector = [self.SPEED,0]
        elif self.direction == direction.WEST:
            vector = [-self.SPEED,0]
        elif self.direction == direction.NORTH:
            vector = [0,-self.SPEED]
        elif self.direction == direction.SOUTH:
            vector = [0,self.SPEED]

        self.move(vector)

    def move(self, vector):
        self.rect.move_ip(vector[0], vector[1])

           
    
