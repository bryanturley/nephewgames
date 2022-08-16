import math, sys, pygame

       
pygame.init()

# screen setup
screen_size = screen_width, screen_height = 1728, 972
screen = pygame.display.set_mode(screen_size)


# image load



# player 1 
x = int(screen_width/2)
y = int(screen_height/2)
dx = int(0)
dy = int(0)

angle = 1
angle_delta = 7



def ship_motion():
    global x, y, dx, dy
    x += dx
    y += dy
    if x > screen_width:
        x -= screen_width
    if y > screen_height:
        y -= screen_height
    if x < 0:
        x += screen_width
    if y < 0:
        y += screen_height

#    if dx > 0:
#        dx -= 0.5
#    if dx < 0:
#        dx += 0.5
#    if dy > 0:
#        dy -= 0.5
#    if dy < 0:
#        dy += 0.5

    dx *= 0.9999
    dy *= 0.9999
    print(dx, dy)

#main loop
while 1:
    # process input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += angle_delta
        if angle >= 360:
            angle -= 360
    if keys[pygame.K_RIGHT]:
        angle -= angle_delta
        if angle < 0:
            angle += 360
    if keys[pygame.K_UP]:
        dx += math.cos(angle * 3.14 / 180)
        dy += math.sin(angle * 3.14 / 180)
    if keys[pygame.K_DOWN]:
        dx -= math.cos(angle * 3.14 / 180)
        dy -= math.sin(angle * 3.14 / 180)

    ship_motion()
        
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 16, 2)
    cx = int(x + math.cos(angle * 3.14 / 180) * 16)
    cy = int(y + math.sin(angle * 3.14 / 180) * 16)
    pygame.draw.circle(screen, (0, 255, 0), (cx, cy), 6, 2)

    
    
    
    
    # flip double buffer
    pygame.display.flip()
    # blank screen
    screen.fill((0, 0, 0))

