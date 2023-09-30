import os
print(os.path)
class Print(object):
	def __init__(self):
		self.data = None

	def print(self):
		print(self.data)

	def add_data(self, data):
		self.data = data

if __name__ == "__main__":
	print("test_pyc")