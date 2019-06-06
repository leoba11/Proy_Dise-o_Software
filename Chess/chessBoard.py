import tkinter as tk
import os
from tkinter import *
from genBoard import *
from caballo import Caballo
from rey import Rey
from reina import Reina
from alfil import Alfil
from torre import Torre
from peon import Peon

from chessRules import *
#caca
import PIL.Image
import PIL.ImageTk

class chessBoard(tk.Frame, genBoard): #Hereda de tk y genBoard
    
    def __init__(self, logic_board,rows, columns, color1, color2, size, parent):
        pass
        genBoard.__init__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado
        
        self.logic_board = logic_board
        
        # Variable to check if one piece is already clicked
        self.isPieceClicked = False
        
        self.temporarySquares = []
        
        #Dimensions
        canvasWidth = columns * size
        canvasHeight = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0, width = canvasWidth, height = canvasHeight, background = 'bisque')
        
        self.caballito = Caballo('b', 0, 6, "images/bn.gif")
        
        # Relates the mouse clicked to a function called piece_clicked
        self.canvas.bind("<Button-1>", self.piece_clicked)
        
        self.canvas.bind("<ButtonRelease-1>", self.piece_dropped)
        
        self.canvas.pack(side = 'top', fill = 'both', expand = True, padx = 2, pady = 2)

        self.frame = tk.Frame(self)

        self.button1 = tk.Button(self.frame, text = 'Ver Reglas', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

        self.canvas.bind('<Configure>', self.refresh)
        
    # Relates the clicked cell of the board to a duple of coordinates
    def piece_clicked(self, event):
        coord_x = int((event.y / self.size))
        coord_y = int((event.x / self.size))
        #print ("clicked at", event.x, event.y, coord_x, coord_y)
        
        # Checks if the square clicked is a piece and if not other one has been pressed
        if ((not (self.logic_board.isEmpty(coord_x, coord_y))) and (not (self.isPieceClicked))):
			
            self.isPieceClicked = True
            possible_moves = self.logic_board.board[coord_x][coord_y].canMove(self.logic_board)
            
            # Copies all the list from possible moves to the temporary colored
            self.temporarySquares = possible_moves[:]
            
            for i in range(len(possible_moves)):
                print(possible_moves)
                x1 = (possible_moves[i][1] * self.size)
                y1 = (possible_moves[i][0] * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill="#9C9C9C", tags="square")
                self.canvas.update_idletasks()
        
        else:
			# Checks if the another piece was clicked
            if ( (self.isPieceClicked) and (not (self.logic_board.isEmpty(coord_x, coord_y)))):

                for j in range(len(self.temporarySquares)):
                    x1 = (self.temporarySquares[j][1] * self.size)
                    y1 = (self.temporarySquares[j][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    summ = self.temporarySquares[j][1] + self.temporarySquares[j][0]
                    color = self.getEvenColor() if (summ % 2 == 0) else self.getOddColor()
                    self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill=color, tags="square")
                
                del (self.temporarySquares[:])    
                possible_moves = self.logic_board.board[coord_x][coord_y].canMove(self.logic_board)
            
                # Copies all the list from possible moves to the temporary colored
                self.temporarySquares = possible_moves[:]
            
                for i in range(len(possible_moves)):
                    x1 = (possible_moves[i][1] * self.size)
                    y1 = (possible_moves[i][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill="#9C9C9C", tags="square")
                
                # Refresh the changes on the board
                self.canvas.update_idletasks()
				
        
        return (coord_x, coord_y)
			
			
        
    # Relates the dropped cell of the board to a duple of coordinates
    def piece_dropped(self, event):
        coord_x = int((event.y / self.size))
        coord_y = int((event.x / self.size))
        #print ("dropped at", event.x, event.y, coord_x, coord_y)
        
        
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
        
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)
   
    def loadInitPosPiece(self):
        names = ["brl", "bnl", "bbl", "bq", "bk", "bbr", "bnr", "brr", "bp", "bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "wp",
        "wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wrl", "wnl", "wbl", "wq", "wk", "wbr", "wnr", "wrr"]
        
        counter = 0
        # Checks the entire board
        for i in range(self.rows):
            for j in range(self.columns):
                
                # Checks if the square checked has a piece
                if (self.logic_board.board[i][j] != '*'):
                    self.addPiece(names[counter], self.logic_board.board[i][j].getImage(), i, j)
                    counter +=1

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
