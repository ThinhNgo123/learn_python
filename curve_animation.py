import pygame
import sys
import math
from typing import Tuple, List

def lerp_linear(a: float, b: float, t: float):
    return a + t * (b - a)

def lerp_linear_point(a: Tuple[float, float], b: Tuple[float, float], t: float):
    return (
        a[0] + t * (b[0] - a[0]),
        a[1] + t * (b[1] - a[1])
    )

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SPEED = 0.03

WHITE_COLOR = (255, 255, 255, 255)
BLACK_COLOR = (  0,   0,   0, 255)
GRAY_COLOR  = (128, 128, 128, 255)
RED_COLOR   = (255,   0,   0, 255)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

points: List[Tuple[int, int]] = []

delta_time = 0
current_frame = 0

window.fill(WHITE_COLOR)

n = 1000
center = (400, 300)
radius = 100
phi_step = 2 * math.pi / n
phi = 0
for i in range(n):
    pygame.draw.line(
        window, 
        RED_COLOR, 
        (center[0] + radius * math.cos(phi), center[1] + radius * math.sin(phi)), 
        (center[0] + radius * math.cos(phi + phi_step), center[1] + radius * math.sin(phi + phi_step)),
        width=3 
    ) 
    phi += phi_step

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicked point", event.pos)
            points.append(event.pos)

    current_fps = clock.get_fps()

    pygame.display.set_caption(f"FPS: {current_fps}")

    delta_time = 1 / (current_fps if current_fps > 0 else 1)

    window.fill(WHITE_COLOR)

    n = 500
    center = (400, 300)
    radius = 100
    phi_step = 2 * math.pi / n
    phi = 0
    for i in range(n):
        pygame.draw.line(
            window, 
            RED_COLOR, 
            (center[0] + radius * math.cos(phi), center[1] + radius * math.sin(phi)), 
            (center[0] + radius * math.cos(phi + phi_step), center[1] + radius * math.sin(phi + phi_step)),
            width=3 
        ) 
        phi += phi_step

    for i in range(len(points) - 1):
        pygame.draw.line(window, GRAY_COLOR, points[i], points[i+1], 5)

    for point in points:
        pygame.draw.circle(window, BLACK_COLOR, point, 10)
    
    if len(points) >= 2:
        red_points = []
        t = (math.sin(current_frame * SPEED) + 1) / 2
        for i in range(len(points) - 1):
            temp_point = lerp_linear_point(points[i], points[i+1], t)
            pygame.draw.circle(window, RED_COLOR, temp_point, 10)
            red_points.append(temp_point)
        
        for i in range(len(red_points) - 1):
            temp_point = lerp_linear_point(red_points[i], red_points[i+1], t)
            pygame.draw.line(window, GRAY_COLOR, red_points[i], red_points[i+1], 5)
            pygame.draw.circle(window, RED_COLOR, temp_point, 10)

    current_frame += 1

    pygame.display.update()
    clock.tick(FPS)