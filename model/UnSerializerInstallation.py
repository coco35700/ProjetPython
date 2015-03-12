#!/usr/bin/env python3
import json
from model.Installation import Installation

class UnSerializerInstallation :
	""" class representing a collection of serialised
		installations
	"""
	path = "data/Installation.json"

	def __init__(self):
		self.collection = []

	""" Transforms a json File containing installations informations
		into a list of installation objects
	"""
	def unSerialize(self):
		with open(UnSerializerInstallation.path) as data:
			json_data = json.load(data)

			for item in json_data["data"]:
				inst = Installation(item["ComLib"],item["ComInsee"],item["InsCodePostal"],item["InsLieuDit"]
					,item["InsNoVoie"],item["InsLibelleVoie"],item["Nb_Equipements"],item["Nb_FicheEquipement"])
				self.collection.append(inst)

