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
		chaine = ""

		for item in c.execute("select * from activity"):
			chaine = chaine+" activity : "+str(item)+"</br>"

		return chaine

	@cherrypy.expose
	def equipment(self):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		chaine = ""

		for item in c.execute("select * from equipment"):
			chaine = chaine+" equipments : "+str(item)+"</br>"

		return chaine

	@cherrypy.expose
	def installation(self):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		bandeau = "<tr><th>comLib</th><th>comInsee</th><th>insCodePostal</th><th>insLieuDit</th>"+"<th>insNoVoie</th><th>insLibelleVoie</th><th>nb_Equipements</th><th>nb_FicheEquipement</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau


		for item in c.execute("select * from installations"):
			tab = str(item).replace("'","").replace("(","").replace(")","").split(",")
			chaine = chaine + "<tr>"
			for i in range(len(tab)):
				chaine = chaine+"<td>"+tab[i]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"
		
cherrypy.quickstart(WebManager())