import tkinter as tk
from tkinter import *

class chessBoard(tk.frame, genBoard): #Hereda de tk y genBoard
    
    def __init__(self, rows, columns, co1or1, color2, size = 32, parent):

        genBoard.__init__(self, rows, columns, color1, color2)
        #super().__inti__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado

        #Dimensions
        canvasWidth = columns * size
        canvasHeight = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0, width = canvas_width, height = canvas_height, background = 'bisque')
        self.canvas.pack(side = 'top', fill = 'both', expand = True, padx = 2, pady = 2)

        self.canvas.bind('<Configure>', self.refresh)



if __name__ == "__main__":
    root = tk.Tk()
    gen = genBoard(8,8,'white','black')
    board = chessBoard(root)
    # board = genBoard(8,8,'white','black')