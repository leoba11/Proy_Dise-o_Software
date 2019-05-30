import tkinter as tk
import math
import os
from tkinter import *
from genBoard import *

from caballo import Caballo
from torre import Torre
from alfil import Alfil
from peon import Peon
from reina import Reina
from rey import Rey
from torre import Torre


class chessBoard(genBoard): #Hereda de tk y genBoard
    
    def __init__(self, rows, columns, color1, color2, size, parent):
        pass
        genBoard.__init__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado
        
        self.tablero = []
        
        for i in range(rows):
            self.tablero.append([0] * columns)
            
        self.tablero[0][0] = "HOLA"
        
        print(self.tablero)
        
        contador = 1
        for i in range(rows):
            for j in range(columns):
                self.tablero[i][j] = contador
                contador+=1
        
        print(self.tablero)
        
    def add_piece(self, pieza, coordX, coordY):
		
        if(not (math.isnan(self.tablero[coordX][coordY]))):
            self.tablero[coordX][coordY] = pieza
		
root = Tk()
tablerito = chessBoard(6, 6, 'blue', 'green', 36, '')

reicito = Rey('b', 0, 4, "images/bk.gif")
caballito = Caballo('b', 0, 6, "images/bn.gif")
torrecita = Torre('b', 0, 7, "images/br.gif")
peoncito = Peon('b', 1, 4, "images/bp.gif")
alfilito = Alfil('b', 0, 5, "images/bb.gif")
reinita = Reina('b', 0, 3, "images/bq.gif")


tablerito.add_piece(alfilito, alfilito.getCoordX(), alfilito.getCoordY())

print(tablerito.tablero)

#print(tablerito.tablero[0][5].printCoords())

for i in tablerito.tablero:
	for j in i:
		print(j, )
	print()

input()
