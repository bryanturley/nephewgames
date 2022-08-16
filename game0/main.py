import sys, pygame

pygame.init()

screen_size = screen_width, screen_height = 320, 240



screen = pygame.display.set_mode(screen_size)





while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    
    screen.fill((0, 0, 0))
    pygame.display.flip()
