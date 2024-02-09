import tkinter as t
import turtle



def configuration_page(configuration_frame):

  font = ('Corbel', 30, 'bold')

  def verify_entry():
    forme_entry = forme_input.get() 
    place_entry = place_input.get()
    if forme_entry in ["carré", "triangle", "étoile"] and place_entry in ["HG", "H", "HD", "G", "C", "D", "BG", "B", "BD"]:
      forme_error.pack_forget()
    else:
      forme_error.pack()


  def depla(x, y):
    tu.up()
    tu.goto(x, y)
    tu.down()


  forme_text = "Veuillez entrer le nom de la forme que vous voulez réaliser parmi \ncelles proposées : carré, triangle, étoile"
  place_text = "Veuillez entrer le nom de l'endroit où vous voulez réaliser votre forme parmi \ncelles proposées : HG, H, HD, G, C, D, BG, B, BD"
  # --------- Title --------- #
  configuration_title_frame = t.Frame(configuration_frame, background='#D1D5C6', borderwidth=5)
  configuration_title = t.Label(configuration_title_frame, text = "Créer votre oeuvre", background = '#324C40', font = font, fg="#D1D5C6")


  # --------- Creation oeuvre --------- #
  configuration_turtle_frame = t.Frame(configuration_frame, background='#324C40')
  configuration_turtle_button = t.Frame(configuration_turtle_frame, background='#D1D5C6', borderwidth=1, height=500)

  # --------- Button Frame --------- #
  forme_frame = t.Frame(configuration_turtle_button, background='#D1D5C6')
  forme_label = t.Label(forme_frame, text=forme_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  forme_input = t.Entry(forme_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')

  place_frame = t.Frame(configuration_turtle_button, background='#D1D5C6')
  place_label = t.Label(place_frame, text=place_text, background='#D1D5C6', font = ('Corbel', 13, 'bold'), fg="#324C40", justify='left')
  place_input = t.Entry(place_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54', justify='center')


  forme_error = t.Label(configuration_turtle_button, bg="#D1D5C6", fg='red', text="Veuillez sélectionner une des options proposées", font = ('Corbel', 13, 'bold'))
  draw_button = t.Button(configuration_turtle_button, background='#577D54', text="Dessiner", font=('Corbel', 14, 'bold'), fg="#D1D5C6", command=verify_entry)





  # --------- Turtle Frame --------- #
  turtle_canvas = t.Canvas(configuration_turtle_frame)
  turtle_canvas.config(width=700, height=500)

  screen = turtle.TurtleScreen(turtle_canvas)
  screen.bgcolor('white')


  # --------- Pack --------- #
  configuration_title_frame.pack(expand=True, pady=50)
  configuration_title.pack(fill='both', ipadx=10, ipady=5)

  configuration_turtle_frame.pack(fill='x', pady= 50)

  configuration_turtle_button.pack(side='left', padx=20, expand=True)

  forme_frame.pack()
  forme_label.pack(pady= 20)
  forme_input.pack(ipadx=10, ipady=5, padx=20, pady=2)

  place_frame.pack()
  place_label.pack(pady= 20)
  place_input.pack(ipadx=10, ipady=5, padx=20, pady=2)


  draw_button.pack(ipadx=10, ipady=5, pady=10)


  turtle_canvas.pack(side='right', padx=20)




  tu = turtle.RawPen(screen)
  depla(-155, 0)
  configuration_frame.pack(fill='both')

#Enregistrer Turtle en Image https://python-forum.io/thread-25822.html