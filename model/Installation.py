#!/usr/bin/env python3

class Installation:

	""" 
	class representing an installation
	has 29 characteristics 8 have been selected, all of thems are Strings
	"""

	def __init__(self, com_lib, com_insee, ins_code_postal, ins_lieu_dit, 
		ins_no_voie, ins_libelle_voie, nb_equipements , nb_fiche_equipement):

		self.com_lib = com_lib
		self.com_insee = com_insee
		self.ins_code_postal = ins_code_postal
		self.ins_lieu_dit = ins_lieu_dit
		self.ins_no_voie = ins_no_voie
		self.ins_libelle_voie = ins_libelle_voie
		self.nb_equipements = nb_equipements
		self.nb_fiche_equipement = nb_equipements


	def __str__(self):
		"""
		allows to check some attributes while testing our objects
		"""
		return "INSTALLATION [commune : " + self.com_lib + " , num insEE : " + self.com_insee+" , nb Equipements : "+self.nb_equipements+" ]"

	def export_to_database(self,database):
		"""
		Allows our object to add itself to the database ( gives a database object in parameter )
		"""
		database.c.execute(''' INSERT INTO installations VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\")'''.format(
			self.com_lib, self.com_insee, self.ins_code_postal , self.ins_lieu_dit, self.ins_no_voie,
			self.ins_libelle_voie, self.nb_equipements , self.nb_fiche_equipement))
		