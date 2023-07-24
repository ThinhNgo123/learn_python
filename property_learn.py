class propertys:
	def __init__(self, fget):
		self.fget = fget
		self.fset = None
		self.fdel = None

	def __get__(self, instance, owner):
		print(instance)
		print(owner)
		return self.fget(instance)

	def __set__(self, instance, value):
		# print(instance, value)
		self.fset(instance, value)

	def __delete__(self, instance):
		self.fdel(instance)

	def setter(self, fset):
		# print(fset)
		self.fset = fset
		return self

	def deleter(self, fdel):
		self.fdel = fdel
		return self

class Number:
	def __init__(self):
		self.__x = 10
	# @property
	# x = propertys(x)
	@propertys
	def x(self):
		# print("get x")
		return self.__x

	@x.setter
	def x(self, value):
		print("set x =", value)
		self.__x = value

	@x.deleter
	def x(self):
		print("delete x")
		del self.__x

number = Number()
number.x = 20
print(number.x)
del number.x
# print(number.x)