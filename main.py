import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import ImageTk


def open_sadry_site():
    webbrowser.open_new("/Users/sadryhilal/Desktop/EPITECH/project/PIXELY/PIXELY/IMG/logo.ico")

def open_image(): 
    photo = ImageTk.PhotoImage(file='./IMG/Antoine.png') 
    item = can1.create_image(250, 250, image = photo) 
    can1.pack() 

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'bon j avoue y a rien c est bien tu es sr de toi bravo BG')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "😈")

#creer une fenetre

window = Tk()
#personnalisation

window.title("PIXELY")
window.geometry("1080x800")
window.minsize(450, 300)
window.iconbitmap("/Users/sadryhilal/Desktop/EPITECH/project/PIXELY/PIXELY/IMG/logo.ico")
window.config(background='#9D9B9A')

#frame

frame = Frame(window, bg='#9D9B9A')

#ajouter de l information 

label_title = Label(frame, text="Bienvenue sur PIXELY", font=("Sans", 25), bg='#9D9B9A')
label_title.pack()

label_subtitle = Label(frame, text="Ici tu purras venir pixeliser tes images", font=("Sans", 12), bg='#9D9B9A')
label_subtitle.pack()




fileMenu = Menubutton(frame, text = 'choisir une image') 
fileMenu.pack(side = TOP) 
me1 = Menu(fileMenu) 
me1.add_command(label = 'Antoine.', command = open_image) 


fileMenu.configure(menu = me1) 
 
can1 = Canvas(window, width = 500, height = 500, bg = 'white') 
 
#ajouter un bouton 

img_button = Button(frame, text="choisir une image", font=("Sans", 12), command=open_sadry_site)
img_button.pack(pady=20, fill=X)

# bouton de sortie
bouton=Button(frame, text="Fermer", command=window.quit)
Button(frame, text='es tu patient ?', command=callback).pack()
bouton.pack()


#afficher $

frame.pack(expand=YES)
window.mainloop()