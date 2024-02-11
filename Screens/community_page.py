import tkinter as t
from PIL import ImageTk, Image

fenetre = t.Tk() #Créer une fenetre
fenetre.title("Turtle Art Creator")
fenetre.attributes('-fullscreen', True)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())


community_frame = t.Frame(fenetre, background='#324C40')
font = ('Corbel', 30, 'bold')
global tkimage
username = t.StringVar()
username.set("Username")

# --------- TOP FRAME --------- #
top_frame = t.Frame(community_frame, background='#324C40')
  # ------ Back Button ------ #
community_back_frame = t.Frame(top_frame, background='#324C40')
back_image = t.PhotoImage(file='./Icons/accueil.png')
community_back_button = t.Button(community_back_frame, background="#577D54", text="<", font = ('Corbel', 25), fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", command="", image=back_image)


  # ------ Title ------ #
community_title_frame = t.Frame(top_frame, background='#D1D5C6', borderwidth=5)
community_title = t.Label(community_title_frame, text = "Les oeuvres de la communauté", background = '#324C40', font = font, fg="#D1D5C6")


# --------- ART FRAME --------- #
community_art_frame = t.Frame(community_frame, background='#324C40')

# ------ Button Frame ------ #
community_button_frame = t.Frame(community_art_frame, background='#324C40')

community_left_frame = t.Frame(community_button_frame, background='#324C40')
community_left_button = t.Button(community_left_frame, text='<', font=font, fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", bg='#577D54')

community_image_frame = t.Frame(community_button_frame, background='#D1D5C6')
im1 = Image.open('./Icons/background.png')
im1_resized = im1.resize((905, 805))
tkimage = ImageTk.PhotoImage(im1_resized)
community_img = t.Label(community_image_frame,image=tkimage, background='#324C40')

community_img.image = tkimage

community_right_frame = t.Frame(community_button_frame, background='#324C40')
community_right_button = t.Button(community_right_frame, text='>', font=font, fg="#D1D5C6", activebackground="#D1D5C6", activeforeground="#577D54", bg='#577D54')


# ------ Delete Frame ------ #
community_delete_frame = t.Frame(community_art_frame, background='yellow')
delete_username_frame = t.Frame(community_delete_frame, background='red')
community_delete_label = t.Label(delete_username_frame, text='Oeuvre réalisée par :')
community_username_label = t.Label(delete_username_frame, textvariable=username)
delete_img = t.PhotoImage(file='./Icons/poubelle-de-recyclage.png')
delete_button = t.Button(community_delete_frame, image=delete_img, bg='#577D54')

delete_username_frame.pack(side='left', expand=True)
delete_button.pack(side='right', ipadx=5, ipady=5, expand=True)
# --------- Pack --------- #
community_frame.pack(fill='both')

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
t.mainloop()