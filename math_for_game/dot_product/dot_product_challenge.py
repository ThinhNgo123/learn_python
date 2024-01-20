import math
import sys
import pygame
from typing import Tuple, List
from pygame.locals import *
pygame.init()

COLOR = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

class Game:
    FPS = 30
    SCREEN_SIZE = (800, 600)
    REG2RAD = math.pi / 180

    def __init__(self) -> None:
        self.running = True
        self.is_collided = False
        self.screen = pygame.display.set_mode(Game.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.mouse_pos = (0, 0)

        self.camera = Camera()

        self.character = Character((Game.SCREEN_SIZE[0] // 4, Game.SCREEN_SIZE[1] // 2), 20)

        self.sound = pygame.mixer.Sound("./coi_canh_bao.mp3")
        self.sound.set_volume(0.1)

    def get_is_collided(self):
        return self.is_collided

    def draw_background(self):
        self.screen.fill(COLOR["white"])

    def draw(self):
        self.draw_background()
        self.camera.draw(self.screen)
        self.character.draw(self.screen)

    def update(self):
        self.camera.update(self.mouse_pos)
        self.check_collision()
        pygame.display.update()

    def handle_event(self):
        self.check_quit()
        self.handle_mouse()
        self.handle_keyboard()
        self.handle_sound()

    def handle_keyboard(self):
        key_board = pygame.key.get_pressed()
        if key_board[K_a]:
            self.camera.rotate_left()
        if key_board[K_d]:
            self.camera.rotate_right()
        if key_board[K_DOWN]:
            self.character.move([0, 1])
        if key_board[K_UP]:
            self.character.move([0, -1])
        if key_board[K_LEFT]:
            self.character.move([-1, 0])
        if key_board[K_RIGHT]:
            self.character.move([1, 0])

    def handle_mouse(self):
        for event in pygame.event.get(MOUSEMOTION):
            self.mouse_pos = event.pos

    def handle_sound(self):
        if self.is_collided:
            self.sound.play()
        else:
            self.sound.stop()

    def check_quit(self):
        for _ in pygame.event.get(QUIT):
            self.running = False
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_ESCAPE:
                self.running = False
                return
            pygame.event.post(event)        

    def check_collision(self):
        camera_centerx, camera_centery = self.camera.get_center()
        character_centerx, character_centery = self.character.get_center()
        
        pygame.draw.line(self.screen, COLOR["black"], (camera_centerx, camera_centery), (character_centerx, character_centery))
        
        vector1 = (self.camera.LASER_WIDTH * math.cos(self.camera.alpha * Game.REG2RAD), -self.camera.LASER_WIDTH * math.sin(self.camera.alpha * Game.REG2RAD))
        vector2 = (character_centerx - camera_centerx, character_centery - camera_centery)
        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

        if dot_product < 0:
            self.is_collided = False
            return

        dis_x = abs(vector2[0])
        distance = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)
        distance1 = distance * (dis_x - self.character.size / 2)

        if distance == 0:
            self.is_collided = True
            return

        angle = math.acos(dot_product / (self.camera.LASER_WIDTH * distance))
        
        if self.camera.LASER_WIDTH * dis_x >= distance1 and \
            angle < self.camera.LASER_ANGLE:
            self.is_collided = True
            return

        self.is_collided = False

    def quit(self):
        pygame.quit()
        sys.exit()

    def loop(self):
        while self.running:
            self.handle_event()
            self.update()
            self.draw()
        self.quit()

class Camera:
    SCALE = 0.5
    ROTATE_SPEED = 1
    LASER_WIDTH = 250
    LASER_ANGLE = 30 * math.pi / 180

    def __init__(self) -> None:
        self.alpha = 0

        self.camera_image = pygame.image.load("./camera.png").convert_alpha()
        self.camera_image = self.scale_image(self.camera_image)
        self.camera_image_rect = self.camera_image.get_rect()
        self.camera_image_rect.center = (Camera.LASER_WIDTH - 4, Camera.LASER_WIDTH - 17)

        self.laser_image = pygame.image.load("./red_pie.png")
        self.laser_image_rect = self.laser_image.get_rect()
        self.laser_image_rect.center = (Camera.LASER_WIDTH, Camera.LASER_WIDTH)
        
        self.surface = pygame.Surface((Camera.LASER_WIDTH * 2 + 2, Camera.LASER_WIDTH * 2), flags=SRCALPHA)
        self.surface_rect = self.surface.get_rect()
        
        self.draw_camera(self.surface)
        self.draw_laser(self.surface)

        self.current_surface = self.surface

    def get_center(self):
        x, y = self.surface_rect.center
        return x, y

    def draw_camera(self, surface: pygame.Surface):
        surface.blit(self.camera_image, self.camera_image_rect)

    def draw_laser(self, surface: pygame.Surface):
        pygame.draw.line(
            surface, 
            COLOR["red"], 
            (Camera.LASER_WIDTH, Camera.LASER_WIDTH),
            (Camera.LASER_WIDTH + Camera.LASER_WIDTH * math.cos(Camera.LASER_ANGLE), Camera.LASER_WIDTH - Camera.LASER_WIDTH * math.sin(Camera.LASER_ANGLE)),
            width=2
        )
        pygame.draw.line(
            surface, 
            COLOR["red"], 
            (Camera.LASER_WIDTH, Camera.LASER_WIDTH),
            (Camera.LASER_WIDTH + Camera.LASER_WIDTH * math.cos(Camera.LASER_ANGLE), Camera.LASER_WIDTH + Camera.LASER_WIDTH * math.sin(Camera.LASER_ANGLE)),
            width=2
        )
        # pygame.draw.arc(surface, (*COLOR["red"], 100), (0, 0, self.LASER_WIDTH * 2, self.LASER_WIDTH * 2), -self.LASER_ANGLE, self.LASER_ANGLE, width=500)
        surface.blit(self.laser_image, self.laser_image_rect)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.current_surface, self.surface_rect)

    def update(self, mouse_pos: Tuple[int, int]):
        self.surface_rect.center = mouse_pos

    def scale_image(self, image: pygame.Surface):
        size_width, size_height = image.get_size()
        return pygame.transform.scale(image, (int(size_width * Camera.SCALE), int(size_height * Camera.SCALE)))

    def rotate_left(self):
        self.alpha += Camera.ROTATE_SPEED
        self.current_surface = pygame.transform.rotate(self.surface, self.alpha)
        self.surface_rect = self.current_surface.get_rect()

    def rotate_right(self):
        self.alpha -= Camera.ROTATE_SPEED
        self.current_surface = pygame.transform.rotate(self.surface, self.alpha)
        self.surface_rect = self.current_surface.get_rect()

class Character:
    def __init__(self, pos: List[int], size: int = 50) -> None:
        self.pos = list(pos)
        self.size = size

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, COLOR["green"], (*self.pos, self.size, self.size))

    def move(self, velocity: List[int]):
        # print(self.pos[0] + velocity[0])
        if 0 <= self.pos[0] + velocity[0] <= Game.SCREEN_SIZE[0] - self.size:
            self.pos[0] += velocity[0]
        if 0 <= self.pos[1] + velocity[1] <= Game.SCREEN_SIZE[1] - self.size:
            self.pos[1] += velocity[1]

    def get_center(self):
        return self.pos[0] + self.size // 2, self.pos[1] + self.size // 2

if __name__ == "__main__":
    game = Game().loop()

# from PIL import Image, ImageDraw
# import math
# img = Image.new("RGBA",size=(500, 500), color=(255, 255, 255, 0))
# draw_image = ImageDraw.Draw(img)
# draw_image.pieslice(((0,0), (500,500)), -30, 30, fill=(255, 0, 0, 100))
# img.show()
# img.save("./pie.png", format="png")