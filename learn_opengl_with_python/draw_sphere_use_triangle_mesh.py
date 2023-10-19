from math import *
from OpenGL.GL import *
import OpenGL.GLU as glu 
import pygame, sys
from pygame.math import Vector3, Vector2

win = pygame.display.set_mode((500, 500), flags=pygame.DOUBLEBUF | pygame.OPENGL)
width = win.get_width()
height = win.get_height()

clock = pygame.time.Clock()
fps = 30
running = True

points = [
    Vector3(0, 1, 0),
    Vector3(0, -0.33333, 0.942809),
    Vector3(0.816497, -0.333333, -0.471405),
    Vector3(-0.816497, -0.333333, -0.471405),
]
radius = 1

def normal(point: Vector3):
    length = sqrt(point.x ** 2 + point.y ** 2 + point.z ** 2)
    return (point / length)

def draw_triangle_3d(
        point1: Vector3, 
        point2: Vector3, 
        point3: Vector3):
    glBegin(GL_TRIANGLES)
    glVertex3f(point1.x, point1.y, point1.z)
    glVertex3f(point2.x, point2.y, point2.z)
    glVertex3f(point3.x, point3.y, point3.z)
    glEnd()

def divide_triangle(point1: Vector3, point2: Vector3, point3: Vector3, depth):
    if depth > 0:
        mp1 = (point1 + point2) / 2
        mp2 = (point1 + point3) / 2
        mp3 = (point2 + point3) / 2
        mp1 = normal(mp1)
        mp2 = normal(mp2)
        mp3 = normal(mp3)
        divide_triangle(point1, mp1, mp2, depth - 1)
        divide_triangle(point2, mp1, mp3, depth - 1)
        divide_triangle(point3, mp3, mp2, depth - 1)
        divide_triangle(mp1, mp3, mp2, depth - 1)
    else:
        draw_triangle_3d(point1, point2, point3)

def draw_sphere(depth = 4):
    divide_triangle(points[0], points[1], points[2], depth)    
    divide_triangle(points[0], points[1], points[3], depth)    
    divide_triangle(points[3], points[1], points[2], depth)    
    divide_triangle(points[3], points[2], points[0], depth)    

#setup gl
glFrontFace(GL_CCW)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)
glClearColor(255, 255, 255, 255)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_MODELVIEW)
glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
# glOrtho(-width / 2, width / 2, -height / 2, height / 2, -width / 2, width / 2)
glOrtho(-1.2, 1.2, -1.2, 1.2, -10, 10)
glu.gluLookAt(1.5, -0.5, 1.5, 0, 0, 0, 0, 1, 0)
# glLineWidth(2)
glColor3d(0, 0, 0)
angle = 0
while running:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle += 5
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glRotated(angle, 0, 1, 0)
                draw_sphere(5)
            elif event.key == pygame.K_RIGHT:
                angle -= 5
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glRotated(angle, 0, 1, 0)
                draw_sphere(5)
        
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glRotated(angle, 0, 1, 0)
        # draw_sphere(4)

    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(fps)
pygame.quit
sys.exit() 