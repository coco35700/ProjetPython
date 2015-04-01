#!/usr/bin/env python3
import json
from model.Installation import Installation

class UnSerializerInstallation :
	""" 
	class representing a collection of serialised
	installations
	"""
	path = "data/installation.json"

	def __init__(self):
		self.collection = []


	def unSerialize(self):
		""" 
		Transforms a json File containing installations informations
		into a list of installation objects

		>>> un = UnSerializerInstallation()
	    >>> un.unSerialize("../test/testInstallation.json")
	    >>> un.collection[0].InsNbPlaceParking
	    '50'
		"""

		if path == None:
			path = UnSerializerActivity.path

		try:
			with open(path) as data:
				json_data = json.load(data)

				for item in json_data["data"]:
					inst = Installation(item["ComLib"],item["ComInsee"],item["InsCodePostal"],item["InsLieuDit"]
						,item["InsNoVoie"],item["InsLibelleVoie"],item["Nb_Equipements"],item["Nb_FicheEquipement"])
					self.collection.append(inst)
					
		except FileNotFoundError:
			print("fichier inexistant")
		except KeyError:
			print("erreur de clé, clé inéxistante ou mal orthographiée")



