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

def draw_circle_2d(center: Vector2, radius, color: tuple = (0, 0, 0), number = 40):
	radian = (2 * pi) / number
	start_pos = Vector2(center.x + radius, center.y)
	end_pos = Vector2(center.x + radius * cos(radian), center.y + radius * sin(radian))
	for index in range(2, number + 2):
		draw_line_2d(start_pos, end_pos, color)
		# draw_line_2d(start_pos, center, color)
		# draw_line_2d(center, end_pos, color)
		start_pos = end_pos
		end_pos = Vector2(center.x + radius * cos(radian * index), center.y + radius * sin(radian * index))		

win = pygame.display.set_mode((500, 500), flags=pygame.DOUBLEBUF | pygame.OPENGL)
width = win.get_width()
height = win.get_height()
# pygame.display.set_palette(palette)
clock = pygame.time.Clock()
fps = 30
running = True
sao_kim_radius = 100
trai_dat_radius = sao_kim_radius * 149600 / 108200

#setup gl
gl.glClearColor(255, 255, 255, 255)
gl.glClear(gl.GL_COLOR_BUFFER_BIT)
gl.glOrtho(-width / 2, width / 2, -height / 2, height / 2, -1, 1)
gl.glLineWidth(2)

sao_kim_speed = 0.05
sao_kim_radian = 0
trai_dat_speed = sao_kim_speed * (8 / 13)
trai_dat_radian = 0
count = 0
while running:

	for event in pygame.event.get():
		if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	# gl.glClear(gl.GL_COLOR_BUFFER_BIT)
	# draw_line_2d(Vector2(50, 50), Vector2(200, 200), (255, 0, 0))
	draw_circle_2d(Vector2(0, 0), sao_kim_radius, (255, 0, 0))
	draw_circle_2d(Vector2(0, 0), trai_dat_radius, (255, 0, 0))
	if count >= 1:

		sao_kim_pos = Vector2(sao_kim_radius * sin(sao_kim_radian), sao_kim_radius * cos(sao_kim_radian))
		trai_dat_pos = Vector2(trai_dat_radius * sin(trai_dat_radian), trai_dat_radius * cos(trai_dat_radian))
		draw_line_2d(sao_kim_pos, trai_dat_pos, (0, 0, 0))
		sao_kim_radian += sao_kim_speed
		trai_dat_radian += trai_dat_speed

		count = 0
	else:
		count += 1

	pygame.display.set_caption(f"FPS: {clock.get_fps()}")
	pygame.display.flip()
	clock.tick(fps)
pygame.quit
sys.exit() 