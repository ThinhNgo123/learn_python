from math import *
from OpenGL.GL import * 
from OpenGL.GLUT import *
import pygame, sys
from pygame.math import Vector3, Vector2

class Point3D:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

def draw_text(x, y, z, str):
    glColor3d(255, 0, 0)
    glRasterPos3f(x, y, z)
    for char in str:
        glutBitmapCharacter(GL_BITMAP_TOKEN, ord(char))

colors = (
    (255, 255, 0), #yellow
    (0, 255, 0),   #green
    (0, 0, 255),   #blue
    (255, 0, 0),   #red
    (255, 0, 255), #magenta
    (0, 255, 255)  #cyan
)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_text(0, 0, 0, "OK")
    glFlush()

def init():
    #setup gl
    glEnable(GL_DEPTH_TEST)
    glClearColor(255, 255, 255, 255)
    # glOrtho()

def main():

    point0 = Point3D(0, 0, 0)
    point1 = Point3D(0, 0, 1)
    point2 = Point3D(1, 0, 1)
    point3 = Point3D(1, 0, 0)
    point4 = Point3D(0, 1, 0)
    point5 = Point3D(0, 1, 1)
    point6 = Point3D(1, 1, 1)
    point7 = Point3D(1, 1, 0)
    angle = 0

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("OpenGL App")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
	main()