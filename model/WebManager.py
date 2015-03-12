import cherrypy
import sqlite3

dataBasePath = "../dataBase/DB.db"

class WebManager():
	"""docstring for ClassName"""


	@cherrypy.expose
	def index(self):
		refActivity = "<a href='http://localhost:8080/activity'>Activités</a>"
		refEquipment = "<a href='http://localhost:8080/equipment'>Equipements</a>"
		refInstallation = "<a href='http://localhost:8080/installation'>Installations</a>"

		return refActivity+"</br>"+refEquipment+"</br>"+refInstallation

	@cherrypy.expose
	def activity(self):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		
		bandeau = "<tr><th>inseeNb</th><th>comLib</th><th>equipmentId</th><th>equNbEquIdentique</th>"
		bandeau = bandeau + "<th>actCode</th><th>actLib</th><th>quActivitePraticable</th>"
		bandeau = bandeau + "<th>equActivitePratique</th><th>equActiviteSalleSpe</th><th>actNivLib</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		for line in c.execute("select * from activity").fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"

	@cherrypy.expose
	def equipment(self):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();

		bandeau = "<tr><th>comInsee</th><th>comLib</th><th>equipmentFile</th><th>equAnneeService</th>"
		bandeau = bandeau + "<th>equNom</th><th>equNomBatiment </th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		for line in c.execute("select * from equipment").fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"

	@cherrypy.expose
	def installation(self):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		bandeau = "<tr><th>comLib</th><th>comInsee</th><th>insCodePostal</th><th>insLieuDit</th>"
		bandeau = bandeau + "<th>insNoVoie</th><th>insLibelleVoie</th><th>nb_Equipements</th><th>nb_FicheEquipement</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		for line in c.execute("select * from installations").fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"
		
cherrypy.quickstart(WebManager())