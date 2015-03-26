#!/usr/bin/env python3
import json
from model.Activity import Activity

class UnSerializerActivity :
	""" 
	class representing a collection of serialised
	activities
	"""
	path = "data/activity.json"

	def __init__(self):
		self.collection = []

	def unSerialize(self):
		""" 
		Transforms a json File containing activities informations
	    into a list of activity objects
		"""
		try:
			with open(UnSerializerActivity.path) as data:
				json_data = json.load(data)

				for item in json_data["data"]:
					acti = Activity(item["ComInsee"],item["ComLib"],item["EquipementId"],item["EquNbEquIdentique"]
						,item["ActCode"],item["ActLib"],item["EquActivitePraticable"],item["EquActivitePratique"],
						item["EquActiviteSalleSpe"],item["ActNivLib"])
					self.collection.append(acti)
					
		except FileNotFoundError:
			print("fichier inexistant")
		except KeyError:
			print("erreur de clé, clé inéxistante ou mal orthographiée")
