import tkinter as tk
import os
from tkinter import *
from genBoard import *


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

        self.canvas.bind('<Configure>', self.refresh)
    
    #Add a piece to the tab to be used
    #TODO: HAcer el algortimo de las piezas de ajedrez
    def addPiece(self, name, image, row, column):
        #print(name)
        self.canvas.create_image(0,0, image = image, tags = (name, 'piece'), anchor = 'c')
        self.placePiece(name, row, column)

    def placePiece(self, name, row, column):
        #print(name)
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)
   
    def loadInitPosPiece(self):
        
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)

        for piece in imgs:
            if piece == "bb.gif": #Black Bishop
                photo = tk.PhotoImage(file = defPath+"bb.gif")
                self.addPiece("bb", photo, 5, 5)
            elif piece == "br.gif":
                photo = tk.PhotoImage(file = defPath+"br.gif")
                self.addPiece("br", photo, 0, 1)
    
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
            self.placePiece(name, self.pieces[name][0], self.pieces[name][1]) #Add the piece
        
        #self.loadInitPosPiece()

        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")



if __name__ == "__main__":

    '''
    root = tk.Tk()
    board = chessBoard(8, 8, 'white', 'black', 64, root)
    board.loadInitPosPiece()
    '''
    
    root = tk.Tk()
    board = chessBoard(8, 8, 'blue', 'green', 64, root)
    board.pack(side='top', fill='both', expand='true', padx=4, pady=4)

    board.loadInitPosPiece()
    
    #photo = tk.PhotoImage(file="bb.gif")
    #board.addPiece("p1", photo, 0,0)

    root.mainloop()
    