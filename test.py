# # import pygame
# # import random

# # # Khởi tạo Pygame
# # pygame.init()

# # # Đặt kích thước màn hình
# # screen_width = 800
# # screen_height = 600
# # screen = pygame.display.set_mode((screen_width, screen_height))

# # # Đặt tiêu đề cửa sổ
# # pygame.display.set_caption('Game Đua Xe')

# # # Tải hình ảnh và tọa độ
# # # player_car = pygame.image.load('player_car.png')
# # player_car = pygame.image.load('car.png')
# # player_car = pygame.transform.scale(player_car, (100, 100))
# # player_car_rect = player_car.get_rect()
# # player_car_rect.topleft = (350, 450)

# # opponent_car = pygame.image.load('obstacles.png')
# # # opponent_car = pygame.image.load('opponent_car.png')
# # opponent_car_rect = opponent_car.get_rect()
# # opponent_car_rect.topleft = (random.randint(100, 700), -200)

# # road = pygame.image.load('background.png')
# # road = pygame.transform.scale(road, (screen_width, screen_height))
# # # road = pygame.image.load('road.png')

# # # Cài đặt vận tốc xe đối thủ
# # opponent_speed = 5

# # clock = pygame.time.Clock()

# # # Chạy vòng lặp chính của game
# # running = True
# # while running:
# #     screen.blit(road, (0, 0))
# #     screen.blit(player_car, player_car_rect.topleft)
# #     screen.blit(opponent_car, opponent_car_rect.topleft)

# #     for event in pygame.event.get():
# #         # Thoát game khi nhấn nút đóng cửa sổ
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Xử lý di chuyển xe người chơi
# #     keys = pygame.key.get_pressed()
# #     if keys[pygame.K_LEFT] and player_car_rect.left > 100:
# #         player_car_rect.x -= 5
# #     if keys[pygame.K_RIGHT] and player_car_rect.right <700:
# #         player_car_rect.x += 5

# #     # Di chuyển xe đối thủ
# #     opponent_car_rect.y += opponent_speed

# #     # Tạo lại xe đối thủ khi đi ra ngoài màn hình
# #     if opponent_car_rect.top > screen_height:
# #         opponent_car_rect.topleft = (random.randint(100, 700), -200)

# #     # Kiểm tra va chạm
# #     if player_car_rect.colliderect(opponent_car_rect):
# #         running = False

# #     pygame.display.flip()
# #     clock.tick(60)

# # pygame.quit()


# import pygame
# import random

# # Khởi tạo Pygame
# pygame.init()

# # Đặt kích thước màn hình
# screen_width = 1000
# screen_height = 550
# screen = pygame.display.set_mode((screen_width, screen_height))

# # Đặt tiêu đề cửa sổ
# pygame.display.set_caption('Game Đua Xe')

# # Tải hình ảnh và tọa độ
# player_car = pygame.image.load('car (1).png').convert_alpha()
# # player_car = pygame.transform.scale(player_car, (100, 100))
# player_car_rect = player_car.get_rect()
# player_car_rect.topleft = (350, 450)

# opponent_cars = []
# for _ in range(3):
#     opponent_car = pygame.image.load('obstacles.png').convert_alpha()

#     opponent_car_rect = opponent_car.get_rect()
#     opponent_car_rect.topleft = (random.randint(100, 700), random.randint(-800, -200))
#     opponent_cars.append((opponent_car, opponent_car_rect))

# road = pygame.image.load('background.png').convert_alpha()
# road = pygame.transform.scale(road, (screen_width, screen_height))

# # Cài đặt vận tốc xe đối thủ
# opponent_speeds = [5, 6, 7] 

# # Tạo font chữ và điểm số
# font = pygame.font.Font(None, 36)
# score = 0

# clock = pygame.time.Clock()

# # Chạy vòng lặp chính của game
# running = True
# while running:
#     screen.blit(road, (0, 0))
#     screen.blit(player_car, player_car_rect.topleft)

#     for opponent_car, opponent_car_rect in opponent_cars:
#         screen.blit(opponent_car, opponent_car_rect.topleft)

