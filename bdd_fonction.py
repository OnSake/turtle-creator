import sqlite3

connexion = sqlite3.connect("BDD/turtle_BDD.db")

curseur = connexion.cursor()

def save(username, filename):
  curseur.execute(f'INSERT INTO Turtle_oeuvre (username, nom_oeuvre) VALUES (?, ?)', (username, filename))
  connexion.commit()

def delete_item(filename):
  curseur.execute(f'DELETE FROM Turtle_oeuvre WHERE nom_oeuvre = ?', (filename,))
  connexion.commit()


def oeuvre_user(username):
  curseur.execute(f'SELECT username, nom_oeuvre FROM Turtle_oeuvre WHERE username = ?', (username,))
  return curseur.fetchall()

def oeuvre_community(username):
  curseur.execute(f'SELECT username, nom_oeuvre FROM Turtle_oeuvre WHERE username != ?', (username,))
  return curseur.fetchall()


def connexion_close():
    connexion.close() #Pour arrêter
