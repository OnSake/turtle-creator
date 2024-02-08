import turtle as t

t.title("ECRAN TEST") # pour mettre un titre à la fenetre
t.setup (width=1000, height=800, startx=0, starty=0)


def carre(l):
  for i in range(4):
    t.forward(l)
    t.left(90)

def Surface_carre(nombreLigneRestant, nombreColonneRestant, longueurCarre, couleur, anglePenche=0, rempli=True):
  t.color(couleur)
  carre(longueurCarre)
  if nombreColonneRestant > 0:
    if nombreLigneRestant > 0:
        t.forward(longueurCarre + 20)
        Surface_carre(nombreLigneRestant-1, nombreColonneRestant, longueurCarre, couleur, anglePenche, rempli)
    t.backward(longueurCarre*nombreLigneRestant + 20*nombreLigneRestant)



Surface_carre(2, 2, 50, "red")

t.exitonclick()