#     # Hiển thị điểm số
#     score_text = font.render(f"Score: {score}", True, (255, 255, 255))
#     screen.blit(score_text, (10, 10))

#     for event in pygame.event.get():
#         # Thoát game khi nhấn nút đóng cửa sổ
#         if event.type == pygame.QUIT:
#             running = False

#     # Xử lý di chuyển xe người chơi
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_car_rect.left > 100:
#         player_car_rect.x -= 5
#     if keys[pygame.K_RIGHT] and player_car_rect.right < 900:#1200:
#         player_car_rect.x += 5

#     # Di chuyển xe đối thủ và kiểm tra va chạm
#     for i, (opponent_car, opponent_car_rect) in enumerate(opponent_cars):
#         opponent_car_rect.y += opponent_speeds[i]

#         # Tạo lại xe đối thủ khi đi ra ngoài màn hình và tăng điểm
#         if opponent_car_rect.top > screen_height:
#             opponent_car_rect.topleft = (random.randint(100, 700), random.randint(-800, -200))
#             opponent_speeds[i] += 0.5#50  # Tăng độ khó
#             score += 1

#         # Kiểm tra va chạm
#         if player_car_rect.colliderect(opponent_car_rect):
#             print(f"Score: {score}")
#             running = False

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_cube(size): 
    glBegin(GL_QUADS) # mặt trước 
    glVertex3f(-size/2, -size/2, size/2) 
    glVertex3f(size/2, -size/2, size/2) 
    glVertex3f(size/2, size/2, size/2) 
    glVertex3f(-size/2, size/2, size/2) # mặt sau 
    glVertex3f(-size/2, -size/2, -size/2) 
    glVertex3f(-size/2, size/2, -size/2) 
    glVertex3f(size/2, size/2, -size/2) 
    glVertex3f(size/2, -size/2, -size/2) # mặt trái 
    glVertex3f(-size/2, -size/2, size/2) 
    glVertex3f(-size/2, size/2, size/2) 
    glVertex3f(-size/2, size/2, -size/2) 
    glVertex3f(-size/2, -size/2, -size/2) # mặt phải 
    glVertex3f(size/2, -size/2, size/2) 
    glVertex3f(size/2, -size/2, -size/2) 
    glVertex3f(size/2, size/2, -size/2) 
    glVertex3f(size/2, size/2, size/2) # mặt trên 
    glVertex3f(-size/2, size/2, size/2) 
    glVertex3f(size/2, size/2, size/2) 
    glVertex3f(size/2, size/2, -size/2) 
    glVertex3f(-size/2, size/2, -size/2) # mặt dưới 
    glVertex3f(-size/2, -size/2, size/2) 
    glVertex3f(-size/2, -size/2, -size/2) 
    glVertex3f(size/2, -size/2, -size/2) 
    glVertex3f(size/2, -size/2, size/2) 
    glEnd()

def draw_car():
    # glPushMatrix()
    # glColor3f(1, 0, 0)
    # glTranslate(car_x, car_y, car_z)
    # # glutSolidCube(2)
    # draw_cube(2)
    # glPopMatrix()
    glPushMatrix() 
    glColor3f(1, 0, 0) 
    glTranslate(car_x, car_y, car_z) 
    glScalef(2, 2, 2) 
    draw_cube(1) 
    glPopMatrix()

def draw_track():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    glVertex3f(-10, -1, -10)
    glVertex3f(-10, -1, 10)
    glVertex3f(10, -1, 10)
    glVertex3f(10, -1, -10)
    glEnd()

pygame.init()
display = (800, 600)
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glTranslate(0, 0, -20)

car_x, car_y, car_z = 0, 0, 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= 1
            if event.key == pygame.K_RIGHT:
                car_x += 1
            if event.key == pygame.K_UP:
                car_z += 1
            if event.key == pygame.K_DOWN:
                car_z -= 1

    # glutInit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    draw_car()
    draw_track()

    pygame.display.flip()

    clock.tick(60)
