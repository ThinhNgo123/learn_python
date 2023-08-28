from UpdateJson import UpdateJson
from json import load
from time import sleep

json_obj = UpdateJson.update()

for i in range(50):
	if not json_obj.read_status:
		json_obj.read_status = True
		with open("Data.json", "r") as file:
			data = load(file)["Internet"]["Ethernet"]
		json_obj.read_status = False
		for key in data:
			print(f"{key}: {data[key]}")
		#print(data)
		print()
	sleep(0.5)