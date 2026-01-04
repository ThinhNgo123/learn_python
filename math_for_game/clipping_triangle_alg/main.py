import types
import pygame
from typing import List

WIDTH = 1000
HEIGHT = 600

class Vec2(object):
	def __init__(self, x=0, y=0) -> None:
		self.x = x
		self.y = y
	
	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vec2(self.x - other.x, self.y - other.y)

	def __iadd__(self, other):
		# print("rijfirj")
		self.x += other.x
		self.y += other.y
		return self

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def dot(self, other):
		return self.x * other.x + self.y * other.y
	
	def __str__(self):
		return f"({self.x}, {self.y})"

class MoveSystem:
	def __init__(self, speed, velocity: Vec2, points=None) -> None:
		self.speed = speed
		self.velocity = velocity
		self.points: List[Vec2] = points

	def set_points(self, points):
		self.points = points

	def handle_event(self):
		keys = pygame.key.get_pressed()
		move_x = 0
		move_y = 0
		if keys[pygame.K_UP]:
			move_y = - self.velocity.y * self.speed
		if keys[pygame.K_DOWN]:
			move_y = self.velocity.y * self.speed
		if keys[pygame.K_RIGHT]:
			move_x = self.velocity.x * self.speed
		if keys[pygame.K_LEFT]:
			move_x = - self.velocity.x * self.speed

		if move_x != 0 or move_y != 0:
			for point in self.points:
				point += Vec2(move_x, move_y)
			
class PointSystem:
	def __init__(self) -> None:
		self.points: List[Vec2] = []

	def add_point(self, point: Vec2):
		self.points.append(point)

	def get_points(self):
		return self.points

	def clear(self):
		self.points.clear()

class RenderSystem:
	def __init__(self, surface) -> None:
		self.surface = surface
		self.line_color = (255, 0, 0)
		self.is_fill = False
		self.line_width = 2
		self.render_points = None

	def set_render_points(self, points):
		self.render_points = points

	def draw_triangles(self):
		if self.render_points == None or len(self.render_points) < 3 or len(self.render_points) % 3 != 0:
			return
		draw_points = [(point.x, point.y) for point in self.render_points]
		# print("draw")
		for i in range(0, len(draw_points), 3):
			pygame.draw.polygon(self.surface, self.line_color, draw_points[i:i+3], 0 if self.is_fill else self.line_width)

class SplitPolygonSystem:
	def __init__(self) -> None:
		pass
	
	def triangle_splits(self, points):
		if points == None or len(points) < 3:
			return points
		new_points = []
		for i in range(1, len(points) - 1):
			new_points.append(points[0])
			new_points.append(points[i])
			new_points.append(points[i+1])
		return new_points

class ClippingSystem:
	def __init__(self, topleft, width, height) -> None:
		self.topleft = Vec2(topleft[0], topleft[1])
		self.bottomleft = Vec2(topleft[0], topleft[1] + height)
		self.topright = Vec2(topleft[0] + width, topleft[1])
		self.bottomright = Vec2(topleft[0], topleft[1] + height)

	def intersec(self, a: Vec2, b: Vec2, c: Vec2, d: Vec2):
		ab = b - a
		cd = d - c
		epsilon = 0.00001
		k2 = (ab.x * (c.y - a.y) - ab.y * (c.x - a.x)) / (ab.y * cd.x - ab.x * cd.y)
		print(ab, cd, k2)
		if k2 > epsilon:
			return Vec2(k2 * cd.x + c.x, k2 * cd.y + c.y)
		return None

	def check_inside(self, point: Vec2):
		return self.topleft.x <= point.x <= self.topright.x and self.topright.y <= point.y <= self.bottomright.y

	def clipping(self, points):
		# print(points)
		if points == None or len(points) % 3 != 0 or len(points) < 3:
			return points
		new_points = []
		edges = [
			[self.topleft, self.topright],
			[self.topright, self.bottomright],
			[self.bottomright, self.bottomleft],
			[self.bottomleft, self.topleft]
		] # top, right, bottom, left
		for i in range(0, len(points), 3):
			inside = [point for point in points[i:i+3] if self.check_inside(point)]
			onside = set(points[i:i+3]) - set(inside)
			len_inside = len(inside)
			len_onside = len(onside)
			print(len_inside, len_onside)
			if len_inside == 0:
				continue
			elif len_inside == 1:
				new_points.extend(points[i:i+3])
				pass
			elif len_inside == 2:
				new_points.extend(points[i:i+3])
				pass
			else:
				new_points.extend(points[i:i+3])
		return new_points

class Screen:
	def __init__(self, width, height, clear_color = (0, 0, 0)):
		self.width = width
		self.height = height
		self.ratio = 0.7
		self.main_width = self.width * self.ratio
		self.main_height = self.height * self.ratio
		self.clear_color = clear_color
		self.main_clear_color = (255, 255, 255)
		self.running = True

		self.screen_display = pygame.display.set_mode((self.width, self.height))
		self.screen_main = pygame.Surface((self.main_width, self.main_height))

		self.point_system = PointSystem()
		self.move_system = MoveSystem(0.3, Vec2(5, 5), self.point_system.get_points())
		self.split_polygon_system = SplitPolygonSystem()
		self.clipping_system = ClippingSystem(
			topleft=((self.width - self.main_width) // 2, (self.height - self.main_height) // 2),
			width=self.main_width,
			height=self.main_height
		)
		self.render_system = RenderSystem(self.screen_display)

	def run(self):
		while self.running:
			self.clear()
			self.event_process()
			self.update()
			self.draw()
			self.swap()

	def clear(self):
		self.screen_display.fill(self.clear_color)
		self.screen_main.fill(self.main_clear_color)

	def event_process(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				elif event.key == pygame.K_r:
					self.point_system.clear()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_valid_point(event.pos):
				self.point_system.add_point(Vec2(event.pos[0], event.pos[1]))
				# print(list(map(lambda p:(p.x, p.y), self.point_system.points)), event.pos)
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
				self.render_system.is_fill = not self.render_system.is_fill
			else:
				pygame.event.post(event)
		
		self.move_system.handle_event()

	def is_valid_point(self, point):
		top_left = ((self.width - self.main_width) // 2, (self.height - self.main_height) // 2)
		bottom_right = ((self.width + self.main_width) // 2, (self.height + self.main_height) // 2)
		return top_left[0] <= point[0] <= bottom_right[0] and \
			top_left[1] <= point[1] <= bottom_right[1]

	def update(self):
		points = self.split_polygon_system.triangle_splits(self.point_system.get_points())
		points = self.clipping_system.clipping(points)
		# print(points)
		self.render_system.set_render_points(points)

	def draw(self):
		self.screen_display.blit(
			self.screen_main, 
			((self.width - self.main_width) / 2, (self.height - self.main_height) / 2)
		)
		self.render_system.draw_triangles()

	def swap(self):
		pygame.display.flip()

def main():
	# print(ClippingSystem((1, 1), 1, 1).intersec(
	# 	Vec2(1, 5),
	# 	Vec2(2, 8),
	# 	Vec2(0, 3),
	# 	Vec2(-1, 8)
	# ))
	screen = Screen(WIDTH, HEIGHT)
	screen.run()

if __name__ == '__main__':
	main()