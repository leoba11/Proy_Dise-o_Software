import tkinter as tk
from tkinter import *
from tkinter import messagebox
from chessBoard import chessBoard
import os
import time

import PIL.Image
import PIL.ImageTk

class initialWindow(tk.Frame):
	
    # Variables to store the players names
    playerWhite_name = "" 
    playerBlack_name = ""
	
    # Builder of the class
    def __init__(self, master, logic_chessboard):
        super().__init__()
        
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
		
        #self.box = Text(master, width=25, height=4, wrap=WORD, background="white")
        #self.box.place(relx=0.08, rely=0.75) To display players selection

        # Creates the button to submit the players names
        self.buttonPlay = Button(master, text="¡¡Jugar!!", bg="#5BD317", bd=5, justify=CENTER, width=12, font=("Helvetica", 16), command=self.button_click)
        self.buttonPlay.place(relx=0.65, rely=0.75)

        self.buttonQuit = Button(master, text="¡Salir!", bg="#BF2222", bd=5, justify=CENTER, width=12, font=("Helvetica",16), command=self.button_quit)
        self.buttonQuit.place(relx=0.40, rely=0.75)

    # Subroutine that extracts the players names and stores them into the class attributes 
    def button_click(self):
        # stores into the variables of the class the names written names
        playerWhite_name = self.entry1.get()
        playerBlack_name = self.entry2.get()

        # Checks if the players names have been written in order to start the game
        if len(playerWhite_name) is 0 or len(playerBlack_name) is 0:
            self.no_names()
        ''' To display players selection
        else:
            self.box.delete(0.0, END)
            self.box.insert(END, playerWhite_name + " juega con fichas blancas")
            self.box.insert(END, " y ")
            self.box.insert(END, playerBlack_name + " juega con fichas negras")
        '''    
        # Hides this window and shows the board
        time.sleep(1)
        self.master.withdraw()
        
        # function to show the window
        self.master.deiconify()
        
        board_root = Toplevel(self.master)
        board = chessBoard(self.logic_chessboard, 8, 8, "#F3D484", "#A05D06", 64, board_root, playerWhite_name, playerBlack_name)
        board.pack(side='top', fill='both', expand='true', padx=4, pady=4)
        board.loadInitPosPiece()
        board.printPieces()

    def button_quit(self):
        self.quit()

    # Subroutine that shows the error message box to the user
    def no_names(self):
        messagebox.showerror("Error!", "Falta uno o más nombres de jugador")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x490")
    app = initialWindow(root)#.pack()
    
    print (root.winfo_pointerxy())
    root.mainloop()
