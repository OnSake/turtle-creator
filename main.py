import tkinter as t
from tkinter import font
from tkinter.filedialog import askopenfilename 
from PIL import Image, ImageTk


fenetre = t.Tk() #Créer une fenetre
fenetre.title("Turtle Art Creator")
fenetre.geometry("1200x1000")
fenetre.minsize(1200, 1000)



# --------------- PAGES --------------- #


home_frame =t.Frame(fenetre, background='#324C40')
profile_frame = t.Frame(fenetre, background='#324C40')
login_frame = t.Frame(fenetre, background='#324C40')


font = ('Corbel', 30, 'bold')



pages = [home_frame, profile_frame, login_frame]


# --------------- LOGIN PAGE --------------- #
def login_access(login_frame):
    def confirm_username():
      if username_input.get() != '':
        global user_name
        user_name = username_input.get()
        username_error_frame.pack_forget()
        username_error_message.pack_forget()
        go_home_page()
      else: 
        error_message.set(value="Veuillez entrer un nom d'utilisateur valide")
        print(error_message.get())
        username_error_frame.pack(expand=True)
        username_error_message.pack(expand=True)

    def choose_img():
      path = askopenfilename(title="Choississez votre photo de profil", filetypes=[('png files','.png'), ('jpg files', '.jpg')])
      im = Image.open(path)
      im = im.resize((200, 200))
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
    error_message = t.StringVar(master=username_error_frame, value="EEEE")
    username_error_message = t.Label(username_error_frame, text=error_message, fg='red', background='#324C40', font=('Corbel', 15, 'bold'))


    profil_img_frame = t.Frame(login_frame, background='#324C40')
    profil_img_choose = t.Button(profil_img_frame, text='Choisir une photo de profil',  command=choose_img)
    im1 = Image.open('background.png')
    tkimage = ImageTk.PhotoImage(im1)
    profil_img = t.Label(profil_img_frame, image=tkimage, background='#324C40')
    profil_img.image = tkimage

    button_confirm = t.Button(login_frame, text='Confirmer', font= ('Corbel', 15), command=confirm_username)
    frame = t.Frame(login_frame, background='#324C40')

    welcome_message.pack(fill='x', expand=True, pady=30)
    presentation_message.pack(fill='x', expand=True, pady= 50)

    username_frame.pack(expand=True, ipady=20)
    username_input.pack(ipadx=20, ipady=15, side='left', padx=20)
    username_error_frame.pack(expand=True)
    username_error_message.pack(expand=True)

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
    b2 = t.Button(home_button_frame, background="#577D54", text="Création de la communauté", font = ('Corbel', 15, 'bold'), fg="#D1D5C6", width= 50, activebackground='#3D5B3A', activeforeground='#D1D5C6')
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
  profile_back_button = t.Button(profile_back_frame, background="#577D54", text="<", font = ('Corbel', 25), fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", command=go_home_page)

  # --------- Title --------- #
  profile_title_frame = t.Frame(profile_frame, background='#D1D5C6', borderwidth=5)
  profile_title = t.Label(profile_title_frame, text = "Mon profil", background = '#324C40', font = font, fg="#D1D5C6")

  # --------- Username + Img --------- #
  profile_header_frame = t.Frame(profile_frame, background='#324C40')
  profil_img = t.PhotoImage(file='Icons/logo.png')
  profile_header_img = t.Label(profile_header_frame, image=profil_img, width=150, height=150, background='#324C40')
  profile_header_name = t.Label(profile_header_frame, text=user_name, background='#324C40', fg = '#D1D5C6', font = font)


  # --------- My Creations Section --------- #
  profile_creation_frame = t.Frame(profile_frame, background='#324C40')
  profile_creation_title = t.Label(profile_creation_frame, text='Mes créations :', fg = '#577D54', font = font, background='#324C40')

  profile_mycreations_frame = t.Frame(profile_frame, background="#324C40")
  profile_mycreations_button = t.Button(profile_mycreations_frame, background="#9EAD84", text="+", width=5, height=4, font = ('Comic sans MS', 45), fg="#38573F", activebackground="#38573F", activeforeground="#9EAD84")

  profile_mycreations_list_frame = t.Frame(profile_mycreations_frame, background='#324C40')
  profile_mycreations_list_frame1 = t.Frame(profile_mycreations_list_frame, background='#D1D5C6', borderwidth=3)
  profile_mycreations_list_project1 = t.Label(profile_mycreations_list_frame1 ,text='Test 1', background='#324C40', font = ('Corbel', 15, 'bold'), fg='#D1D5C6')
  profile_mycreations_list_view1 = t.Button(profile_mycreations_list_frame1, font = ('Corbel', 15, 'bold'), text="Voir l'oeuvre", background='#D1D5C6', relief='groove')
  profile_mycreations_list_frame2 = t.Frame(profile_mycreations_list_frame, background='#D1D5C6', borderwidth=3)
  profile_mycreations_list_project2 = t.Label(profile_mycreations_list_frame2 ,text='Test 2', background='#324C40', font = ('Corbel', 15, 'bold'), fg='#D1D5C6')
  profile_mycreations_list_view2 = t.Button(profile_mycreations_list_frame2, font = ('Corbel', 15, 'bold'), text="Voir l'oeuvre", background='#D1D5C6', relief='groove')

  creation_frames = [profile_mycreations_list_frame1, profile_mycreations_list_frame2]
  creation_frames_projects = [profile_mycreations_list_project1, profile_mycreations_list_project2]
  creation_frames_buttons = [profile_mycreations_list_view1, profile_mycreations_list_view2]

  frame = t.Frame(profile_frame, background='#324C40')

  # --------- Packs --------- #
  profile_back_frame.pack(fill='x')
  profile_back_button.pack(side='left', padx=15, pady=15)

  profile_title_frame.pack(pady=10)
  profile_title.pack(ipadx=25, ipady=25)

  profile_header_img.pack(side='left', ipadx=10)
  profile_header_name.pack(side='left', fill='both')
  profile_header_frame.pack(fill='x')

  profile_creation_title.pack(side='left', ipadx=20, ipady=10, pady=25)
  profile_creation_frame.pack(fill='both')

  profile_mycreations_frame.pack(fill="both")
  profile_mycreations_button.pack(side="left", padx=20)



  profile_mycreations_list_frame.pack(side='right',fill='both')
  
  for frame in creation_frames:
    frame.pack(fill='both', padx=20, pady=10)
  for project in creation_frames_projects:
    project.pack(fill='both',ipadx=350,ipady=20, side='left')
  for button in creation_frames_buttons:
    button.pack(side='right', padx=10)

  

    
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


login_access(login_frame)
login_frame.pack(fill='both', ipady=100)


t.mainloop() #Laisser la fenetre ouverte