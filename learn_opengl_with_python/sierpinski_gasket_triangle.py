from math import *
import OpenGL.GL as gl 
import pygame, sys
from pygame.math import Vector3, Vector2
def draw_line_2d(point1: Vector2, point2: Vector2, color: tuple = (0, 0, 0)):
	gl.glColor4d(color[0], color[1], color[2], 255)
	gl.glBegin(gl.GL_LINES)
	gl.glVertex2f(point1.x, point1.y)	
	gl.glVertex2f(point2.x, point2.y)	
	gl.glEnd()
	gl.glFlush()

def draw_triangle_2d(
        point1: Vector2, 
        point2: Vector2, 
        point3: Vector2, 
        color: tuple = (0, 0, 0)):
    gl.glColor4d(color[0], color[1], color[2], 255)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(point1.x, point1.y)
    gl.glVertex2f(point2.x, point2.y)
    gl.glVertex2f(point3.x, point3.y)
    gl.glEnd()
    gl.glFlush()

def draw_sierpinski_triangle(
        point1: Vector2, 
        point2: Vector2, 
        point3: Vector2, 
        color = (0, 0, 0), depth = 4):
    gl.glColor4d(*color,  255)
    if depth > 0:
        #de quy
        midpoint1 = Vector2((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
        midpoint2 = Vector2((point2.x + point3.x) / 2, (point2.y + point3.y) / 2)
        midpoint3 = Vector2((point3.x + point1.x) / 2, (point3.y + point1.y) / 2)
        draw_sierpinski_triangle(point1, midpoint1, midpoint3, color, depth - 1)
        draw_sierpinski_triangle(midpoint1, point2, midpoint2, color, depth - 1)
        draw_sierpinski_triangle(midpoint3, midpoint2, point3, color, depth - 1)
    else:
        draw_triangle_2d(point1, point2, point3, color)

win = pygame.display.set_mode((500, 500), flags=pygame.DOUBLEBUF | pygame.OPENGL)
width = win.get_width()
height = win.get_height()

clock = pygame.time.Clock()
fps = 30
running = True

#setup gl
gl.glClearColor(255, 255, 255, 255)
gl.glClear(gl.GL_COLOR_BUFFER_BIT)
gl.glOrtho(-width / 2, width / 2, -height / 2, height / 2, -1, 1)
gl.glLineWidth(2)

point1 = Vector2(-200, -150)
point2 = Vector2(200, -150)
point3 = Vector2(0, 250 * (sqrt(3) / 2))

draw_sierpinski_triangle(point1, point2, point3, (255, 0, 0), 5)
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            

    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(fps)
pygame.quit
sys.exit() 