import tkinter as t
from tkinter.filedialog import askopenfilename 


fenetre = t.Tk() #Créer une fenetre
fenetre.title("Turtle Art Creator")
fenetre.geometry("1200x1000")
fenetre.minsize(1200, 1000)

configuration_frame = t.Frame(fenetre, background='#324C40')
first_page = t.Frame(fenetre, background='#324C40')

username = ''
profil_img = ''
def confirm_username():
  username = username_input.get()
  if username_input.get() != '':
    username = username_input.get()
    username_error_frame.pack_forget()
    username_error_message.pack_forget()
  else: 
    username_error_frame.pack(expand=True)
    username_error_message.pack(expand=True)


def choose_img():
  profil_img = askopenfilename()
  photo = t.Label(username_frame, image=profil_img, width=150, height=150, background='#324C40')
  photo.pack()
  


welcome_message = t.Label(first_page, text='Bienvenue', font=('Corbel', 50, 'bold'), background='#324C40', fg='#D1D5C6')
presentation_message = t.Label(first_page, text="Avant de commencer, veuillez entrer un nom d'utilisateur", font=('Corbel', 25, 'bold'), background='#324C40', fg='#D1D5C6')



username_frame = t.Frame(first_page, background='#324C40')
username_input = t.Entry(username_frame, font=('Corbel', 15, 'bold'), fg='#D1D5C6', background='#577D54')
username_confirm = t.Button(username_frame, text='Confirmer', font= ('Corbel', 15), command=confirm_username)
username_error_frame = t.Frame(first_page, background='red')
username_error_message = t.Label(username_error_frame, text="Veuillez entrer un nom d'utilisateur valide", fg='red', background='#324C40', font=('Corbel', 15, 'bold'))


profil_img_frame = t.Frame(first_page, background='red')
profil_img_choose = t.Button(profil_img_frame, text='Choisir une photo de profil', command=choose_img)


welcome_message.pack(fill='x', expand=True, pady=30)
presentation_message.pack(fill='x', expand=True, pady= 50)
first_page.pack(fill='both')



username_frame.pack(expand=True, ipady=20)
username_input.pack(ipadx=20, ipady=15, side='left', padx=20)
username_confirm.pack(side='right')

profil_img_frame.pack()
profil_img_choose.pack()
t.mainloop()
