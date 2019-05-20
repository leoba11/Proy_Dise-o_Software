from tkinter import *

import PIL.Image
import PIL.ImageTk

root = Tk()

def new_winF(): # new window definition
    # newwin = Toplevel(root)
    # display = Label(newwin, text="Humm, see a new window !")
    # display.pack()    

    text1 = Text(root, height=36, width=68)

    im = PIL.Image.open("che.jpg")
    photo = PIL.ImageTk.PhotoImage(im)

    text1.image_create(END, image=photo)

    text1.pack(side=LEFT)

    text2 = Text(root, height=36, width=65)
    scroll = Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color', foreground='#476040', font=('Tempus Sans ITC', 12, 'bold'))
    text2.insert(END,' Reglas\n', 'big')
    quote = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    """
    text2.insert(END, quote, 'color')
    text2.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)

button1 =Button(root, text ="open new window", command =new_winF) #command linked
button1.pack()

root.mainloop()