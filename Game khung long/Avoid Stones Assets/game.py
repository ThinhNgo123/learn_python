import pygame, sys, time, random
from pygame.locals import *

def get_mask(image):
	mask = []
	for x in range(image.get_width()):
		col = []
		for y in range(image.get_height()):
			# print(image.get_at((x, y)))
			if image.get_at((x, y))[3]:
				col.append(1)
			else:
				col.append(0)
		mask.append(col)
	return mask

def collide_mask(rect1, rect2, mask1, mask2):
	rect = rect1.clip(rect2)

	if rect.width == 0 or rect.height == 0:
		return False

	# top, left = rect.top, rect.left
	
	x1, y1 = rect.x - rect1.x, rect.y - rect1.y
	x2, y2 = rect.x - rect2.x, rect.y - rect2.y

	for x in range(rect.width):
		for y in range(rect.height):
			if mask1[x1 + x][y1 + y] and mask2[x2 + x][y2 + y]:
				return True
	return False


def get_index():
	index = (int(time.time())) % 8 
	return index

def drawScore(score):
	font_surf = font.render('Score: ' + str(score), True, (255, 0, 0))
	font_rect = font_surf.get_rect()
	font_rect.topleft = (WINDOWWIDTH / 2 - font_rect.width / 2, 20)
	window.blit(font_surf, font_rect)


WINDOWWIDTH = 800
WINDOWHEIGHT = 300
FONTSIZE = 30

pygame.init()
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Game khung long")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', FONTSIZE)

background_image = pygame.image.load("Sprites/Maps/layer-1.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (WINDOWWIDTH, WINDOWHEIGHT))

ground_image = pygame.image.load("Sprites/Maps/layer-2.png").convert_alpha()
ground_image = pygame.transform.scale(ground_image, (WINDOWWIDTH, WINDOWHEIGHT))

dino_images = []
for i in range(8):
	dino = pygame.image.load("Sprites/Dino/Run (" + str(i+1) + ").png").convert_alpha()
	dino = pygame.transform.scale(dino, (WINDOWWIDTH // 6, WINDOWHEIGHT // 4))
	dino_images.append(dino)
dino_rect_image = dino_images[0].get_rect()
# print(dino_rect.x, dino_rect.y)
# dino_mask = dino_images[0].get_masks()
dino_mask = get_mask(dino_images[0])

jump_img = pygame.image.load("Sprites/Dino/Idle (1).png").convert_alpha()
jump_img = pygame.transform.scale(jump_img, (WINDOWWIDTH, WINDOWHEIGHT))

rock1_image = pygame.image.load("Sprites/Rock_01.png").convert_alpha()
rock1_image = pygame.transform.scale(rock1_image, (WINDOWWIDTH // 10, WINDOWHEIGHT // 4))
rock2_image = pygame.image.load("Sprites/Rock_02.png").convert_alpha()
rock2_image = pygame.transform.scale(rock2_image, (WINDOWWIDTH // 10, WINDOWHEIGHT //  4)) 
rock_rect = rock1_image.get_rect()
rocks_image = [rock1_image, rock2_image]
# rock1_mask = rock1_image.get_masks()
# rock2_mask = rock2_image.get_masks()
rock1_mask = get_mask(rock1_image)
rock2_mask = get_mask(rock2_image)

sound_background = pygame.mixer.Sound("Audios/BG_Music.ogg")
sound_background.set_volume(0.05)
sound_hit = pygame.mixer.Sound("Audios/HitGround.ogg")
# sound_hit.set_volume(0.2)
sound_lose = pygame.mixer.Sound("Audios/Lose.ogg")
sound_lose.set_volume(0.2)

# pre_time = time.time()
dino = None
index = 0
move_background = 0
move_rock = 0
gravity = 2
speed = 0
dino_pos_y = 194
rock1_pos_x = 980
rock2_pos_x = 600
score = 0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_SPACE and dino_pos_y >= 194:
				dino = jump_img
				speed = -16
				sound_hit.play()
	sound_background.play()				

	dino = dino_images[int(index)]
	window.fill((255, 255, 255))
	window.blit(background_image, (move_background, 0))
	window.blit(background_image, (WINDOWWIDTH + move_background ,0))
	window.blit(ground_image, (move_background, 0))
	window.blit(ground_image, (WINDOWWIDTH + move_background, 0))
	drawScore(score)
	window.blit(rock1_image, (rock1_pos_x, 210))
	window.blit(rock2_image, (rock2_pos_x, 210))
	rock1_rect = rock1_image.get_rect()
	rock1_rect.top = 210
	rock1_rect.left = rock1_pos_x

	window.blit(rock2_image, (rock2_pos_x, 210))
	rock2_rect = rock2_image.get_rect()
	rock2_rect.top = 210
	rock2_rect.left = rock2_pos_x
	# pygame.draw.rect(window, (0,255,0), (rock_pos_x, 210, 2, 2), 2)
	# pygame.draw.rect(window, (255, 0, 0), (rock1_pos_x, 210, rock_rect.width, rock_rect.height), 2)
	window.blit(dino, (100, dino_pos_y))
	dino_rect = pygame.Rect(100, dino_pos_y, dino_rect_image.width, dino_rect_image.height)
	# pygame.draw.rect(window, (255, 0, 0), (100, dino_pos_y, dino_rect_image.width - 50, dino_rect_image.height), 2)
	# if rock1_rect.colliderect(dino_rect) or rock2_rect.colliderect(dino_rect):
	
	if collide_mask(dino_rect, rock1_rect, dino_mask, rock1_mask) or collide_mask(dino_rect, rock2_rect, dino_mask, rock2_mask): 	
		sound_background.stop()
		sound_lose.play()
		pygame.time.wait(1000)
		pygame.quit()
		sys.exit() 
	dino_pos_y += speed
	speed += 1
	move_background -= 10  
	rock1_pos_x -= 10
	rock2_pos_x -= 10
	index += 0.5
	if int(index) == 8:
		index = 0
	if abs(move_background) >= WINDOWWIDTH:
		move_background = 0
	if dino_pos_y >= 194:
		dino_pos_y = 194
	if rock1_pos_x <= -170:
		rock1_pos_x = random.randint(900, 1500)
	if rock2_pos_x <= -170:
		rock2_pos_x = random.randint(900, 1500)
	if 100 >= rock1_pos_x or 100 >= rock2_pos_x:
		score += 1
	pygame.display.update()
	clock.tick(30)   