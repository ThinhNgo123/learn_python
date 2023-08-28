from json import load, dump
from threading import Thread
try:
	from UpdateJson import UpdateJson
except:
	from Json.UpdateJson import UpdateJson
from time import sleep

json_obj = UpdateJson.update()

class DataJson:
	PATH = "Data.json"
	PATH1 = "Json/Data.json"
	
	def __init__(self):
		self.data = None
	
	def load_json(self):
		while True:
			if not json_obj.read_status:
				json_obj.read_status = True
				try:
					with open(self.PATH, "r") as file:
						self.data = load(file)
				except:
					with open(self.PATH1, "r") as file:
						self.data = load(file)
				json_obj.read_status = False
			sleep(0.1)
			
			#print(self.data)
			
data_json = DataJson()
Thread(target=data_json.load_json).start()
#print(data_json.data)