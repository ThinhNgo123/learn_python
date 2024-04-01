import pygame
import random
from typing import Dict, List
from pygame.locals import *

def load_image(path, scale=None):
    image = pygame.image.load(path).convert_alpha()
    if scale:
        width_image, height_image = image.get_size()
        image = pygame.transform.scale(image, size=(width_image * scale, height_image * scale))
    return image

def rotate_image(image, angle=0):
    return pygame.transform.rotate(image, angle)

def random_shape(shapes):
    return random.choice(random.choice(shapes))

def create_board_game(width, height):
    board = []
    for _ in range(height):
        row = ["_"] * width
        board.append(row)
    return board

def rotate_shape(shape: pygame.Surface, shape_list: List[List[pygame.Surface]]):
    list_shape = None
    position = None
    for shapes in shape_list:
        try:
            temp = shapes.index(shape)
            list_shape = shapes
            position = temp
            break
        except ValueError:
            pass
    lenght = len(list_shape)
    position = (position + 1) % lenght
    return list_shape[position]

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

#image
SCALE_BOARD = 0.5
BOARD_IMG = load_image("./Board/Board.png", SCALE_BOARD)
SCALE_TITLE = (WIDTH - BOARD_WIDTH * SCALE_BOARD) / TITLE_WIDTH
TITLE_IMG = load_image("./Title/Title.png", SCALE_TITLE)
SCALE_SHAPE = 0.5

SHAPE_IMAGE = {
    "T": load_image("./Shape Blocks/T.png", SCALE_SHAPE),
    "I": load_image("./Shape Blocks/I.png", SCALE_SHAPE),
    "Z": load_image("./Shape Blocks/Z.png", SCALE_SHAPE),
    "J": load_image("./Shape Blocks/J.png", SCALE_SHAPE),
    "L": load_image("./Shape Blocks/L.png", SCALE_SHAPE),
    "O": load_image("./Shape Blocks/O.png", SCALE_SHAPE),
    "S": load_image("./Shape Blocks/S.png", SCALE_SHAPE)
}

SHAPE = [
    [SHAPE_IMAGE["T"], rotate_image(SHAPE_IMAGE["T"], 90), rotate_image(SHAPE_IMAGE["T"], 180), rotate_image(SHAPE_IMAGE["T"], 270)],
    [SHAPE_IMAGE["I"], rotate_image(SHAPE_IMAGE["I"], 90)],
    [SHAPE_IMAGE["Z"], rotate_image(SHAPE_IMAGE["Z"], 90), rotate_image(SHAPE_IMAGE["Z"], 180), rotate_image(SHAPE_IMAGE["Z"], 270)],
    [SHAPE_IMAGE["J"], rotate_image(SHAPE_IMAGE["J"], 90), rotate_image(SHAPE_IMAGE["J"], 180), rotate_image(SHAPE_IMAGE["J"], 270)],
    [SHAPE_IMAGE["L"], rotate_image(SHAPE_IMAGE["L"], 90), rotate_image(SHAPE_IMAGE["L"], 180), rotate_image(SHAPE_IMAGE["L"], 270)],
    [SHAPE_IMAGE["O"]],
    [SHAPE_IMAGE["S"], rotate_image(SHAPE_IMAGE["S"], 90), rotate_image(SHAPE_IMAGE["S"], 180), rotate_image(SHAPE_IMAGE["S"], 270)]
]

FREQ_FALL = FPS // 2

board_game = create_board_game(
    int((BOARD_WIDTH - 3 * CELL_SIZE) * SCALE_BOARD / CELL_SIZE),
    int((BOARD_HEIGHT - 3 * CELL_SIZE) * SCALE_BOARD / CELL_SIZE)  
)


def main():
    current_frame = 0
    current_shape = random_shape(SHAPE)
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
                # if event.key == K_DOWN:
                #     y += CELL_SIZE
                # elif event.key == K_UP:
                #     y -= CELL_SIZE
                if event.key == K_RIGHT:
                    x += CELL_SIZE
                elif event.key == K_LEFT:
                    x -= CELL_SIZE
                elif event.key == K_SPACE:
                    current_shape = rotate_shape(current_shape, SHAPE)

        win.fill(BLACK)
        win.blit(BOARD_IMG, (0, 0))
        win.blit(TITLE_IMG, (BOARD_IMG.get_size()[0], 0))
        win.blit(current_shape, (x, y))
        # print(random.choice(random.choice(SHAPE)))

        # update frame
        current_frame += 1
        if current_frame >= FREQ_FALL:
            y += CELL_SIZE
            current_frame = 0
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()