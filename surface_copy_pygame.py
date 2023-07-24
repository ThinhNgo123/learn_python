import pygame, sys, random

def main():
	pygame.init()
	window = pygame.display.set_mode((500, 500))
	clock = pygame.time.Clock()
	running = True
	window.fill((255, ) * 3)
	surface = pygame.Surface((150, 150))
	surface.fill((0, 255, 0))
	surface1 = pygame.Surface((50, 50))
	surface.blit(surface1, (20, 20))
	window.blit(surface, (20, 20))
	base = surface.copy()
	# window.blit(base, (250, 250))
	x = 0
	y = 0
	event_random = pygame.USEREVENT + 1
	pygame.time.set_timer(event_random, 1000)
	while(running):
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				running = False
			if event.type == event_random:
				x = random.randint(0, 350)
				y = random.randint(0, 350)

		# window.blit(surface, (20, 20))
		window.fill((255, ) * 3)
		window.blit(surface, (20, 20))
		window.blit(base, (x, y))
		# x += 1
		pygame.display.update()
		clock.tick(60)

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()