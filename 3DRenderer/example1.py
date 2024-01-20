import sys
import pygame
import math
import random

width, height = 500, 500
ortho_left = -2
ortho_right = 2
ortho_bottom = -2
ortho_top = 2
scale_x = width / (ortho_right - ortho_left)
scale_y = height / (ortho_top - ortho_bottom)
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

cube_vertex = [
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0],
    [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]
]

size = 200
cube_vertex1 = [[pos * size for pos in vertex] for vertex in cube_vertex]
# print(cube_vertex1)

cube_face = [
    [0, 1, 5, 3], [2, 6, 7, 4], [0, 2, 6, 1], [6, 7, 5, 1], [7, 4, 3, 5], [0, 2, 4, 3]
]


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def translate(vertexs, x, y, z):
    for vertex in cube_vertex:
        vertex[0] += x
        vertex[1] += y
        vertex[2] += z

def draw_cube(vertexs_2d):
    for index, face in enumerate(cube_face):
        vertexs = []
        for vertex_index in face:
            vertexs.append(vertexs_2d[vertex_index])
        pygame.draw.polygon(win, cube_colors[index], vertexs, 2)

def dot_product_3d(point1, point2):
    return point1[0] * point2[0] + point1[1] * point2[1] + point1[2] * point2[2]

def projection_of_the_point(vertex, eye, plane):
    direction_vector = [vertex[0] - eye[0], vertex[1] - eye[1], vertex[2] - eye[2]]
    t = (plane["z"] - vertex[2]) / direction_vector[2]
    x = vertex[0] + direction_vector[0] * t
    y = vertex[1] + direction_vector[1] * t
    return [x, y]

camera_eye = [0.5, 0.5, 5]

plane = {
    "x": 200,
    "y": 200,
    "z": 2.5,
    "width": width,
    "height": height
}

cube_colors = [random_color() for _ in range(6)]
# print(cube_colors)
vertexs = []
# for vertex in cube_vertex:
#     point = projection_of_the_point(vertex, camera_eye, plane)
#     vertexs.append([point[0] * scale_x, point[1] * scale_y])
# print(vertexs)

while True:
    vertexs.clear()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    #move camera eye
    if keys[pygame.K_a]:
        camera_eye[0] -= 0.1
    if keys[pygame.K_d]:
        camera_eye[0] += 0.1
    if keys[pygame.K_s]:
        camera_eye[1] += 0.1
    if keys[pygame.K_w]:
        camera_eye[1] -= 0.1
    if keys[pygame.K_q]:
        camera_eye[2] += 0.1
    if keys[pygame.K_e]:
        camera_eye[2] -= 0.1

    #move cube
    if keys[pygame.K_LEFT]:
        translate(cube_vertex, -0.1, 0, 0)
    if keys[pygame.K_RIGHT]:
        translate(cube_vertex, 0.1, 0, 0)
    if keys[pygame.K_DOWN]:
        translate(cube_vertex, 0, 0.1, 0)
    if keys[pygame.K_UP]:
        translate(cube_vertex, 0, -0.1, 0)
    if keys[pygame.K_SPACE]:
        translate(cube_vertex, 0, 0, 0.1)
        # print([vertex[2] for vertex in cube_vertex])
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
        translate(cube_vertex, 0, 0, -0.1)
        # print([vertex[2] for vertex in cube_vertex])

    win.fill((255, 255, 255))

    for vertex in cube_vertex:
        point = projection_of_the_point(vertex, camera_eye, plane)
        vertexs.append([point[0] * scale_x, point[1] * scale_y])
        # vertexs.append(point)
    # print(vertexs)
    draw_cube(vertexs)

    pygame.display.set_caption(f"{clock.get_fps()} fps")
    pygame.display.update()
    clock.tick(30)