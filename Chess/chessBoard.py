import tkinter as tk
import os
from tkinter import *
from genBoard import *

from chessRules import *

from caballo import Caballo
from peon import Peon
from reina import Reina
from rey import Rey
from torre import Torre


class chessBoard(tk.Frame, genBoard): #Hereda de tk y genBoard
    
    def __init__(self, rows, columns, color1, color2, size, parent):
        pass
        genBoard.__init__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado
        
        #Dimensions
        canvasWidth = columns * size
        canvasHeight = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0, width = canvasWidth, height = canvasHeight, background = 'bisque')
        self.canvas.pack(side = 'top', fill = 'both', expand = True, padx = 2, pady = 2)

        self.frame = tk.Frame(self)
        self.button1 = tk.Button(self.frame, text = 'Ver Reglas', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

        self.canvas.bind('<Configure>', self.refresh)
        
    #Agregar nueva ventana
    def new_window(self):
        self.newWindow = tk.Toplevel()
        self.newWindow.title('CHESS RULES')
        self.app = chessRules(self.newWindow)
        #self.refresh(self.refresh)


    #Add a piece to the tab to be used
    def addPiece(self, name, image, row, column):
        self.canvas.create_image(0,0, image = image, tags = (name, 'piece'), anchor = 'c')
        self.placePiece(name, row, column)

    def placePiece(self, name, row, column):

        self.pieces[name] = (row, column)
        
        #print(self.pieces)
        
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)
   
    def loadInitPosPiece(self):
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)

        for piece in imgs:

            #----------------Black ones---------------------
            if piece == "bb.gif": #Black Bishop 2
                photo = tk.PhotoImage(file = defPath+"bb.gif")
                photo.image = photo
                self.addPiece("bbr", photo, 0, 1)
                self.addPiece("bbl", photo, 0, 6)

            if piece == "bk.gif": #Black King
                photo2 = tk.PhotoImage(file = defPath+"bk.gif")
                photo2.image = photo2
                self.addPiece("bk", photo2, 0, 4)

            if piece == "bn.gif": #Black Knigth 2 
                photo3 = tk.PhotoImage(file = defPath+"bn.gif")
                photo3.image = photo3
                self.addPiece("bnl", photo3, 0, 2)     
                self.addPiece("bnr", photo3, 0, 5)

            if piece == "bp.gif": #Black Pawn 8
                photo4 = tk.PhotoImage(file = defPath+"bp.gif")
                photo4.image = photo4
                self.addPiece("bp", photo4, 1, 0)     
                self.addPiece("bp1", photo4, 1, 1)
                self.addPiece("bp2", photo4, 1, 2)
                self.addPiece("bp3", photo4, 1, 3)
                self.addPiece("bp4", photo4, 1, 4)
                self.addPiece("bp5", photo4, 1, 5)
                self.addPiece("bp6", photo4, 1, 6)
                self.addPiece("bp7", photo4, 1, 7)                

            if piece == "br.gif": #Balck Rook 2
                photo5 = tk.PhotoImage(file = defPath+"br.gif")
                photo5.image = photo5
                self.addPiece("brl", photo5, 0, 0)
                self.addPiece("brr", photo5, 0, 7)

            if piece == "bq.gif": #Balck Queen 
                photo6 = tk.PhotoImage(file = defPath+"bq.gif")
                photo6.image = photo6
                self.addPiece("bq", photo6, 0, 3)      

            #----------------Black ones---------------------
            #----------------White ones---------------------
        
            if piece == "wb.gif": #White Bishop 2
                photo7 = tk.PhotoImage(file = defPath+"wb.gif")
                photo7.image = photo7
                self.addPiece("wbr", photo7, 7, 1)
                self.addPiece("wbl", photo7, 7, 6)

            if piece == "wk.gif": #White King
                photo8 = tk.PhotoImage(file = defPath+"wk.gif")
                photo8.image = photo8
                self.addPiece("wk", photo8, 7, 4)

            if piece == "wn.gif": #White Knigth 2 
                photo9 = tk.PhotoImage(file = defPath+"wn.gif")
                photo9.image = photo9
                self.addPiece("wnl", photo9, 7, 2)     
                self.addPiece("wnr", photo9, 7, 5)

            if piece == "wp.gif": #white Pawn 8
                photo10 = tk.PhotoImage(file = defPath+"wp.gif")
                photo10.image = photo10
                self.addPiece("wp", photo10, 6, 0)     
                self.addPiece("wp1", photo10, 6, 1)
                self.addPiece("wp2", photo10, 6, 2)
                self.addPiece("wp3", photo10, 6, 3)
                self.addPiece("wp4", photo10, 6, 4)
                self.addPiece("wp5", photo10, 6, 5)
                self.addPiece("wp6", photo10, 6, 6)
                self.addPiece("wp7", photo10, 6, 7)                

            if piece == "wr.gif": #White Rook 2
                photo11 = tk.PhotoImage(file = defPath+"wr.gif")
                photo11.image = photo11
                self.addPiece("wrl", photo11, 7, 0)
                self.addPiece("wrr", photo11, 7, 7)

            if piece == "wq.gif": #White
                photo12 = tk.PhotoImage(file = defPath+"wq.gif")
                photo12.image = photo12
                self.addPiece("wq", photo12, 7, 3) 

            #----------------White ones---------------------

    def printPieces(self):
        print(self.pieces)
    
    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

        for name in self.pieces:
            #print ("entré al for de refresh")
            self.placePiece(name, self.pieces[name][0], self.pieces[name][1]) #Add the piece
        
        

        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


'''
if __name__ == "__main__":
    
    #----------------------GeneraTablero---------------------------------
    root = tk.Tk()
    board = chessBoard(8, 8, 'blue', 'green', 64, root)
    board.pack(side='top', fill='both', expand='true', padx=4, pady=4)
    #board.loadInitPosPiece()
    
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
        '''
    
