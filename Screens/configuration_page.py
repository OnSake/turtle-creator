import tkinter as t
import turtle
from datetime import datetime
from PIL import ImageGrab 

from Screens.save_in_bdd import save
from Screens.forme import Surface

# fenetre = t.Tk() #Créer une fenetre
# fenetre.title("Turtle Art Creator")
# fenetre.attributes('-fullscreen', True)
# fenetre.bind('<Escape>',lambda e: fenetre.destroy())
# configuration_frame = t.Frame(fenetre, background='#324C40')

def configuration_page(configuration_frame, username):

  font = ('Corbel', 30, 'bold')
  forme_text = "Veuillez entrer le nom de la forme que vous voulez réaliser parmi celles proposées : carré, spirale, flocon, sierpinsky, geo, cercle"
  place_text = "Veuillez entrer le nom de l'endroit où vous voulez réaliser votre forme parmi celles proposées : HG, H, HD, G, C, D, BG, B, BD"
  surface_text = "Veuillez entrer le nombre de lignes et de colonne pour la figure choisie"
  couleur_text = "Veuillez entrer une couleur"
  
  error_text = t.StringVar(configuration_frame)
  image_path = 'Oeuvres/'

  def verify_entry():
    forme_entry = forme_input.get() 
    place_entry = place_input.get()
    surface_entry = [surface_input.get(), surface_input1.get()]
    color_entry = couleur_input.get()
    longueur_entry = longueur_input.get()
    nb_cote_entry = nb_cote_input.get()    
    if check.get() == 0:
      fill_entry = False
    else:
      fill_entry = True

    if forme_entry in ["carré", "spirale", "flocon", "sierpinsky", "geo", "cercle"] :
      if place_entry in ["HG", "H", "HD", "G", "C", "D", "BG", "B", "BD"]:
          if surface_entry[0].isdigit() and surface_entry[1].isdigit():
            if longueur_entry.isdigit():
              if nb_cote_entry.isdigit() or nb_cote_entry == '':
                forme_error.pack_forget()
                if nb_cote_entry == '':
                  position_turtle(place_entry, forme_entry, surface_entry, color_entry, fill_entry, int(longueur_entry), 1)
                else:
                  position_turtle(place_entry, forme_entry, surface_entry, color_entry, fill_entry, int(longueur_entry), int(nb_cote_entry))
              else:
                error_text.set("Veuillez indiquer un nombre de côté valide")
                forme_error.pack()                
            else:
              error_text.set("Veuillez indiquer une longueur valide")
              forme_error.pack()
          else:
            error_text.set("Veuillez indiquer uniquement des données sous le format int()")
            forme_error.pack()
      else :
        error_text.set("Veuillez sélectionner une position proposée")
        forme_error.pack()
    else:
      error_text.set("Veuillez sélectionner une des figures proposée")
      forme_error.pack()

  def reset_turtle():
    tu.reset()
    tu.hideturtle()

  def save_turtle():
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
    fileName = 'turtle' + date
    # Capture de toute la fenêtre
    img = ImageGrab.grab(bbox=(995, 225, 1900, 1030))
    img.save(image_path+ fileName + '.png', format='PNG') 

    save(username, fileName)

  def depla(x, y):
    tu.up()
    tu.goto(x, y)
    tu.down()

  def position_turtle(pos, forme, surface, couleur, rempli, longueur, nb_cote_spirale):
    tu.speed(0)
    if pos in ["HG", "H", "HD"]:
      depla(0, 300)
      if pos == 'HG':
        depla(-400, 300)
      elif pos == 'HD':
        depla(400, 300)
    elif pos in ["BG", "B", "BD"]: 
      depla(0, -350)
      if pos == 'BG':
        depla(-400, -300)
      elif pos == 'BD':
        depla(400, -300)
    else:
      if pos == 'G':
        depla(-350, 0)
      elif pos == 'D':
        depla(350, 0)
      else:
        depla(0, 0)
    
    Surface(t=tu, Coordonnees=(tu.xcor(), tu.ycor()), Cote=longueur, Forme=forme, Ligne=int(surface[0]), Colonne=int(surface[1]), Couleur=couleur, Rempli=rempli, Forme_Spirale=nb_cote_spirale, Taille_Sierpinsky_Geo=nb_cote_spirale)

  

  # --------- Title --------- #
  configuration_title_frame = t.Frame(configuration_frame, background='#D1D5C6', borderwidth=5)
  configuration_title = t.Label(configuration_title_frame, text = "Créer votre oeuvre", background = '#324C40', font = font, fg="#D1D5C6")


  # --------- Creation oeuvre --------- #
  configuration_turtle_frame = t.Frame(configuration_frame, background='#324C40')
  configuration_turtle_button = t.Frame(configuration_turtle_frame, background='#324C40', borderwidth=1, height=500)

  # ------ Button Frame ------ #
  button_frame = t.Frame(configuration_turtle_button, background='#D1D5C6')

  forme_frame = t.Frame(button_frame, background='#D1D5C6')
  forme_label = t.Label(forme_frame, text=forme_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  forme_input = t.Entry(forme_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')

  place_frame = t.Frame(button_frame, background='#D1D5C6')
  place_label = t.Label(place_frame, text=place_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  place_input = t.Entry(place_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')

  surface_frame = t.Frame(button_frame, background='#D1D5C6')
  surface_label = t.Label(surface_frame, text=surface_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  surface_input_frame = t.Frame(surface_frame, background='#D1D5C6')
  surface_input = t.Entry(surface_input_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')
  surface_input1 = t.Entry(surface_input_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')

  couleur_setting_frame = t.Frame(button_frame, background='#D1D5C6')
  couleur_frame = t.Frame(couleur_setting_frame, background='#D1D5C6')
  couleur_label = t.Label(couleur_frame, text=couleur_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  couleur_input = t.Entry(couleur_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')
  
  check_frame = t.Frame(couleur_setting_frame, background='#D1D5C6')
  couleur__check_label = t.Label(check_frame, text="Votre forme est pleine", background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  check = t.IntVar()
  check.set(0)
  couleur_check = t.Checkbutton(check_frame, bg='#D1D5C6', onvalue=1, offvalue=0, variable=check)

  spec_forme_frame = t.Frame(button_frame, background='#D1D5C6')
  longueur_frame = t.Frame(spec_forme_frame, background='#D1D5C6')
  longueur_label = t.Label(longueur_frame, text='Veuillez entrer la longueur de votre forme', background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  longueur_input = t.Entry(longueur_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')

  nb_cote_frame = t.Frame(spec_forme_frame, background='#D1D5C6')
  nb_cote_label = t.Label(nb_cote_frame, text='Veuillez entrer le nombre de côtés pour votre spirale', background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  nb_cote_input = t.Entry(nb_cote_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')



  forme_error = t.Label(button_frame, bg="#D1D5C6", fg='red', textvariable=error_text , font = ('Corbel', 13, 'bold'))
  draw_button = t.Button(button_frame, background='#577D54', text="Dessiner", font=('Corbel', 14, 'bold'), fg="#D1D5C6", command=verify_entry)

  # ------ Save Frame ------ #
  save_frame = t.Frame(configuration_turtle_button, background='#3D5B3A')
  save_button = t.Button(save_frame, text='Enregistrer', bg='#577D54', fg='#D1D5C6', font=('Corbel', 20, 'bold'), command=save_turtle)
  reset_button = t.Button(save_frame, text='Réinitialiser', bg='#577D54', fg='#D1D5C6', font=('Corbel', 20, 'bold'), command=reset_turtle)


  # --------- Turtle Frame --------- #
  turtle_canvas = t.Canvas(configuration_turtle_frame)
  turtle_canvas.config(width=1000, height=800)

  screen = turtle.TurtleScreen(turtle_canvas)
  screen.bgcolor('white')


  # --------- Pack --------- #
  configuration_title_frame.pack(expand=True, pady=50)
  configuration_title.pack(fill='both', ipadx=10, ipady=5)

  configuration_turtle_frame.pack(fill='x', pady= 50)

  configuration_turtle_button.pack(side='left', padx=20, expand=True, fill='both')
  button_frame.pack(fill='x')
  forme_frame.pack()
  forme_label.pack(pady= 20, fill='x')
  forme_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  place_frame.pack()
  place_label.pack(pady= 20, fill='x')
  place_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  surface_frame.pack(pady=10)
  surface_label.pack(pady= 20, fill='x')
  surface_input_frame.pack(expand=True)
  surface_input.pack(side='left', ipadx=20, ipady=5, padx=20, pady=2)
  surface_input1.pack(side='right', ipadx=20, ipady=5, padx=20, pady=2)

  couleur_setting_frame.pack( fill='x')

  couleur_frame.pack(side='left', expand=True, padx=10)
  couleur_label.pack(pady= 20)
  couleur_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  check_frame.pack(side='right', expand=True, padx=10, ipadx=20)
  couleur__check_label.pack(pady= 20)
  couleur_check.pack(ipadx=20, ipady=5, padx=20, pady=2)

  spec_forme_frame.pack(fill='x')
  longueur_frame.pack(side='left', expand=True)
  longueur_label.pack()
  longueur_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  nb_cote_frame.pack(side='left', expand=True)
  nb_cote_label.pack()
  nb_cote_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  draw_button.pack(ipadx=15, ipady=5, pady=20)

  save_frame.pack(fill='both', ipadx=100, ipady=50)
  save_button.pack(ipadx=26, ipady=10, side='left', expand=True)
  reset_button.pack(ipadx=20, ipady=10, side='right', expand=True)
  
  
  turtle_canvas.pack(side='right', padx=20, fill='x')




  tu = turtle.RawPen(screen)
  tu.hideturtle()
  tu.speed(0)
  depla(0, 0)
  configuration_frame.pack(fill='both')

  
