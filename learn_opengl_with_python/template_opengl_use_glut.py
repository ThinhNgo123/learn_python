import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glClearColor(255, 255, 255, 255)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glFlush()

def main():
    glutInit(sys.argv)
    # glut
    glutInitWindowSize(500, 500)
    glutCreateWindow("OpenGL App")
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()