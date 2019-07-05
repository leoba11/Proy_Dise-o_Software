import tkinter as tk
from tkinter import *
from tkinter import messagebox
from chessBoard import chessBoard
from absChessWindow import AbsChessWindow
import os
import time
import PIL
import PIL.Image
import PIL.ImageTk

class initialWindow(tk.Frame, AbsChessWindow):
	
    # Builder of the class
    def __init__(self, master, logic_chessboard, controller):
        super().__init__()
        
        self.controller = controller
        
        self.master.title("Ajedrez Diseño de Software")
        self.pack()
        
        self.logic_chessboard = logic_chessboard

        im2 = PIL.Image.open('images/ajedrez.jpg')
        self.icon = PIL.ImageTk.PhotoImage(im2)
        self.icon.image = self.icon 

        self.labelito = Label(master, image=self.icon)
        self.labelito.pack()

        self.grupo = Label(master, text="Diseño de Software", width=20, fg="white",bg="#000000", font=("Helvetica", 24, 'bold'))
        self.grupo.place(relx=0.53, rely=0.06)

        # Creates the labels with the Entry boxes for the white and black pieces players
        self.lbl1 = Label(master, text="Jugador con fichas blancas:", width=25, anchor=NW, fg="white",font=("Helvetica", 16), bg="grey")
        
        # places the object in a relative position of the window
        self.lbl1.place(relx=0.08, rely=0.2)

        self.entry1 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry1.place(relx=0.55, rely=0.2)

        self.lbl2 = Label(master, text="Jugador con fichas negras:", width=25, anchor=NW, font=("Helvetica", 16), bg="grey")
        self.lbl2.place(relx=0.08, rely=0.5)

        self.entry2 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry2.place(relx=0.55, rely=0.5)

        # Creates the button to submit the players names
        self.buttonPlay = Button(master, text="¡¡Jugar!!", bg="#5BD317", bd=5, justify=CENTER, width=12, font=("Helvetica", 16), command=self.controller.button_click)
        self.buttonPlay.place(relx=0.65, rely=0.75)

        self.buttonQuit = Button(master, text="¡Salir!", bg="#BF2222", bd=5, justify=CENTER, width=12, font=("Helvetica",16), command=self.controller.button_quit)
        self.buttonQuit.place(relx=0.40, rely=0.75)
