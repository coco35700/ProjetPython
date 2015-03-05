#!/usr/bin/env python3

class Equipment :
	''' class representing an equipment
		has too many characteristics, 6 have been selected
		all of thems are Strings
	'''

	def __init__(self,comInsee,comLib,equipmentFile,equAnneeService,equDateMaj,equNomBatiment):

		self.comInsee = comInsee 
		self.comLib = comLib
		self.equipmentFile = equipmentFile
		self.equAnneeService = equAnneeService
		self.equDateMaj = equDateMaj
		self.equNomBatiment = equNomBatiment

	def __str__(self):
		return "EQUIPMENT [comLib : " + self.comLib + " , num INSEE : " + self.comInsee+" , lastMAJ : "+self.equDateMaj+" ]"