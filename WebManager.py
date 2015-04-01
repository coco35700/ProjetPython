import cherrypy
import sqlite3
from mako.template import Template
from mako.lookup import TemplateLookup

dataBasePath = "dataBase/DB.db"
lookup = TemplateLookup(directories=["html"])

class WebManager(object):
	""" 
	Webmanager allows you to create a website which 
	will then display information about our database
	"""


	@cherrypy.expose
	def index(self):
		"""
		Creates the main page of The website, a form to search within the tables
		and links to view tables as a whole
		"""
		template = lookup.get_template("index.html")  
		return template.render()

	@cherrypy.expose
	def routeur(self,RA,RE,RI):
		"""
		Redirects to the good page with the selected parameter
		"""

		if(RA != "" and RE == "" and RI == "" ):
			return self.search_activity(RA)
		elif(RE != "" and RA == "" and RI == "" ):
			return self.search_equipment(RE)
		elif(RI != "" and RA == "" and RE == "" ):
			return self.search_installation(RI)
		else:
			return "<h1>Vous ne pouvez rechercher que dans une table a la foi ! </h1>"
		

	@cherrypy.expose
	def activity(self):
		"""
		This page shows our Activities as a whole
		"""
		
		dataBasePath = 'dataBase/DB.db'
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor()
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
		"""
		This page shows our equipments a whole
		"""
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
		"""
		This page shows our installations as a whole
		"""
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

	@cherrypy.expose
	def search_activity(self,param):
		"""
		This page shows the selected lines from the activity Table
		"""
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		
		bandeau = "<tr><th>inseeNb</th><th>comLib</th><th>equipmentId</th><th>equNbEquIdentique</th>"
		bandeau = bandeau + "<th>actCode</th><th>actLib</th><th>quActivitePraticable</th>"
		bandeau = bandeau + "<th>equActivitePratique</th><th>equActiviteSalleSpe</th><th>actNivLib</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		request = "select * from activity where inseeNb ='"+param+"' OR comLib like '%"+param+"%'"
		request = request + " OR equipementId ='"+param+"' OR actlib like '%"+param+"%'"
		for line in c.execute(request).fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"

	@cherrypy.expose
	def search_equipment(self,param):
		"""
		This page shows the selected lines from the equipment Table
		"""
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();

		bandeau = "<tr><th>comInsee</th><th>comLib</th><th>equipmentFile</th><th>equAnneeService</th>"
		bandeau = bandeau + "<th>equNom</th><th>equNomBatiment </th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		request = "select * from equipment where comInsee ='"+param+"' OR comLib like '%"+param+"%' OR"
		request = request + " equAnneeService='"+param+"' OR equNom like '%"+param+"%'"
		for line in c.execute(request).fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"

	@cherrypy.expose
	def search_installation(self,param):
		"""
		This page shows the selected lines from the installation Table
		"""
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		bandeau = "<tr><th>comLib</th><th>comInsee</th><th>insCodePostal</th><th>insLieuDit</th>"
		bandeau = bandeau + "<th>insNoVoie</th><th>insLibelleVoie</th><th>nb_Equipements</th><th>nb_FicheEquipement</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		request = "select * from installations where comLib like '%"+param+"%' OR comInsee ='"+param+"' OR insCodePostal='"+param+"'"
		request = request + " OR insLieuDit like '%"+param+"%' OR insLibelleVoie like '%"+param+"%'"
		for line in c.execute(request).fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"


		
cherrypy.quickstart(WebManager())


