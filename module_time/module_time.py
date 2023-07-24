import pygame, time, sys

class Test(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.frames = [pygame.image.load(f'{i}.png') for i in range(1, 7)]
		self.frames = [pygame.transform.scale2x(self.frames[i]).convert_alpha() for i in range(6)]
		self.frame_index = 0
		self.frame_counter = 0

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(midleft = (0, 360))
		self.pos_x = self.rect.x

		self.rotation = 0
		self.direction = 1
		self.move_speed = 200
		self.animation_speed = 0.25

	def animate(self):
		self.frame_index += self.animation_speed 
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def animate1(self, delta):
		self.frame_counter += delta * 10
		self.frame_index = int(self.frame_counter % 6)
		print(self.frame_index)
		self.image = self.frames[self.frame_index]

	def move(self, delta):
		self.pos_x += self.direction * self.move_speed * delta
		self.rect.x = self.pos_x
		# print(self.rect.x)
		if self.rect.right > 800 or self.rect.left < 0:
			self.direction *= -1

	def rotate(self, delta):
		# self.rotation += delta * 100
		self.image = pygame.transform.rotozoom(self.image, self.rotation, 1)

	def update(self, delta, surface):
		self.animate1(delta)
		self.move(delta)
		# self.draw(surface)
		self.rotate(delta)

	def draw(self, surface):
		surface.blit(self.image, self.rect)


pygame.init()
win = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
time_pre = time.time()
fps = 300
# x = 0
test_group = pygame.sprite.Group()
test_group.add(Test())
while True:
	delta = time.time() - time_pre
	time_pre = time.time()
	# print(delta)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	win.fill((255, 255, 255))

	test_group.update(delta, win)
	test_group.draw(win)
	# pygame.draw.rect(win, (255, 0, 0), (x, 400, 50, 50))
	# print(x)
	# x += 200 * delta
	pygame.display.update()
	clock.tick(fps)
	# time.sleep(1/fps)






























