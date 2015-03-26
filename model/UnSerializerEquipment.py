#!/usr/bin/env python3
import json
from model.Equipment import Equipment

class UnSerializerEquipment :
	""" 
	class representing a collection of serialised
	equipments
	"""
	path = "data/equipment.json"

	def __init__(self):
		self.collection = []

	def unSerialize(self):
		"""
		Transforms a json File containing equipments informations
		into a list of equipment objects
		"""	
		try:
			with open(UnSerializerEquipment.path) as data:
				json_data = json.load(data)

				for item in json_data["data"]:
					equi = Equipment(item["ComInsee"],item["ComLib"],item["EquipementFiche"],item["EquAnneeService"]
						,item["EquNom"],item["EquNomBatiment"])
					self.collection.append(equi)
					
		except FileNotFoundError:
			print("fichier inexistant")
		except KeyError:
			print("erreur de clé, clé inéxistante ou mal orthographiée")


