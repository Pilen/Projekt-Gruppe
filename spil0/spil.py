
import pygame
import config


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
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
        


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
    
    def update():
        if self.direction == "stay":
            pass
        elif self.direction == "right":
            self.x += 32
        elif self.direction == "left":
            self.x -= 32
        elif self.direction == "up":
            self.y -= 32
        elif self.direction == "down":
            self.y += 32
        
    def move(direction):
        self.direction = direction

def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sploink")
    clock = pygame.time.Clock()

    screen.blit(background, (0,0))
    pygame.display.update()


    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif

if __name__ == "__main__":
    main()
