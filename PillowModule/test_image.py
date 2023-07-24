import pygame, sys

# image = pygame.image.load("background.png")
image = pygame.image.load("background.png")

win = pygame.display.set_mode((image.get_width(), image.get_height()))
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()
	win.fill((255, 255, 0))
	win.blit(image, (0, 0))
	pygame.display.update()
	clock.tick(60)