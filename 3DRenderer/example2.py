import sys
import pygame
import math
import random
import numpy as np
import transform as tf

width, height = 500, 500
ortho_left = -2
ortho_right = 2
ortho_bottom = -2
ortho_top = 2
scale_x = width / (ortho_right - ortho_left)
scale_y = height / (ortho_top - ortho_bottom)
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

cube_vertex = np.array([
    [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1],
    [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]
])

cube_face = [
    [0, 1, 5, 3], [2, 6, 7, 4], [0, 2, 6, 1], [6, 7, 5, 1], [7, 4, 3, 5], [0, 2, 4, 3]
]

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

color = random_color()

def draw_cube(vertexs_2d):
    for index, face in enumerate(cube_face):
        vertexs = []
        for vertex_index in face:
            vertexs.append(vertexs_2d[vertex_index])
        pygame.draw.polygon(win, color, vertexs, 2)

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

vertexs = []

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
    #rotate cube
    if keys[pygame.K_a]:
        cube_vertex = cube_vertex @ tf.rotateY(0.1)
    if keys[pygame.K_d]:
        cube_vertex = cube_vertex @ tf.rotateY(-0.1)
    if keys[pygame.K_w]:
        cube_vertex = cube_vertex @ tf.rotateX(0.1)
    if keys[pygame.K_s]:
        cube_vertex = cube_vertex @ tf.rotateX(-0.1)
    if keys[pygame.K_q]:
        cube_vertex = cube_vertex @ tf.rotateZ(-0.1)
    if keys[pygame.K_e]:
        cube_vertex = cube_vertex @ tf.rotateZ(0.1)

    #move cube
    if keys[pygame.K_LEFT]:
        camera_eye[0] -= 0.1
        cube_vertex = cube_vertex @ tf.translate(-0.1, 0, 0)
    if keys[pygame.K_RIGHT]:
        camera_eye[0] += 0.1
        cube_vertex = cube_vertex @ tf.translate(0.1, 0, 0)
    if keys[pygame.K_DOWN]:
        camera_eye[1] += 0.1
        cube_vertex = cube_vertex @ tf.translate(0, 0.1, 0)
    if keys[pygame.K_UP]:
        camera_eye[1] -= 0.1
        cube_vertex = cube_vertex @ tf.translate(0, -0.1, 0)
    if keys[pygame.K_SPACE]:
        cube_vertex = cube_vertex @ tf.translate(0, 0, 0.1)
        # print([vertex[2] for vertex in cube_vertex])
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
        cube_vertex = cube_vertex @ tf.translate(0, 0, -0.1)
        # print([vertex[2] for vertex in cube_vertex])

    #scale cube
    mouses = pygame.mouse.get_pressed()
    # print(mouses)
    if mouses[0]:
        cube_vertex = cube_vertex @ tf.scale(1.01, 1.01, 1.01)
    if mouses[2]:
        cube_vertex = cube_vertex @ tf.scale(0.99, 0.99, 0.99)

    # win.fill((255, 255, 255))
    win.fill((0, 0, 0))

    for vertex in cube_vertex:
        point = projection_of_the_point(vertex, camera_eye, plane)
        vertexs.append([point[0] * scale_x, point[1] * scale_y])
        # vertexs.append(point)
    # print(vertexs)
    draw_cube(vertexs)

    pygame.display.set_caption(f"{clock.get_fps()} fps")
    pygame.display.update()
    clock.tick(30)