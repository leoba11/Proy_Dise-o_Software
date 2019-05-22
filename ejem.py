from tkinter import *
import PIL.Image
import PIL.ImageTk

root = Tk()

def new_winF(): # new window definition
    newwin = Toplevel(root)  

button1 =Button(root, text ="REGLAS", command =new_winF) #command linked
button1.pack()

root.mainloop()