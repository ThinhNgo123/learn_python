# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import matplotlib.cm
# from vectors import *
# from math import *
# # vector.dot()
# def normal(face):
#     vt0 = Vector(*face[0])
#     vt1 = Vector(*face[1])
#     vt2 = Vector(*face[2])
#     print((vt1.substract(vt0)).cross(vt2.substract(vt0)))
#     return (vt1.substract(vt0)).cross(vt2.substract(vt0))
  
# print(normal([(1,2,3),(4,5,6),(7,8,9)]))
# blues = matplotlib.cm.get_cmap('Blues')
# print(blues)
  
# def shade(face,color_map=blues,light=(1,2,3)):
#     return color_map(1 - dot(unit(normal(face)), unit(light)))

# light = (1,2,3)
# faces = [
#     [(1,0,0), (0,1,0), (0,0,1)],
#     [(1,0,0), (0,0,-1), (0,1,0)],
#     [(1,0,0), (0,0,1), (0,-1,0)],
#     [(1,0,0), (0,-1,0), (0,0,-1)],
#     [(-1,0,0), (0,0,1), (0,1,0)],
#     [(-1,0,0), (0,1,0), (0,0,-1)],
#     [(-1,0,0), (0,-1,0), (0,0,1)],
#     [(-1,0,0), (0,0,-1), (0,-1,0)],
# ]

# pygame.init()
# display = (400,400)
# window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
# gluPerspective(45, 1, 0.1, 50.0)
# glTranslatef(0.0,0.0, -5)
# glEnable(GL_CULL_FACE)
# glEnable(GL_DEPTH_TEST)
# glCullFace(GL_BACK)
# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
 
#     clock.tick()
#     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#     glBegin(GL_TRIANGLES)
#     for face in faces:
#         color = shade(face,blues,light)
#         for vertex in face:
#             glColor3fv((color[0], color[1], color[2]))
#             glVertex3fv(vertex)
#     glEnd()
#     pygame.display.flip()

# def partial(func, *args, **keywords):
# 	# args = (1, 2)
#     def newfunc(*fargs, **fkeywords):
#     	# fargs = (3 ,4)
#         newkeywords = {**keywords, **fkeywords}
#         return func(*args, *fargs, **newkeywords)
#     return newfunc

# def sum(a, b, c, d):
# 	return a + b + c + d
# sum1 = partial(sum, 1, 2)
# print(sum1(3, 4))

import pygame, sys
from pygame.locals import *
import OpenGL.GL as gl
import OpenGL.GLU as glu

def init():
	gl.glClearColor(1, 1, 1, 1) #dat mau nen
	gl.glColor3f(255, 0, 0) #dat mau ve
	# dieu chinh he truc toa do
	# gl.glMatrixMode(gl.GL_PROJECTION)
	# gl.glLoadIdentity()
	gl.glOrtho(-250, 250, -250, 250, -1, 1)

def draw_shape():
	# ve truc toa do Ox
	gl.glBegin(gl.GL_LINES)
	gl.glVertex2d(-250, 0)
	gl.glVertex2d(250, 0)
	# gl.glBegin(gl.GL_POLYGON)
	# gl.glVertex2d(-250, -1)
	# gl.glVertex2d(-250, 1)
	# gl.glVertex2d(250, 1)
	# gl.glVertex2d(250, -1)
	# ve trucc toa do Oy
	gl.glVertex2d(0, -250)
	gl.glVertex2d(0, 250)
	# gl.glBegin(gl.GL_POLYGON)
	# gl.glVertex2d(-1, 250)
	# gl.glVertex2d(1, 250)
	# gl.glVertex2d(1, -250)
	# gl.glVertex2d(-1, -250)
	gl.glEnd()
	# ve hinh tam giac
	gl.glBegin(gl.GL_POLYGON)
	gl.glVertex2d(50, 50)
	gl.glVertex2d(150, 50)
	gl.glVertex2d(50, 150)
	gl.glEnd()

def mydisplay():
	gl.glClear(gl.GL_COLOR_BUFFER_BIT)
	gl.glViewport(0, 0, 250, 250)
	draw_shape()
	gl.glViewport(0, 250, 250, 250)
	draw_shape()
	gl.glViewport(250, 250, 250, 250)
	draw_shape()
	gl.glViewport(250, 0, 250, 250)
	draw_shape()
	gl.glViewport(30, 30, 250, 250)
	draw_shape()

	# gl.glFlush()

win = pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL | RESIZABLE)
clock = pygame.time.Clock()
init()
# gl.glEnable(gl.GL_CULL_FACE)
# gl.glEnable(gl.GL_DEPTH_TEST)
# gl.glCullFace(gl.GL_BACK)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
	# gl.glClearColor(255, 255, 0, 255)
	mydisplay()
	# gl.gl
	pygame.display.flip()
	clock.tick(60)