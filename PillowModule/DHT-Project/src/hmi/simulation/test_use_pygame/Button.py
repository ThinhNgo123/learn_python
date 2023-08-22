import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Button:

	def __init__(self, window, width=10, height=10, border=None, color_on=BLACK, color_off=WHITE, key=None):
		self.window = window
		self.width = width
		self.height = height
		self.border = border
		self.color_on = color_on
		self.color_off = color_off
		self.color = self.color_off
		self.key = key

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def set_border(self, border):
		self.border = border

	def set_color_on(self, color):
		self.color_on = color

	def set_color_off(self, color):
		self.color_off = color

	def set_key(self, key):
		self.key = key

	def set_color_off(self):
		self.color = self.color_off

	def draw(self, x=0, y=0):
		pygame.draw.rect(self.window, self.color, (x, y, self.width, self.height), border_radius=self.border)
		pygame.draw.rect(self.window, BLACK, (x, y, self.width, self.height), width=5)

	def check_key_down(self, key=None):
		if self.key:
			if self.key == key:
				self.color = self.color_on
			else:
				self.color = self.color_off
		else:
			self.color = self.color_off













