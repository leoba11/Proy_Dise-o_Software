import tkinter as tk
import os
from tkinter import *
from genBoard import *
from peon import Peon
from alfil import Alfil
from caballo import Caballo
from torre import Torre
from reina import Reina
from rey import Rey
from chessRules import *
import time


class chessBoard(tk.Frame, genBoard): #Hereda de tk y genBoard
    
    def __init__(self, rows, columns, color1, color2, size, parent):
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
        
        self.loadInitPosPiece()	# Creates and loads all the pieces
        
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
        
        # Creates all the black pieces and draws them into the board
        black_king = Rey('b', 0, 4, defPath + "bk.gif")
        black_king.image.image = black_king.image
        self.addPiece("bk", black_king.image, black_king.getCoordX(), black_king.getCoordY())
        black_queen = Reina('b', 0,3, defPath + "bq.gif")
        black_queen.image.image = black_queen.image
        self.addPiece("bq", black_queen.getImage(), black_queen.getCoordX(), black_queen.getCoordY())
        black_bishop1 = Alfil('b', 0, 2, defPath + "bb.gif")
        black_bishop1.image.image = black_bishop1.image
        self.addPiece("bbr", black_bishop1.image, black_bishop1.getCoordX(), black_bishop1.getCoordY())
        black_bishop2 = Alfil('b', 0, 5, defPath + "bb.gif")
        black_bishop2.image.image = black_bishop2.image
        self.addPiece("bbl", black_bishop2.image, black_bishop2.getCoordX(), black_bishop2.getCoordY())
        black_knigth1 = Caballo('b', 0, 1, defPath + "bn.gif")
        black_knigth1.image.image = black_knigth1.image
        self.addPiece("bnr", black_knigth1.image, black_knigth1.getCoordX(), black_knigth1.getCoordY())
        black_knigth2 = Caballo('b', 0, 6, defPath + "bn.gif")
        black_knigth2.image.image = black_knigth2.image
        self.addPiece("bnl", black_knigth2.image, black_knigth2.getCoordX(), black_knigth2.getCoordY())
        black_rook1 = Torre('b', 0, 0, defPath + "br.gif")
        black_rook1.image.image = black_rook1.image
        self.addPiece("brr", black_rook1.image, black_rook1.getCoordX(), black_rook1.getCoordY())
        black_rook2 = Torre('b', 0, 7, defPath + "br.gif")
        black_rook2.image.image = black_rook2.image
        self.addPiece("brl", black_rook2.image, black_rook2.getCoordX(), black_rook2.getCoordY())
        black_pawn1 = Peon('b', 1, 0, defPath + "bp.gif")
        black_pawn1.image.image = black_pawn1.image
        self.addPiece("bp0", black_pawn1.image, black_pawn1.getCoordX(), black_pawn1.getCoordY())
        black_pawn2 = Peon('b', 1, 1, defPath + "bp.gif")
        black_pawn2.image.image = black_pawn2.image
        self.addPiece("bp1", black_pawn2.image, black_pawn2.getCoordX(), black_pawn2.getCoordY())
        black_pawn3 = Peon('b', 1, 2, defPath + "bp.gif")
        black_pawn3.image.image = black_pawn3.image
        self.addPiece("bp2", black_pawn3.image, black_pawn3.getCoordX(), black_pawn3.getCoordY())
        black_pawn4 = Peon('b', 1, 3, defPath + "bp.gif")
        black_pawn4.image.image = black_pawn4.image
        self.addPiece("bp3", black_pawn4.image, black_pawn4.getCoordX(), black_pawn4.getCoordY())
        black_pawn5 = Peon('b', 1, 4, defPath + "bp.gif")
        black_pawn5.image.image = black_pawn5.image
        self.addPiece("bp4", black_pawn5.image, black_pawn5.getCoordX(), black_pawn5.getCoordY())
        black_pawn6 = Peon('b', 1, 5, defPath + "bp.gif")
        black_pawn6.image.image = black_pawn6.image
        self.addPiece("bp5", black_pawn6.image, black_pawn6.getCoordX(), black_pawn6.getCoordY())
        black_pawn7 = Peon('b', 1, 6, defPath + "bp.gif")
        black_pawn7.image.image = black_pawn7.image
        self.addPiece("bp6", black_pawn7.image, black_pawn7.getCoordX(), black_pawn7.getCoordY())
        black_pawn8 = Peon('b', 1, 7, defPath + "bp.gif")
        black_pawn8.image.image = black_pawn8.image
        self.addPiece("bp7", black_pawn8.image, black_pawn8.getCoordX(), black_pawn8.getCoordY())
        
        
        # Creates all the white pieces and draws them into the board
        white_king = Rey('w', 7, 4, defPath + "wk.gif")
        white_king.image.image = white_king.image
        self.addPiece("wk", white_king.image, white_king.getCoordX(), white_king.getCoordY())
        white_queen = Reina('w', 7,3, defPath + "wq.gif")
        white_queen.image.image = white_queen.image
        self.addPiece("wq", white_queen.image, white_queen.getCoordX(), white_queen.getCoordY())
        white_bishop1 = Alfil('w', 7, 2, defPath + "wb.gif")
        white_bishop1.image.image = white_bishop1.image
        self.addPiece("wbl", white_bishop1.image, white_bishop1.getCoordX(), white_bishop1.getCoordY())
        white_bishop2 = Alfil('w', 7, 5, defPath + "wb.gif")
        white_bishop2.image.image = white_bishop2.image
        self.addPiece("wbr", white_bishop2.image, white_bishop2.getCoordX(), white_bishop2.getCoordY())
        white_knigth1 = Caballo('w', 7, 1, defPath + "wn.gif")
        white_knigth1.image.image = white_knigth1.image
        self.addPiece("wnl", white_knigth1.image, white_knigth1.getCoordX(), white_knigth1.getCoordY())
        white_knigth2 = Caballo('w', 7, 6, defPath + "wn.gif")
        white_knigth2.image.image = white_knigth2.image
        self.addPiece("wnr", white_knigth2.image, white_knigth2.getCoordX(), white_knigth2.getCoordY())
        white_rook1 = Torre('w', 7, 0, defPath + "wr.gif")
        white_rook1.image.image = white_rook1.image
        self.addPiece("wrl", white_rook1.image, white_rook1.getCoordX(), white_rook1.getCoordY())
        white_rook2 = Torre('w', 7, 7, defPath + "wr.gif")
        white_rook2.image.image = white_rook2.image
        self.addPiece("wrr", white_rook2.image, white_rook2.getCoordX(), white_rook2.getCoordY())
        white_pawn1 = Peon('w', 6, 0, defPath + "wp.gif")
        white_pawn1.image.image = white_pawn1.image
        self.addPiece("wp0", white_pawn1.image, white_pawn1.getCoordX(), white_pawn1.getCoordY())
        white_pawn2 = Peon('w', 6, 1, defPath + "wp.gif")
        white_pawn2.image.image = white_pawn2.image
        self.addPiece("wp1", white_pawn2.image, white_pawn2.getCoordX(), white_pawn2.getCoordY())
        white_pawn3 = Peon('w', 6, 2, defPath + "wp.gif")
        white_pawn3.image.image = white_pawn3.image
        self.addPiece("wp2", white_pawn3.image, white_pawn3.getCoordX(), white_pawn3.getCoordY())
        white_pawn4 = Peon('w', 6, 3, defPath + "wp.gif")
        white_pawn4.image.image = white_pawn4.image
        self.addPiece("wp3", white_pawn4.image, white_pawn4.getCoordX(), white_pawn4.getCoordY())
        white_pawn5 = Peon('w', 6, 4, defPath + "wp.gif")
        white_pawn5.image.image = white_pawn5.image
        self.addPiece("wp4", white_pawn5.image, white_pawn5.getCoordX(), white_pawn5.getCoordY())
        white_pawn6 = Peon('w', 6, 5, defPath + "wp.gif")
        white_pawn6.image.image = white_pawn6.image
        self.addPiece("wp5", white_pawn6.image, white_pawn6.getCoordX(), white_pawn6.getCoordY())
        white_pawn7 = Peon('w', 6, 6, defPath + "wp.gif")
        white_pawn7.image.image = white_pawn7.image
        self.addPiece("wp6", white_pawn7.image, white_pawn7.getCoordX(), white_pawn7.getCoordY())
        white_pawn8 = Peon('w', 6, 7, defPath + "wp.gif")
        white_pawn8.image.image = white_pawn8.image
        self.addPiece("wp7", white_pawn8.image, white_pawn8.getCoordX(), white_pawn8.getCoordY())
        '''for piece in imgs:

            #----------------Black ones---------------------
            if piece == "bb.gif": #Black Bishop 2
                photo = tk.PhotoImage(file = defPath+"bb.gif")
                photo.image = photo
                self.addPiece("bbr", photo, 0, 2)
                self.addPiece("bbl", photo, 0, 5)

            if piece == "bk.gif": #Black King
                photo2 = tk.PhotoImage(file = defPath+"bk.gif")
                photo2.image = photo2
                self.addPiece("bk", photo2, 0, 4)

            if piece == "bn.gif": #Black Knigth 2 
                photo3 = tk.PhotoImage(file = defPath+"bn.gif")
                photo3.image = photo3
                self.addPiece("bnl", photo3, 0, 1)     
                self.addPiece("bnr", photo3, 0, 6)

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
                self.addPiece("wbr", photo7, 7, 2)
                self.addPiece("wbl", photo7, 7, 5)

            if piece == "wk.gif": #White King
                photo8 = tk.PhotoImage(file = defPath+"wk.gif")
                photo8.image = photo8
                self.addPiece("wk", photo8, 7, 4)

            if piece == "wn.gif": #White Knigth 2 
                photo9 = tk.PhotoImage(file = defPath+"wn.gif")
                photo9.image = photo9
                self.addPiece("wnl", photo9, 7, 1)     
                self.addPiece("wnr", photo9, 7, 6)

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

            #----------------White ones---------------------'''

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
    
