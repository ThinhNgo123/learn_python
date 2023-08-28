import json
from random import randint
from threading import Thread
from time import sleep

class UpdateJson:
	def __init__(self):
		self.data = None
		self.read_status = False
		
	def load_data(self):
		if self.read_status == False:
			self.read_status = True
			with open("Json/Data.json", "r") as file:
				self.data = dict(json.load(file))
				#print(self.data)
			self.data["Internet"]["Ethernet"]["IP"] = "192.168.1.1"
			self.data["Internet"]["Ethernet"]["Speed"] = "1/1000 (Mbps)"
			self.read_status = False
		
	def update():
		obj = UpdateJson()
		obj._update()
		return obj
	
	def _update(self):
		if not self.data:
			self.load_data()
			#print(self.data["Internet"]["Ethernet"])
		Thread(target=self._update_thread).start()
		
	def _update_thread(self):
		ip = 2
		speed = 2
		while True:
			self.data["Internet"]["Ethernet"]["IP"] = self.data["Internet"]["Ethernet"]["IP"][:10] + str(ip)
			speed_str = self.data["Internet"]["Ethernet"]["Speed"]
			self.data["Internet"]["Ethernet"]["Speed"] = str(speed) + speed_str[speed_str.find("/"):]
			self.data["Internet"]["Ethernet"]["MAC"] = f"{self.random()}:{self.random()}:{self.random()}:{self.random()}:{self.random()}:{self.random()}"
			#print(self.data["Internet"]["Ethernet"])
			if self.read_status == False:
				self.read_status = True
				with open("Json/Data.json", "w") as file:
					json.dump(self.data, file)
				self.read_status = False
			ip += 1
			speed += 1
			
			sleep(3)
			
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