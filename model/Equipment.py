#!/usr/bin/env python3

class Equipment :
	''' 
	class representing an equipment
	has too many characteristics, 6 have been selected
	all of thems are Strings
	'''

	def __init__(self,com_insee,com_lib,equipment_file,equ_annee_service,equ_nom,equ_nomBatiment):

		self.com_insee = com_insee 
		self.com_lib = com_lib
		self.equipment_file = equipment_file
		self.equ_annee_service = equ_annee_service
		self.equ_nom = equ_nom
		self.equ_nomBatiment = equ_nomBatiment

	def __str__(self):
		"""
		allows to check some attributes while testing our objects
		"""
		return "EQUIPMENT [nom : "+self.equ_nom+", com_lib : " + self.com_lib + " , num INSEE : " + self.com_insee+" ]"

	def export_to_database(self,database):
		"""
		Allows our object to add itself to the database ( gives a database object in parameter )
		"""
		database.c.execute('''INSERT INTO equipment
    		VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\")'''.format(
    			self.com_insee,self.com_lib,self.equipment_file,
    			self.equ_annee_service,self.equ_nom.replace('"',"'"),self.equ_nomBatiment))
		