import pygame
from pygame.locals import *

# constant
WIDTH, HEIGHT = 768, 704
BOARD_WIDTH = 768
BOARD_HEIGHT = 1408
TITLE_WIDTH = 2880
CELL_SIZE = 32
FPS = 30
BLACK = (0, 0, 0)

# global
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():
    # image
    SCALE_BOARD = 0.5
    BOARD_IMG = load_image("./Board/Board.png", SCALE_BOARD)
    SCALE_TITLE = (WIDTH - BOARD_WIDTH * SCALE_BOARD) / TITLE_WIDTH
    TITLE_IMG = load_image("./Title/Title.png", SCALE_TITLE)
    SCALE_SHAPE = 0.5
    SHAPE = {
        "T": load_image("./Shape Blocks/T.png", SCALE_SHAPE),
        "I": load_image("./Shape Blocks/I.png", SCALE_SHAPE),
        "Z": load_image("./Shape Blocks/Z.png", SCALE_SHAPE),
        "J": load_image("./Shape Blocks/J.png", SCALE_SHAPE),
        "L": load_image("./Shape Blocks/L.png", SCALE_SHAPE),
        "O": load_image("./Shape Blocks/O.png", SCALE_SHAPE),
        "S": load_image("./Shape Blocks/S.png", SCALE_SHAPE)
    }
    index = 0
    list = ["T", "I", "Z", "J", "L", "O", "S"]
    running = True
    x = 32
    y = 64
    # loop
    while running:
        #event
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    y += CELL_SIZE
                elif event.key == K_UP:
                    y -= CELL_SIZE
                elif event.key == K_RIGHT:
                    x += CELL_SIZE
                elif event.key == K_LEFT:
                    x -= CELL_SIZE
                elif event.key == K_SPACE:
                    index = (index + 1) % 7

        win.fill(BLACK)
        win.blit(BOARD_IMG, (0, 0))
        win.blit(TITLE_IMG, (BOARD_IMG.get_size()[0], 0))
        win.blit(SHAPE[list[index]], (x, y))

        # update frame
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

def load_image(path, scale=None):
    image = pygame.image.load(path).convert_alpha()
    if scale:
        width_image, height_image = image.get_size()
        image = pygame.transform.scale(image, size=(width_image * scale, height_image * scale))
    return image

if __name__ == "__main__":
    main()