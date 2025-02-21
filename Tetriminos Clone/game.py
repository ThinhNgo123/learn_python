from os import truncate
import pygame
import random
from typing import Dict, List, Any, Union, Optional
from pygame.locals import *
from setting import *

def load_image(path):
    return pygame.image.load(path).convert_alpha()

def scale_image(image, scale):
    width_image, height_image = image.get_size()
    return pygame.transform.scale(image, size=(width_image * scale, height_image * scale))

def random_shape(shapes: Dict[str, List[List[int]]]):
    return random.choice(random.choice(list(shapes.values())))

def random_block(blocks: List[pygame.Surface]):
    return random.choice(blocks)

def rotate_shape(shape: List[List[int]], shapes: Dict[str, List[List[int]]]):
    for shape_name in shapes:
        for i in range(len(shapes[shape_name])):
            if shape == shapes[shape_name][i]:
                return shapes[shape_name][(i + 1) % len(shapes[shape_name])] 

def create_board_game(width, height):
    # print(width, height)
    board = []
    for _ in range(width):
        board.append([None for _ in range(height)])
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         print(id(board[i][j]), end=" ")
    return board 

def draw_board(win: pygame.Surface, board: List[Union[pygame.Surface, None]], cell_size):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != None:
                win.blit(board[i][j], (cell_size * (i + 1), cell_size * (j + 1 - 4)))

def add_shape_to_board(board: List[Union[pygame.Surface, None]], shape, block, positions: List[List[int]]):
    index_pos = 0
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if shape[i][j] == 1 and (not check_position_outside_board(positions[index_pos])):
                board[positions[index_pos][0]][positions[index_pos][1]] = block
            index_pos += 1

def move_curret_blocks(board: List[Union[pygame.Surface, None]], move_x: int, move_y: int, shape_current, positions: List[List[int]]):
    shape_in_board = []
    index_pos = 0
    for i in range(len(shape_current)):
        for j in range(len(shape_current[0])):
            # print("pos", positions[index_pos])
            # print("shape", shape_current[i][j])
            if check_position_outside_board(positions[index_pos]) or shape_current[i][j] == 0:
                index_pos += 1
                shape_in_board.append(None)
                continue
            # print("board", board[positions[index_pos][0]][positions[index_pos][1]])
            shape_in_board.append(board[positions[index_pos][0]][positions[index_pos][1]])
            board[positions[index_pos][0]][positions[index_pos][1]] = None
            index_pos += 1
    index_pos = 0
    for i in range(len(shape_current)):
        for j in range(len(shape_current[0])):
            if (not check_position_outside_board(positions[index_pos])) and shape_current[i][j] == 1:
                board[positions[index_pos][0] + move_x][positions[index_pos][1] + move_y] = shape_in_board[index_pos]
            positions[index_pos][0] += move_x
            positions[index_pos][1] += move_y
            index_pos += 1

def remove_blocks(board: List[Union[pygame.Surface, None]], shape, positions: List[List[int]]):
    index_pos = 0
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if check_position_outside_board(positions[index_pos]) or shape[i][j] == 0:
                index_pos += 1
                continue
            board[positions[index_pos][0]][positions[index_pos][1]] = None
            index_pos += 1


def check_position_outside_board(position: List[int]):
    if position[0] < 0 or position[1] < 0 or position[0] > 9 or position[1] > 23:
        return True
    return False

def check_can_move_in_direction(board: List[Union[pygame.Surface, None]], shape, block, positions, direction: str):
    # print(board)
    # print(shape)
    # print(positions)
    if direction == "DOWN":
        remove_blocks(board, shape, positions)
        index_pos = 0
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                # print("board", positions[index_pos][0], positions[index_pos][1] + 1)
                if shape[i][j] == 1 and \
                    (positions[index_pos][1] >= 23 or \
                    (board[positions[index_pos][0]][positions[index_pos][1] + 1] != None)):
                    # print(positions[index_pos], shape[i][j])
                    add_shape_to_board(board, shape, block, positions)
                    return False
                index_pos += 1
        add_shape_to_board(board, shape, block, positions)        
    elif direction == "LEFT":
        remove_blocks(board, shape, positions)
        index_pos = 0
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] == 1 and \
                    (positions[index_pos][0] <= 0 or \
                    (board[positions[index_pos][0] - 1][positions[index_pos][1]] != None)):
                    # print(positions[index_pos], shape[i][j])
                    add_shape_to_board(board, shape, block, positions)
                    return False
                index_pos += 1
        add_shape_to_board(board, shape, block, positions)        
        # print()
    elif direction == "RIGHT":
        remove_blocks(board, shape, positions)
        index_pos = 0
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] == 1 and \
                    (positions[index_pos][0] >= 9 or \
                    board[positions[index_pos][0] + 1][positions[index_pos][1]] != None):
                    add_shape_to_board(board, shape, block, positions)
                    return False
                index_pos += 1
        add_shape_to_board(board, shape, block, positions)
    return True

