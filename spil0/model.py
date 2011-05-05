
import random
import pygame
import direction, data, resources, functions

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("wall.png")
        self.rect.move_ip(x,y)

        self.add(data.walls)

        
class Gold(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("gold.png",-1)
        self.rect.move_ip(x,y)
        
        self.add(data.gold)
        self.add(data.entities)


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("monster.png", -1)
        self.rect.move_ip(x,y)

        self.add(data.entities)
        self.add(data.monsters)

        self.SPEED = 3
        self.SENSES = 100
        self.timetochangedirection = data.gamespeed * 10
        self.timeleft = self.timetochangedirection

    def update(self):

        if functions.distance_between(self.rect,data.player.rect)> self.SENSES:
            if self.timetochangedirection <= 0:
                self.direction = direction.random()
            
            self.timeleft -= 1
            
        else:
            #ai.pathfind(self.rect, player.rect) #not implemented yet
            vector = [random.randint(0,self.SPEED*2)-self.SPEED,
                      random.randint(0,self.SPEED*2)-self.SPEED]
            self.move(vector)

               
    def move(self, vector):
        rect = self.rect
        self.rect = self.rect.move(vector[0], vector[1])
        if len(pygame.sprite.spritecollide(self,data.walls, False)) > 0:
            self.rect = rect




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("player.png",-1)
        self.rect.move_ip(x,y)
        self.add(data.entities)
        self.direction = direction.NONE
        self.SPEED = 2
        self.gold = 0
        self.add(data.entities)
        data.player = self
    
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
        rect = self.rect
        self.rect = self.rect.move(vector[0], vector[1])
        if len(pygame.sprite.spritecollide(self,data.walls, False)) > 0:
            self.rect = rect

        self.gold += len(pygame.sprite.spritecollide(self,data.gold, True))

    
           
    
