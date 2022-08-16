import math, sys, pygame
from dataclasses import dataclass
       
pygame.init()
clock = pygame.time.Clock()

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

# array=[0]*element_count
MAX_BULLETS = 2048

@dataclass
class Bullet:
    act: bool = True
    x: float = 0
    y: float = 0
    dx: float = 0
    dy: float = 0
    l: int = 0


bullets = []
for i in range(MAX_BULLETS):
    bullets.append(Bullet())



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

def bullet_motion():
    cnt = 0
    for i in range(MAX_BULLETS):
        if bullets[i].act == False:
            continue
        cnt += 1
        bullets[i].x += bullets[i].dx
        bullets[i].y += bullets[i].dy
        bullets[i].l -= 1
        if bullets[i].l < 2:
            bullets[i].act = False
        if bullets[i].x < 0:
            bullets[i].x += screen_width
        if bullets[i].x >= screen_width:
            bullets[i].x -= screen_width
        if bullets[i].y < 0:
            bullets[i].y += screen_height
        if bullets[i].y >= screen_height:
            bullets[i].y -= screen_height
        print(cnt, " of ", MAX_BULLETS)

def bullet_start(x, y, angle):
    for i in range(MAX_BULLETS):
        if bullets[i].act == False:
            bullets[i].act = True
            bullets[i].x = x
            bullets[i].y = y
            bullets[i].dx = math.cos(angle * 3.14 / 180) * 16
            bullets[i].dy = math.sin(angle * 3.14 / 180) * 16
            bullets[i].l = 255
            break
def bullet_draw():
    for i in range(MAX_BULLETS):
        if bullets[i].act == False:
            continue
        start = (int(bullets[i].x), int(bullets[i].y))
        end = (int(bullets[i].x - bullets[i].dx), int(bullets[i].y - bullets[i].dy))

        l = bullets[i].l
        if l < 72:
            l = 72
        color = (l/3, l, l/3)

        pygame.draw.line(screen, color, start, end, 3)


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
    if keys[pygame.K_SPACE]:
        sx = x + math.cos(angle * 3.14 / 180) * 16
        sy = y + math.sin(angle * 3.14 / 180) * 16
        bullet_start(sx, sy, angle)

    ship_motion()
    bullet_motion()

    
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 16, 2)
    cx = int(x + math.cos(angle * 3.14 / 180) * 16)
    cy = int(y + math.sin(angle * 3.14 / 180) * 16)
    pygame.draw.circle(screen, (0, 255, 0), (cx, cy), 6, 2)


    bullet_draw()
    
    
    # flip double buffer
    pygame.display.flip()
    clock.tick(60)
    
    # blank screen
    screen.fill((0, 0, 0))

