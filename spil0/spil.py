
import pygame

def main():
    pygame.init()
    import direction, config, classes

    pygame.display.set_caption("Sploink")
    config.clock = pygame.time.Clock()

    config.screen.blit(config.background, (0,0))
    config.walls.draw(config.screen)
    pygame.display.flip()


    while True:
        config.clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_UP:
                    config.player.direction = direction.NORTH
                elif event.key == pygame.K_DOWN:
                    config.player.direction = direction.SOUTH
                elif event.key == pygame.K_LEFT:
                    config.player.direction = direction.WEST
                elif event.key == pygame.K_RIGHT:
                    config.player.direction = direction.EAST

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and config.player.direction == direction.NORTH:
                    config.player.direction = direction.NONE
                elif event.key == pygame.K_DOWN and config.player.direction == direction.SOUTH:
                    config.player.direction = direction.NONE
                elif event.key == pygame.K_LEFT and config.player.direction == direction.WEST:
                    config.player.direction = direction.NONE
                elif event.key == pygame.K_RIGHT and config.player.direction == direction.EAST:                 
                    config.player.direction = direction.NONE
                        

        config.entities.update()
        config.entities.clear(config.screen, config.background)
        pygame.display.update(config.entities.draw(config.screen))
    





if __name__ == "__main__":
    main()
