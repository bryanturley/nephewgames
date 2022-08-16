import sys, pygame

pygame.init()

screen_size = screen_width, screen_height = 1728, 972



screen = pygame.display.set_mode(screen_size)




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    
    screen.fill((0, 0, 0))
    pygame.display.flip()
