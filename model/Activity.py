#!/usr/bin/env python3

class Activity :
	''' class representing an activity
		has 10 characteristics, 10 have been selected
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
		return "ACTIVITY [commune : " + self.comLib + " , num INSEE : " + self.inseeNb+" , id : "+self.equipementId+" ]"

	def exportToDataBase(self,database):
		database.c.execute('''INSERT INTO activity
    		VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\")'''.format(
    			self.inseeNb.strip(),self.comLib.strip(),self.equipementId.strip(),self.equNbEquIdentique.strip(),
    			self.actCode,self.actLib,self.equActivitePraticable,self.equActivitePratique,
    			self.equActiviteSalleSpe,self.actNivLib))

