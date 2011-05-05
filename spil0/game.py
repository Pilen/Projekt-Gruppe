
import sys
import pygame
import direction, data, functions

    
def main():
    pygame.init()

    pygame.display.set_caption("Sploink")
    data.clock = pygame.time.Clock()

    data.screen.blit(data.background, (0,0))
    data.walls.draw(data.screen)
    pygame.display.flip()
    mainloop()

def mainloop():
    while True:
        data.clock.tick(data.gamespeed)
        handle_input()
        data.entities.update()
        draw()
        

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functions.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                functions.quit()
            elif event.key == pygame.K_UP:
                data.player.direction = direction.NORTH
            elif event.key == pygame.K_DOWN:
                data.player.direction = direction.SOUTH
            elif event.key == pygame.K_LEFT:
                data.player.direction = direction.WEST
            elif event.key == pygame.K_RIGHT:
                data.player.direction = direction.EAST
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and data.player.direction == direction.NORTH:
                data.player.direction = direction.NONE
            elif event.key == pygame.K_DOWN and data.player.direction == direction.SOUTH:
                data.player.direction = direction.NONE
            elif event.key == pygame.K_LEFT and data.player.direction == direction.WEST:
                data.player.direction = direction.NONE
            elif event.key == pygame.K_RIGHT and data.player.direction == direction.EAST:                 
                data.player.direction = direction.NONE
                
def draw():
    data.entities.clear(data.screen, data.background)
    pygame.display.update(data.entities.draw(data.screen))



if __name__ == "__main__":
    main()
