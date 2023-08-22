import pygame

class Text:
	def __init__(self, window, text, font, size, color):
		self.window = window
		self.text = text
		self.color = color
		self.font = pygame.font.Font(font, size)
		self.surface = self._get_surface()

	def draw(self, x, y):
		rect = self._get_rect(x, y)
		self.window.blit(self.surface, rect)

	def _get_rect(self, x, y):
		rect = self.surface.get_rect()
		rect.center = (x, y)
		return rect

	def _get_surface(self):
		return self.font.render(self.text, True, self.color)
