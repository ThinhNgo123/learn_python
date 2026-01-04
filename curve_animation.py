import pygame
import sys
import math
from typing import Tuple, List, Dict

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SPEED = 0.03

WHITE_COLOR = (255, 255, 255, 255)
BLACK_COLOR = (  0,   0,   0, 255)
GRAY_COLOR  = (128, 128, 128, 255)
RED_COLOR   = (255,   0,   0, 255)

def lerp_linear(a, b, t):
    return a + t * (b - a)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def __mul__(self, scalar: float):
        return Point(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float):
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

class CurveAnimation:
    def __init__(self):
        self.root_points: List[Point] = []
        self.gizmos = True
        self.step_number = 50
        self.step = 1 / self.step_number
        self.curve_points: List[Point] = []

    def gizmos_enable(self, status: bool):
        self.gizmos = status

    def add_point(self, point: Point):
        self.root_points.append(point)
        self.curve_points.clear()

    def calculate_point_current_step(self, step: float):
        return self.calculate_level_point(step, self.root_points)
    
    def calculate_level_point(self, step: float, points: List[Point]):
        points_level = []
        for i in range(len(points) - 1):
            points_level.append(lerp_linear(points[i], points[i+1], step))
        if len(points_level) == 1:
            return points_level[0]
        return self.calculate_level_point(step, points_level)

    def update(self, step: float):
        if len(self.root_points) <= 1:
            return
        step_number = int(step * self.step_number)
        if len(self.curve_points) > step_number:
            return
        if len(self.curve_points) + 1 == step_number:
            self.curve_points.append(self.calculate_point_current_step(step))
        else:
            self.curve_points.clear()
            for i in range(step_number):
                self.curve_points.append(self.calculate_point_current_step(i / self.step_number))

    def print(self):
        if len(self.points) <= 0:
            return
        print("[")
        for i in range(len(self.points)):
            print("[", end="")
            for j in range(len(self.points[i])):
                print(self.points[i][j], end=", ")
            print("]")
        print("]")

    def draw(self, window: pygame.Surface):
        # if self.gizmos:
        #     self.draw_gizmos(window)

        # if len(self.points) <= 1:
        #     return

        # for i in range(len(self.cache_curve) - 1):
        #     pygame.draw.line(
        #         window, 
        #         RED_COLOR, 
        #         (self.cache_curve[i].x, self.cache_curve[i].y), 
        #         (self.cache_curve[i+1].x, self.cache_curve[i+1].y),
        #         width=5
        #     )
        
        # print("[")
        # for point in self.cache_curve:
        #     print(point, end=", ")
        # print("]")

        # pygame.draw.circle(
        #     window, 
        #     RED_COLOR, 
        #     (self.points[-1][0].x, self.points[-1][0].y), 
        #     10
        # )
        
        for i in range(len(self.curve_points) - 1):
            pygame.draw.line(
                window, 
                RED_COLOR, 
                (self.curve_points[i].x, self.curve_points[i].y), 
                (self.curve_points[i+1].x, self.curve_points[i+1].y), 
                width=5
            )

    def draw_gizmos(self, window: pygame.Surface):
        # if len(self.points) < 1:
        #     return
        
        # for i in range(len(self.points)):
        #     for j in range(len(self.points[i]) - 1):
        #         pygame.draw.line(
        #             window, 
        #             GRAY_COLOR, 
        #             (self.points[i][j].x, self.points[i][j].y), 
        #             (self.points[i][j+1].x, self.points[i][j+1].y),
        #             width=5
        #         )

        # for i in range(len(self.points)):
        #     for j in range(len(self.points[i])):
        #         pygame.draw.circle(
        #             window, BLACK_COLOR, 
        #             (self.points[i][j].x, self.points[i][j].y), 
        #             10
        #         )
        pass


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.DOUBLEBUF)
clock = pygame.time.Clock()

delta_time = 0
current_frame = 0

# n = 1000
# center = (400, 300)
# radius = 100
# phi_step = 2 * math.pi / n
# phi = 0
# for i in range(n):
#     pygame.draw.line(
#         window, 
#         RED_COLOR, 
#         (center[0] + radius * math.cos(phi), center[1] + radius * math.sin(phi)), 
#         (center[0] + radius * math.cos(phi + phi_step), center[1] + radius * math.sin(phi + phi_step)),
#         width=3 
#     ) 
#     phi += phi_step

# window.fill(WHITE_COLOR)

curve_animation = CurveAnimation()

is_pause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                curve_animation.gizmos_enable(not curve_animation.gizmos)
            if event.key == pygame.K_p:
                is_pause = not is_pause
        if event.type == pygame.MOUSEBUTTONDOWN:
            curve_animation.add_point(Point(*event.pos))
            # print(curve_animation.points)

    current_fps = clock.get_fps()

    pygame.display.set_caption(f"FPS: {current_fps}")

    delta_time = 1 / (current_fps if current_fps > 0 else 1)

    window.fill(WHITE_COLOR)

    t = (math.sin(current_frame * SPEED) + 1) / 2

    # if not is_pause:
    #     curve_animation.update(t)

    curve_animation.update(t)

    curve_animation.draw(window)

    # curve_animation.print()

    current_frame += 1

    pygame.display.flip()
    clock.tick(FPS)