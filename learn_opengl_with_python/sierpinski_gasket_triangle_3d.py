from math import *
import OpenGL.GL as gl
import OpenGL.GLU as glu 
import pygame, sys
from pygame.math import Vector3, Vector2
from typing import List, Tuple

def draw_triangle_3d(
        point1: Vector3, 
        point2: Vector3, 
        point3: Vector3, 
        color: Tuple = (0, 0, 0)):
    gl.glColor3d(*color)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex3f(point1.x, point1.y, point1.z)
    gl.glVertex3f(point2.x, point2.y, point2.z)
    gl.glVertex3f(point3.x, point3.y, point3.z)
    gl.glEnd()
    gl.glFlush()

def draw_tetrahedron(
        point1: Vector3, 
        point2: Vector3, 
        point3: Vector3,
        point4: Vector3, 
        color: List[Tuple]):
    draw_triangle_3d(point1, point2, point3, color[0])
    draw_triangle_3d(point1, point2, point4, color[1])
    draw_triangle_3d(point1, point3, point4, color[2])
    draw_triangle_3d(point2, point3, point4, color[3])

def draw_sierpinski_triangle_3d(
        point1: Vector3, 
        point2: Vector3, 
        point3: Vector3,
        point4: Vector3, 
        color = List[Tuple], depth = 4):
    if depth > 0:
        #de quy
        midpoint1 = Vector3((point1.x + point2.x) / 2, (point1.y + point2.y) / 2, (point1.z + point2.z) / 2)
        midpoint2 = Vector3((point2.x + point3.x) / 2, (point2.y + point3.y) / 2, (point2.z + point3.z) / 2)
        midpoint3 = Vector3((point3.x + point1.x) / 2, (point3.y + point1.y) / 2, (point3.z + point1.z) / 2)
        midpoint4 = Vector3((point4.x + point1.x) / 2, (point4.y + point1.y) / 2, (point4.z + point1.z) / 2)
        midpoint5 = Vector3((point4.x + point2.x) / 2, (point4.y + point2.y) / 2, (point4.z + point2.z) / 2)
        midpoint6 = Vector3((point4.x + point3.x) / 2, (point4.y + point3.y) / 2, (point4.z + point3.z) / 2)
        draw_sierpinski_triangle_3d(point4, midpoint4, midpoint5, midpoint6, color, depth - 1)
        draw_sierpinski_triangle_3d(point1, midpoint1, midpoint3, midpoint4, color, depth - 1)
        draw_sierpinski_triangle_3d(point3, midpoint6, midpoint2, midpoint3, color, depth - 1)
        draw_sierpinski_triangle_3d(point2, midpoint2, midpoint5, midpoint1, color, depth - 1)
    else:
        draw_tetrahedron(point1, point2, point3, point4, color)		

win = pygame.display.set_mode((500, 500), flags=pygame.DOUBLEBUF | pygame.OPENGL)
width = win.get_width()
height = win.get_height()

clock = pygame.time.Clock()
fps = 30
running = True

#setup gl
gl.glEnable(gl.GL_DEPTH_TEST)
gl.glClearColor(255, 255, 255, 255)
gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
gl.glMatrixMode(gl.GL_MODELVIEW)
# glu.gluPerspective(45, 1, 0.1, 50.0)
gl.glOrtho(-250, 250, -250, 250, -250, 250)
glu.gluLookAt(-1, -1, -1, 0, 0, 0, 0, 1, 0)
# gl.glLineWidth(1)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLOR = [YELLOW ,RED, GREEN, BLUE]

point1 = Vector3(0, 0, 0)
point2 = Vector3(250, 0, 0)
point3 = Vector3(0, 250, 0)
point4 = Vector3(0, 0, 250)
# rotation_z = Vector3(0, 0, 1)
draw_sierpinski_triangle_3d(point1, point2, point3, point4, COLOR, 3)

while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    # gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    # draw_tetrahedron(point1, point2, point3, point4, COLOR)
    # draw_triangle_3d(point1, point2, point3)
    # print(point2)
    # point4 += rotation_z 
    # point3 += Vector3(0, 1, 0)


    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(fps)
pygame.quit
sys.exit() 