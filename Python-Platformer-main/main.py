import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 600#800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    # SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        # win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

        pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))

def get_background(name):
    # print(join("assets", "Background", name))
    image = pygame.image.load(join("assets", "Background", name)).convert_alpha()
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    # print(tiles)
    # print(image)
    return tiles, image

def draw(window, background, bg_image, player):
	for pos in background:
		window.blit(bg_image, pos)

	player.draw(window, 20)

	pygame.display.update()

def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    # collide_left = collide(player, objects, -PLAYER_VEL * 2)
    # collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT]:# and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:# and not collide_right:
        player.move_right(PLAYER_VEL)

    # vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    # to_check = [collide_left, collide_right, *vertical_collide]

    # for obj in to_check:
    #     if obj and obj.name == "fire":
    #         player.make_hit()

def main(window):
	global WIDTH, HEIGHT
	clock = pygame.time.Clock()
	player = Player(100, 100, 50, 50)
	run = True
	while run:
		clock.tick(FPS)

		WIDTH, HEIGHT = window.get_width(), window.get_height()
		background, bg_image = get_background("Blue.png")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
		draw(window, background, bg_image, player)
	pygame.quit()
	quit()

if __name__ == '__main__':
	main(window)




































































