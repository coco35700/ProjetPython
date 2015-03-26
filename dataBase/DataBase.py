import sqlite3

class DataBase:
	"""
	This class allows us to create the database containing
	information about installations, equipments and activities
	"""

	def __init__(self):
		self.conn = sqlite3.connect('dataBase/DB.db')
		self.c = self.conn.cursor()

	def disconnect(self):
		"""
		disconnects from the database
		"""
		self.conn.close()

	def connect(self):
		"""
		connects to the database
		"""
		self.conn = sqlite3.connect('dataBase/DB.db')
		
	def creation_table_installation(self):
		"""
		creates the table installation
		"""

		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations(comLib text,comInsee text,insCodePostal text,insLieuDit text,
						insNoVoie text , insLibelleVoie text , nb_Equipements text, nb_FicheEquipement text)''')
		self.conn.commit()

	def creation_table_activity(self):
		"""
		creates the table activity
		"""

		self.c.execute("DROP TABLE IF EXISTS activity")
		self.c.execute('''CREATE TABLE activity(inseeNb text, comLib text,equipementId text,equNbEquIdentique text,
						actCode text , actLib text , equActivitePraticable text , equActivitePratique text,
						equActiviteSalleSpe text, actNivLib text)''')
		self.conn.commit()

	def creation_table_equipment(self):
		"""
		creates the table equipment
		"""

		self.c.execute("DROP TABLE IF EXISTS equipment")
		self.c.execute('''CREATE TABLE equipment(comInsee text, comLib text,equipmentFile text,equAnneeService text,
						equNom text , equNomBatiment text)''')
		self.conn.commit()

	def export_object_list(self,listObjects):
		"""
		allows a list of object to export themselves to the database
		"""

		for item in listObjects:
			item.export_to_database(self)

		self.conn.commit()
