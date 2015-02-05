#!/usr/bin/env python3

class Equipment :
	''' class representing an equipment
		has 10 characteristics, 6 have been selected
		all of thems are Strings
	'''

	def __init__(self,inseeNb,comLib,equipementId,equNbEquIdentique,actCode,actLib,
		equActivitePraticable,equActivitePratique,equActiviteSalleSpe,actNivLib):

		self.inseeNb = inseeNb 
		self.comLib = comLib
		self.equipementId = equipementId
		self.equNbEquIdentique = equNbEquIdentique
		self.actCode = actCode
		self.actLib = actLib
		self.equActivitePraticable = equActivitePraticable
		self.equActivitePratique = equActivitePratique
		self.equActiviteSalleSpe = equActiviteSalleSpe
		self.actNivLib = actNivLib

	def __str__(self):
		return "EQUIPMENT [commune : " + self.comLib + " , num INSEE : " + self.comInsee+" ]"