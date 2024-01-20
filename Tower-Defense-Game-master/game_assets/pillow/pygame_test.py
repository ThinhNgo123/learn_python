import sys
import pygame
pygame.init()
width, height = 500, 500
win = pygame.display.set_mode((width, height))
img = pygame.image.load("./pngtree-game-button-set-yellow-png-png-image_5996878.jpg").convert_alpha()
img = pygame.transform.scale(img, (width, height))
img.set_colorkey((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.blit(img, (0, 0))
    pygame.display.update()