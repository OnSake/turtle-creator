import tkinter as t
from tkinter import font
from tkinter.filedialog import askopenfilename 
from PIL import Image, ImageTk, ImageGrab
import turtle
from datetime import datetime


from bdd_fonction import delete_item, save, oeuvre_community, connexion_close
from forme import Surface

fenetre = t.Tk() #Créer une fenetre
fenetre.title("Turtle Art Creator")
fenetre.attributes('-fullscreen', True)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())


# --------------- PAGES --------------- #
home_frame =t.Frame(fenetre, background='#324C40')
profile_frame = t.Frame(fenetre, background='#324C40')
login_frame = t.Frame(fenetre, background='#324C40')
configuration_frame = t.Frame(fenetre, background='#324C40')
community_frame = t.Frame(fenetre, background='#324C40')

font = ('Corbel', 30, 'bold')


pages = [home_frame, profile_frame, login_frame, configuration_frame, community_frame]

back_image = t.PhotoImage(file='./Icons/bouton-retour.png')
avant_img = t.PhotoImage(file='./Icons/avant.png')
apres_img = t.PhotoImage(file='./Icons/envoyer.png')
delete_img = t.PhotoImage(file='./Icons/poubelle-de-recyclage.png')


# --------------- LOGIN PAGE --------------- #
def login_access(login_frame):
    def confirm_username():
      if username_input.get() != '':
        global user_name
        user_name = username_input.get()
        username_error_message.pack_forget()
        go_home_page()
      else: 
        error_message.set(value="Veuillez entrer un nom d'utilisateur valide")
        username_error_message.pack(expand=True)

    def choose_img():
      path = askopenfilename(title="Choississez votre photo de profil", filetypes=[('png files','.png'), ('jpg files', '.jpg')])
      im = Image.open(path)
      im = im.resize((150, 150))
      tkimage = ImageTk.PhotoImage(im)
      profile_img = t.Label(profil_img_frame, image=tkimage, background='#324C40')
      profile_img.image = tkimage
      profil_img.pack_forget()
      profile_img.pack(pady=20)

    welcome_message = t.Label(login_frame, text='Bienvenue', font=('Corbel', 50, 'bold'), background='#324C40', fg='#D1D5C6')
    presentation_message = t.Label(login_frame, text="Avant de commencer, veuillez entrer un nom d'utilisateur", font=('Corbel', 25, 'bold'), background='#324C40', fg='#D1D5C6')


    username_frame = t.Frame(login_frame, background='#324C40')
    username_input = t.Entry(username_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54')
    username_error_frame = t.Frame(login_frame, background='red')
    error_message = t.StringVar(fenetre)
    username_error_message = t.Label(username_error_frame, textvariable=error_message, fg='red', background='#324C40', font=('Corbel', 15, 'bold'))


    profil_img_frame = t.Frame(login_frame, background='#324C40')
    profil_img_choose = t.Button(profil_img_frame, text='Choisir une photo de profil', bg='#577D54', fg='#D1D5C6', font=('Corbel', 15, 'bold'),  command=choose_img)
    im1 = Image.open('Icons/background.png')
    global tkimage
    tkimage = ImageTk.PhotoImage(im1)
    profil_img = t.Label(profil_img_frame, image=tkimage, background='#324C40')
    profil_img.image = tkimage

    button_confirm = t.Button(login_frame, text='Confirmer', font= ('Corbel', 15, 'bold'), bg='#577D54', fg='#D1D5C6', command=confirm_username)
    frame = t.Frame(login_frame, background='#324C40')


    # --------- Pack --------- #
    welcome_message.pack(fill='x', expand=True, pady=30)
    presentation_message.pack(fill='x', expand=True, pady= 50)

    username_frame.pack(expand=True, ipady=20)
    username_input.pack(ipadx=20, ipady=15, side='left', padx=20)
    username_error_frame.pack(expand=True)


    profil_img_frame.pack()
    profil_img_choose.pack()
    profil_img.pack(pady=20)

    button_confirm.pack(pady=50)
    frame.pack(fill='both', ipady=100)

# --------------- HOME PAGE --------------- #

def home_access(home_frame):

    # --------- Title --------- #
    home_title_frame = t.Frame(home_frame, background='#D1D5C6', borderwidth=5)
    home_title = t.Label(home_title_frame, text = "Accueil", background = '#324C40', font = font, fg="#D1D5C6")

    # --------- Buttons --------- #
    home_button_frame= t.Frame(home_frame, background='#324C40')
    b1 = t.Button(home_button_frame, background="#577D54", text="Accéder à son profil", font = ('Corbel', 15, 'bold'), fg="#D1D5C6", width= 50, activebackground='#3D5B3A', activeforeground='#D1D5C6', command=go_profile_page)
    b2 = t.Button(home_button_frame, background="#577D54", text="Création de la communauté", font = ('Corbel', 15, 'bold'), fg="#D1D5C6", width= 50, activebackground='#3D5B3A', activeforeground='#D1D5C6', command=go_community_page)
    home_bouton = b1, b2
    frame = t.Frame(home_frame, background='#324C40')

    # --------- Packs --------- #
    home_title_frame.pack(pady=100)
    home_title.pack(ipady= 25, ipadx=50)
    home_button_frame.pack(pady=25)
    for bouton in home_bouton:
        bouton.pack(ipady = 50, ipadx = 25, pady=50)
    frame.pack(pady=50)

# --------------- PROFILE PAGE --------------- #
        
def profile_access(profile_frame):
  
  profile_back_frame = t.Frame(profile_frame, background='#324C40')

  profile_back_button = t.Button(profile_back_frame, background="#577D54", text="<", font = ('Corbel', 25), fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", command=go_home_page, image=back_image)

  # --------- Title --------- #
  profile_title_frame = t.Frame(profile_frame, background='#D1D5C6', borderwidth=5)
  profile_title = t.Label(profile_title_frame, text = "Mon profil", background = '#324C40', font = font, fg="#D1D5C6")

  # --------- Username + Img --------- #
  profile_header_frame = t.Frame(profile_frame, background='#324C40')
  profile_header_img = t.Label(profile_header_frame, image=tkimage, width=150, height=150, background='#324C40')
  profile_header_img.image = tkimage
  profile_header_name = t.Label(profile_header_frame, text=user_name, background='#324C40', fg = '#D1D5C6', font = font)


  # --------- My Creations Section --------- #
  profile_creation_frame = t.Frame(profile_frame, background='#324C40')
  profile_creation_title = t.Label(profile_creation_frame, text='Mes créations :', fg = '#577D54', font = font, background='#324C40')

  profile_mycreations_frame = t.Frame(profile_frame, background="#324C40")
  
  profile_mycreations_button = t.Button(profile_mycreations_frame, background="#9EAD84", text="+", width=7, height=4, font = ('Comic sans MS', 45), fg="#38573F", activebackground="#38573F", activeforeground="#9EAD84", command=go_configuration_page)


  profile_mycreations_list_frame = t.Frame(profile_mycreations_frame, background='#324C40')

  profile_mycreations_list_frame1 = t.Frame(profile_mycreations_list_frame, background='#D1D5C6', borderwidth=3)
  profile_mycreations_list_project1 = t.Label(profile_mycreations_list_frame1 ,text='Test 1', background='#3D5B3A', font = ('Corbel', 15, 'bold'), fg='#D1D5C6')
  profile_mycreations_list_view1 = t.Button(profile_mycreations_list_frame1, font = ('Corbel', 15, 'bold'), text="Voir l'oeuvre", background='#D1D5C6', relief='groove')
  
  profile_mycreations_list_frame2 = t.Frame(profile_mycreations_list_frame, background='#D1D5C6', borderwidth=3)
  profile_mycreations_list_project2 = t.Label(profile_mycreations_list_frame2 ,text='Test 2', background='#3D5B3A', font = ('Corbel', 15, 'bold'), fg='#D1D5C6')
  profile_mycreations_list_view2 = t.Button(profile_mycreations_list_frame2, font = ('Corbel', 15, 'bold'), text="Voir l'oeuvre", background='#D1D5C6', relief='groove')

  creation_frames = [profile_mycreations_list_frame1, profile_mycreations_list_frame2]
  creation_frames_projects = [profile_mycreations_list_project1, profile_mycreations_list_project2]
  creation_frames_buttons = [profile_mycreations_list_view1, profile_mycreations_list_view2]

  frame = t.Frame(profile_frame, background='#324C40')

  # --------- Packs --------- #
  profile_back_frame.pack(fill='x')
  profile_back_button.pack(side='left', padx=15, pady=15, ipadx=5, ipady=5)

  profile_title_frame.pack(pady=10)
  profile_title.pack(ipadx=25, ipady=25)

  profile_header_img.pack(side='left', ipadx=10)
  profile_header_name.pack(side='left', fill='both')
  profile_header_frame.pack(fill='x')

  profile_creation_title.pack(side='left', ipadx=20, ipady=10, pady=25)
  profile_creation_frame.pack(fill='both')

  profile_mycreations_frame.pack(fill="both")
  profile_mycreations_button.pack(side="left", padx=20)



  profile_mycreations_list_frame.pack(side='right', expand=True, fill='x')
  
  for frame_crea in creation_frames:
    frame_crea.pack(padx=20, pady=10)
  for project in creation_frames_projects:
    project.pack(fill='both',ipady=20, ipadx=650, side='left')
  for button in creation_frames_buttons:
    button.pack(side='right', padx=10)

  frame.pack(ipady=150)
  
# --------------- COMMUNITY PAGE --------------- #

def community_access(frame):
  global back_image, avant_img, apres_img, delete_img, tkimage #Pour PhotoImage
  font = ('Corbel', 30, 'bold')
  username = t.StringVar()
  index_liste = 0
  liste_oeuvre = oeuvre_community(user_name)
  username.set(liste_oeuvre[index_liste][0])
  nom_oeuvre = liste_oeuvre[index_liste][1]

  def oeuvre_avant(liste, username): 
      nonlocal index_liste, nom_oeuvre
      if index_liste > 0:
        index_liste -= 1
      else:
        index_liste = len(liste)-1
      
      username.set(liste[index_liste][0])
      nom_oeuvre = liste[index_liste][1]
      im = Image.open(f'./Oeuvres/{nom_oeuvre}.png')
      im_resized = im.resize((905, 805))
      tkimg = ImageTk.PhotoImage(im_resized)
      community_username_label.pack(side='right')
      community_img.create_image(0, 0, anchor=t.NW, image=tkimg)
      community_img.image = tkimg


  def oeuvre_apres(liste, username): 
      nonlocal index_liste, nom_oeuvre
      if index_liste < len(liste)-1:
        index_liste += 1
      else:
        index_liste = 0


      username.set(liste[index_liste][0])
      nom_oeuvre = liste[index_liste][1]
      im = Image.open(f'./Oeuvres/{nom_oeuvre}.png')
      im_resized = im.resize((905, 805))
      tkimg = ImageTk.PhotoImage(im_resized)
      community_username_label.pack(side='right')
      community_img.create_image(0, 0, anchor=t.NW, image=tkimg)
      community_img.image = tkimg
 
      
  def delete_image(filename):
    delete_item(filename)
    nonlocal  liste_oeuvre 
    liste_oeuvre = oeuvre_community(user_name)

  # --------- TOP FRAME --------- #
  top_frame = t.Frame(frame, background='#324C40')
    # ------ Back Button ------ #
  community_back_frame = t.Frame(top_frame, background='#324C40')
  community_back_button = t.Button(community_back_frame, background="#577D54", text="<", font = ('Corbel', 25), fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", command=go_home_page, image=back_image, )


    # ------ Title ------ #
  community_title_frame = t.Frame(top_frame, background='#D1D5C6', borderwidth=5)
  community_title = t.Label(community_title_frame, text = "Les oeuvres de la communauté", background = '#324C40', font = font, fg="#D1D5C6")


  # --------- ART FRAME --------- #
  community_art_frame = t.Frame(frame, background='#324C40')

  # ------ Button Frame ------ #
  community_button_frame = t.Frame(community_art_frame, background='#324C40')


  community_left_frame = t.Frame(community_button_frame, background='#324C40')
  community_left_button = t.Button(community_left_frame, image=avant_img, font=font, fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", bg='#577D54')

  community_image_frame = t.Frame(community_button_frame, background='#D1D5C6')
  im1 = Image.open(f'./Oeuvres/{nom_oeuvre}.png')
  im1_resized = im1.resize((905, 805))
  tkimage = ImageTk.PhotoImage(im1_resized)
  community_img = t.Canvas(community_image_frame, width=905, height=805)
  community_img.create_image(0, 0, anchor = t.NW, image=tkimage)


  community_right_frame = t.Frame(community_button_frame, background='#324C40')  
  community_right_button = t.Button(community_right_frame, image=apres_img, font=font, fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", bg='#577D54')


  # ------ Delete Frame ------ #
  community_delete_frame = t.Frame(community_art_frame, background='#324C40')
  delete_username_frame = t.Frame(community_delete_frame, background='#324C40')
  community_delete_label = t.Label(delete_username_frame, text='Oeuvre réalisée par :', font=font, bg='#324C40', fg="#D1D5C6")
  community_username_label = t.Label(delete_username_frame, textvariable=username, font=font,bg='#324C40', fg="#D1D5C6")
  delete_button = t.Button(community_delete_frame, image=delete_img, bg='#577D54')
  

  # --------- Pack --------- #
  frame.pack(fill='both')

  # ---- TOP FRAME ----- #
  top_frame.pack(side='top', fill='x')
    # ---- Title ----- #
  community_title_frame.pack(pady=20, expand=True, side='right')
  community_title.pack(ipadx=10, ipady=5)

    # ---- Back Button ----- #
  community_back_frame.pack(side='left',padx=20, fill='x')
  community_back_button.pack(ipadx=5, ipady=5)

  # ---- ART FRAME ----- #
  community_art_frame.pack(side='bottom', fill='x', pady=20)

    # ---- Button Area ----- #
  community_button_frame.pack(side='top', fill='x')

      # ---- Left Button Area ----- #
  community_left_frame.pack(side='left', ipadx=100, padx=50)
  community_left_button.pack(expand=True, ipadx=20, ipady=25)

      # ---- Image Button Area ----- #
  community_image_frame.pack(expand=True, side='left', ipadx=10, ipady=10)
  community_img.pack(expand=True)

      # ---- Right Button Area ----- #
  community_right_frame.pack(side='right', ipadx=100, padx=50)
  community_right_button.pack(expand=True, ipadx=20, ipady=25)

    # ---- Delete Area ----- #
  community_delete_frame.pack(side='bottom', ipadx=20, ipady= 100, fill='both', pady=10)
  community_delete_label.pack()

  delete_username_frame.pack(side='left', expand=True)
  community_delete_label.pack(side='left')
  community_username_label.pack(side='right')
  delete_button.pack(side='right', ipadx=5, ipady=5, expand=True)
  

  community_left_button['command'] = lambda: oeuvre_avant(liste_oeuvre, username)
  community_right_button['command'] = lambda: oeuvre_apres(liste_oeuvre, username)
  delete_button['command'] = lambda: delete_image(nom_oeuvre)
# --------------- CONFIGURATION PAGE --------------- #

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

    if forme_entry in ["carré", "spirale", "flocon", "sierpinsky", "geo", "cercle"] : #Tu me rajoutes les formes possibles ici
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
  top_frame = t.Frame(configuration_frame, background='#324C40') 
  configuration_back_frame = t.Frame(top_frame, background='#324C40')
  configuration_back_button = t.Button(configuration_back_frame, background="#577D54", text="<", font = ('Corbel', 25), fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", command=go_profile_page, image=back_image, )



  configuration_title_frame = t.Frame(top_frame, background='#D1D5C6', borderwidth=5)
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
  top_frame.pack(side='top', fill='x')
  configuration_back_frame.pack(side='left', padx=10)
  configuration_back_button.pack(ipadx=5, ipady=5)

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

# --------------- PAGE ACCESS FUNCTION --------------- #

def go_profile_page():
    for p in pages:
        p.pack_forget()

    profile_access(profile_frame)
    profile_frame.pack(fill='both', ipady=100)

def go_home_page():
    for p in pages:
        p.pack_forget()
    
    home_access(home_frame)
    home_frame.pack(fill='both', ipady=100)

def go_login_page():
  for p in pages:
      p.pack_forget()
  login_access()
  login_frame.pack(fill='both', ipady=100)

def go_configuration_page():
  for p in pages:
      p.pack_forget()
  configuration_page(configuration_frame, user_name)
  
def go_community_page():
  for p in pages:
      p.pack_forget()
  community_access(community_frame)


login_access(login_frame)
login_frame.pack(fill='both', ipady=100)


t.mainloop() #Laisser la fenetre ouverte
connexion_close()