import pygame
import sys
from .Button import Button
from .Text import Text

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Control:
	def __init__(self, screen):
		self.screen = screen
		self.control_surface = pygame.Surface((300, 300))
		self.WIDTH_BUTTON = 100
		self.HEIGHT_BUTTON = 100
		self.BORDER_BUTTON = 30
		self.FONT = "test_use_pygame/Source Sans Pro/SourceSansPro-Black.ttf"
		self.FONT1 = "./Font/Source Sans Pro/SourceSansPro-Black.ttf"
		self.FONT_SIZE = 20
		self.FONT_COLOR = BLACK
		self.buttons = [
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_UP),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_LEFT),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_RIGHT),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_DOWN),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_RETURN),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_F1),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_F2),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_F3),
					Button(self.control_surface, self.WIDTH_BUTTON, self.HEIGHT_BUTTON, self.BORDER_BUTTON, GREEN, RED, pygame.K_F4)
				]
		try:
			self.texts = [
						Text(self.control_surface, "UP", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "LEFT", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "RIGHT", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "DOWN", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "OK", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F1", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F2", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F3", self.FONT, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "DELETE", self.FONT, self.FONT_SIZE, BLACK)
					]
		except:
			self.texts = [
						Text(self.control_surface, "UP", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "BACK", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "NEXT", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "DOWN", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "OK", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F1", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F2(Help)", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F3(ADD)", self.FONT1, self.FONT_SIZE, BLACK),
						Text(self.control_surface, "F4(DEL)", self.FONT1, self.FONT_SIZE, BLACK)
					]
	def check_key_down(self, event):
		for button in self.buttons:
			button.check_key_down(event.key)
			
	def check_key_up(self):
		for button in self.buttons:
			button.check_key_down()

	def draw(self, x, y):
		self.buttons[0].draw(100, 0)
		self.buttons[1].draw(0, 100)
		self.buttons[2].draw(200, 100)
		self.buttons[3].draw(100, 200)
		self.buttons[4].draw(100, 100)
		self.buttons[5].draw(0, 0)
		self.buttons[6].draw(200, 0)
		self.buttons[7].draw(0, 200)
		self.buttons[8].draw(200, 200)

		self.texts[0].draw(100 + self.buttons[0].width // 2, self.buttons[0].height // 2)
		self.texts[1].draw(0 + self.buttons[1].width // 2, 100 + self.buttons[1].height // 2)
		self.texts[2].draw(200 + self.buttons[2].width // 2, 100 + self.buttons[2].height // 2)
		self.texts[3].draw(100 + self.buttons[3].width // 2, 200 + self.buttons[3].height // 2)
		self.texts[4].draw(100 + self.buttons[4].width // 2, 100 + self.buttons[4].height // 2)
		self.texts[5].draw(self.buttons[4].width // 2, self.buttons[4].height // 2)
		self.texts[6].draw(200 + self.buttons[4].width // 2, self.buttons[4].height // 2)
		self.texts[7].draw(self.buttons[4].width // 2, 200 + self.buttons[4].height // 2)
		self.texts[8].draw(200 + self.buttons[4].width // 2, 200 + self.buttons[4].height // 2)

		self.screen.blit(self.control_surface, (x, y))