"""
from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def fill(self, color):
		pass

	# @staticmethod
	def draw(self):
		print("draw implementation")

class Square(Shape):
	def fill(self, color):
		print("fill implementation")

# shape = Shape()
square = Square()
square.fill("Red")
square.draw()
print(Square.mro())
"""

"""
class Shape:
	def __init__(self):
		self._lineCount = 0

	def getLineCount(self):
		return self.__lineCount

class Square(Shape):
	def __init__(self):
		super(Square, self).__init__()
		# self.__lineCount = 4

	def getLineCount(self):
		return self._lineCount

square = Square()
lineCount = square._lineCount
print(lineCount)
"""

"""
class Shape:
	def __init__(self):
		self.name = "Shape"

	def getName(self):
		return self.name

class Square(Shape):
	def __init__(self):
		super(Square, self).__init__()
		self.name = "Square"
	
	def setX(self, value):
		self.x = value


	def draw(self):
		print("draw")
square = Square()
print(square.name)
square.setX(5)
square.__class__ = Shape
print(square.__class__)
print(square.name)
# square.draw()
print(square.getName())
print(square.x)
"""

"""
import abc
class Shape(abc.ABC):
	@abc.abstractmethod
	def get_area(self):
		pass

	@property
	@abc.abstractmethod
	def line_count(self):
		return 0

class Square(Shape):
	def __init__(self, s_length):
		self.sideLength = s_length

	def get_area(self):
		return self.sideLength ** 2

	@property
	def line_count(self):
		return 4

square = Square(5)
area = square.get_area()
print(area)
"""