def check_can_rotate_and_rotate(board: List[Union[pygame.Surface, None]], shape_current, shape_rotate, block, positions):
    # print(positions)
    can_rotate = True
    index_pos = 0
    for i in range(len(shape_rotate)):
        for j in range(len(shape_rotate[0])):
            if shape_rotate[i][j] == 0:
                index_pos += 1
                continue
            if check_position_outside_board(positions[index_pos]) or \
                (board[positions[index_pos][0]][positions[index_pos][1]] != None and shape_current[i][j] == 0):
                can_rotate = False
                # print("break")
                break
            index_pos += 1
        if not can_rotate:
            break
    
    if not can_rotate:
        return shape_current
    remove_blocks(board, shape_current, positions)
    add_shape_to_board(board, shape_rotate, block, positions)
    return shape_rotate

def check_line_complete(board: List[Union[pygame.Surface, None]], line_index):
    for column_index in range(len(board)):
        if board[column_index][line_index] == None:
            return False
    return True

def delete_lines_complete(board: List[Union[pygame.Surface, None]]):
    # print("call delete")
    BOARD_HEIGHT = 24
    BOARD_WIDTH = 10
    line_index = BOARD_HEIGHT - 1
    number_line_complete = 0
    while line_index >= 0:
        if check_line_complete(board, line_index):
            # print("delete line", line_index)
            for i in range(line_index, 0, -1):
                for j in range(BOARD_WIDTH):
                    board[j][i] = board[j][i - 1]
            board[BOARD_WIDTH - 1][0] = None
            number_line_complete += 1
        else:
            line_index -= 1
    return number_line_complete

def check_gameover(board):
    pass

def draw_shape_next(win: pygame.Surface, background_imgs: Dict[str, pygame.Surface], shape_next: List[List[int]], block, cell_size):
    # print(shape_next)
    WIDTH = HEIGHT = 6
    x, y = 450, 400
    for i in range(WIDTH):
        win.blit(background_imgs["BORDER"], (x + i * cell_size, y))
    swap = 0
    for i in range(HEIGHT - 2):
        win.blit(background_imgs["BORDER"], (x, y + (i + 1) * cell_size))
        for j in range(len(shape_next)):
            win.blit(background_imgs[f"BG{(swap + j) % 2 + 1}"], (x + (j + 1) * cell_size, y + (i + 1) * cell_size))
            if shape_next[i][j] == 0:
                continue
            win.blit(block, (x + (j + 1) * cell_size, y + (i + 1) * cell_size))
        swap = (swap + 1) % 2
        win.blit(background_imgs["BORDER"], (x + (WIDTH - 1) * cell_size, y + (i + 1) * cell_size))
    for i in range(WIDTH):
        win.blit(background_imgs["BORDER"], (x + i * cell_size, y + (HEIGHT - 1) * cell_size))

