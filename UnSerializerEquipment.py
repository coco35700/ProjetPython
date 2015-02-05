#!/usr/bin/env python3
import json

class UnSerializerEquipment :
	''' class representing a collection of serialised
		equipments
	'''

	def __init__(self):
		self.collection = []

	def unSerialize(self):
		with open("Equipment.json") as data:
			json_data = json.load(data)

			for item in json_data["data"]:
				equi = Equipment(item["ComInsee"],item["ComLib"],item["equipementId"],item["equNbEquIdentique"]
					,item["actCode"],item["actLib"],item["equActivitePraticable"],item["equActivitePratique"],
					item["equActiviteSalleSpe"],item["actNivLib"])


seri = UnSerializerEquipment()
seri.unSerialize()
print(seri.collection)
