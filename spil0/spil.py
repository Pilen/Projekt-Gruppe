
import pygame

def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sploink")
    clock = pygame.time.Clock()

    import direction, config, classes

    player = classes.Player(128,128)
    wall = classes.Wall(256,256)
    wall = None

    screen.blit(config.background, (0,0))
    config.all_walls.draw(screen)
    pygame.display.flip()


    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_UP:
                    player.direction = direction.NORTH
                elif event.key == pygame.K_DOWN:
                    player.direction = direction.SOUTH
                elif event.key == pygame.K_LEFT:
                    player.direction = direction.WEST
                elif event.key == pygame.K_RIGHT:
                    player.direction = direction.EAST

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and player.direction == direction.NORTH:
                    player.direction = direction.NONE
                elif event.key == pygame.K_DOWN and player.direction == direction.SOUTH:
                    player.direction = direction.NONE
                elif event.key == pygame.K_LEFT and player.direction == direction.WEST:
                    player.direction = direction.NONE
                elif event.key == pygame.K_RIGHT and player.direction == direction.EAST:                 
                    player.direction = direction.NONE
                        

        config.all_entities.update()
        pygame.display.update(config.all_entities.draw(screen))
    





if __name__ == "__main__":
    main()
