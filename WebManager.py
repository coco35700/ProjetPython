import cherrypy
import sqlite3

dataBasePath = "../dataBase/DB.db"

class WebManager():
	"""docstring for ClassName"""


	@cherrypy.expose
	def index(self):
		page =  """	<html>
					<body>
					<h1>Recherche</h1>
					<form method='get' action='test'>
						<table border="1">
						<tr>
							<td>Activités</td>
							<td><input type ='textArea' name='RA'></td>
						</tr>
						<tr>
							<td>Equipements</td>
							<td><input type ='textArea' name='RE'></td>
						</tr>
						<tr>
							<td>installations</td>
							<td><input type ='textArea' name='RI'></td>
						</tr>
						</table>
						<button type="submit">Rechercher</button>
					</form>

						<h1>Afficher dirrectement les tables : </h1>

						<a href='http://localhost:8080/activity'>Activités</a></br>
						<a href='http://localhost:8080/equipment'>Equipements</a></br>
						<a href='http://localhost:8080/installation'>Installations</a></br>
						
					</body>
					</html>
				"""  
		return page

	@cherrypy.expose
	def test(self,RA,RE,RI):
		if(RA != "" and RE == "" and RI == "" ):
			return self.searchActivity(RA)
		elif(RE != "" and RA == "" and RI == "" ):
			return self.searchEquipment(RE)
		elif(RI != "" and RA == "" and RE == "" ):
			return "<h1>Afficher table installations<h1>"
		else:
			return "<h1>Vous ne pouvez rechercher que dans une table a la foi ! </h1>"
		

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
	def searchActivity(self,param):
		conn = sqlite3.connect(dataBasePath)
		c = conn.cursor();
		
		bandeau = "<tr><th>inseeNb</th><th>comLib</th><th>equipmentId</th><th>equNbEquIdentique</th>"
		bandeau = bandeau + "<th>actCode</th><th>actLib</th><th>quActivitePraticable</th>"
		bandeau = bandeau + "<th>equActivitePratique</th><th>equActiviteSalleSpe</th><th>actNivLib</th></tr>"
		chaine = "<table style='width:100%' border='1'>"+bandeau

		for line in c.execute("select * from activity where inseeNb ='"+param+"'"" OR comLib like '%"+param+"%' OR equipementId ='"+param+"' OR actlib like '%"+param+"%'").fetchall():
			chaine = chaine + "<tr>"
			for elem in range(len(line)):
				chaine = chaine+"<td>"+line[elem]+"</td>"

			chaine = chaine + "</tr>"
		return chaine+"</table>"

	@cherrypy.expose
	def searchEquipment(self,param):
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


