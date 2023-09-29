import sys
from math import *
from pygame import *
from pygame.locals import *

def square_magnitude(vec1, vec2):
    return (vec1[0] - vec2[0]) ** 2 + (vec1[1] - vec2[1]) ** 2

def normalization(vector2):
    x, y = vector2
    magnitude = sqrt(x**2 + y**2)
    return (x / magnitude, y / magnitude)

width, height = 500, 500
win = display.set_mode((width, height))
clock = time.Clock()

running = True
mouse_pos = (50, 50)
center = (50, 50)
radius = 5
speed = 5
win.fill((255, 255, 255))
delete_rect = Rect((0, 0, 50, 50))
delete = False
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEMOTION:
            mouse_pos = e.pos
        elif e.type == MOUSEBUTTONDOWN:
            delete = True
            mouse_pos = e.pos
        elif e.type == MOUSEBUTTONUP:
            delete = False
            # print(mouse_pos)
    # win.fill((255, 255, 255))

    if square_magnitude(mouse_pos, center) >= radius**2 and not delete:
        direction_vector = normalization((mouse_pos[0] - center[0], mouse_pos[1] - center[1]))
        speed_vector = (direction_vector[0] * speed, direction_vector[1] * speed)
        center = (center[0] + speed_vector[0], center[1] + speed_vector[1])

    if delete:
        delete_rect.center = mouse_pos
        draw.rect(win, (255, 255, 255), delete_rect)

    draw.circle(win, (255, 0, 0), center, radius)
    display.update()
    clock.tick(30)
quit()
sys.exit()