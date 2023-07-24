class Resources:
	def __del__(self):
		print("died")

res = Resources()

class Package:
	def __enter__(self):
		print("enter")
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		print(self, exc_type, exc_value, traceback)
		print("exit")

with Package() as package:
	# print(package)
	print("some operations")