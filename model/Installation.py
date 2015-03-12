#!/usr/bin/env python3

class Installation:

	""" class representing an installation
		has 29 characteristics 8 have been selected, all of thems are Strings
	"""

	def __init__(self, comLib, comInsee, insCodePostal , insLieuDit, 
		insNoVoie, insLibelleVoie, nb_Equipements , nb_FicheEquipement):

		self.comLib = comLib
		self.comInsee = comInsee
		self.insCodePostal = insCodePostal
		self.insLieuDit = insLieuDit
		self.insNoVoie = insNoVoie
		self.insLibelleVoie = insLibelleVoie
		self.nb_Equipements = nb_Equipements
		self.nb_FicheEquipement = nb_Equipements

	def __str__(self):
		return "INSTALLATION [commune : " + self.comLib + " , num insEE : " + self.comInsee+" , nb Equipements : "+self.nb_Equipements+" ]"

	def exportToDataBase(self,database):
		database.c.execute(''' INSERT INTO installations VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\")'''.format(
			self.comLib, self.comInsee, self.insCodePostal , self.insLieuDit, self.insNoVoie,
			self.insLibelleVoie, self.nb_Equipements , self.nb_FicheEquipement))
		