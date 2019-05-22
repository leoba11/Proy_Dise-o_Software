import tkinter as tk
from tkinter import *
from tkinter import messagebox
from chessBoard import chessBoard
import os
import time

class VentanaInicial(Frame):
	
    # Variables to store the players names
    playerWhite_name = "" 
    playerBlack_name = ""
	
    # Builder of the class
    def __init__(self, master):
        super().__init__()
        
        self.master.title("Ajedrez Diseno de Software")
        self.pack()

        self.labelito = Label(master, image=PhotoImage(file="avion.gif"))
        self.labelito.pack()

        # Creates the labels with the Entry boxes for the white and black pieces players
        self.lbl1 = Label(master, text="Jugador con fichas blancas:", width=25, anchor=NW, fg="white",font=("Helvetica", 16))
        
        # places the object in a relative position of the window
        self.lbl1.place(relx=0.08, rely=0.2)

        self.entry1 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry1.place(relx=0.55, rely=0.2)

        self.lbl2 = Label(master, text="Jugador con fichas negras:", width=25, anchor=NW, font=("Helvetica", 16))
        self.lbl2.place(relx=0.08, rely=0.5)

        self.entry2 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry2.place(relx=0.55, rely=0.5)
        
        # Creates a text box
        self.box = Text(master, width=25, height=4, wrap=WORD, background="white")
        self.box.place(relx=0.08, rely=0.75)
		
        # Creates the button to submit the players names
        self.buttonPlay = Button(master, text="Jugar!!", bg="green", bd=5, justify=CENTER, width=10, font=("Helvetica", 16), command=self.button_click)
        self.buttonPlay.place(relx=0.65, rely=0.75)

        self.buttonQuit = Button(master, text="Salir!", bg="red", bd=5, justify=CENTER, width=10, font=("Helvetica",16), command=self.button_quit)
        self.buttonQuit.place(relx=0.40, rely=0.75)        

    # Subroutine that extracts the players names and stores them into the class attributes 
    def button_click(self):
        # stores into the variables of the class the names written names
        playerWhite_name = self.entry1.get()
        playerBlack_name = self.entry2.get()

        # Checks if the players names have been written in order to start the game
        if len(playerWhite_name) is 0 or len(playerBlack_name) is 0:
            self.no_names()
        else:
            self.box.delete(0.0, END)
            self.box.insert(END, playerWhite_name + " juega con fichas blancas")
            self.box.insert(END, " y ")
            self.box.insert(END, playerBlack_name + " juega con fichas negras")
            
        # Hides this window and shows the board
        time.sleep(1)
        self.master.withdraw()
        
        # function to show the window
        self.master.deiconify()
        
        board_root = Toplevel(self.master)
        board = chessBoard(8, 8, 'blue', 'green', 64, board_root)
        board.pack(side='top', fill='both', expand='true', padx=4, pady=4)
        
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)

        for piece in imgs:

            #----------------Black ones---------------------
            if piece == "bb.gif": #Black Bishop 2
                photo = tk.PhotoImage(file = defPath+"bb.gif")
                board.addPiece("bbr", photo, 0, 1)
                board.addPiece("bbl", photo, 0, 6)

            if piece == "bk.gif": #Black King
                photo2 = tk.PhotoImage(file = defPath+"bk.gif")
                board.addPiece("bk", photo2, 0, 4)

            if piece == "bn.gif": #Black Knigth 2 
                photo3 = tk.PhotoImage(file = defPath+"bn.gif")
                board.addPiece("bnl", photo3, 0, 2)     
                board.addPiece("bnr", photo3, 0, 5)

            if piece == "bp.gif": #Black Pawn 8
                photo4 = tk.PhotoImage(file = defPath+"bp.gif")
                board.addPiece("bp", photo4, 1, 0)     
                board.addPiece("bp1", photo4, 1, 1)
                board.addPiece("bp2", photo4, 1, 2)
                board.addPiece("bp3", photo4, 1, 3)
                board.addPiece("bp4", photo4, 1, 4)
                board.addPiece("bp5", photo4, 1, 5)
                board.addPiece("bp6", photo4, 1, 6)
                board.addPiece("bp7", photo4, 1, 7)                

            if piece == "br.gif": #Balck Rook 2
                photo5 = tk.PhotoImage(file = defPath+"br.gif")
                board.addPiece("brl", photo5, 0, 0)
                board.addPiece("brr", photo5, 0, 7)

            if piece == "bq.gif": #Balck Queen 
                photo6 = tk.PhotoImage(file = defPath+"br.gif")
                board.addPiece("bq", photo6, 0, 3)      

            #----------------Black ones---------------------

            #----------------White ones---------------------
        
            if piece == "wb.gif": #White Bishop 2
                photo7 = tk.PhotoImage(file = defPath+"wb.gif")
                board.addPiece("wbr", photo7, 7, 1)
                board.addPiece("wbl", photo7, 7, 6)

            if piece == "wk.gif": #White King
                photo8 = tk.PhotoImage(file = defPath+"wk.gif")
                board.addPiece("wk", photo8, 7, 4)

            if piece == "wn.gif": #White Knigth 2 
                photo9 = tk.PhotoImage(file = defPath+"wn.gif")
                board.addPiece("wnl", photo9, 7, 2)     
                board.addPiece("wnr", photo9, 7, 5)

            if piece == "wp.gif": #white Pawn 8
                photo10 = tk.PhotoImage(file = defPath+"wp.gif")
                board.addPiece("wp", photo10, 6, 0)     
                board.addPiece("wp1", photo10, 6, 1)
                board.addPiece("wp2", photo10, 6, 2)
                board.addPiece("wp3", photo10, 6, 3)
                board.addPiece("wp4", photo10, 6, 4)
                board.addPiece("wp5", photo10, 6, 5)
                board.addPiece("wp6", photo10, 6, 6)
                board.addPiece("wp7", photo10, 6, 7)                

            if piece == "wr.gif": #White Rook 2
                photo11 = tk.PhotoImage(file = defPath+"wr.gif")
                board.addPiece("wrl", photo11, 7, 0)
                board.addPiece("wrr", photo11, 7, 7)

            if piece == "wq.gif": #White
                photo12 = tk.PhotoImage(file = defPath+"wr.gif")
                board.addPiece("wq", photo12, 7, 3) 

            #----------------White ones---------------------
        #----------------------GeneraTablero---------------------------------

        board.printPieces()
        
        
        
        
        
        
        

    # Subroutine that closes the complete window
    def button_quit(self):
        self.quit()

    # Subroutine that shows the error message box to the user
    def no_names(self):
        messagebox.showerror("Error!", "Falta uno o más nombres de jugador")

def main():
    root = Tk()
    root.geometry("600x300")
    app = VentanaInicial(root)#.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
