from math import *
from OpenGL.GL import * 
import pygame, sys
from pygame.math import Vector3, Vector2

def main():
	fps = 30
	width, height = (500, 500)
	win = pygame.display.set_mode((width, height), flags=pygame.DOUBLEBUF | pygame.OPENGL)
	clock = pygame.time.Clock()
	running = True

	#setup gl
	glEnable(GL_DEPTH_TEST)
	glClearColor(255, 255, 255, 255)
	glOrtho(-width / 2, width / 2, -height / 2, height / 2, -1, 1)

	while running:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False
	
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		pygame.display.set_caption(f"FPS: {clock.get_fps()}")
		pygame.display.flip()
		clock.tick(fps)
	pygame.quit()
	sys.exit() 

if __name__ == "__main__":
	main()