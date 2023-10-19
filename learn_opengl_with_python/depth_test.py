from math import *
import OpenGL.GL as gl 
import OpenGL.GLUT as glut
import pygame, sys
from pygame.math import Vector3, Vector2

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
# gl.glOrtho(-width / 2, width / 2, -height / 2, height / 2, -1, 1)
gl.glLineWidth(2)

glut.glutInit(sys.argv)
gl.glColor3d(255, 0, 0)
gl.glTranslated(0, 0, 0)
glut.glutSolidCube(1)
gl.glColor3d(0, 0, 255)
gl.glTranslated(0, 0, 1)
glut.glutSolidTeapot(0.5)
gl.glColor3d(0, 0, 255)
gl.glTranslated(0, 0, 2)
glut.glutSolidSphere(0.3, 50, 50)

while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False


    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(fps)
pygame.quit
sys.exit() 