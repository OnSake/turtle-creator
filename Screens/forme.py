import turtle
from random import randint



def initialisation (t, Coordonnees) :
    t.pu()
    t.goto(Coordonnees)
    t.pd()

def random_couleur_turtle (t) :
    liste = ["red","green","blue","yellow","gray","black","pink","purple"]
    t.color(liste[randint(0,len(liste)-1)])
    t.fillcolor(liste[randint(0,len(liste)-1)])

def carre (t, Cote,Angle=0,Rempli=False) :


    if Rempli == True :
        t.begin_fill()
    t.left(Angle)

    for i in range(4) :#Carré
        t.forward(Cote)
        t.left(90)

    if Rempli == True :
        t.end_fill()

    t.right(Angle)#On remet droit



def spirale_rec(t, longueur,cote) :
    if longueur > 20 :
        spirale_rec(t, longueur-10,cote)
    t.forward(longueur)
    t.left(360/cote)

def koch(t, step,L) :
    if step == 0 :
        t.forward(L)
    else :
        koch(t, step-1,L//3)
        t.left(60)
        koch(t, step-1,L//3)
        t.right(120)
        koch(t, step-1,L//3)
        t.left(60)
        koch(t, step-1,L//3)


def somme_geo(t, n,longueur) :
    for i in range(4) :
        t.forward(longueur)
        t.left(90)
    t.left(90)
    t.forward(longueur//2)
    t.right(90)
    t.forward(longueur)
    t.right(180)
    t.forward(longueur)
    t.left(90)
    t.forward(longueur//2)
    t.left(90)
    if n > 0 :
        somme_geo(t, n-1,longueur//2)


def flocon (t, Cote,Rempli=False) :

    t.begin_fill()
    t.left(60)
    koch(t, 2,Cote)
    t.right(120)
    koch(t, 2,Cote)
    t.right(120)
    koch(t, 2,Cote)
    t.right(180)
    t.end_fill()



def Sierpinsky (t, n,L) :

    if n > 0 :
        t.left(60)
        t.forward(L/2)
        t.right(60)
        t.begin_fill()
        Sierpinsky(t, n-1,L/2)
        t.end_fill()
        t.left(60)
        t.forward(L/2)
        t.right(120)
        t.forward(L)
        t.left(60)
        t.backward(L/2)
        t.begin_fill()
        Sierpinsky(t, n-1,L/2)
        t.end_fill()
        t.backward(L/2)
        t.begin_fill()
        Sierpinsky(t, n-1,L/2)
        t.end_fill()
    elif n == 0 :
        t.left(60)
        t.forward(L)
        t.right(120)
        t.forward(L)
        t.left(60)
        t.backward(L)

def cercle (t, Rayon,Rempli=False) :
    if Rempli == True :
        t.begin_fill()

    t.circle(Rayon)

    if Rempli == True :
        t.end_fill()





def Surface (t, Coordonnees,Cote,Forme,Couleur,Ligne,Colonne,Angle=0,Rempli=False,Forme_Spirale = 0,Taille_Sierpinsky_Geo=0,Ecart_cercle=0) :
    initialisation(t, Coordonnees)
    for i in range (Ligne) :
        for j in range (Colonne) :
            initialisation(t, (int(Coordonnees[0])+j*Cote,int(Coordonnees[1])-i*Cote))
            #----------------Couleur------------------------
            if Couleur == "rainbow" :
                random_couleur_turtle(t)#Couleur aléatoire par la fonction
            else :
                t.color(Couleur)#Couleur choisie
                t.fillcolor(Couleur)
            #----------------------------------------
            #----------------Formes------------------------
            if Forme == "carré":
                carre (t, Cote,Angle,Rempli)
            elif Forme == "spirale" :
                spirale_rec(t, Cote,Forme_Spirale)
            elif Forme == "flocon" :
                flocon (t, Cote,Rempli)
            elif Forme == "sierpinsky" :
                Sierpinsky(t, Taille_Sierpinsky_Geo,Cote)
            elif Forme == "geo" :
                somme_geo(t, Taille_Sierpinsky_Geo,Cote)
            elif Forme == "cercle" :
                cercle(t, Cote,Rempli)

#carre((0,100),100,"red",20,True)
#flocon(200,2,"pale turquoise")
#somme_geo(10,250)
#koch(3,500)
#Sierpinsky(4,200)
#spirale_rec(300,3)

#Surface(turtle, (-500,0),100,"spirale","rainbow",5,8,45,True,5,3,100)
"""On va voir ##################
def Stalagmite (Taille,Rond=False) :
    #On met une valeur mediane pour les angles des stalagmites : randint(60,120)
    angle = randint(60,90)
    t.left(angle)
    t.forward(Taille)
    t.right(90)
    t.forward(Taille)
"""
#Stalagmite(100,False)

#turtle.exitonclick()