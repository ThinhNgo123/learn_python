import json
from random import randint
from threading import Thread
from time import sleep

class UpdateJson:
	def __init__(self):
		self.data = None
		
	def load_data(self):
		with open("Data.json", "r") as file:
			self.data = json.load(file)
			print(self.data)
		self.data["Internet"]["Ethernet"]["IP"] = "192.168.1.1"
		self.data["Internet"]["Ethernet"]["Speed"] = "1/1000 (Mbps)"
		
	def update():
		UpdateJson()._update()
		
	def _update(self):
		if not self.data:
			self.load_data()
			print(self.data)
		else:
			Thread(target=self._update_thread).start()
		
	def _update_thread(self):
		ip = 2
		speed = 2
		while True:
			self.data["Internet"]["Ethernet"]["IP"] = self.data["Internet"]["Ethernet"]["IP"][:10] + str(ip)
			self.data["Internet"]["Ethernet"]["Speed"] = str(speed) + self.data["Internet"]["Ethernet"]["Speed"][1:]
			#print("ok")
			with open("Data.json", "w") as file:
				json.dump(self.data, file)
			ip += 1
			speed += 1
			sleep(1)
			
	def random(self):
		number = randint(0, 2)
		if number == 0:
			return str(randint(0, 9)) + str(randint(0, 9))
		elif number == 1:
			return str(randint(0, 9)) + chr(randint(97, 122))
		elif number == 2:
			return chr(randint(97, 122)) + str(randint(0, 9))
			
def main():
	UpdateJson.update()
		
if __name__ == "__main__":
	main()		