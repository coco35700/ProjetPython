#!/usr/bin/env python3

class Activity :
	''' 
	class representing an activity
	has 10 characteristics, 10 have been selected
	all of thems are Strings
	'''

	def __init__(self,insee_nb,com_lib,equipment_id,equ_identique,act_code,act_lib,
		equ_Activite_prat,equ_Activite_pratique,equ_Activite_sallespe,acti_niv_lib):

		self.insee_nb = insee_nb 
		self.com_lib = com_lib
		self.equipment_id = equipment_id
		self.equ_identique = equ_identique
		self.act_code = act_code
		self.act_lib = act_lib
		self.equ_Activite_prat = equ_Activite_prat
		self.equ_Activite_pratique = equ_Activite_pratique
		self.equ_Activite_sallespe = equ_Activite_sallespe
		self.acti_niv_lib = acti_niv_lib

	def __str__(self):
		"""
		allows to check some attributes while testing our objects
		"""
		return "ACTIVITY [commune : " + self.com_lib + " , num INSEE : " + self.insee_nb+" , id : "+self.equipment_id+" ]"

	def export_to_database(self,database):
		"""
		Allows our object to add itself to the database ( gives a database object in parameter )
		"""
		database.c.execute('''INSERT INTO activity
    		VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\")'''.format(
    			self.insee_nb.strip(),self.com_lib.strip(),self.equipment_id.strip(),self.equ_identique.strip(),
    			self.act_code,self.act_lib,self.equ_Activite_prat,self.equ_Activite_pratique,
    			self.equ_Activite_sallespe,self.acti_niv_lib))

