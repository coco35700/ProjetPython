import sqlite3

class DataBase:


	def __init__(self):
		self.conn = sqlite3.connect('DB.db')
		self.c = self.conn.cursor()

	def disconnect(self):
		self.conn.close()
		
	def creationTableInstallation(self):
		c = self.conn.cursor()

		c.execute("DROP TABLE IF EXISTS installations")
		c.execute('''CREATE TABLE installations(comLib text,comInsee text,insCodePostal text,insLieuDit text,
						insNoVoie text , insLibelleVoie text , nb_Equipements text, nb_FicheEquipement text)''')
		self.conn.commit()
		self.conn.close()

	def creationTableEquipement(self):
		self.conn = sqlite3.connect('DB.db')
		c = self.conn.cursor()

		c.execute("DROP TABLE IF EXISTS equipement")
		c.execute('''CREATE TABLE equipement(inseeNb text, comLib text,equipementId text,equNbEquIdentique text,
						actCode text , actLib text , equActivitePraticable text , equActivitePratique text,
						equActiviteSalleSpe text, actNivLib text)''')
		self.conn.commit()
		self.conn.close()