def draw_text(win: pygame.Surface, font: pygame.font.SysFont, text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    win.blit(text_surface, text_rect)

def draw_score_and_level(win: pygame.Surface, score, score_pos, level, level_pos, font, color):
    draw_text(win, font, f"Level: {int(level)}", level_pos[0], level_pos[1], color)
    draw_text(win, font, f"Score: {int(score)}", score_pos[0], score_pos[1], color)

def calc_score_and_level(line_number_deleted: int):
    return line_number_deleted * 10, int((line_number_deleted * 10 / 100) + 1)

pygame.init()
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#image
BOARD_IMG = load_image("./Board/Board.png")
BOARD_WIDTH, BOARD_HEIGHT = BOARD_IMG.get_size()
SCALE_BOARD = WINDOW_HEIGHT / BOARD_HEIGHT
BOARD_IMG = scale_image(BOARD_IMG, SCALE_BOARD)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_IMG.get_size()
# BOARD_CELL_WIDTH, BOARD_CELL_HEIGHT = 10, 20

# TITLE_IMG = scale_image(load_image("./Title/Title.png"), 0.2)

BLOCK_IMG = load_image("./Single Blocks/Blue.png")

CELL_SIZE = int(BOARD_WIDTH / (BOARD_CELL_WIDTH + 2))
SCALE_SHAPE = CELL_SIZE / BLOCK_IMG.get_width()

BLOCK_IMGS = [
    scale_image(load_image("./Single Blocks/Blue.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/Green.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/LightBlue.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/Orange.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/Purple.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/Red.png"), SCALE_SHAPE),
    scale_image(load_image("./Single Blocks/Yellow.png"), SCALE_SHAPE),
]

BACKGROUND_IMGS = {
    "BORDER": scale_image(load_image("./Board/Border.png"), SCALE_SHAPE),
    "BG1": scale_image(load_image("./Board/BG_1.png"), SCALE_SHAPE),
    "BG2": scale_image(load_image("./Board/BG_2.png"), SCALE_SHAPE)
}

# global
clock = pygame.time.Clock()
# sans
FONT = pygame.font.SysFont("ConsolasBold", 60)

def main():
    board = create_board_game(BOARD_CELL_WIDTH, BOARD_CELL_HEIGHT + 4)
    block_current = random_block(BLOCK_IMGS)
    shape_current = random_shape(SHAPES)
    position_shape_current = [
        [3, 0], [4, 0], [5, 0], [6, 0],
        [3, 1], [4, 1], [5, 1], [6, 1],
        [3, 2], [4, 2], [5, 2], [6, 2],
        [3, 3], [4, 3], [5, 3], [6, 3]
    ]
    # print(shape_current)
    block_next = random_block(BLOCK_IMGS)
    shape_next = random_shape(SHAPES)
    add_shape_to_board(board, shape_current, block_current, position_shape_current)
    number_line_deleted = 0
    score = 0
    level = 1
    current_frame = 0
    running = True
    # loop
    while running:
        #event
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if check_can_move_in_direction(board, shape_current, block_current, position_shape_current, "DOWN"):
                        move_curret_blocks(board, 0, 1, shape_current, position_shape_current)
                elif event.key == K_UP:
                    move_curret_blocks(board, 0, -1, shape_current, position_shape_current)
                if event.key == K_RIGHT:
                    # print(position_shape_current)
                    if check_can_move_in_direction(board, shape_current, block_current, position_shape_current, "RIGHT"):
                        move_curret_blocks(board, 1, 0, shape_current, position_shape_current)
                    # print(position_shape_current)
                elif event.key == K_LEFT:
                    if check_can_move_in_direction(board, shape_current, block_current, position_shape_current, "LEFT"):
                        move_curret_blocks(board, -1, 0, shape_current, position_shape_current)
                elif event.key == K_SPACE:
                    shape_current = check_can_rotate_and_rotate(
                        board, 
                        shape_current,
                        rotate_shape(shape_current, SHAPES),
                        block_current, 
                        position_shape_current
                    )
                elif event.key == K_q:
                    pass


        # update frame
        current_frame += 1
        if current_frame >= FREQ_FALL - level * 2:
            if check_can_move_in_direction(board, shape_current, block_current, position_shape_current, "DOWN"):
                # print("down")
                move_curret_blocks(board, 0, 1, shape_current, position_shape_current)
            else:
                # print("ok")
                number_line_deleted += delete_lines_complete(board)
                score, level = calc_score_and_level(number_line_deleted)
                block_current = block_next
                shape_current = shape_next
                block_next = random_block(BLOCK_IMGS)
                shape_next = random_shape(SHAPES)
                position_shape_current = [
                    [3, 0], [4, 0], [5, 0], [6, 0],
                    [3, 1], [4, 1], [5, 1], [6, 1],
                    [3, 2], [4, 2], [5, 2], [6, 2],
                    [3, 3], [4, 3], [5, 3], [6, 3]
                ]
            current_frame = 0

        win.fill(DARK_CHARCOAL)
        win.blit(BOARD_IMG, (0, 0))
        draw_board(win, board, CELL_SIZE)
        draw_shape_next(win, BACKGROUND_IMGS, shape_next, block_next, CELL_SIZE)
        draw_score_and_level(win, score, (460, 200), level, (460, 130), FONT, WHITE)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()