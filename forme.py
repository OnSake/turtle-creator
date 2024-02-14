import turtle
from random import randint



def initialisation (t, Coordonnees) :
    t.pu()
    t.goto(Coordonnees)
    t.pd()
    t.speed(0)

def random_couleur_turtle (t) :
    liste = ["red","green","blue","yellow","gray","black","pink","purple"]
    t.color(liste[randint(0,len(liste)-1)])
    t.fillcolor(liste[randint(0,len(liste)-1)])

###RECU-----------------------------------------------------
def blob (t,L) :
    if L < 5 :
        t.forward(randint(-2,2))
        t.circle(3)
    else :
        t.forward(randint(-2,2))
        t.circle(L)
        t.pu()
        t.left(90)
        t.forward(5)
        t.right(90)
        t.pd()
        blob(t,L-5)

def spirale_rec(t, longueur,cote) :
    if longueur > 20 :
        spirale_rec(t, longueur-10,cote)
    t.forward(longueur)
    t.left(360/cote)

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

def icicles (t,Cote) :
    if Cote > 1 :
        cercle(t,Cote,True)
        t.right(90)
        t.forward(5)
        t.left(90)
        icicles(t,Cote-1)


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




###FORME BASIQUES------------------------
def cercle (t, Rayon,Rempli=False) :
    if Rempli == True :
        t.begin_fill()

    t.circle(Rayon)

    if Rempli == True :
        t.end_fill()


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

def triangle (t,L,Rempli=False) :
    if Rempli == True :
        t.begin_fill()

    t.left(60)
    for i in range(3) :
        t.forward(L)
        t.right(120)
    t.right(60)
    if Rempli == True :
            t.end_fill()

def stalagmite (t,L,Rempli=False) :
    if Rempli == True :
        t.begin_fill()

    angle = randint(60,85)
    t.left(angle)
    t.forward(L)
    t.right(2*angle)
    t.forward(L)
    t.left(angle)

    if Rempli == True :
            t.end_fill()

def etoile (t,L,branche=2,Rempli=False) :
    if Rempli == True :
        t.begin_fill()

    angle = 360 / branche
    t.left(angle)
    for i in range(branche) :
        triangle(t,L)
        t.forward(L)
        t.right(angle)


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
                t.pensize(3)
                spirale_rec(t, Cote,Forme_Spirale)
                t.pensize(1)
            elif Forme == "flocon" :
                flocon (t, Cote,Rempli)
            elif Forme == "sierpinsky" :
                Sierpinsky(t, 4,Cote)
            elif Forme == "geo" :
                somme_geo(t, 6,Cote)
            elif Forme == "cercle" :
                cercle(t, Cote,Rempli)
            elif Forme == "triangle" :
                triangle(t,Cote,Rempli)
            elif Forme == "stalagmite" :
                stalagmite(t,Cote,Rempli)
            elif Forme == "etoile" :
                etoile(t,Cote,Forme_Spirale,Rempli)
            elif Forme == "icicles" :
                icicles(t,Cote)
            elif Forme == "blob" :
                t.pensize(3)
                blob(t,Cote)
                t.pensize(1)



#Surface(turtle, (0,0),50,"blob","red",1,1,45,True,5,)
#turtle.exitonclick()