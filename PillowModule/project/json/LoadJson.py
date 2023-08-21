from UpdateJson import UpdateJson
from json import load
from time import sleep

UpdateJson.update()
with open("Data.json", "r") as file:
	data = load(file)
print(data)
"""
for i in range(10):
	with open("Data.json", "r") as file:
		data = load(file)["Internet"]["Ethernet"]
	for key in data:
		print(f"{key}: {data[key]}")
	#print(data)
	print()
	sleep(2)"""