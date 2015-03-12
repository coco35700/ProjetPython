import sqlite3

class DataBase:


	def __init__(self):
		self.conn = sqlite3.connect('dataBase/DB.db')
		self.c = self.conn.cursor()

	def disconnect(self):
		self.conn.close()

	def connect(self):
		self.conn = sqlite3.connect('dataBase/DB.db')
		
	def creationTableInstallation(self):

		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations(comLib text,comInsee text,insCodePostal text,insLieuDit text,
						insNoVoie text , insLibelleVoie text , nb_Equipements text, nb_FicheEquipement text)''')
		self.conn.commit()

	def creationTableActivity(self):

		self.c.execute("DROP TABLE IF EXISTS activity")
		self.c.execute('''CREATE TABLE activity(inseeNb text, comLib text,equipementId text,equNbEquIdentique text,
						actCode text , actLib text , equActivitePraticable text , equActivitePratique text,
						equActiviteSalleSpe text, actNivLib text)''')
		self.conn.commit()

	def creationTableEquipment(self):

		self.c.execute("DROP TABLE IF EXISTS equipment")
		self.c.execute('''CREATE TABLE equipment(comInsee text, comLib text,equipmentFile text,equAnneeService text,
						equNom text , equNomBatiment text)''')
		self.conn.commit()

	def exportObjectList(self,listObjects):
		for item in listObjects:
			item.exportToDataBase(self)

		
