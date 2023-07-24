import pygame, sys

def get_mask(image):
	mask = []
	for x in range(image.get_width()):
		col = []
		for y in range(image.get_height()):
			# print(image.get_at((x, y)))
			col.append(image.get_at((x, y)))
		mask.append(col)
	return mask

def draw_image(image_mask, draw_color=None):
	for x in range(len(image_mask)):
		for y in range(len(image_mask[0])):
			if image_mask[x][y][3]:
				if draw_color:
					color = draw_color
				else:
					color = image_mask[x][y]
				pygame.draw.line(win, color, (x, y), (x, y))		

win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
image = pygame.image.load("Game khung long/Avoid Stones Assets/Sprites/Dino/Idle (1).png").convert_alpha()
image = pygame.transform.scale(image, (500, 500))
image_mask = get_mask(image)
# image.set_at(x_y, color)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	win.fill((255, 255, 255))
	draw_image(image_mask, (255, 35, 155))
	draw_image(image_mask)
	pygame.display.update()
	clock.tick(30)