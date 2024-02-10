import sqlite3

connexion = sqlite3.connect("BDD/turtle_BDD.db")

curseur = connexion.cursor()

def save(username, filename):
  curseur.execute(f'INSERT INTO Turtle_oeuvre (username, nom_oeuvre) VALUES ("{username}", "{filename}")')
  connexion.commit()
  connexion.close() #pour arreter
