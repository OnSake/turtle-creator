import tkinter as t
import turtle
from datetime import datetime
from PIL import Image, ImageGrab 

fenetre = t.Tk() #Créer une fenetre
fenetre.title("Turtle Art Creator")
fenetre.attributes('-fullscreen', True)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())
configuration_frame = t.Frame(fenetre, background='#324C40')

def configuration_page(configuration_frame):

  font = ('Corbel', 30, 'bold')
  forme_text = "Veuillez entrer le nom de la forme que vous voulez réaliser parmi celles proposées : carré, triangle, étoile"
  place_text = "Veuillez entrer le nom de l'endroit où vous voulez réaliser votre forme parmi celles proposées : HG, H, HD, G, C, D, BG, B, BD"
  surface_text = "Veuillez entrer le nombre de lignes et de colonne pour la figure choisie"
  error_text = t.StringVar(fenetre)


  def verify_entry():
    forme_entry = forme_input.get() 
    place_entry = place_input.get()
    surface_entry = [surface_input.get(), surface_input1.get()]
    if forme_entry in ["carré", "triangle", "étoile"] :
      if place_entry in ["HG", "H", "HD", "G", "C", "D", "BG", "B", "BD"]:
          if surface_entry[0].isdigit() and surface_entry[1].isdigit():
            forme_error.pack_forget()
            depla(350, 0)
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

  def save_turtle():
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
    fileName = 'turtle' + date

    # Capture de toute la fenêtre
    img = ImageGrab.grab(bbox=(975, 225, 1900, 1030))
    img.save(fileName + '.png', format='PNG') 


  def depla(x, y):
    tu.up()
    tu.goto(x, y)
    tu.down()



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
  button_frame.pack(fill='x', pady=50)
  forme_frame.pack()
  forme_label.pack(pady= 20, fill='x')
  forme_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  place_frame.pack()
  place_label.pack(pady= 20, fill='x')
  place_input.pack(ipadx=20, ipady=5, padx=20, pady=2)

  surface_frame.pack()
  surface_label.pack(pady= 20, fill='x')
  surface_input_frame.pack(expand=True)
  surface_input.pack(side='left', ipadx=20, ipady=5, padx=20, pady=2)
  surface_input1.pack(side='right', ipadx=20, ipady=5, padx=20, pady=2)

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

#Enregistrer Turtle en Image https://python-forum.io/thread-25822.html
  
configuration_page(configuration_frame)
t.mainloop()